/**
 * CryoPack OS — Problem 115: Online 3D Bin Packing
 */
// ── STATE + CONSTANTS ──
const STATE={username:'',unitW:8,unitD:8,unitH:8,isOnline:false,queue:[],onlineSequence:[],currentBoxIndex:0,results:null,onlineUnits:[],placedBoxes:[],scene:null,camera:null,renderer:null,phi:Math.PI/4,theta:Math.PI/4,radius:32,target:null,dragging:false,lx:0,ly:0};
const COLORS=[0x00e5ff,0x00ff9d,0xff6b9d,0xffa500,0xcc66ff,0xff6b35,0x7bc67e,0xffb300];
const $=id=>document.getElementById(id);
const hex=i=>(COLORS[i%COLORS.length]).toString(16).padStart(6,'0');
window.addEventListener('DOMContentLoaded',async()=>{await checkAuth();initThree();updateUI();loadPreset();});
// ── AUTH ──
async function checkAuth(){
  try{const d=await fetch('/api/auth/status',{credentials:'include'}).then(r=>r.json());
    if(!d.authenticated)return(window.location.href='/login.html');
    STATE.username=d.username||'User';
  }catch{window.location.href='/login.html';}}
// ── MODE SWITCHING ──
function toggleMode(){STATE.isOnline?stopOnlineMode():startOnlineMode();}
function startOnlineMode(){
  if(!STATE.queue.length){toast('Add boxes to queue first','e');return;}
  Object.assign(STATE,{isOnline:true,onlineSequence:JSON.parse(JSON.stringify(STATE.queue)),currentBoxIndex:0,onlineUnits:[],placedBoxes:[]});
  $('omBadge').textContent='⚡ ONLINE';$('omBadge').classList.add('active');
  $('toggleModeBtn').classList.add('active');$('omPanel').classList.add('active');
  $('offlinePanel').style.display='none';
  drawUnit();updateOnlineUI();
  toast('⚡ Online Mode Started — Real-time sequential packing!','i');
  $('sTxt').textContent='ONLINE: Make decisions in real-time';}
function stopOnlineMode(){
  STATE.isOnline=false;
  $('omBadge').textContent='📊 OFFLINE';$('omBadge').classList.remove('active');
  $('toggleModeBtn').classList.remove('active');$('omPanel').classList.remove('active');
  $('offlinePanel').style.display='block';
  drawUnit();$('sTxt').textContent='Ready';}
// ── ONLINE MODE ──
function updateOnlineUI(){
  if(!STATE.isOnline)return;
  if(STATE.currentBoxIndex>=STATE.onlineSequence.length){
    $('currDims').textContent='✓ COMPLETE!';$('currVol').textContent='All boxes processed successfully';
    $('placeBtn').disabled=true;$('placeBtn').textContent='✓ DONE';return;}
  const b=STATE.onlineSequence[STATE.currentBoxIndex];
  $('currDims').textContent=`${b.w}×${b.d}×${b.h}`;$('currVol').textContent=`Volume: ${b.w*b.d*b.h}u³`;
  const nb=STATE.onlineSequence[STATE.currentBoxIndex+1];
  $('nextDims').textContent=nb?`${nb.w}×${nb.d}×${nb.h}`:'(END)';
  generateSmartRecommendations();renderSupportLayers();}
