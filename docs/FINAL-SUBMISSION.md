# Final Submission — The Orchestra (Official Template)

> **Deadline extended:** 14 Agustus 2026, **12:30 AM IST** (= **02:00 WIB** / **04:00 SGT**)
>
> **Post di:** Discord `#orchestra-project-showcase`
>
> **Checklist resmi:** https://maaztwts.notion.site/The-Orchestra-3b532902e4a38040aedbc66966f4fc06

---

## Copy-paste ke Discord (isi link X + LinkedIn dulu)

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

---

## Pre-submit checklist

- [ ] X thread live dengan `#agentorchestrator` + tag @aoagents
- [ ] LinkedIn post live dengan `#agentorchestrator`
- [ ] **X Post Link** dan **LinkedIn Post Link** sudah diisi di template atas
- [ ] Post final submission text di `#orchestra-project-showcase` (format resmi di atas)
- [ ] GitHub repo public + README + CI badge
- [ ] Live demo Try It works: https://web-flax-xi-10.vercel.app
- [ ] Demo video plays + AO Kanban visible
- [ ] Notion Submission Checklist reviewed

## Quick verify

```bash
curl https://web-flax-xi-10.vercel.app/api/health
curl -X POST https://web-flax-xi-10.vercel.app/api/analyze \
  -H "Content-Type: application/json" -d '{"sample":"naive-agent"}'
./scripts/demo.sh
```
