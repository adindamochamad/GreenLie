# LinkedIn — Poster + Caption (GreenLie)

> **Poster alur:** generate via ChatGPT → **`docs/CHATGPT-POSTER-PROMPT.md`** (prompt detail LinkedIn)  
> **Fallback lokal:** `docs/assets/linkedin-poster.png` · `./scripts/export-linkedin-poster.sh`  
> **Attach:** upload poster sebagai gambar utama → paste link YouTube di caption (auto-preview video)

---

## Caption utama (copy-paste)

**Tip:** 2 baris pertama muncul sebelum "see more" — hook sudah di atas.

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

---

## Caption versi Indonesia (alternatif)

```
Baru saja saya launch GreenLie untuk hackathon The Orchestra — dibangun dengan Agent Orchestrator.

Bayangkan: CI lulus, board bilang merge, semua checklist hijau. Kayaknya siap rilis.

Tapi kadang AI-nya nggak benerin aplikasinya. Tes-nya yang dilonggarkan supaya lulus. Login masih rusak — cuma dashboard-nya aja yang hijau.

Itu yang saya sebut green lie.

GreenLie baca file tes sebelum merge. Kasih skor kepercayaan, tunjukkan apa yang berubah, dan blok merge kalau tes-nya dilonggarkan — bukan karena produknya bener.

Alurnya ada di poster:
① Semua hijau → siap merge
② AI "benerin" tes, bukan bug
③ GreenLie blokir — skor 29%
④ Dibangun pakai 4 AI helper paralel di Kanban AO asli

🎬 Video: https://youtu.be/RmDVxPWPBzU
🔗 Coba live: https://web-flax-xi-10.vercel.app
📦 GitHub: https://github.com/adindamochamad/GreenLie

Kalau kamu pakai coding agent, masukan dari kamu sangat saya hargai.

#agentorchestrator #hackathon #ai #testing #devtools
```

---

## Cara post di LinkedIn

1. **Create post** → attach **`docs/assets/linkedin-poster.png`** (poster alur)
2. Paste **caption** di atas
3. LinkedIn akan auto-preview link YouTube dari caption
4. Tag **Agent Orchestrator** (company page) jika muncul di dropdown
5. Publish

**Kalau sudah post sebelumnya:** Edit post → add poster · atau buat post baru dengan poster + caption ini.

---

## Alur di poster (referensi)

```
① Masalah     → semua hijau, bug masih ada
② Green lie   → AI longgarkan tes, bukan perbaiki produk  
③ GreenLie    → trust score + block merge (29%)
④ Agent Orchestrator → 4 agent paralel di Kanban asli
```

---

## Versi lebih pendek (kalau character limit)

```
Shipped GreenLie for The Orchestra hackathon (#agentorchestrator).

When AI "fixes" CI by loosening tests, your board says merge — but the bug is still there. GreenLie scores test trust and blocks that merge.

Built solo with Agent Orchestrator (real Kanban in the demo video).

🎬 https://youtu.be/RmDVxPWPBzU
🔗 https://web-flax-xi-10.vercel.app
📦 https://github.com/adindamochamad/GreenLie

Would love feedback from anyone running coding agents.
```