function generateSmartRecommendations(){
  if(STATE.currentBoxIndex>=STATE.onlineSequence.length)return;
  const box=STATE.onlineSequence[STATE.currentBoxIndex];
  const opts=STATE.onlineUnits.flatMap((unit,idx)=>findValidPlacements(unit,box).map(pos=>({unitIdx:idx,pos,score:evaluatePlacement(pos,box,unit),label:`Unit ${idx+1}: (${pos.x},${pos.y},${pos.z})`})));
  opts.push({unitIdx:STATE.onlineUnits.length,pos:{x:0,y:0,z:0},score:80,label:'NEW UNIT: Fresh start'});
  opts.sort((a,b)=>b.score-a.score);
  $('placementsList').innerHTML=opts.length
    ?opts.map((o,i)=>`<div class="placement-opt ${i===0?'best':''}" onclick="placeBoxAt(${o.unitIdx},${o.pos.x},${o.pos.y},${o.pos.z})"><div><div class="po-score">${o.score.toFixed(0)}/100 ${i===0?'⭐ BEST':''}</div><div class="po-desc">${o.label} — Score: ${o.score.toFixed(0)}</div></div></div>`).join('')
    :'<div style="color:var(--text3);font-size:.72rem;text-align:center;padding:12px">No valid placements!</div>';}
function evaluatePlacement(pos,box,unit){
  let s=50;
  if(pos.z>0)s+=20;
  if((STATE.unitW-pos.x-box.w)<1&&(STATE.unitD-pos.y-box.d)<1)s+=15;
  if((STATE.unitH-pos.z-box.h)<1)s+=10;
  if(!hasFullSupport(pos,box,unit))s-=50;
  return Math.max(0,s);}
function findValidPlacements(unit,box){
  const pl=[];
  const push=(x,y,z)=>{const pos={x,y,z};if(!hasOverlap(unit,box,pos)&&hasFullSupport(pos,box,unit)&&z+box.h<=STATE.unitH)pl.push(pos);};
  for(let x=0;x<=STATE.unitW-box.w;x++)for(let y=0;y<=STATE.unitD-box.d;y++)push(x,y,0);
  (unit.placements||[]).forEach(p=>{for(let x=p.x;x<p.x+p.box.w&&x<=STATE.unitW-box.w;x++)for(let y=p.y;y<p.y+p.box.d&&y<=STATE.unitD-box.d;y++)push(x,y,p.z+p.box.h);});
  return pl;}
function hasFullSupport(pos,box,unit){
  if(pos.z===0)return true;
  const{x:bl,y:bf,z:bz}=pos,br=bl+box.w,bb=bf+box.d;
  const area=(unit.placements||[]).reduce((s,p)=>{const sl=Math.max(p.x,bl),sr=Math.min(p.x+p.box.w,br);const sf=Math.max(p.y,bf),sb=Math.min(p.y+p.box.d,bb);return(p.z+p.box.h===bz&&sl<sr&&sf<sb)?s+(sr-sl)*(sb-sf):s;},0);
  return area>=box.w*box.d*0.9;}
function hasOverlap(unit,box,pos){
  return(unit.placements||[]).some(p=>!(pos.x+box.w<=p.x||pos.x>=p.x+p.box.w||pos.y+box.d<=p.y||pos.y>=p.y+p.box.d||pos.z+box.h<=p.z||pos.z>=p.z+p.box.h));}
function renderSupportLayers(){
  if(!STATE.isOnline)return;
  const el=$('layersViz');
  if(!STATE.onlineUnits.length){el.innerHTML='<div style="font-size:.7rem;color:var(--text3)">Start with fresh unit</div>';return;}
  el.innerHTML=STATE.onlineUnits.map((u,i)=>{const h=(u.placements||[]).reduce((m,p)=>Math.max(m,p.z+p.box.h),0);return`<div class="sv-item" onclick="placeBoxAt(${i},0,0,${h})"><div class="sv-label">U${i+1}:</div><div class="sv-bar"><div class="sv-fill" style="width:${h/STATE.unitH*100}%"></div></div><div style="font-size:.65rem;color:var(--text2);min-width:45px;text-align:right">${h}/${STATE.unitH}</div></div>`;}).join('');}
