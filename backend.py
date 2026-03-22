"""CryoPack OS — Vaccine Cold-Chain Logistics Backend
Flask + SQLite (local) / PostgreSQL (Render) | Auth | 3D Bin Packing | Dataset Persistence
Automatically uses PostgreSQL on Render and SQLite on local laptop.
"""
from flask import Flask,request,jsonify,session,send_from_directory,make_response
from werkzeug.security import generate_password_hash,check_password_hash
import json,os,uuid,time
from datetime import datetime,timedelta
from functools import wraps
import urllib.parse as urlparse
# ── DATABASE SETUP ──
DATABASE_URL=os.environ.get('DATABASE_URL','')
USE_PG=bool(DATABASE_URL)
app=Flask(__name__,static_folder='static',static_url_path='/static')
app.config.update(
    SECRET_KEY=os.environ.get('SECRET_KEY','cryopack-os-secret-2024-vaccine-logistics'),
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SECURE=False,
    SESSION_COOKIE_SAMESITE='Lax',
    SESSION_COOKIE_NAME='cryopack_session',
    PERMANENT_SESSION_LIFETIME=timedelta(days=30)
)
CORS_HEADERS={
    'Access-Control-Allow-Credentials':'true',
    'Access-Control-Allow-Headers':'Content-Type, Authorization',
    'Access-Control-Allow-Methods':'GET, POST, DELETE, OPTIONS'
}
@app.after_request
def add_cors(r):
    origin=request.headers.get('Origin','')
    r.headers['Access-Control-Allow-Origin']=origin or '*'
    for k,v in CORS_HEADERS.items():
        r.headers[k]=v
    return r
@app.before_request
def handle_preflight():
    if request.method=='OPTIONS':
        r=make_response()
        r.headers['Access-Control-Allow-Origin']=request.headers.get('Origin','*')
        for k,v in CORS_HEADERS.items():
            r.headers[k]=v
        return r
# ── DB CONNECTION ──
def db():
    if USE_PG:
        import pg8000
        r=urlparse.urlparse(DATABASE_URL)
        conn=pg8000.connect(
            host=r.hostname,
            port=r.port or 5432,
            database=r.path[1:],
            user=r.username,
            password=r.password,
            ssl_context=True
        )
        return conn
    import sqlite3
    return sqlite3.connect('cryopack.db')
# SQLite uses ? PostgreSQL uses %s — fixed automatically
def ph(sql):
    if USE_PG:
        return sql.replace('?','%s')
    return sql
# Run SELECT return all rows
def db_fetch(sql,params=()):
    conn=db()
    try:
        cur=conn.cursor()
        cur.execute(ph(sql),params)
        rows=cur.fetchall()
        cur.close()
        return rows
    finally:
        conn.close()
# Run SELECT return one row
def db_fetchone(sql,params=()):
    conn=db()
    try:
        cur=conn.cursor()
        cur.execute(ph(sql),params)
        row=cur.fetchone()
        cur.close()
        return row
    finally:
        conn.close()
# Run INSERT UPDATE DELETE
def db_execute(sql,params=()):
    conn=db()
    try:
        cur=conn.cursor()
        cur.execute(ph(sql),params)
        conn.commit()
        cur.close()
    finally:
        conn.close()
