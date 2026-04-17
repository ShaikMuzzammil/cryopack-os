<div align="center">
# ❄️ CryoPack OS — v4.0 Ultimate
### Vaccine Cold-Chain Logistics — Online 3D Bin Packing System
**🌐 Live at: https://cryopack-os.onrender.com
## 📌 Problem Statement
### Problem 115 — Online 3D Bin Packing for Vaccine Cold-Chain Logistics
**Problem Definition:**
Given a sequence of 3-dimensional rectangular boxes (vaccine packages) arriving one at a time, pack them into the minimum possible number of 3D bins (cooling units / refrigerators) such that:
- No two boxes overlap
- Every box lies completely within the bin boundaries
- Each box must be placed immediately upon arrival without knowing future boxes
- Boxes may be rotated in all 6 orientations to find the best fit
- The cooling unit has fixed dimensions W × D × H
**Formal Statement:**
```
Input:
  - Cooling unit dimensions: W × D × H (e.g. 8 × 8 × 8 units)
  - Sequence of boxes: B1, B2, ..., Bn where each Bi has dimensions (wi × di × hi)
Output:
  - Assignment of each box to a bin
  - Placement coordinates (x, y, z) for each box within its bin
  - Minimize: total number of bins used
  - Maximize: volumetric efficiency (total box volume / total bin volume used)
Constraints:
  - Online: box Bi must be placed before Bi+1 is revealed
  - No overlap between any two placed boxes
  - All boxes must be within bin boundaries
  - No floating boxes (support constraint ≥ 78% base area contact)
```
**Complexity:** This is an NP-hard problem. No polynomial-time optimal algorithm is known. CryoPack OS implements 10 heuristic algorithms and compares their performance.
**Why Online (not Offline)?** In real vaccine distribution, packages arrive from manufacturers at different times. Decisions must be made immediately — you cannot wait to see all packages before loading cooling units.
---
## 🧊 What is CryoPack OS?
CryoPack OS is a **full-stack web application** that solves the Online 3D Bin Packing problem specifically for **vaccine cold-chain logistics**. It provides:
1. **Packing Engine** — runs 10 different bin packing algorithms on your box data
2. **Real-time 3D Visualization** — see exactly how boxes are packed inside cooling units using WebGL
3. **Algorithm Comparison** — run two algorithms side by side and compare with 8 detailed charts
4. **Benchmark System** — run all 10 algorithms at once and rank them by efficiency
5. **Step-by-Step Mode** — watch each box being placed one by one with animations
6. **Terminal Interface** — command-line style interaction for power users
7. **Dataset Persistence** — save box configurations and reload them anytime
8. **Run History** — all packing results saved with metrics
---
## 🌍 Why This Matters — Real World Impact
Vaccines must be maintained between **2°C and 8°C** throughout the entire supply chain. Every cooling unit uses electricity and costs money to operate. Poor packing means:
| Problem | Real Impact |
|---|---|
| Boxes packed inefficiently | More cooling units needed = higher cost |
| Wasted space in refrigerators | Same electricity cost, fewer vaccines transported |
| Suboptimal packing decisions | Longer transport times, higher risk of temperature excursion |
| No algorithm comparison | Cannot know which packing strategy is best for a given shipment |
**CryoPack OS solves this** by providing instant packing optimization with visual verification, allowing logistics planners to:
- See exactly how boxes fit before physical loading
- Compare algorithms to find which uses fewest cooling units
- Export results for documentation
- Save and reuse box configurations for recurring shipments
---
## ⚙️ How It Works
### Overall Flow
```
User configures cooling unit dimensions (W × D × H)
              ↓
User adds vaccine box types with quantities
(or loads a saved preset / dataset)
              ↓
User selects packing algorithm(s) to run
              ↓
Backend runs algorithm:
  - Sorts boxes by volume (largest first for BFD/FFD/HBF)
  - For each box tries all 6 rotations
  - Finds best position using corner-point candidates
  - Checks for overlap and support constraints
  - Assigns box to best fitting bin or opens new bin
              ↓
Returns placement coordinates for every box
              ↓
Three.js renders all boxes in 3D with colors and labels
              ↓
Charts show efficiency, units used, wasted space, runtime
              ↓
Results saved to PostgreSQL database
```
### Placement Algorithm — Corner Point Method
For each box to be placed, the algorithm:
1. Generates **candidate positions** from corners of already-placed boxes
2. Sorts candidates by priority (z-height first = gravity-like stacking)
3. For each candidate, checks:
   - Does the box fit within bin boundaries?
   - Does it overlap with any existing box?
   - Does it have sufficient support (≥78% base contact)?
