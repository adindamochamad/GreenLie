# GreenLie — YouTube Upload (The Orchestra / AO Hackathon)

> **Setelah upload:** copy URL → ganti `[VIDEO_URL]` di `docs/TIER-D-READY.md` → lanjut Discord + X + LinkedIn.

---

## Settings YouTube (wajib)

| Field | Value |
|-------|--------|
| **Visibility** | **Unlisted** (bukan Private — juri harus bisa buka link) |
| **Category** | Science & Technology |
| **Language** | English |
| **Audience** | Not made for kids |
| **Comments** | On (optional, untuk engagement) |

---

## Title (copy-paste, pilih satu)

**Recommended:**
```
GreenLie — Catch When AI "Fixes" Tests Instead of Bugs | Agent Orchestrator Hackathon #agentorchestrator
```

**Alternatif lebih pendek:**
```
GreenLie Demo — The Orchestra Hackathon (Agent Orchestrator) #agentorchestrator
```

**Alternatif non-teknis:**
```
When Every Check Is Green But the Bug Is Still There — GreenLie | #agentorchestrator
```

---

## Description (copy-paste)

```
GreenLie — demo for The Orchestra hackathon (Agent Orchestrator).

Your board says ship. Your tests say pass. But the AI didn't fix the app — it made the test easier to pass. GreenLie catches that before merge.

Built with Agent Orchestrator as the workspace — parallel AI agents on engine, website, API, and samples (real AO Kanban shown in video).

🔗 Live demo: https://web-flax-xi-10.vercel.app
📦 GitHub: https://github.com/adindamochamad/GreenLie
🛠 Agent Orchestrator: https://aoagents.dev/
🏆 Hackathon: https://luma.com/iw1v5erp

Try it yourself:
• Open the live demo → scroll to "Try It" → click analyze
• Or clone the repo and run: ./scripts/demo.sh

Built by Adinda Panca Mochamad (solo)

#agentorchestrator #AgentOrchestrator #TheOrchestra #GreenLie #devtools #testing #ci #hackathon #aiagents

---
Timestamps (edit if your video differs):
0:00 — The problem (green checks, hidden bug)
0:15 — Built with Agent Orchestrator (Kanban board)
0:50 — Naive merge vs GreenLie block
1:15 — Live scan on demo site
1:35 — Command-line proof
2:00 — Links & wrap-up
```

---

## Tags (copy-paste, comma-separated di YouTube)

```
agent orchestrator, agentorchestrator, the orchestra hackathon, greenlie, ai coding agents, test integrity, ci cd, devtools, hackathon demo, aoagents, software testing, ai agents, kanban
```

**Max ~500 chars — YouTube allows ~15 tags. Prioritas:**
1. `agent orchestrator`
2. `agentorchestrator`
3. `the orchestra hackathon`
4. `greenlie`
5. `aoagents`
6. `ai coding agents`
7. `devtools`
8. `ci cd`
9. `software testing`
10. `hackathon demo`

---

## Thumbnail (optional tapi bagus)

**Teks di thumbnail (Canva / Figma, 1280×720):**
```
GreenLie
CI passed. Tests lied.
#agentorchestrator
```

**Warna:** background gelap (#0d0f0c), teks hijau (#3dff7a) + merah untuk "lied"

**Screenshot:** frame AO Kanban atau website 29% integrity

---

## Upload checklist (centang saat selesai)

- [ ] Video file uploaded (MP4/MOV)
- [ ] Visibility = **Unlisted**
- [ ] Title includes **Agent Orchestrator** + **#agentorchestrator**
- [ ] Description has: live demo, GitHub, aoagents.dev, hackathon link
- [ ] Tags include `agent orchestrator` and `agentorchestrator`
- [ ] Video plays correctly (audio + AO Kanban section visible)
- [ ] Copy video URL → paste ke `docs/TIER-D-READY.md` (replace `[VIDEO_URL]`)
- [ ] Test URL in incognito / logged-out browser

---

## Setelah dapat URL

```bash
# 1. Ganti [VIDEO_URL] di TIER-D-READY (manual atau sed)
# 2. Buka helper submission
./scripts/post-tier-d.sh
```

**Format URL:** `https://www.youtube.com/watch?v=XXXXXXXXXXX`  
**Shorts:** hindari — pakai video biasa landscape untuk demo hackathon.

---

## Rules hackathon — mapping

| Rule | Cara dipenuhi di YouTube |
|------|---------------------------|
| Demo video required | Unlisted link di Discord showcase |
| AO Kanban in video | Scene 2 di video kamu + sebut di description |
| Public GitHub | Link di description |
| Live demo | Link di description |
| `#agentorchestrator` | Title atau description + tags |
| Tag @aoagents (X/LinkedIn) | Di post sosial, bukan YouTube |

---

## Quick upload flow (5 menit)

1. Buka https://studio.youtube.com → **Create** → **Upload video**
2. Drop file video kamu
3. Paste **Title** + **Description** + **Tags** dari dokumen ini
4. Visibility → **Unlisted** → **Publish**
5. Copy link → update `TIER-D-READY.md`
6. Discord `#orchestra-project-showcase` (Step 2)