# ── INIT DATABASE ──
def init_db():
    conn=db()
    try:
        cur=conn.cursor()
        if USE_PG:
            cur.execute("""CREATE TABLE IF NOT EXISTS users(
                id TEXT PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                last_login TEXT
            )""")
            cur.execute("""CREATE TABLE IF NOT EXISTS runs(
                id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                unit_w INTEGER,unit_d INTEGER,unit_h INTEGER,
                algorithm TEXT,
                boxes_json TEXT,results_json TEXT,
                efficiency REAL,units_used INTEGER,boxes_placed INTEGER,
                runtime_ms REAL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )""")
            cur.execute("""CREATE TABLE IF NOT EXISTS datasets(
                id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                name TEXT,boxes_json TEXT,unit_config TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )""")
        else:
            cur.executescript("""
                CREATE TABLE IF NOT EXISTS users(id TEXT PRIMARY KEY,username TEXT UNIQUE NOT NULL,password_hash TEXT NOT NULL,created_at TEXT DEFAULT CURRENT_TIMESTAMP,last_login TEXT);
                CREATE TABLE IF NOT EXISTS runs(id TEXT PRIMARY KEY,user_id TEXT NOT NULL,unit_w INTEGER,unit_d INTEGER,unit_h INTEGER,algorithm TEXT,boxes_json TEXT,results_json TEXT,efficiency REAL,units_used INTEGER,boxes_placed INTEGER,runtime_ms REAL,created_at TEXT DEFAULT CURRENT_TIMESTAMP);
                CREATE TABLE IF NOT EXISTS datasets(id TEXT PRIMARY KEY,user_id TEXT NOT NULL,name TEXT,boxes_json TEXT,unit_config TEXT,created_at TEXT DEFAULT CURRENT_TIMESTAMP);
            """)
        conn.commit()
        cur.close()
    finally:
        conn.close()
init_db()
# Migrate old schema — only on laptop
def migrate_db():
    if USE_PG:
        return
    try:
        import sqlite3
        conn=sqlite3.connect('cryopack.db')
        cols=[r[1] for r in conn.execute("PRAGMA table_info(runs)")]
        if 'unit_b' in cols and 'unit_d' not in cols:
            conn.executescript("""
                CREATE TABLE runs_new(id TEXT PRIMARY KEY,user_id TEXT NOT NULL,unit_w INTEGER,unit_d INTEGER,unit_h INTEGER,algorithm TEXT,boxes_json TEXT,results_json TEXT,efficiency REAL,units_used INTEGER,boxes_placed INTEGER,runtime_ms REAL,created_at TEXT DEFAULT CURRENT_TIMESTAMP);
                INSERT INTO runs_new SELECT id,user_id,unit_w,unit_b,unit_h,algorithm,boxes_json,results_json,efficiency,units_used,boxes_placed,runtime_ms,created_at FROM runs;
                DROP TABLE runs;
                ALTER TABLE runs_new RENAME TO runs;
            """)
        conn.close()
    except Exception as e:
        print(f'Migration warning: {e}')
migrate_db()
# ── Static routes ──
@app.route('/')
def serve_root():
    return send_from_directory('.','login.html')
for _path,_file in [('/login.html','login.html'),('/index.html','index.html'),('/analysis.html','analysis.html')]:
    app.add_url_rule(_path,_path[1:],lambda f=_file:send_from_directory('.',f))
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.',filename) if os.path.exists(filename) else({'error':'Not found'},404)
# Ping route — keeps server alive, used by UptimeRobot every 5 minutes
@app.route('/ping')
def ping():
    return jsonify({'status':'ok','service':'CryoPack OS'}),200
# Auth decorator
def require_login(f):
    @wraps(f)
    def dec(*a,**kw):
        if 'user_id' not in session:
            return jsonify({'error':'Unauthorized'}),401
        return f(*a,**kw)
    return dec
uid=lambda:session.get('user_id')
# ── Auth ──
@app.route('/api/auth/register',methods=['POST'])
def register():
    d=request.json
    u,p=d.get('username','').strip(),d.get('password','').strip()
    if len(u)<3:
        return jsonify({'error':'Username must be at least 3 characters'}),400
    if len(p)<6:
        return jsonify({'error':'Password must be at least 6 characters'}),400
    try:
        user_id=str(uuid.uuid4())
        db_execute('INSERT INTO users(id,username,password_hash) VALUES(?,?,?)',(user_id,u,generate_password_hash(p)))
        session.update({'user_id':user_id,'username':u})
        session.permanent=True
        return jsonify({'success':True,'user_id':user_id,'username':u}),201
    except Exception:
        return jsonify({'error':'Username already exists'}),409