4. Returns the first valid position found
### Support Constraint
A box cannot float in mid-air. The system checks that at least **78% of the box's base area** is supported by either the bin floor or other boxes below it.
```python
# A box at height z needs 78% of its base covered
supported_area = sum of overlapping area with boxes at height (z - box_height)
if supported_area >= box.w * box.d * 0.78:
    placement is valid
```
---
## ✨ All Features
### Main Dashboard (index.html)
| Feature | Description |
|---|---|
| **Dual 3D View** | Storage scene on top shows all packed cooling units. Conveyor belt scene below shows boxes travelling from entry to cooling unit |
| **Conveyor Belt Animation** | Boxes animate along a 3D conveyor belt with rollers, entry port, packing station, and connection beam to active cooling unit |
| **Fly-In Animation** | Each box flies from the packing station into its exact position inside the cooling unit with arc trajectory |
| **Step-Through Mode** | Place one box at a time — watch each placement individually |
| **Pause / Resume** | Pause the animation at any point and resume |
| **Speed Control** | Slider from 1x to 10x animation speed |
| **Expand View** | Full-screen modal for either the storage view or belt view with orbit, zoom, pan, auto-rotate, front/top/iso presets |
| **Unit Tabs** | Click any cooling unit tab to focus the 3D view on that unit |
| **Overflow Banner** | Warning shown when boxes require a second cooling unit |
| **Live Metrics** | Units used, boxes placed, volumetric efficiency %, algorithm runtime in ms |
| **Placement Log** | Scrollable log showing every box with its unit assignment and coordinates |
| **Queue System** | Add boxes by dimension, generate random boxes, load preset, clear queue |
| **Unit Config** | Set cooling unit W × D × H, shows calculated floor area, volume, estimated max boxes |
| **Run History Sidebar** | Load any previous packing run — restores all results and 3D view |
| **Dataset Save/Load** | Save current box queue to database, reload named datasets |
### Algorithm Analysis (analysis.html)
Full analysis dashboard with:
| Section | Content |
|---|---|
| **Overview** | Summary stats — best efficiency, min units, fastest time, total boxes |
| **8 Performance Charts** | Volume efficiency, cooling units required, wasted space, boxes-per-unit density, per-unit fill levels, volume by box type, algorithm runtime, box size distribution |
| **Head-to-Head Table** | Side by side comparison of all metrics with winner highlighted in gold |
| **Unit Fill Distribution** | Progress bars for every individual cooling unit showing fill % |
| **Placement Logs** | Complete I/O log with box number, name, dimensions, assigned unit, position, volume |
| **Algorithm Cards** | Detailed description of each algorithm with complexity rating |
| **Dataset Selector** | Load saved datasets directly from the analysis page |
| **Override Dims** | Change cooling unit dimensions and rerun without going back to main page |
| **Print Report** | Export full analysis as printable HTML page |
---
## ☁️ Cross‑Device Sync — Your Data Everywhere

CryoPack OS stores all your datasets, packing results, and algorithm comparisons in a **cloud PostgreSQL database** (Neon / Render). This means:

| Device | Action | What happens |
|--------|--------|---------------|
| **Laptop** | Save a dataset ("Hospital July") | Data written to cloud database |
| **Mobile** | Log in with same account | Seamlessly see "Hospital July" in your workspace |
| **Tablet** | Run a packing comparison | Result saved and available on all devices |
| **Any device** | Load a previous run | Full 3D view and metrics restored instantly |