function placeBoxAt(unitIdx,x,y,z){
  if(!STATE.isOnline||STATE.currentBoxIndex>=STATE.onlineSequence.length)return;
  const box=STATE.onlineSequence[STATE.currentBoxIndex];
  while(STATE.onlineUnits.length<=unitIdx)STATE.onlineUnits.push({placements:[]});
  const pl={box,x,y,z,unit_id:unitIdx,boxIndex:STATE.placedBoxes.length};
  STATE.onlineUnits[unitIdx].placements.push(pl);STATE.placedBoxes.push(pl);
  addBoxMesh(pl,STATE.placedBoxes.length-1);STATE.currentBoxIndex++;
  updateOnlineUI();updateOnlineMetrics();
  toast(`✓ Placed in Unit ${unitIdx+1} — Next box!`,'s');}
function placeCurrentBox(){
  if(!STATE.isOnline||STATE.currentBoxIndex>=STATE.onlineSequence.length)return;
  const box=STATE.onlineSequence[STATE.currentBoxIndex];
  const opts=STATE.onlineUnits.flatMap((unit,idx)=>findValidPlacements(unit,box).map(pos=>({unitIdx:idx,pos,score:evaluatePlacement(pos,box,unit)})));
  const best=opts.sort((a,b)=>b.score-a.score)[0];
  best?placeBoxAt(best.unitIdx,best.pos.x,best.pos.y,best.pos.z):placeBoxAt(STATE.onlineUnits.length,0,0,0);}
function updateOnlineMetrics(){
  const placed=STATE.placedBoxes.length,units=STATE.onlineUnits.length;
  const vol=STATE.placedBoxes.reduce((s,p)=>s+p.box.w*p.box.d*p.box.h,0);
  const eff=Math.round(vol/(units*STATE.unitW*STATE.unitD*STATE.unitH)*100);
  $('mU').textContent=units;$('mB').textContent=placed;$('mE').textContent=eff+'%';
  $('sTxt').textContent=`ONLINE: ${placed}/${STATE.onlineSequence.length} placed in ${units} unit(s) · ${eff}% eff`;}
// ── OFFLINE MODE ──
function addBox(){
  const[w,d,h,qty]=['bW','bD','bH','bQ'].map(id=>+$(id).value);
  if(w<1||d<1||h<1||qty<1){toast('Invalid dimensions','e');return;}
  for(let i=0;i<qty;i++)STATE.queue.push({w,d,h});
  renderQueue();toast(`Added ${qty}× ${w}×${d}×${h}`,'s');}
function genRnd(){
  const n=Math.floor(Math.random()*16)+8;
  const r=max=>Math.floor(Math.random()*Math.max(1,Math.floor(max*0.6)))+1;
  for(let i=0;i<n;i++)STATE.queue.push({w:r(STATE.unitW),d:r(STATE.unitD),h:r(STATE.unitH)});
  renderQueue();toast(`Generated ${n} boxes`,'i');}
function loadPreset(){
  STATE.queue=[{w:4,d:2,h:3},{w:4,d:2,h:3},{w:3,d:4,h:2},{w:3,d:4,h:2},{w:2,d:2,h:4},{w:2,d:2,h:4},{w:1,d:3,h:3},{w:3,d:2,h:3},{w:4,d:4,h:1},{w:2,d:2,h:2},{w:2,d:3,h:2},{w:4,d:3,h:1}];
  renderQueue();toast('Problem 115 Preset Loaded','i');}
function clearQ(){STATE.queue=[];renderQueue();}
function renderQueue(){
  const cnt=$('qCnt'),el=$('qL');
  cnt.textContent=`( ${STATE.queue.length} )`;
  el.innerHTML=STATE.queue.length
    ?STATE.queue.map((b,i)=>`<div class="qi"><div class="qi-l"><div class="qi-dot" style="background:#${hex(i)}"></div><span class="qi-nm">#${i+1} ${b.w}×${b.d}×${b.h}</span></div><div style="display:flex;align-items:center;gap:8px"><span class="qi-v">V=${b.w*b.d*b.h}</span><span class="qi-x" onclick="STATE.queue.splice(${i},1);renderQueue()">✕</span></div></div>`).join('')
    :'<div class="qempty">Queue is empty</div>';}