@app.route('/api/auth/login',methods=['POST'])
def login():
    d=request.json
    u,p=d.get('username','').strip(),d.get('password','').strip()
    if not u or not p:
        return jsonify({'error':'Username and password required'}),400
    row=db_fetchone('SELECT id,password_hash FROM users WHERE username=?',(u,))
    if row and check_password_hash(row[1],p):
        db_execute('UPDATE users SET last_login=? WHERE id=?',(datetime.now().isoformat(),row[0]))
        session.update({'user_id':row[0],'username':u})
        session.permanent=True
        return jsonify({'success':True,'user_id':row[0],'username':u}),200
    return jsonify({'error':'Invalid credentials'}),401
@app.route('/api/auth/logout',methods=['POST'])
def logout():
    session.clear()
    return jsonify({'success':True}),200
@app.route('/api/auth/status')
def auth_status():
    if 'user_id' in session:
        return jsonify({'authenticated':True,'username':session.get('username'),'user_id':session.get('user_id')}),200
    return jsonify({'authenticated':False}),200
# ══════════════════════════════════════════════════
# 3D BIN PACKING ALGORITHMS
# ══════════════════════════════════════════════════
def can_place(pls,bw,bd,bh,px,py,pz,uw,ud,uh):
    if px+bw>uw or py+bd>ud or pz+bh>uh:
        return False
    return all(px+bw<=p['x'] or px>=p['x']+p['w'] or py+bd<=p['y'] or py>=p['y']+p['d'] or pz+bh<=p['z'] or pz>=p['z']+p['h'] for p in pls)
# Generate all unique rotation variants for a box
def get_rotations(bw,bd,bh):
    seen,out=set(),[]
    for d in[(bw,bd,bh),(bw,bh,bd),(bd,bw,bh),(bd,bh,bw),(bh,bw,bd),(bh,bd,bw)]:
        if d not in seen:
            seen.add(d)
            out.append(d)
    return out
# Generate candidate placement positions
def get_candidates(pls,uw,ud,uh):
    c={(0,0,0)}
    for p in pls:
        c.update([(p['x']+p['w'],p['y'],p['z']),(p['x'],p['y']+p['d'],p['z']),(p['x'],p['y'],p['z']+p['h'])])
    return list(c)
# FFD: first valid position sorted by z,x,y
def try_place_default(pls,bw,bd,bh,uw,ud,uh):
    cands=sorted(get_candidates(pls,uw,ud,uh),key=lambda c:(c[2],c[0],c[1]))
    for(x,y,z) in cands:
        if can_place(pls,bw,bd,bh,x,y,z,uw,ud,uh):
            return(x,y,z)
    return None
# BFD/HYBRID: gravity sort
def try_place_gravity(pls,bw,bd,bh,uw,ud,uh):
    cands=sorted(get_candidates(pls,uw,ud,uh),key=lambda c:(c[2],-(c[0]+c[1])))
    for(x,y,z) in cands:
        if can_place(pls,bw,bd,bh,x,y,z,uw,ud,uh):
            return(x,y,z)
    return None
# FF: spread sort
def try_place_spread(pls,bw,bd,bh,uw,ud,uh):
    cands=sorted(get_candidates(pls,uw,ud,uh),key=lambda c:(c[0]+c[1],c[2]))
    for(x,y,z) in cands:
        if can_place(pls,bw,bd,bh,x,y,z,uw,ud,uh):
            return(x,y,z)
    return None
