<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:001d3d,30:003566,60:0077b6,100:00b4d8&height=200&section=header&text=❄️%20CryoPack%20OS&fontSize=55&fontColor=caf0f8&fontAlignY=38&desc=v4.0%20Ultimate%20·%20Online%203D%20Bin%20Packing%20System&descSize=16&descAlignY=58&descColor=90e0ef&animation=fadeIn" width="100%"/>

<br/>

<a href="https://cryopack-os.onrender.com">
<img src="https://readme-typing-svg.demolab.com?font=Orbitron&size=22&duration=3000&pause=1000&color=00B4D8&center=true&vCenter=true&width=700&lines=Vaccine+Cold-Chain+Logistics+Optimizer;Online+3D+Bin+Packing+Engine;10+Heuristic+Algorithms+%7C+Real-Time+WebGL;Cross-Device+Cloud+Sync+%7C+Full+Analytics" alt="Typing SVG"/>
</a>

<br/><br/>

[![Live Demo](https://img.shields.io/badge/🌐%20LIVE%20DEMO-cryopack--os.onrender.com-00b4d8?style=for-the-badge&labelColor=001d3d)](https://cryopack-os.onrender.com)

<br/>

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-white?style=for-the-badge&logo=flask&logoColor=black)](https://flask.palletsprojects.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-18-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org)
[![Three.js](https://img.shields.io/badge/Three.js-r128-black?style=for-the-badge&logo=three.js&logoColor=white)](https://threejs.org)
[![Chart.js](https://img.shields.io/badge/Chart.js-4.4.0-FF6384?style=for-the-badge&logo=chart.js&logoColor=white)](https://chartjs.org)
[![Render](https://img.shields.io/badge/Deployed-Render-46E3B7?style=for-the-badge&logo=render&logoColor=black)](https://render.com)
[![License](https://img.shields.io/badge/License-Private-ef233c?style=for-the-badge&logo=github)](https://github.com/ShaikMuzzammil/cryopack-os)

<br/>

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║           ❄  Pack smarter.   🧊  Ship colder.   💉  Save lives.            ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

</div>

---

<div align="center">

## 📌 Problem Statement

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=15&duration=2500&pause=800&color=90E0EF&center=true&vCenter=true&width=700&lines=Online+3D+Bin+Packing+for+Vaccine+Cold-Chain+Logistics" alt="Section heading"/>

</div>

**Problem Definition:** Given a sequence of 3‑dimensional rectangular boxes (vaccine packages) arriving one at a time, pack them into the minimum possible number of 3D bins (cooling units / refrigerators) such that:

<div align="center">

|  | Constraint | Rule |
|:-:|:----------:|------|
| 🚫 | **No Overlap** | No two boxes may occupy the same 3D space |
| 📦 | **Bin Bounds** | Every box must lie completely within bin boundaries |
| ⚡ | **Online** | Each box must be placed immediately upon arrival |
| 🔄 | **Rotation** | Boxes may rotate in all **6 orientations** |
| 📐 | **Fixed Bin** | Cooling unit has fixed dimensions **W × D × H** |

</div>

**Formal Statement:**

```
╔══════════════════════════════════════════════════════════════════════════╗
║  INPUT                                                                   ║
║  ──────────────────────────────────────────────────────────────────────  ║
║  · Cooling unit dimensions  :  W × D × H  (e.g.  8 × 8 × 8 units)      ║
║  · Sequence of boxes        :  B₁, B₂, ..., Bₙ                         ║
║    where each Bᵢ has dimensions (wᵢ × dᵢ × hᵢ)                         ║
║                                                                          ║
║  OUTPUT                                                                  ║
║  ──────────────────────────────────────────────────────────────────────  ║
║  · Assignment of each box to a bin                                       ║
║  · Placement coordinates (x, y, z) for each box within its bin          ║
║  · Minimize  :  total number of bins used                                ║
║  · Maximize  :  volumetric efficiency                                    ║
║                 (total box volume ÷ total bin volume used)               ║
║                                                                          ║
║  CONSTRAINTS                                                             ║
║  ──────────────────────────────────────────────────────────────────────  ║
║  ✔  Online  ·  Bᵢ must be placed before Bᵢ₊₁ is revealed               ║
║  ✔  No overlap between any two placed boxes                              ║
║  ✔  All boxes must remain within bin boundaries                          ║
║  ✔  Support constraint  ≥  78%  base area contact (no floating)         ║
╚══════════════════════════════════════════════════════════════════════════╝
```

> [!IMPORTANT]
> **Complexity:** This is an **NP‑hard problem**. No polynomial‑time optimal algorithm is known. CryoPack OS implements **10 heuristic algorithms** and compares their performance in real time.

> [!NOTE]
> **Why Online (not Offline)?** In real vaccine distribution, packages arrive from manufacturers at different times. Decisions must be made immediately — you cannot wait to see all packages before loading cooling units.

---

<div align="center">

## 🧊 What is CryoPack OS?

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=15&duration=2500&pause=800&color=90E0EF&center=true&vCenter=true&width=700&lines=A+full-stack+web+application+solving+Online+3D+Bin+Packing+for+vaccine+logistics" alt="Section heading"/>

</div>

<div align="center">

| `#` | ✦ Feature | Description |
|:---:|:---------:|-------------|
| `01` | **🔧 Packing Engine** | Runs 10 different bin packing algorithms on your box data |
| `02` | **🎮 Real‑time 3D Visualization** | See exactly how boxes are packed inside cooling units using WebGL |
| `03` | **📊 Algorithm Comparison** | Run two algorithms side by side and compare with 8 detailed charts |
| `04` | **🏆 Benchmark System** | Run all 10 algorithms at once and rank them by efficiency |
| `05` | **🎬 Step‑by‑Step Mode** | Watch each box being placed one by one with animations |
| `06` | **💾 Dataset Persistence** | Save box configurations and reload them anytime |
| `07` | **📜 Run History** | All packing results saved with full metrics |
| `08` | **☁️ Cross‑Device Sync** | Data available on all your devices via cloud database |

</div>

---

<div align="center">

## 🌍 Why This Matters — Real‑World Impact

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=15&duration=2500&pause=800&color=90E0EF&center=true&vCenter=true&width=700&lines=Every+inefficiently+packed+vaccine+shipment+costs+lives+and+resources" alt="Section heading"/>

</div>

> [!WARNING]
> Vaccines must be maintained between **2°C and 8°C** throughout the entire supply chain. Every cooling unit uses electricity and costs money to operate. Poor packing decisions have direct consequences.

<div align="center">

| ❌ Problem | 💥 Real Impact |
|:----------:|:-------------:|
| Boxes packed inefficiently | More cooling units needed = **higher cost** |
| Wasted space in refrigerators | Same electricity cost, **fewer vaccines** transported |
| Suboptimal packing decisions | Longer transport times, **higher risk** of temperature excursion |
| No algorithm comparison | Cannot know which packing strategy is **best** for a given shipment |

</div>

<br/>

**CryoPack OS solves this** by providing instant packing optimization with visual verification, allowing logistics planners to:

- 🔭 See exactly how boxes fit **before** physical loading
- ⚖️ Compare algorithms to find which uses **fewest cooling units**
- 📤 **Export results** for documentation and audit trails
- 💾 **Save and reuse** box configurations for recurring shipments

---

<div align="center">

## ⚙️ How It Works

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=15&duration=2500&pause=800&color=90E0EF&center=true&vCenter=true&width=700&lines=Corner-Point+Method+%7C+6-Rotation+Search+%7C+78%25+Support+Constraint" alt="Section heading"/>

</div>

### 🔄 Overall System Flow

```
  ┌─────────────────────────────────────────────────────────────────────┐
  │  📐  Configure cooling unit  ──────────────  W × D × H dimensions  │
  └──────────────────────────────────┬──────────────────────────────────┘
                                     │
                                     ▼
  ┌─────────────────────────────────────────────────────────────────────┐
  │  📦  Add vaccine boxes  ───────────────────  types · dims · qty     │
  │      (or load a saved preset / dataset)                             │
  └──────────────────────────────────┬──────────────────────────────────┘
                                     │
                                     ▼
  ┌─────────────────────────────────────────────────────────────────────┐
  │  🧠  Select packing algorithm(s)  ─────────  1 of 10 heuristics    │
  └──────────────────────────────────┬──────────────────────────────────┘
                                     │
                                     ▼
  ┌─────────────────────────────────────────────────────────────────────┐
  │  ⚡  Backend algorithm runs                                          │
  │      ├─ Sort boxes by volume (largest first for BFD / FFD / HBF)   │
  │      ├─ For each box, try all 6 rotations                           │
  │      ├─ Find best position via corner-point candidates              │
  │      ├─ Check overlap + support constraints (≥ 78%)                │
  │      └─ Assign to best-fitting bin or open a new bin               │
  └──────────────────────────────────┬──────────────────────────────────┘
                                     │
                                     ▼
  ┌─────────────────────────────────────────────────────────────────────┐
  │  📍  Returns (x, y, z) coordinates for every box placed             │
  └──────────────────────────────────┬──────────────────────────────────┘
                                     │
                                     ▼
  ┌─────────────────────────────────────────────────────────────────────┐
  │  🎮  Three.js renders all boxes in 3D  ───  colors · labels · glow  │
  └──────────────────────────────────┬──────────────────────────────────┘
                                     │
                                     ▼
  ┌─────────────────────────────────────────────────────────────────────┐
  │  📊  8 charts generated  ──  efficiency · waste · runtime · density │
  └──────────────────────────────────┬──────────────────────────────────┘
                                     │
                                     ▼
  ┌─────────────────────────────────────────────────────────────────────┐
  │  🗄️  Results saved  ───────────────────────  PostgreSQL database    │
  └─────────────────────────────────────────────────────────────────────┘
```

<br/>

### 📐 Placement Algorithm — Corner Point Method

For each box to be placed, the algorithm:

```
  Step 1 ── Generate candidate positions from corners of already-placed boxes
  Step 2 ── Sort candidates by priority  (lowest z first = gravity simulation)
  Step 3 ── For each candidate position, validate:
              ├─ 📐  Does the box fit within bin boundaries?
              ├─ 🚫  Does it overlap with any existing box?
              └─ 🏗️  Does it have ≥ 78% base area support?
  Step 4 ── Return the first valid position found
```

<br/>

### 🏗️ Support Constraint — No Floating Boxes

```python
# A box at height z needs 78% of its base covered by floor or boxes below
supported_area = sum of overlapping area with boxes at height (z - box_height)
if supported_area >= box.w * box.d * 0.78:
    placement is valid   ✔
else:
    placement rejected   ✗
```

---

<div align="center">

## ✨ All Features

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=15&duration=2500&pause=800&color=90E0EF&center=true&vCenter=true&width=700&lines=3+Pages+%7C+15%2B+Dashboard+Features+%7C+8+Analytics+Charts" alt="Section heading"/>

</div>

### 🖥️ Main Dashboard — `index.html`

<div align="center">

| Feature | Description |
|---------|-------------|
| **Dual 3D View** | Storage scene on top shows all packed cooling units. Conveyor belt scene below shows boxes travelling from entry to cooling unit |
| **Conveyor Belt Animation** | Boxes animate along a 3D conveyor belt with rollers, entry port, packing station, and connection beam to active cooling unit |
| **Fly‑In Animation** | Each box flies from the packing station into its exact position inside the cooling unit with arc trajectory |
| **Step‑Through Mode** | Place one box at a time — watch each placement individually |
| **Pause / Resume** | Pause the animation at any point and resume |
| **Speed Control** | Slider from 1× to 10× animation speed |
| **Expand View** | Full‑screen modal for either view with orbit, zoom, pan, auto‑rotate, front/top/iso presets |
| **Unit Tabs** | Click any cooling unit tab to focus the 3D view on that unit |
| **Overflow Banner** | Warning shown when boxes require a second cooling unit |
| **Live Metrics** | Units used · boxes placed · volumetric efficiency % · algorithm runtime ms |
| **Placement Log** | Scrollable log showing every box with its unit assignment and coordinates |
| **Queue System** | Add boxes by dimension, generate random boxes, load preset, clear queue |
| **Unit Config** | Set cooling unit W × D × H, shows calculated floor area, volume, estimated max boxes |
| **Run History Sidebar** | Load any previous packing run — restores all results and 3D view |
| **Dataset Save/Load** | Save current box queue to database, reload named datasets |

</div>

<br/>

### 📊 Algorithm Analysis — `analysis.html`

<div align="center">

| Section | Content |
|---------|---------|
| **Overview** | Summary stats — best efficiency, min units, fastest time, total boxes |
| **8 Performance Charts** | Volume efficiency · cooling units required · wasted space · boxes‑per‑unit density · per‑unit fill levels · volume by box type · algorithm runtime · box size distribution |
| **Head‑to‑Head Table** | Side by side comparison of all metrics with winner highlighted in gold |
| **Unit Fill Distribution** | Progress bars for every individual cooling unit showing fill % |
| **Placement Logs** | Complete I/O log with box number, name, dimensions, assigned unit, position, volume |
| **Algorithm Cards** | Detailed description of each algorithm with complexity rating |
| **Dataset Selector** | Load saved datasets directly from the analysis page |
| **Override Dims** | Change cooling unit dimensions and rerun without going back to main page |
| **Print Report** | Export full analysis as printable HTML page |

</div>

---

<div align="center">

## ☁️ Cross‑Device Sync — Your Data Everywhere

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=15&duration=2500&pause=800&color=90E0EF&center=true&vCenter=true&width=700&lines=Cloud+PostgreSQL+%7C+No+manual+transfer+%7C+One+account+%2C+one+truth" alt="Section heading"/>

</div>

CryoPack OS stores all your datasets, packing results, and algorithm comparisons in a **cloud PostgreSQL database** (Neon / Render).

<div align="center">

| Device | Action | What Happens |
|:------:|--------|:------------:|
| 💻 **Laptop** | Save a dataset `"Hospital July"` | Data written to cloud database |
| 📱 **Mobile** | Log in with same account | Seamlessly see `"Hospital July"` in workspace |
| 📟 **Tablet** | Run a packing comparison | Result saved and available on all devices |
| 🖥️ **Any device** | Load a previous run | Full 3D view and metrics restored instantly |

</div>

<br/>

### 🔁 What Is Synchronised?

<div align="center">

| Data Type | Sync | Notes |
|-----------|:----:|-------|
| Saved datasets (name + boxes + unit config) | ✅ **Fully synced** | Automatic — appears on all devices after login |
| Packing run history (results, placements, efficiency) | ✅ **Fully synced** | Automatic — every run is saved to database |
| **Current queue** (boxes waiting to be packed) | ⚠️ **Manual** | Save the queue as a dataset 💾, then load on another device |
| **3D view state** (camera angle, zoom, active unit) | ❌ **Not synced** | Each device has its own screen size and preferences |

</div>

> [!TIP]
> **Best practice:** After adding boxes to the queue, save it as a dataset. Then you can load it on any device instantly.

<br/>

### 🔁 How It Works — Simple Explanation

```
  Step 1 ── You log in
             └─ Browser receives a secure session cookie
                (Secure=True  +  SameSite=None  for mobile compatibility)

  Step 2 ── You save a dataset
             └─ Frontend sends  POST /api/datasets
                with boxes array + unit dimensions

  Step 3 ── Backend stores it
             └─ Data saved to  datasets  table, linked to your user_id

  Step 4 ── You open another device
             └─ Frontend calls  GET /api/datasets
                → returns ALL datasets you ever saved

  Step 5 ── You load a dataset
             └─ Backend fetches exact box list + unit config
                → runs packing algorithm → returns 3D view
```

> ✅ **No manual transfer. No export/import. Just log in and your data is there.**

<br/>

### 🌐 Real‑World Benefit for Vaccine Logistics

A logistics coordinator can:

- 🖥️ **On desktop** — design a box configuration for a new shipment, test with 10 algorithms, save the best dataset
- 📟 **On the warehouse tablet** — load the same dataset, run packing, see how to load the cooling unit **in 3D**
- 📱 **On mobile** — check the placement log and fill percentages while supervising loading

> **No emailing files. No re‑entering dimensions. No version confusion. One account, one truth.**

<br/>

### 🔒 Security

<div align="center">

| 🛡️ Protection | 🔧 Implementation |
|:-------------:|:----------------:|
| **Password storage** | Werkzeug PBKDF2 hash — never stored in plain text |
| **Session cookies** | `HttpOnly` · `Secure` · `SameSite=Lax/None` — XSS and CSRF protected |
| **Database credentials** | Render environment variables — never exposed in code |

</div>

<br/>

### 🧪 Demo — Cross‑Device Sync Test

```
  Step 1 ── On laptop  →  log in  →  save a dataset called "Test Sync"
  Step 2 ── On mobile  →  open cryopack-os.onrender.com  →  log in (same credentials)
  Step 3 ── Open Workspace sidebar → My Datasets → "Test Sync" appears instantly ✔
  Step 4 ── Load it  →  run packing  →  same 3D view appears on both devices ✔

  Note: This works because SESSION_COOKIE_SECURE=True and SESSION_COOKIE_SAMESITE='None'
        were set in the backend. Without these, mobile browsers reject the session cookie.
```

---

<div align="center">

## 🔢 All 10 Packing Algorithms

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=15&duration=2500&pause=800&color=90E0EF&center=true&vCenter=true&width=700&lines=10+heuristics+%7C+More+than+any+similar+tool+%7C+NP-Hard+solved+in+milliseconds" alt="Section heading"/>

</div>

<div align="center">

| 🏷️ Key | 📛 Full Name | 🧠 Strategy | ⏱️ Complexity | 🎯 Best For |
|:------:|:------------|:-----------|:------------:|:-----------|
| `HBF` | **Hybrid Best‑Fit** | Sort descending · Best remaining space that still fits · gravity placement | `O(N·B)` | Highest efficiency overall |
| `BFD` | **Best Fit Decreasing** | Sort descending · Bin with least remaining space that fits the box | `O(N·B)` | Best quality/speed balance |
| `FFD` | **First Fit Decreasing** | Sort descending · First bin where box fits | `O(N·B)` | Fast, good quality |
| `FF`  | **First Fit** | No sort · First bin where box fits | `O(N·B)` | Real‑time online scenarios |
| `WFD` | **Worst Fit Decreasing** | Sort descending · Bin with MOST remaining space | `O(N·B)` | Spreading load evenly |
| `GU`  | **Guillotine** | Sort descending · Minimize remaining space after placement | `O(N·B)` | Irregular box sizes |
| `SK`  | **Stack‑Key** | Sort descending · Lowest z‑height placement position | `O(N·B)` | Tall box heavy loads |
| `NF`  | **Next Fit** | No sort · Current bin only, open new if full | `O(N)` | Fastest possible · streaming |
| `DF`  | **Depth‑First** | Sort descending · Maximize depth (y) utilization first | `O(N·B)` | Deep storage optimization |
| `LF`  | **Layer Fill** | Sort descending · Minimize z × x position score | `O(N·B)` | Layer‑by‑layer packing |

> **N** = number of boxes · **B** = number of open bins

</div>

<br/>

### 🗺️ Algorithm Selection Guide

```
  ╔══════════════════════════════════════════════════════════════════╗
  ║               WHICH ALGORITHM SHOULD I USE?                     ║
  ╠══════════════════════════════════════════════════════════════════╣
  ║                                                                  ║
  ║  Need maximum efficiency?       ──────────▶  HBF  or  BFD       ║
  ║  Boxes arriving in real‑time?   ──────────▶  NF   or  FF        ║
  ║  Large dataset, need speed?     ──────────▶  FFD  or  FF        ║
  ║  Boxes vary greatly in size?    ──────────▶  GU   or  SK        ║
  ║  Don't know which to pick?      ──────────▶  🏆  Run Benchmark  ║
  ║                                              (tests all 10)     ║
  ╚══════════════════════════════════════════════════════════════════╝
```

---

<div align="center">

## 📄 Pages and Interfaces

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=15&duration=2500&pause=800&color=90E0EF&center=true&vCenter=true&width=700&lines=3+Pages+%7C+Login+%7C+Main+Dashboard+%7C+Algorithm+Analysis" alt="Section heading"/>

</div>

### 🔑 Page 1 — Login / Register · `login.html`

- Clean split‑screen design — branding left, auth form right
- Toggle between Login and Register with animated tab switch
- Password strength meter (5 levels — red to green)
- Animated background with floating particles and snowflakes
- Error messages with shake animation
- Auto‑redirects to main dashboard if already logged in
- Feature pills: `3D Packing Engine` · `Efficiency Analytics` · `Secure Workspaces` · `Dataset Persistence` · `Algorithm Reports` · `Real‑time 3D View`

<br/>

### 🖥️ Page 2 — Main Dashboard · `index.html`

*Primary packing interface · Three‑column layout*

<div align="center">

| Panel | Contents |
|:-----:|---------|
| **⬅️ Left** | Unit config · box input · queue · run controls |
| **🖥️ Center** | Dual 3D canvas (storage top · conveyor belt bottom) with draggable divider |
| **➡️ Right** | Live metrics · unit breakdown · placement log |

</div>

<br/>

### 📊 Page 3 — Algorithm Analysis · `analysis.html`

*Full‑page analysis report*

<div align="center">

| Area | Contents |
|:----:|---------|
| **⬅️ Left sidebar** | Section navigation — Overview · Algorithms · Comparison · Datasets · Report |
| **🖥️ Main content** | Dynamic content per section with Chart.js visualizations |

</div>

---

<div align="center">

## 📁 Project Structure

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=15&duration=2500&pause=800&color=90E0EF&center=true&vCenter=true&width=700&lines=Flask+backend+%7C+3+HTML+pages+%7C+Modular+CSS+%2B+JS" alt="Section heading"/>

</div>

```
CryoPack-Os/
│
├── 🐍  backend.py           Flask server — all API routes, packing algorithms, DB
├── 📋  requirements.txt     Python packages  (Flask · gunicorn · pg8000 · Werkzeug)
├── 🚀  Procfile             Render deployment — tells server to use gunicorn
├── 🔒  .gitignore           Excludes cryopack.db · __pycache__ · .env
│
├── 🏠  index.html           Main dashboard — conveyor belt + dual 3D view
├── 🔑  login.html           Login and registration page
├── 📊  analysis.html        Algorithm comparison and analysis dashboard
│
├── 🎨  styles.css           Global design system — CSS variables, reset, components
│                            (buttons · cards · badges · forms · progress · scrollbar)
│
├── 💫  animations.css       27 keyframe animations · 10 utility classes
│                            5 stagger delays · GPU helpers · reduced-motion support
│
├── ⚡  app-main.js          JavaScript for main page
│                            (online mode · offline mode · 3D controls · queue · toast)
│
└── 💾  cryopack.db          SQLite database — LOCAL ONLY, not committed to GitHub
                             Auto-created on first run · replaced by PostgreSQL on Render
```

---

<div align="center">

## 🛠️ Tech Stack

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=15&duration=2500&pause=800&color=90E0EF&center=true&vCenter=true&width=700&lines=Python+%7C+Flask+%7C+PostgreSQL+%7C+Three.js+%7C+Chart.js+%7C+Render" alt="Section heading"/>

</div>

### 🖧 Backend

<div align="center">

[![Python](https://skillicons.dev/icons?i=python)](https://python.org)
[![Flask](https://skillicons.dev/icons?i=flask)](https://flask.palletsprojects.com)
[![PostgreSQL](https://skillicons.dev/icons?i=postgres)](https://postgresql.org)
[![SQLite](https://skillicons.dev/icons?i=sqlite)](https://sqlite.org)

</div>

<div align="center">

| Technology | Version | Purpose |
|:----------:|:-------:|---------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) **Python** | `3.11+` | Backend language |
| ![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white) **Flask** | `2.3.3` | Web framework — routes, sessions, serving files |
| **Werkzeug** | `2.3.7` | PBKDF2 password hashing for secure authentication |
| ![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?style=flat-square&logo=gunicorn&logoColor=white) **gunicorn** | `21.2.0` | Production WSGI server (Render deployment) |
| **pg8000** | `1.31.1` | Pure Python PostgreSQL driver — works with Python 3.14 |
| ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white) **SQLite** | built‑in | Local development database — zero setup needed |
| ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat-square&logo=postgresql&logoColor=white) **PostgreSQL** | `18` | Production database on Render — permanent data storage |

</div>

<br/>

### 🌐 Frontend

<div align="center">

[![JavaScript](https://skillicons.dev/icons?i=js)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![HTML](https://skillicons.dev/icons?i=html)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS](https://skillicons.dev/icons?i=css)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![Three.js](https://skillicons.dev/icons?i=threejs)](https://threejs.org)

</div>

<div align="center">

| Technology | Version | Purpose |
|:----------:|:-------:|---------|
| ![Three.js](https://img.shields.io/badge/Three.js-000000?style=flat-square&logo=three.js&logoColor=white) **Three.js** | `r128` | WebGL 3D rendering — boxes, cooling units, conveyor belt, lighting, shadows |
| ![Chart.js](https://img.shields.io/badge/Chart.js-FF6384?style=flat-square&logo=chart.js&logoColor=white) **Chart.js** | `4.4.0` | 8 types of performance charts in analysis dashboard |
| ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black) **Vanilla JavaScript** | `ES2020+` | All interactivity — no framework overhead |
| **CSS Custom Properties** | — | Dark theme design system with consistent tokens |

</div>

<br/>

### 🔤 Typography

<div align="center">

| Font | Usage |
|:----:|-------|
| **Orbitron** | Branding, headings |
| **JetBrains Mono** | Terminal output, code‑like labels, metrics |
| **Share Tech Mono** | Status pills, secondary monospace elements |
| **Outfit** | Body text in main dashboard |
| **Unbounded** | Large display headings in login page |
| **Syne** | Button text in main dashboard |
| **Space Mono** | Form labels, badge text |
| **Poppins** | General body text fallback |

</div>

<br/>

### 🚀 Deployment

<div align="center">

[![GitHub](https://skillicons.dev/icons?i=github)](https://github.com/ShaikMuzzammil/cryopack-os)
[![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=black)](https://render.com)

</div>

<div align="center">

| Service | Purpose |
|:-------:|---------|
| ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white) **GitHub** | Code version control — [`github.com/ShaikMuzzammil/cryopack-os`](https://github.com/ShaikMuzzammil/cryopack-os) |
| ![Render](https://img.shields.io/badge/Render-46E3B7?style=flat-square&logo=render&logoColor=black) **Render** | Flask server hosting — free tier |
| **Render PostgreSQL** | Permanent database — free tier (90 days) |

</div>

---

<div align="center">

## 🔌 API Reference

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=15&duration=2500&pause=800&color=90E0EF&center=true&vCenter=true&width=700&lines=RESTful+API+%7C+Session-cookie+auth+%7C+JSON+payloads" alt="Section heading"/>

</div>

> [!NOTE]
> All API routes require login (session cookie) except authentication routes.

### 🔐 Authentication

<div align="center">

| Method | Route | Body | Response |
|:------:|-------|------|---------|
| `POST` | `/api/auth/register` | `{username, password}` | `{success, user_id, username}` |
| `POST` | `/api/auth/login` | `{username, password}` | `{success, user_id, username}` |
| `POST` | `/api/auth/logout` | — | `{success}` |
| `GET` | `/api/auth/status` | — | `{authenticated, username, user_id}` |

</div>

### 📦 Packing

<div align="center">

| Method | Route | Body | Response |
|:------:|-------|------|---------|
| `POST` | `/api/pack` | `{unit_w, unit_d, unit_h, algorithm, boxes[]}` | `{placements[], units_used, boxes_placed, efficiency, runtime_ms}` |
| `POST` | `/api/analysis/compare` | `{unit_w, unit_d, unit_h, boxes[]}` | `{HYBRID:{}, BFD:{}, FFD:{}, FF:{}}` |

</div>

### 🕓 Run History

<div align="center">

| Method | Route | Description |
|:------:|-------|-------------|
| `GET` | `/api/runs` | Get last 50 runs for current user |
| `GET` | `/api/runs/<id>` | Get specific run with full placement data |
| `DELETE` | `/api/runs/<id>` | Delete a single run |
| `DELETE` | `/api/runs/all` | Delete all runs for current user |

</div>

### 💾 Datasets

<div align="center">

| Method | Route | Description |
|:------:|-------|-------------|
| `POST` | `/api/datasets` | Save a named box configuration |
| `GET` | `/api/datasets` | Get all saved datasets for current user |
| `GET` | `/api/datasets/<id>` | Get specific dataset |
| `DELETE` | `/api/datasets/<id>` | Delete a dataset |

</div>

### 📂 Static Files

<div align="center">

| Route | Serves |
|:-----:|--------|
| `/` | `login.html` |
| `/index.html` | Main dashboard |
| `/analysis.html` | Analysis page |
| `/<filename>` | Any static file (CSS, JS, etc.) |

</div>

---

<div align="center">

## 🗄️ Database Schema

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=15&duration=2500&pause=800&color=90E0EF&center=true&vCenter=true&width=700&lines=SQLite+locally+%7C+PostgreSQL+on+Render+%7C+UUID+primary+keys" alt="Section heading"/>

</div>

```sql
-- ═══════════════════════════════════════════════════════════════════
--  👤  USERS  —  Stores login credentials
-- ═══════════════════════════════════════════════════════════════════
CREATE TABLE users (
    id            TEXT PRIMARY KEY,       -- UUID v4
    username      TEXT UNIQUE NOT NULL,   -- Login username
    password_hash TEXT NOT NULL,          -- Werkzeug PBKDF2 hash
    created_at    TEXT DEFAULT CURRENT_TIMESTAMP,
    last_login    TEXT                    -- ISO timestamp of last login
);

-- ═══════════════════════════════════════════════════════════════════
--  📦  RUNS  —  Stores packing results
-- ═══════════════════════════════════════════════════════════════════
CREATE TABLE runs (
    id            TEXT PRIMARY KEY,       -- UUID v4
    user_id       TEXT NOT NULL,          -- References users.id
    unit_w        INTEGER,                -- Cooling unit width
    unit_d        INTEGER,                -- Cooling unit depth
    unit_h        INTEGER,                -- Cooling unit height
    algorithm     TEXT,                   -- HYBRID / BFD / FFD / FF
    boxes_json    TEXT,                   -- Input box list as JSON
    results_json  TEXT,                   -- Placement results as JSON
    efficiency    REAL,                   -- Volumetric efficiency %
    units_used    INTEGER,                -- Number of cooling units opened
    boxes_placed  INTEGER,                -- Total boxes successfully placed
    runtime_ms    REAL,                   -- Algorithm execution time
    created_at    TEXT DEFAULT CURRENT_TIMESTAMP
);

-- ═══════════════════════════════════════════════════════════════════
--  💾  DATASETS  —  Stores saved box configurations
-- ═══════════════════════════════════════════════════════════════════
CREATE TABLE datasets (
    id          TEXT PRIMARY KEY,         -- UUID v4
    user_id     TEXT NOT NULL,            -- References users.id
    name        TEXT,                     -- User-given dataset name
    boxes_json  TEXT,                     -- Box list as JSON
    unit_config TEXT,                     -- Unit dimensions as JSON
    created_at  TEXT DEFAULT CURRENT_TIMESTAMP
);
```

---

<div align="center">

## 🚀 Running Locally

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=15&duration=2500&pause=800&color=90E0EF&center=true&vCenter=true&width=700&lines=Python+3.8%2B+%7C+4+steps+%7C+Zero+database+setup+needed" alt="Section heading"/>

</div>

**Requirements:** Python 3.8 or higher · Git

```bash
# ──────────────────────────────────────────────────────────────────
#  Step 1 — Clone the repository
# ──────────────────────────────────────────────────────────────────
git clone https://github.com/ShaikMuzzammil/cryopack-os.git
cd cryopack-os

# ──────────────────────────────────────────────────────────────────
#  Step 2 — Install Python packages
# ──────────────────────────────────────────────────────────────────
pip install -r requirements.txt
# on Windows:
py -m pip install -r requirements.txt

# ──────────────────────────────────────────────────────────────────
#  Step 3 — Start the server
# ──────────────────────────────────────────────────────────────────
py backend.py

# ──────────────────────────────────────────────────────────────────
#  Step 4 — Open in browser
# ──────────────────────────────────────────────────────────────────
#  http://localhost:5000
```

<div align="center">

| Environment | Database | Terminal Output |
|:-----------:|:--------:|:--------------:|
| 🖥️ **Local** | SQLite (`cryopack.db`) — auto-created, zero setup | `Mode: SQLite (Local)` |
| ☁️ **Render** | PostgreSQL — permanent cloud storage | `Mode: PostgreSQL (Render)` |

</div>

---

<div align="center">

## 🧪 Preset Test Case

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=15&duration=2500&pause=800&color=90E0EF&center=true&vCenter=true&width=700&lines=Built-in+preset+%7C+12+boxes+%7C+8×8×8+cooling+unit+%7C+39.6%25+efficiency" alt="Section heading"/>

</div>

```
  ╔══════════════════════════════════════════════════════════════════════╗
  ║  📐  Cooling Unit  :  8 × 8 × 8   (W × D × H)                      ║
  ║  📦  Unit Volume   :  512 u³                                        ║
  ╠══════════════════════════════════════════════════════════════════════╣
  ║                                                                      ║
  ║   BOX  SEQUENCE                                                      ║
  ║   ─────────────────────────────────────────────────────────────────  ║
  ║   Box  1   :  4 × 2 × 3   (V = 24 u³)                              ║
  ║   Box  2   :  4 × 2 × 3   (V = 24 u³)                              ║
  ║   Box  3   :  3 × 4 × 2   (V = 24 u³)                              ║
  ║   Box  4   :  3 × 4 × 2   (V = 24 u³)                              ║
  ║   Box  5   :  2 × 2 × 4   (V = 16 u³)                              ║
  ║   Box  6   :  2 × 2 × 4   (V = 16 u³)                              ║
  ║   Box  7   :  1 × 3 × 3   (V =  9 u³)                              ║
  ║   Box  8   :  3 × 2 × 3   (V = 18 u³)                              ║
  ║   Box  9   :  4 × 4 × 1   (V = 16 u³)                              ║
  ║   Box 10   :  2 × 2 × 2   (V =  8 u³)                              ║
  ║   Box 11   :  2 × 3 × 2   (V = 12 u³)                              ║
  ║   Box 12   :  4 × 3 × 1   (V = 12 u³)                              ║
  ║   ─────────────────────────────────────────────────────────────────  ║
  ║   Total box volume              :  203 u³                           ║
  ║   Unit capacity                 :  512 u³                           ║
  ║   Theoretical max efficiency    :   39.6%  (in 1 unit)              ║
  ║   HYBRID result                 :  All 12 boxes in 1 unit  ✅       ║
  ╚══════════════════════════════════════════════════════════════════════╝
```

---

<div align="center">

## 📊 Algorithm Performance on Preset Test Case

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=15&duration=2500&pause=800&color=90E0EF&center=true&vCenter=true&width=700&lines=All+descending-sort+algorithms+achieve+optimal+1-unit+packing" alt="Section heading"/>

</div>

<div align="center">

| Rank | Algorithm | Units Used | Efficiency | Time |
|:----:|:---------:|:----------:|:----------:|:----:|
| 🥇 | **HBF** — Hybrid Best‑Fit | **1** | **39.6%** | ~2ms |
| 🥈 | **BFD** — Best Fit Decreasing | **1** | **39.6%** | ~1ms |
| 🥉 | **FFD** — First Fit Decreasing | **1** | **39.6%** | ~1ms |
| 4️⃣ | **FF** — First Fit | **1** | **39.6%** | ~1ms |
| 5️⃣ | **NF** — Next Fit | 2 | ~19.8% | <1ms |

> *All descending‑sort algorithms achieve optimal 1‑unit packing for this test case.*

</div>

---

<div align="center">

## 👤 Author

<br/>

<a href="https://github.com/ShaikMuzzammil">
<img src="https://readme-typing-svg.demolab.com?font=Orbitron&size=26&duration=3000&pause=1000&color=00B4D8&center=true&vCenter=true&width=500&lines=Shaik+Muzzammil" alt="Author"/>
</a>

<br/><br/>

[![GitHub](https://img.shields.io/badge/GitHub-ShaikMuzzammil-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ShaikMuzzammil)
[![Live Site](https://img.shields.io/badge/Live_Site-cryopack--os.onrender.com-00b4d8?style=for-the-badge&logo=render&logoColor=white)](https://cryopack-os.onrender.com)
[![Repository](https://img.shields.io/badge/Repository-cryopack--os-2ea44f?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ShaikMuzzammil/cryopack-os)

</div>

---

<div align="center">

## 📜 License

This project is **private**. All rights reserved © 2026 Shaik Muzzammil.

</div>

---

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00b4d8,40:0077b6,80:003566,100:001d3d&height=120&section=footer&text=Made%20with%20❄️%20for%20vaccine%20cold-chain%20logistics&fontSize=14&fontColor=caf0f8&fontAlignY=60&animation=fadeIn" width="100%"/>