async function runPack(){
  if(!STATE.queue.length){toast('Add boxes first','e');return;}
  const btn=$('runBtn');btn.textContent='⏳ Computing...';
  try{
    const d=await fetch('/api/pack',{method:'POST',credentials:'include',headers:{'Content-Type':'application/json'},body:JSON.stringify({unit_w:STATE.unitW,unit_d:STATE.unitD,unit_h:STATE.unitH,algorithm:'HYBRID',boxes:STATE.queue.map(({w,d,h})=>({w,d,h}))})}).then(r=>r.json());
    if(!d.success)throw new Error(d.error);
    STATE.results=d;renderResults(d);
    toast(`✓ ${d.boxes_placed}/${d.boxes_total} placed · ${d.efficiency}% eff`,'s');
  }catch(e){toast('Error: '+e.message,'e');}
  btn.textContent='▶ RUN PACKING';}
function renderResults(d){
  ['mU','mB','mE','mT'].forEach((id,i)=>$(id).textContent=[d.units_used,d.boxes_placed,d.efficiency+'%',d.runtime_ms.toFixed(2)+'ms'][i]);
  STATE.scene.children=STATE.scene.children.filter(c=>!c.userData?.bx);
  drawUnit();d.placements.forEach((p,i)=>addBoxMesh(p,i));
  $('pLog').innerHTML=`<div class="lhdr"><div class="lhdr-t">CryoPack OS</div><div class="lhdr-s">${d.units_used} units · ${d.boxes_placed}/${d.boxes_total} · ${d.efficiency}%</div></div>`+d.placements.map((p,i)=>`<div class="le" style="border-left-color:#${hex(i)}"><div class="le-t" style="color:#${hex(i)}">B[${i+1}]</div><div class="le-d">${p.box.w}×${p.box.d}×${p.box.h} @ U${p.unit_id+1}:(${p.x},${p.y},${p.z})</div></div>`).join('');}
function resetAll(){
  Object.assign(STATE,{results:null,queue:[],onlineUnits:[],placedBoxes:[],currentBoxIndex:0});
  if(STATE.isOnline)stopOnlineMode();
  renderQueue();drawUnit();
  ['mU','mB','mE','mT'].forEach(id=>$(id).textContent='0');
  $('pLog').innerHTML='<div style="color:var(--text3);text-align:center;padding:18px">No placements</div>';
  $('uBrk').innerHTML='<div style="color:var(--text3);font-size:.78rem;text-align:center;padding:14px">Run packing</div>';
  $('pF').style.width='0%';$('pLbl').textContent='Ready';$('sTxt').textContent='Ready';}
// ── 3D VISUALIZATION ──
function initThree(){
  const cv=$('canvas3d'),cw=cv.parentElement.clientWidth,ch=cv.parentElement.clientHeight-98;
  STATE.scene=new THREE.Scene();
  STATE.camera=new THREE.PerspectiveCamera(58,cw/ch,0.1,1000);
  STATE.renderer=new THREE.WebGLRenderer({canvas:cv,antialias:true,alpha:true});
  STATE.renderer.setSize(cw,ch);STATE.renderer.setClearColor(0x04080f,1);
  STATE.scene.add(new THREE.AmbientLight(0xffffff,0.55));
  const dl=new THREE.DirectionalLight(0x00e5ff,0.7);dl.position.set(25,35,25);STATE.scene.add(dl);
  const g=new THREE.GridHelper(80,40,0x162338,0x0d1c2e);g.position.y=-0.05;STATE.scene.add(g);
  STATE.target=new THREE.Vector3(4,4,4);STATE.radius=32;
  setupMouse(cv);drawUnit();
  (function anim(){requestAnimationFrame(anim);updateCam();STATE.renderer.render(STATE.scene,STATE.camera);})();
  window.addEventListener('resize',()=>{const nw=cv.parentElement.clientWidth,nh=cv.parentElement.clientHeight-98;STATE.camera.aspect=nw/nh;STATE.camera.updateProjectionMatrix();STATE.renderer.setSize(nw,nh);});}