PLACERS={'HYBRID':try_place_gravity,'BFD':try_place_gravity,'FFD':try_place_default,'FF':try_place_spread}
# Core packing loop
def run_algorithm(algo,uw,ud,uh,boxes):
    t0=time.time()
    units=[]
    all_pl=[]
    if {'HYBRID':True,'BFD':True,'FFD':True,'FF':False}.get(algo,False):
        boxes=sorted(boxes,key=lambda b:b['w']*b['d']*b['h'],reverse=True)
    for idx,box in enumerate(boxes):
        bw,bd,bh=box['w'],box['d'],box['h']
        rots=get_rotations(bw,bd,bh)
        best=None
        if algo=='HYBRID':
            bvol=float('inf')
            for ui,up in enumerate(units):
                used=sum(p['w']*p['d']*p['h'] for p in up)
                rem=uw*ud*uh-used
                if rem<bw*bd*bh:
                    continue
                for(rw,rd,rh) in rots:
                    pos=try_place_gravity(up,rw,rd,rh,uw,ud,uh)
                    if pos and rem<bvol:
                        bvol,best=rem,(ui,pos,rw,rd,rh)
        elif algo=='BFD':
            uvol=uw*ud*uh
            br=float('inf')
            for ui,up in enumerate(units):
                used=sum(p['w']*p['d']*p['h'] for p in up)
                rem=uvol-used
                if rem<bw*bd*bh:
                    continue
                for(rw,rd,rh) in rots:
                    pos=try_place_gravity(up,rw,rd,rh,uw,ud,uh)
                    if pos and rem<br:
                        br,best=rem,(ui,pos,rw,rd,rh)
        elif algo=='FFD':
            for ui,up in enumerate(units):
                pos=try_place_default(up,bw,bd,bh,uw,ud,uh)
                if pos:
                    up.append({'x':pos[0],'y':pos[1],'z':pos[2],'w':bw,'d':bd,'h':bh,'box_idx':idx,'unit_id':ui})
                    all_pl.append({'box':box,'x':pos[0],'y':pos[1],'z':pos[2],'unit_id':ui,'box_idx':idx,'rotated':False})
                    best=True
                    break
        else:
            for ui,up in enumerate(units):
                pos=try_place_spread(up,bw,bd,bh,uw,ud,uh)
                if pos:
                    up.append({'x':pos[0],'y':pos[1],'z':pos[2],'w':bw,'d':bd,'h':bh,'box_idx':idx,'unit_id':ui})
                    all_pl.append({'box':box,'x':pos[0],'y':pos[1],'z':pos[2],'unit_id':ui,'box_idx':idx,'rotated':False})
                    best=True
                    break
        if best and algo in('HYBRID','BFD') and isinstance(best,tuple):
            ui,pos,rw,rd,rh=best
            pb={'w':rw,'d':rd,'h':rh}
            units[ui].append({'x':pos[0],'y':pos[1],'z':pos[2],'w':rw,'d':rd,'h':rh,'box_idx':idx,'unit_id':ui})
            all_pl.append({'box':pb,'x':pos[0],'y':pos[1],'z':pos[2],'unit_id':ui,'box_idx':idx,'rotated':(rw,rd,rh)!=(bw,bd,bh)})
        elif not best:
            placer=PLACERS[algo]
            bp,br2=None,(bw,bd,bh)
            for(rw,rd,rh) in rots:
                pos=placer([],rw,rd,rh,uw,ud,uh)
                if pos:
                    bp,br2=pos,(rw,rd,rh)
                    break
            bp=bp or(0,0,0)
            rw,rd,rh=br2
            nuid=len(units)
            units.append([{'x':bp[0],'y':bp[1],'z':bp[2],'w':rw,'d':rd,'h':rh,'box_idx':idx,'unit_id':nuid}])
            all_pl.append({'box':{'w':rw,'d':rd,'h':rh},'x':bp[0],'y':bp[1],'z':bp[2],'unit_id':nuid,'box_idx':idx,'rotated':(rw,rd,rh)!=(bw,bd,bh)})
    return all_pl,len(units),(time.time()-t0)*1000