### What is synchronised across devices (and what isn't)

| Data type | Sync behaviour | How to sync if needed |
|-----------|----------------|----------------------|
| Saved datasets (name + boxes + unit config) | ✅ **Fully synced** | Automatic – appears on all devices after login. |
| Packing run history (results, placements, efficiency) | ✅ **Fully synced** | Automatic – every run is saved to database. |
| **Current queue** (boxes waiting to be packed) | ⚠️ **Not auto‑synced** | Save the queue as a dataset (💾 button), then load it on another device. This gives you control. |
| **3D view state** (camera angle, zoom, active unit) | ❌ **Not synced** | Each device has its own screen size and preferences. Syncing camera would be disorienting. |

> ✅ **Best practice:** After adding boxes to the queue, save it as a dataset. Then you can load it on any device instantly.

### How it works (simple explanation)

1. **You log in** – your browser gets a secure session cookie (now fixed for mobile with `Secure=True` and `SameSite=None`).
2. **You save a dataset** – the frontend sends a `POST /api/datasets` with the boxes and unit dimensions.
3. **Backend stores it** – the data is saved to the `datasets` table, linked to your `user_id`.
4. **You open another device** – the frontend calls `GET /api/datasets`, which returns **all datasets you ever saved**.
5. **You load a dataset** – the backend fetches the exact box list and unit configuration, then runs the packing algorithm.

> ✅ **No manual transfer. No export/import. Just log in and your data is there.**

### Real‑world benefit for vaccine logistics

A logistics coordinator can:

- **On desktop** – design a box configuration for a new vaccine shipment, test with 10 algorithms, save the best dataset.
- **On the warehouse tablet** – load the same dataset, run the packing algorithm, and see exactly how to load the cooling unit – **in 3D**.
- **On mobile** – check the placement log and unit fill percentages while supervising the loading process.

No emailing files, no re‑entering dimensions, no version confusion. **One account, one truth.**

### Security note

- All passwords are hashed with **Werkzeug PBKDF2** – never stored in plain text.
- Session cookies are `HttpOnly`, `Secure`, and `SameSite=Lax/None` – protected against XSS and CSRF.
- Database credentials are stored as Render environment variables – never exposed in code.

### Demo (real test)

1. On your laptop, log in and save a dataset called `"Test Sync"`.
2. On your mobile, open the same URL and log in with the **same username/password**.
3. Open the Workspace sidebar → **My Datasets** – `"Test Sync"` appears instantly.
4. Load it, run packing – the 3D view shows the same boxes on both devices.

> **This works because we fixed the mobile cookie issue** – changed `SESSION_COOKIE_SECURE=True` and `SESSION_COOKIE_SAMESITE='None'` in the backend. Without these, mobile browsers would reject the session cookie.

