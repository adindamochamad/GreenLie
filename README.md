# GreenLie

**Detektor saat agent "memperbaiki" CI dengan melemahkan test ù bukan memperbaiki bug.**

> What happens when your agent "fixes" CI by weakening the test ù and your Kanban board says ready to merge?

Built for [The Orchestra](https://luma.com/iw1v5erp) ù Agent Orchestrator's first hackathon.

> **Konteks lengkap proyek:** lihat [`CONTEXT.md`](CONTEXT.md) ù hackathon rules, strategi, arsitektur, timeline, submission checklist.

---

## The Problem

Agentic coding workflows promise: CI fails ? agent fixes ? merge.

The failure mode nobody talks about:

- CI fails on `expect(status).toBe(401)`
- Agent changes it to `expect(status).toBeGreaterThan(0)`
- Board shows **Ready to merge**
- Production shows **outage**

GreenLie catches the green lie before it ships.

---

## Live Demo

| | URL |
|---|---|
| **Website + API** | https://web-flax-xi-10.vercel.app (`/api/analyze`, `/api/health`) |
| **GitHub** | https://github.com/adindamochamad/GreenLie |

---

## Quick Try

```bash
git clone https://github.com/adindamochamad/GreenLie
cd GreenLie

./scripts/demo.sh
```

Expected output:

```
Integrity Score: 29%
Assertions: 2/7 intact
Findings: 5 critical
Exit code: 1 (test backslide detected)
```

---

## What GreenLie Detects

| Pattern | Before | After | Verdict |
|---------|--------|-------|---------|
| Exact ? range | `toBe(401)` | `toBeGreaterThan(0)` | TEST_BACKSLIDE |
| Exact ? truthy | `toBe('Unauthorized')` | `toBeDefined()` | TEST_BACKSLIDE |
| Assertion removed | `expect(id).toBe('user-123')` | *(deleted)* | ASSERTION_DROPPED |

---

## Stack

| Layer | Tech |
|-------|------|
| Engine | Python 3.11+ |
| API | FastAPI |
| Demo | Next.js 15 |
| Built with | [Agent Orchestrator](https://aoagents.dev/) |

---

## License

MIT