# Helpers
def prep_boxes(boxes_data,uw,ud,uh):
    out=[]
    for b in boxes_data:
        for _ in range(int(b.get('qty',1))):
            bw,bd,bh=int(b['w']),int(b.get('d',b.get('b',1))),int(b['h'])
            seen,uniq=set(),[]
            for d in[(bw,bd,bh),(bw,bh,bd),(bd,bw,bh),(bd,bh,bw),(bh,bw,bd),(bh,bd,bw)]:
                if d not in seen:
                    seen.add(d)
                    uniq.append(d)
            fits=next((d for d in uniq if d[0]<=uw and d[1]<=ud and d[2]<=uh),None)
            out.append({'w':fits[0],'d':fits[1],'h':fits[2]} if fits else {'w':min(bw,uw),'d':min(bd,ud),'h':min(bh,uh)})
    return out
# Calculate volumetric efficiency
def calc_eff(pls,n_units,uw,ud,uh):
    if not n_units:
        return 0
    return round(sum(p['box']['w']*p['box']['d']*p['box']['h'] for p in pls)/(n_units*uw*ud*uh)*100,2)
# ── Pack ──
@app.route('/api/pack',methods=['POST'])
@require_login
def pack():
    d=request.json
    uw,ud,uh=int(d.get('unit_w',10)),int(d.get('unit_d',10)),int(d.get('unit_h',10))
    algo=d.get('algorithm','HYBRID')
    boxes_flat=prep_boxes(d.get('boxes',[]),uw,ud,uh)
    pls,n_units,rt=run_algorithm(algo,uw,ud,uh,boxes_flat)
    eff=calc_eff(pls,n_units,uw,ud,uh)
    pl_data=[{'box':p['box'],'x':p['x'],'y':p['y'],'z':p['z'],'unit_id':p['unit_id'],'box_idx':p['box_idx'],'rotated':p.get('rotated',False)} for p in pls]
    run_id=str(uuid.uuid4())
    db_execute('INSERT INTO runs(id,user_id,unit_w,unit_d,unit_h,algorithm,boxes_json,results_json,efficiency,units_used,boxes_placed,runtime_ms) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',
        (run_id,uid(),uw,ud,uh,algo,json.dumps(d.get('boxes',[])),json.dumps(pl_data),eff,n_units,len(pls),rt))
    return jsonify({'success':True,'placements':pl_data,'units_used':n_units,'boxes_placed':len(pls),'boxes_total':len(boxes_flat),'efficiency':eff,'runtime_ms':round(rt,3),'algorithm':algo,'run_id':run_id}),200
# ── Runs ──
@app.route('/api/runs',methods=['GET'])
@require_login
def get_runs():
    rows=db_fetch('SELECT id,algorithm,efficiency,units_used,boxes_placed,runtime_ms,created_at,unit_w,unit_d,unit_h FROM runs WHERE user_id=? ORDER BY created_at DESC LIMIT 50',(uid(),))
    return jsonify([dict(zip(['id','algorithm','efficiency','units_used','boxes_placed','runtime_ms','created_at','unit_w','unit_d','unit_h'],r)) for r in rows]),200
@app.route('/api/runs/<run_id>',methods=['GET'])
@require_login
def get_run(run_id):
    r=db_fetchone('SELECT id,algorithm,efficiency,units_used,boxes_placed,runtime_ms,created_at,unit_w,unit_d,unit_h,boxes_json,results_json FROM runs WHERE id=? AND user_id=?',(run_id,uid()))
    if not r:
        return jsonify({'error':'Not found'}),404
    out=dict(zip(['id','algorithm','efficiency','units_used','boxes_placed','runtime_ms','created_at','unit_w','unit_d','unit_h'],r[:10]))
    out.update({'boxes':json.loads(r[10] or '[]'),'placements':json.loads(r[11] or '[]'),'success':True,'boxes_total':r[4]})
    return jsonify(out),200
@app.route('/api/runs/<run_id>',methods=['DELETE'])
@require_login
def delete_run(run_id):
    db_execute('DELETE FROM runs WHERE id=? AND user_id=?',(run_id,uid()))
    return jsonify({'success':True}),200
@app.route('/api/runs/all',methods=['DELETE'])
@require_login
def delete_all_runs():
    db_execute('DELETE FROM runs WHERE user_id=?',(uid(),))
    return jsonify({'success':True}),200
