# GreenLie

**Detektor saat agent "memperbaiki" CI dengan melemahkan test — bukan memperbaiki bug.**

> What happens when your agent "fixes" CI by weakening the test — and your Kanban board says ready to merge?

Built for [The Orchestra](https://luma.com/iw1v5erp) — Agent Orchestrator's first hackathon · workspace: [Agent Orchestrator](https://aoagents.dev/)

> **Konteks lengkap proyek:** lihat [`CONTEXT.md`](CONTEXT.md) — hackathon rules, strategi, arsitektur, timeline, submission checklist.

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
| **Website + API** | https://web-flax-xi-10.vercel.app |
| **Demo video** | https://youtu.be/RmDVxPWPBzU |
| **GitHub** | https://github.com/adindamochamad/GreenLie |
| **Hackathon** | [The Orchestra](https://luma.com/iw1v5erp) · Built with [Agent Orchestrator](https://aoagents.dev/) |

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

## Where it fits in an AO workflow

After an agent "fixes" CI, run GreenLie **before merge**:

```bash
greenlie analyze --before ./path/to/tests-before --after ./path/to/tests-after
# exit 0 = no backslide · exit 1 = weakened tests ? block merge
```

In [Agent Orchestrator](https://aoagents.dev/)'s CI feedback loop, this is the guardrail between *agent fixed CI* and *board says merge*.

This repo's GitHub Action runs the same check on every push — see [`.github/workflows/ci.yml`](.github/workflows/ci.yml).

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
