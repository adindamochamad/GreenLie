# GreenLie — Tier D Submission Pack (READY)

> **Semua URL siap** — demo video: https://youtu.be/RmDVxPWPBzU

| Resource | URL |
|----------|-----|
| Live demo | https://web-flax-xi-10.vercel.app |
| GitHub | https://github.com/adindamochamad/GreenLie |
| Demo video | https://youtu.be/RmDVxPWPBzU |
| API health | https://web-flax-xi-10.vercel.app/api/health |
| API analyze | POST https://web-flax-xi-10.vercel.app/api/analyze |
| Hackathon | https://luma.com/iw1v5erp |
| AO | https://aoagents.dev/ |
| Discord | https://discord.gg/87NPrAuDa |

---

## Step 1 — Upload video ke YouTube ✅

**Done:** https://youtu.be/RmDVxPWPBzU

---

## Step 2 — Discord `#orchestra-project-showcase` (FINAL — official template)

> **Deadline:** 14 Agustus 2026, **12:30 AM IST** (02:00 WIB)
>
> **Full pack:** [`docs/FINAL-SUBMISSION.md`](FINAL-SUBMISSION.md)

Copy-paste (isi **X Post Link** + **LinkedIn Post Link** dulu):

```
**Team Name:** Adinda Panca Mochamad (solo)

**Team Members:** Adinda Panca Mochamad

**Project Name:** GreenLie

**Short Description:** GreenLie is a test integrity guard for agentic CI. It catches when AI coding agents "fix" failing CI by weakening test assertions instead of fixing the actual bug — your Kanban says merge, every check looks green, but the bug can still ship. GreenLie scores assertion integrity (sample: 29%) and blocks merge when tests were loosened, not when the product was fixed.

**GitHub Repo:** https://github.com/adindamochamad/GreenLie

**Live Link:** https://web-flax-xi-10.vercel.app

**Demo Video:** https://youtu.be/RmDVxPWPBzU

**X Post Link:** https://x.com/adindacq/status/2087568818956824691

**LinkedIn Post Link:** https://lnkd.in/p/gQNncPvH

**How we used AO:** Built the entire project in Agent Orchestrator as the workspace. Ran four parallel agents on separate workstreams — Python backslide engine, FastAPI/Vercel API, Next.js demo site, and sample test fixtures — coordinated through the AO Kanban board. Demo video includes real AO Kanban footage showing cards move across engine, web, api, and samples branches. GreenLie directly addresses AO's CI feedback loop failure mode: when an agent "fixes" CI by editing tests instead of code, GreenLie is the guardrail before merge.
```

<details>
<summary>Legacy showcase post (optional — sudah dipost sebelumnya)</summary>

```
Hey everyone!

I'm Adinda Panca Mochamad (solo) and I just shipped GreenLie for The Orchestra hackathon.

GreenLie catches a failure mode when AI coding agents "fix" CI by weakening tests instead of fixing the actual bug. Your Kanban says merge, every check looks green — but the bug can still ship. For example: a login test that used to check for a real error now accepts almost any response, so even a broken server looks fine.

GreenLie scores test integrity and blocks the merge when tests were loosened, not when the product was fixed.

I built it with Agent Orchestrator as my workspace — four parallel agents on the engine, website, API, and sample files. The demo video shows the real AO Kanban board.

Live demo: https://web-flax-xi-10.vercel.app
GitHub: https://github.com/adindamochamad/GreenLie
Demo video: https://youtu.be/RmDVxPWPBzU

Feedback welcome — #agentorchestrator
```

</details>

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
Demo: https://youtu.be/RmDVxPWPBzU

#agentorchestrator @aoagents
```

---

## Step 4 — LinkedIn

**Poster:** ChatGPT → `docs/CHATGPT-POSTER-PROMPT.md` · **Caption:** `docs/LINKEDIN-POST.md`

```
I just shipped GreenLie for The Orchestra hackathon — built with Agent Orchestrator.

Picture this: CI passes, your board says merge, every checklist is green. Looks ready to ship.

But sometimes the AI didn't fix the app. It loosened the test so it would pass. Login can still be broken — and nobody noticed because the dashboard looks fine.

I call that the green lie.

GreenLie reads the test file before merge. It gives a trust score, flags what changed, and blocks the merge when the test was weakened — not when the product was actually fixed.

The demo video walks through the full flow:
① Everything looks green → ready to merge
② AI "fixes" the test, not the bug
③ GreenLie blocks — 29% trust score
④ Built with four parallel AI helpers on a real AO Kanban board

🎬 Watch: https://youtu.be/RmDVxPWPBzU
🔗 Try live: https://web-flax-xi-10.vercel.app
📦 GitHub: https://github.com/adindamochamad/GreenLie

If you ship with coding agents, I'd genuinely love your feedback.

#agentorchestrator #hackathon #ai #testing #devtools

Built for The Orchestra · Agent Orchestrator
```

Attach poster sebagai gambar utama post.

---

## Step 5 — Discord `#orchestra-general`

```
Just shipped GreenLie for The Orchestra — would love feedback before deadline 🙏

Catches when agents weaken tests to pass CI (401 → toBeGreaterThan(0)).
Live: https://web-flax-xi-10.vercel.app
Video: https://youtu.be/RmDVxPWPBzU

Built with AO. #agentorchestrator
```

---

## Step 6 — Engagement (jam pertama)

- [x] Discord `#orchestra-project-showcase` posted
- [x] X thread posted (@aoagents #agentorchestrator)
- [x] LinkedIn posted
- [ ] Reply setiap komentar di Discord showcase (ongoing)
- [ ] Minta 2–3 teman RT/reply thread X dalam 60 menit (optional)
- [ ] Comment di post AO organizers jika ada (optional)
- [ ] Pin tweet thread (optional)

---

## Step 7 — Final gate

- [x] Video URL filled di Discord + X + LinkedIn
- [x] Discord showcase posted (legacy format)
- [ ] **Final submission repost** dengan official template (`docs/FINAL-SUBMISSION.md`)
- [ ] **X Post Link** + **LinkedIn Post Link** diisi di submission
- [x] X thread posted
- [x] LinkedIn posted
- [ ] `./scripts/demo.sh` → 29%, 5 findings (verify)
- [ ] Live site Try It → live API response
- [x] GitHub public ✓
- [x] AO Kanban visible di video ✓
- [ ] Notion Submission Checklist reviewed

**Deadline: 14 Agustus 2026, 12:30 AM IST** (02:00 WIB)

---

## Quick verify commands

```bash
curl https://web-flax-xi-10.vercel.app/api/health
curl -X POST https://web-flax-xi-10.vercel.app/api/analyze \
  -H "Content-Type: application/json" -d '{"sample":"naive-agent"}'
./scripts/demo.sh
```