# ── Datasets ──
@app.route('/api/datasets',methods=['POST'])
@require_login
def save_dataset():
    d=request.json
    did=str(uuid.uuid4())
    db_execute('INSERT INTO datasets(id,user_id,name,boxes_json,unit_config) VALUES(?,?,?,?,?)',
        (did,uid(),d.get('name','Unnamed'),json.dumps(d.get('boxes',[])),json.dumps(d.get('unit_config',{}))))
    return jsonify({'id':did,'success':True}),201
@app.route('/api/datasets',methods=['GET'])
@require_login
def get_datasets():
    rows=db_fetch('SELECT id,name,boxes_json,unit_config,created_at FROM datasets WHERE user_id=? ORDER BY created_at DESC',(uid(),))
    return jsonify([{'id':r[0],'name':r[1],'boxes':json.loads(r[2]),'unit_config':json.loads(r[3]),'created_at':r[4]} for r in rows]),200
@app.route('/api/datasets/<did>',methods=['GET'])
@require_login
def get_dataset(did):
    r=db_fetchone('SELECT id,name,boxes_json,unit_config FROM datasets WHERE id=? AND user_id=?',(did,uid()))
    if not r:
        return jsonify({'error':'Not found'}),404
    return jsonify({'id':r[0],'name':r[1],'boxes':json.loads(r[2]),'unit_config':json.loads(r[3])}),200
@app.route('/api/datasets/<did>',methods=['DELETE'])
@require_login
def delete_dataset(did):
    db_execute('DELETE FROM datasets WHERE id=? AND user_id=?',(did,uid()))
    return jsonify({'success':True}),200
# ── Analysis ──
ALGO_NAMES={'HYBRID':'Hybrid Best-Fit','BFD':'Best Fit Decreasing','FFD':'First Fit Decreasing','FF':'First Fit'}
@app.route('/api/analysis/compare',methods=['POST'])
@require_login
def compare_algorithms():
    d=request.json
    uw,ud,uh=int(d.get('unit_w',10)),int(d.get('unit_d',10)),int(d.get('unit_h',10))
    boxes_flat=[{'w':int(b['w']),'d':int(b.get('d',b.get('b',1))),'h':int(b['h'])} for b in d.get('boxes',[]) for _ in range(int(b.get('qty',1)))]
    results={}
    for algo in('HYBRID','BFD','FFD','FF'):
        pls,n_units,rt=run_algorithm(algo,uw,ud,uh,boxes_flat[:])
        eff=calc_eff(pls,n_units,uw,ud,uh)
        results[algo]={'name':ALGO_NAMES[algo],'efficiency':eff,'units_used':n_units,'boxes_placed':len(pls),'runtime_ms':round(rt,3),'placements':[{'box':p['box'],'x':p['x'],'y':p['y'],'z':p['z'],'unit_id':p['unit_id'],'rotated':p.get('rotated',False)} for p in pls]}
    return jsonify(results),200
# ── KEEP ALIVE — prevents Render free tier from sleeping ──
import threading,time,urllib.request
def self_ping():
    time.sleep(60)  # wait 1 min after startup before first ping
    while True:
        try:
            url=os.environ.get('RENDER_EXTERNAL_URL','')  # get app URL from Render
            if url:urllib.request.urlopen(url+'/',timeout=10)  # ping own server
        except:pass  # ignore errors silently
        time.sleep(840)  # wait 14 mins then ping again (Render sleeps at 15 mins)
# Start pinger only on Render — not on local laptop
if os.environ.get('RENDER'):
    threading.Thread(target=self_ping,daemon=True).start()
if __name__=='__main__':
    print("\n CryoPack OS - Starting server...")
    print(f" Mode: {'PostgreSQL (Render)' if USE_PG else 'SQLite (Local)'}")
    print(" Access at: http://localhost:5000\n")
    port=int(os.environ.get('PORT',5000))
    app.run(debug=False,host='0.0.0.0',port=port)