function updateCam(){
  if(!STATE.camera||!STATE.target)return;
  STATE.camera.position.set(STATE.radius*Math.sin(STATE.phi)*Math.cos(STATE.theta)+STATE.target.x,STATE.radius*Math.cos(STATE.phi)+STATE.target.y,STATE.radius*Math.sin(STATE.phi)*Math.sin(STATE.theta)+STATE.target.z);
  STATE.camera.lookAt(STATE.target);}
function setupMouse(cv){
  cv.addEventListener('mousedown',e=>{STATE.dragging=true;STATE.lx=e.clientX;STATE.ly=e.clientY;});
  window.addEventListener('mouseup',()=>STATE.dragging=false);
  window.addEventListener('mousemove',e=>{if(!STATE.dragging)return;STATE.theta-=(e.clientX-STATE.lx)*0.009;STATE.phi=Math.max(0.08,Math.min(Math.PI-0.08,STATE.phi-(e.clientY-STATE.ly)*0.009));STATE.lx=e.clientX;STATE.ly=e.clientY;});
  cv.addEventListener('wheel',e=>{STATE.radius=Math.max(4,Math.min(120,STATE.radius+e.deltaY*0.06));e.preventDefault();},{passive:false});}
function drawUnit(){
  STATE.scene.children=STATE.scene.children.filter(c=>!c.userData?.cu&&!c.userData?.bx);
  const{unitW:w,unitD:d,unitH:h}=STATE;
  const wf=new THREE.LineSegments(new THREE.EdgesGeometry(new THREE.BoxGeometry(w,h,d)),new THREE.LineBasicMaterial({color:0x00e5ff,transparent:true,opacity:0.75}));
  wf.position.set(w/2,h/2,d/2);wf.userData.cu=true;STATE.scene.add(wf);}
function addBoxMesh(p,idx){
  const col=COLORS[idx%COLORS.length];
  const geo=new THREE.BoxGeometry(p.box.w-.1,p.box.h-.1,p.box.d-.1);
  const mesh=new THREE.Mesh(geo,new THREE.MeshPhongMaterial({color:col,transparent:true,opacity:0.85}));
  mesh.position.set(p.x+p.box.w/2,p.z+p.box.h/2,p.y+p.box.d/2);mesh.userData.bx=true;STATE.scene.add(mesh);
  const el=new THREE.LineSegments(new THREE.EdgesGeometry(geo),new THREE.LineBasicMaterial({color:0x000000,transparent:true,opacity:0.22}));
  el.position.copy(mesh.position);el.userData.bx=true;STATE.scene.add(el);}
function resetView(){STATE.phi=Math.PI/4;STATE.theta=Math.PI/4;STATE.radius=Math.max(STATE.unitW,STATE.unitD,STATE.unitH)*2.9;STATE.target=new THREE.Vector3(STATE.unitW/2,STATE.unitH/2,STATE.unitD/2);drawUnit();}
function onUC(){STATE.unitW=+$('uW').value||8;STATE.unitD=+$('uD').value||8;STATE.unitH=+$('uH').value||8;drawUnit();}
function updateUI(){}
function goAnalysis(){if(STATE.results)sessionStorage.setItem('cp_result',JSON.stringify(STATE.results));window.open('/analysis.html','_blank');}
async function saveCurDS(){if(!STATE.queue.length&&!STATE.placedBoxes.length){toast('No data to save','e');return;}toast('Data saved!','s');}
// ── TOAST ──
function toast(msg,t='i'){
  const el=document.createElement('div');
  el.className=`toast ${t}`;
  el.innerHTML=`<span>${{s:'✓',e:'✕',i:'ℹ'}[t]||'ℹ'}</span><span>${msg}</span>`;
  $('tc').appendChild(el);
  setTimeout(()=>{el.style.animation='tout 0.28s ease forwards';setTimeout(()=>el.remove(),300);},3200);}