---
## 🔢 All 10 Packing Algorithms
CryoPack OS implements **10 bin packing heuristics**, more than any similar tool:
| Key | Full Name | Strategy | Complexity | Best For |
|---|---|---|---|---|
| **HBF** | Hybrid Best-Fit | Sort descending. Best remaining space that still fits, gravity placement | O(N·B) | Highest efficiency overall |
| **BFD** | Best Fit Decreasing | Sort descending. Bin with least remaining space that fits the box | O(N·B) | Best quality/speed balance |
| **FFD** | First Fit Decreasing | Sort descending. First bin where box fits | O(N·B) | Fast, good quality |
| **FF** | First Fit | No sort. First bin where box fits | O(N·B) | Real-time online scenarios |
| **WFD** | Worst Fit Decreasing | Sort descending. Bin with MOST remaining space | O(N·B) | Spreading load evenly |
| **GU** | Guillotine | Sort descending. Minimize remaining space after placement | O(N·B) | Irregular box sizes |
| **SK** | Stack-Key | Sort descending. Lowest z-height placement position | O(N·B) | Tall box heavy loads |
| **NF** | Next Fit | No sort. Current bin only, open new if full | O(N) | Fastest possible, streaming |
| **DF** | Depth-First | Sort descending. Maximize depth (y) utilization first | O(N·B) | Deep storage optimization |
| **LF** | Layer Fill | Sort descending. Minimize z × x position score | O(N·B) | Layer-by-layer packing |
**N** = number of boxes, **B** = number of open bins
### Algorithm Selection Guide
```
Need maximum efficiency?           → Use HBF or BFD
Boxes arriving in real-time?       → Use NF or FF  
Large dataset, need speed?         → Use FFD or FF
Boxes vary greatly in size?        → Use GU or SK
Want to compare two strategies?    → Use Terminal → Option 8 Benchmark
Don't know which to pick?          → Run Benchmark — it tests all 10
```
---
## 📄 Pages and Interfaces
### Page 1 — Login / Register (`login.html`)
- Clean split-screen design — branding left, auth form right
- Toggle between Login and Register with animated tab switch
- Password strength meter (5 levels — red to green)
- Animated background with floating particles and snowflakes
- Error messages with shake animation
- Auto-redirects to main dashboard if already logged in
- Feature pills showing: 3D Packing Engine, Efficiency Analytics, Secure Workspaces, Dataset Persistence, Algorithm Reports, Real-time 3D View
### Page 2 — Main Dashboard (`index.html`)
Primary packing interface. Three-column layout:
- **Left panel** — Unit config, box input, queue, run controls
- **Center panel** — Dual 3D canvas (storage top, conveyor belt bottom) with draggable divider
- **Right panel** — Live metrics, unit breakdown, placement log
### Page 3 — Algorithm Analysis (`analysis.html`)
Full-page analysis report:
- **Left sidebar** — Section navigation (Overview, Algorithms, Comparison, Datasets, Report)
- **Main content** — Dynamic content based on selected section with Chart.js visualizations
---
## 📁 Project Structure
```
CryoPack-Os/
│
├── backend.py           # Flask server — all API routes, packing algorithms, DB
├── requirements.txt     # Python packages (Flask, gunicorn, pg8000, Werkzeug)
├── Procfile             # Render deployment — tells server to use gunicorn
├── .gitignore           # Excludes cryopack.db, __pycache__, .env
│
├── index.html           # Main dashboard — conveyor belt + dual 3D view
├── login.html           # Login and registration page
├── analysis.html        # Algorithm comparison and analysis dashboard
│
├── styles.css           # Global design system — CSS variables, reset, components
│                        # (buttons, cards, badges, forms, progress, scrollbar)
├── animations.css       # 27 keyframe animations, 10 utility classes,
│                        # 5 stagger delays, GPU helpers, reduced-motion support
├── app-main.js          # JavaScript for app-main page
│                        # (online mode, offline mode, 3D controls, queue, toast)
│
└── cryopack.db          # SQLite database — LOCAL ONLY, not in GitHub
                         # Auto-created on first run, replaced by PostgreSQL on Render
```
---
## 🛠 Tech Stack
### Backend
| Technology | Version | Purpose |
|---|---|---|
| **Python** | 3.11+ | Backend language |
| **Flask** | 2.3.3 | Web framework — routes, sessions, serving files |
| **Werkzeug** | 2.3.7 | PBKDF2 password hashing for secure authentication |
| **gunicorn** | 21.2.0 | Production WSGI server (Render deployment) |
| **pg8000** | 1.31.1 | Pure Python PostgreSQL driver — works with Python 3.14 |
| **SQLite** | built-in | Local development database — zero setup needed |
| **PostgreSQL** | 18 | Production database on Render — permanent data storage |
### Frontend
| Technology | Version | Purpose |
|---|---|---|
| **Three.js** | r128 | WebGL 3D rendering — boxes, cooling units, conveyor belt, lighting, shadows |
| **Chart.js** | 4.4.0 | 8 types of performance charts in analysis dashboard |
| **Vanilla JavaScript** | ES2020+ | All interactivity — no framework overhead |
| **CSS Custom Properties** | — | Dark theme design system with consistent tokens |
### Fonts Used
| Font | Usage |
|---|---|
| **Orbitron** | Branding, headings in terminal interface |
| **JetBrains Mono** | Terminal output, code-like labels, metrics |
| **Share Tech Mono** | Status pills, secondary monospace elements |
| **Outfit** | Body text in main dashboard |
| **Unbounded** | Large display headings in login page |
| **Syne** | Button text in main dashboard |
| **Space Mono** | Form labels, badge text |
| **Poppins** | General body text fallback |
### Deployment
| Service | Purpose |
|---|---|
| **GitHub** | Code version control — `github.com/ShaikMuzzammil/cryopack-os` |
| **Render** | Flask server hosting — free tier |
| **Render PostgreSQL** | Permanent database — free tier (90 days) |
---
## 🔌 API Reference
All API routes require login (session cookie) except auth routes.
### Authentication
| Method | Route | Body | Response |
|---|---|---|---|
| `POST` | `/api/auth/register` | `{username, password}` | `{success, user_id, username}` |
| `POST` | `/api/auth/login` | `{username, password}` | `{success, user_id, username}` |
| `POST` | `/api/auth/logout` | — | `{success}` |
| `GET` | `/api/auth/status` | — | `{authenticated, username, user_id}` |
### Packing
| Method | Route | Body | Response |
|---|---|---|---|
| `POST` | `/api/pack` | `{unit_w, unit_d, unit_h, algorithm, boxes[]}` | `{placements[], units_used, boxes_placed, efficiency, runtime_ms}` |
| `POST` | `/api/analysis/compare` | `{unit_w, unit_d, unit_h, boxes[]}` | `{HYBRID:{}, BFD:{}, FFD:{}, FF:{}}` |
### Run History
| Method | Route | Description |
|---|---|---|
| `GET` | `/api/runs` | Get last 50 runs for current user |
| `GET` | `/api/runs/<id>` | Get specific run with full placement data |
| `DELETE` | `/api/runs/<id>` | Delete a single run |
| `DELETE` | `/api/runs/all` | Delete all runs for current user |
### Datasets
| Method | Route | Description |
|---|---|---|
| `POST` | `/api/datasets` | Save a named box configuration |
| `GET` | `/api/datasets` | Get all saved datasets for current user |
| `GET` | `/api/datasets/<id>` | Get specific dataset |
| `DELETE` | `/api/datasets/<id>` | Delete a dataset |
### Static Files
| Route | Serves |
|---|---|
| `/` | login.html |
| `/index.html` | Main dashboard |
| `/analysis.html` | Analysis page |
| `/<filename>` | Any static file (CSS, JS, etc.) |
---
## 🗄 Database Schema
```sql
-- Users — stores login credentials
CREATE TABLE users (
    id            TEXT PRIMARY KEY,      -- UUID v4
    username      TEXT UNIQUE NOT NULL,  -- Login username
    password_hash TEXT NOT NULL,         -- Werkzeug PBKDF2 hash
    created_at    TEXT DEFAULT CURRENT_TIMESTAMP,
    last_login    TEXT                   -- ISO timestamp of last login
);
-- Runs — stores packing results
CREATE TABLE runs (
    id            TEXT PRIMARY KEY,      -- UUID v4
    user_id       TEXT NOT NULL,         -- References users.id
    unit_w        INTEGER,               -- Cooling unit width
    unit_d        INTEGER,               -- Cooling unit depth
    unit_h        INTEGER,               -- Cooling unit height
    algorithm     TEXT,                  -- HYBRID / BFD / FFD / FF
    boxes_json    TEXT,                  -- Input box list as JSON
    results_json  TEXT,                  -- Placement results as JSON
    efficiency    REAL,                  -- Volumetric efficiency %
    units_used    INTEGER,               -- Number of cooling units opened
    boxes_placed  INTEGER,               -- Total boxes successfully placed
    runtime_ms    REAL,                  -- Algorithm execution time
    created_at    TEXT DEFAULT CURRENT_TIMESTAMP
);
-- Datasets — stores saved box configurations
CREATE TABLE datasets (
    id          TEXT PRIMARY KEY,        -- UUID v4
    user_id     TEXT NOT NULL,           -- References users.id
    name        TEXT,                    -- User-given dataset name
    boxes_json  TEXT,                    -- Box list as JSON
    unit_config TEXT,                    -- Unit dimensions as JSON
    created_at  TEXT DEFAULT CURRENT_TIMESTAMP
);
```
---
## 🚀 Running Locally
### Requirements
- Python 3.8 or higher
- Git
### Steps
```bash
# 1. Clone the repository
git clone https://github.com/ShaikMuzzammil/cryopack-os.git
cd cryopack-os
# 2. Install Python packages
pip install -r requirements.txt
# or on Windows:
py -m pip install -r requirements.txt
# 3. Start the server
py backend.py
# 4. Open browser and go to:
# http://localhost:5000
```
When you run locally:
- App automatically uses **SQLite** (`cryopack.db`)
- Database file is created automatically on first run
- No database setup needed
- Terminal will print: `Mode: SQLite (Local)`
When deployed on Render:
- App automatically switches to **PostgreSQL**
- Terminal prints: `Mode: PostgreSQL (Render)`
- All data is permanently stored
---
## 🧪 Problem 115 Preset Test Case
The built-in preset loads the official Problem 115 test case:
```
Cooling Unit:  8 × 8 × 8  (W × D × H)
Unit Volume:   512 u³
Box Sequence:
  Box 1:  4 × 2 × 3  (V = 24)
  Box 2:  4 × 2 × 3  (V = 24)
  Box 3:  3 × 4 × 2  (V = 24)
  Box 4:  3 × 4 × 2  (V = 24)
  Box 5:  2 × 2 × 4  (V = 16)
  Box 6:  2 × 2 × 4  (V = 16)
  Box 7:  1 × 3 × 3  (V = 9)
  Box 8:  3 × 2 × 3  (V = 18)
  Box 9:  4 × 4 × 1  (V = 16)
  Box 10: 2 × 2 × 2  (V = 8)
  Box 11: 2 × 3 × 2  (V = 12)
  Box 12: 4 × 3 × 1  (V = 12)
Total box volume: 203 u³
Unit capacity:    512 u³
Theoretical max efficiency (1 unit): 39.6%
HYBRID result: All 12 boxes in 1 unit — 39.6% efficiency
```
---
## 📊 Algorithm Performance on Problem 115
| Rank | Algorithm | Units Used | Efficiency | Time |
|---|---|---|---|---|
| 1 | HBF — Hybrid Best-Fit | 1 | 39.6% | ~2ms |
| 2 | BFD — Best Fit Decreasing | 1 | 39.6% | ~1ms |
| 3 | FFD — First Fit Decreasing | 1 | 39.6% | ~1ms |
| 4 | FF — First Fit | 1 | 39.6% | ~1ms |
| 5 | NF — Next Fit | 2 | ~19.8% | <1ms |
*All descending-sort algorithms achieve optimal 1-unit packing for this test case.*
---
## 👤 Author
**Shaik Muzzammil**
- 🐙 GitHub: [ShaikMuzzammil](https://github.com/ShaikMuzzammil)
- 🌐 Live Site: [https://cryopack-os.onrender.com](https://cryopack-os.onrender.com)
- 📦 Repository: [github.com/ShaikMuzzammil/cryopack-os](https://github.com/ShaikMuzzammil/cryopack-os)
---
## 📜 License
This project is private. All rights reserved © 2026 Shaik Muzzammil.
---
<div align="center">
Made with ❄️ for vaccine cold-chain logistics optimization
</div>
