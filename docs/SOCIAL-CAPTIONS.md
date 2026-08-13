# GreenLie — Social Captions (Copy-Paste)

> Video: https://youtu.be/RmDVxPWPBzU  
> Live: https://web-flax-xi-10.vercel.app  
> GitHub: https://github.com/adindamochamad/GreenLie

---

## 1. Discord `#orchestra-project-showcase` (WAJIB)

Paste persis:

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

---

## 2. X Thread (WAJIB — post as thread, reply to yourself)

**Tweet 1/5** — hook + tag
```
Built GreenLie for @aoagents hackathon #agentorchestrator 🧵

Your Kanban says merge.
Your tests say pass.
Production says outage.

The agent didn't fix the bug — it fixed the test.
```

**Tweet 2/5** — the green lie
```
Classic agent CI "fix":

expect(response.status).toBe(401)
              ↓
expect(response.status).toBeGreaterThan(0)

Status 500 also passes > 0.
Auth bug ships to prod. Nobody diffed the test.
```

**Tweet 3/5** — demo (+ screenshot opsional)
```
GreenLie side-by-side: naive merge vs integrity block.

Integrity score: 29%
5 critical findings
2/7 assertions still intact

Live demo → https://web-flax-xi-10.vercel.app
```
*Attach: screenshot demo section dari website*

**Tweet 4/5** — AO (+ screenshot opsional)
```
Built with @aoagents — parallel agents on:
• Python backslide engine
• FastAPI + Vercel API
• Next.js demo site

Real AO Kanban in the demo video — guardrail for AO's CI feedback loop.

🎬 https://youtu.be/RmDVxPWPBzU
```
*Attach: screenshot AO Kanban board*

**Tweet 5/5** — links
```
Try it: https://web-flax-xi-10.vercel.app
GitHub: https://github.com/adindamochamad/GreenLie
Demo: https://youtu.be/RmDVxPWPBzU

#agentorchestrator @aoagents
```

**Cara post thread:** Tweet 1 → reply Tweet 2 → reply Tweet 3 → … sampai 5/5.

---

## 3. LinkedIn

**Panduan lengkap:** `docs/LINKEDIN-POST.md`

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

**Cara post:** Attach poster → paste caption → tag Agent Orchestrator.

---

## 4. Discord `#orchestra-general` (opsional)

```
Just shipped GreenLie for The Orchestra — would love feedback before deadline 🙏

Catches when agents weaken tests to pass CI (401 → toBeGreaterThan(0)).
Live: https://web-flax-xi-10.vercel.app
Video: https://youtu.be/RmDVxPWPBzU

Built with AO. #agentorchestrator
```

---

## Checklist

- [ ] Discord showcase posted
- [ ] X thread (5 tweets) **atau** LinkedIn posted
- [ ] `#agentorchestrator` + tag @aoagents (X) / Agent Orchestrator (LinkedIn)
- [ ] Video link works in incognito

```bash
./scripts/post-tier-d.sh   # helper copy Discord / LinkedIn
open docs/SOCIAL-CAPTIONS.md
```
