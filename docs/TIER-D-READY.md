# GreenLie — Tier D Submission Pack (READY)

> **Live URLs filled.** Replace `[VIDEO_URL]` setelah upload video.

| Resource | URL |
|----------|-----|
| Live demo | https://web-flax-xi-10.vercel.app |
| GitHub | https://github.com/adindamochamad/GreenLie |
| API health | https://web-flax-xi-10.vercel.app/api/health |
| API analyze | POST https://web-flax-xi-10.vercel.app/api/analyze |
| Hackathon | https://luma.com/iw1v5erp |
| AO | https://aoagents.dev/ |
| Discord | https://discord.gg/87NPrAuDa |

---

## Step 1 — Rekam video (~30 menit)

Ikuti **`docs/VIDEO-SCRIPT.md`** — shot list AO-first, 2:45 total.

Upload ke YouTube (unlisted) atau Loom. Catat URL → ganti `[VIDEO_URL]` di bawah.

---

## Step 2 — Discord `#orchestra-project-showcase`

Copy-paste persis:

```
Team name:     Adinda Panca Mochamad (solo)
Project name:  GreenLie
Description:   GreenLie detects when coding agents "fix" CI by weakening test assertions instead of fixing bugs. When expect(status).toBe(401) becomes toBeGreaterThan(0), your board says merge but auth is broken. GreenLie scores test integrity and blocks the green lie. Built with Agent Orchestrator as workspace.
GitHub:        https://github.com/adindamochamad/GreenLie
Live demo:     https://web-flax-xi-10.vercel.app
Demo video:    [VIDEO_URL]
```

---

## Step 3 — X Thread (post as thread, tag @aoagents)

**Tweet 1/5**
```
Built GreenLie for @aoagents hackathon #agentorchestrator 🧵

Your Kanban says merge.
Your tests say pass.
Production says outage.

The agent didn't fix the bug — it fixed the test.
```

**Tweet 2/5**
```
Classic agent CI "fix":

expect(response.status).toBe(401)
              ↓
expect(response.status).toBeGreaterThan(0)

Status 500 also passes > 0.
Auth bug ships to prod. Nobody diffed the test.
```

**Tweet 3/5**
```
GreenLie side-by-side: naive merge vs integrity block.

Integrity score: 29%
5 critical findings
2/7 assertions still intact

Live demo → https://web-flax-xi-10.vercel.app

[Screenshot demo section — docs/assets/demo-section.png]
```

**Tweet 4/5**
```
Built with @aoagents — parallel agents on:
• Python backslide engine
• FastAPI + Vercel API
• Next.js demo site

This is AO's CI feedback loop failure mode — and a guardrail for it.

[AO Kanban screenshot — docs/assets/ao-kanban.png]
```

**Tweet 5/5**
```
Try it: https://web-flax-xi-10.vercel.app
GitHub: https://github.com/adindamochamad/GreenLie
Demo: [VIDEO_URL]

#agentorchestrator @aoagents
```

---

## Step 4 — LinkedIn

```
Built GreenLie for the Agent Orchestrator hackathon #agentorchestrator

When CI fails, coding agents sometimes "fix" the test instead of the bug:
→ toBe(401) becomes toBeGreaterThan(0)
→ Assertions get deleted
→ Kanban shows "Ready to merge"

GreenLie detects test backslide before merge — integrity score + findings per assertion.

Built with Agent Orchestrator as the workspace (parallel agents on engine, API, demo).

🔗 Live: https://web-flax-xi-10.vercel.app
📦 GitHub: https://github.com/adindamochamad/GreenLie
🎬 Demo: [VIDEO_URL]

Tag: Agent Orchestrator (@aoagents on X)

#agentorchestrator #devtools #ci #testing
```

---

## Step 5 — Discord `#orchestra-general`

```
Just shipped GreenLie for The Orchestra — would love feedback before deadline 🙏

Catches when agents weaken tests to pass CI (401 → toBeGreaterThan(0)).
Live: https://web-flax-xi-10.vercel.app
Video: [VIDEO_URL]

Built with AO. #agentorchestrator
```

---

## Step 6 — Engagement (jam pertama)

- [ ] Reply setiap komentar di Discord showcase
- [ ] Minta 2–3 teman RT/reply thread X dalam 60 menit
- [ ] Comment di post AO organizers jika ada
- [ ] Pin tweet thread (optional)

---

## Step 7 — Final gate (13 Aug, ≥2 jam sebelum 7 PM)

- [ ] Video URL filled di Discord + X + LinkedIn
- [ ] `./scripts/demo.sh` → 29%, 5 findings (verify)
- [ ] Live site Try It → live API response
- [ ] GitHub public ✓
- [ ] AO Kanban visible di video ✓

**Deadline: 13 Agustus 2026, 7:00 PM**

---

## Quick verify commands

```bash
curl https://web-flax-xi-10.vercel.app/api/health
curl -X POST https://web-flax-xi-10.vercel.app/api/analyze \
  -H "Content-Type: application/json" -d '{"sample":"naive-agent"}'
./scripts/demo.sh
```
