# Demo Video Script — GreenLie (2:45)

> **Rules:** Demo video WAJIB menampilkan AO Kanban. AO footage = 35%+ screen time.

---

## Pre-recording checklist

- [ ] AO terbuka dengan project GreenLie visible
- [ ] Terminal di `GreenLie/` folder
- [ ] Browser tab: https://web-flax-xi-10.vercel.app
- [ ] Screen recorder: QuickTime / OBS / Loom (1080p, mic on)
- [ ] Notifikasi dimatikan

---

## Shot list

| Time | Scene | Action | Audio (narasi) |
|------|-------|--------|----------------|
| **0:00–0:15** | Terminal atau black | Hook text optional | *"CI passed. Auth was broken. The agent didn't fix the bug — it fixed the test."* |
| **0:15–0:50** | **AO Kanban FULL SCREEN** | Scroll cards: engine, web, api, samples. Tunjukkan status cards. | *"GreenLie was built with Agent Orchestrator — parallel agents on engine, API, and demo site."* |
| **0:50–1:15** | Website hero | Scroll ke `#demo` | *"Same agent fix. Two outcomes. Naive merge — board green, CI pass."* |
| **1:15–1:30** | Website demo toggle | Klik **GreenLie block** | *"GreenLie: integrity 29%. Five critical findings. Merge blocked."* |
| **1:30–1:50** | Website Try It | Klik `greenlie analyze` | *"Live API scan — same engine, same sample."* |
| **1:50–2:10** | Terminal | `./scripts/demo.sh` | *"CLI: GL-001 — toBe(401) became toBeGreaterThan(0). Status 500 also passes."* |
| **2:10–2:30** | Split: GitHub + AO | Show repo + Kanban PiP | *"Open source. Built for The Orchestra hackathon."* |
| **2:30–2:45** | End card | URLs on screen | *"Try it at web-flax-xi-10.vercel.app. GreenLie — CI passed. Tests lied."* |

---

## GL-001 highlight (zoom terminal)

```
[CRITICAL] GL-001
  Before: expect(response.status).toBe(401);
  After:  expect(response.status).toBeGreaterThan(0);
```

Pause 3 detik. Narasi: *"500 also passes greater than zero."*

---

## Recording commands

```bash
# Terminal demo (record this window)
cd /Users/mac/Development/GreenLie
./scripts/demo.sh

# Open site
open https://web-flax-xi-10.vercel.app

# Open AO
open -a "Agent Orchestrator"
```

---

## Upload

1. YouTube → Unlisted → copy link
2. Atau Loom → copy link
3. Paste ke `docs/TIER-D-READY.md` — replace `[VIDEO_URL]`
4. Post Discord + X + LinkedIn dari file yang sama

---

## PiP tip (optional, +impact)

Saat demo website (0:50+), kecilkan AO Kanban di corner kanan bawah — juri selalu lihat AO selama produk demo.

---

## End card text (screenshot or slide)

```
GreenLie
https://web-flax-xi-10.vercel.app
https://github.com/adindamochamad/GreenLie
#agentorchestrator · Built with Agent Orchestrator
```
