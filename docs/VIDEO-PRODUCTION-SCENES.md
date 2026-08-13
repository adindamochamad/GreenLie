# GreenLie — Video Production (Flow + Screen Record + ElevenLabs)

> **Total:** ~2:45 (165 detik) · **Rules AO:** Kanban footage ≥35% screen time (Scene 2 + PiP Scene 8)
>
> **Workflow:** Generate visual per scene → Generate audio per scene di ElevenLabs → Edit di CapCut/Descript (sync per scene)

---

## Setup ElevenLabs (semua scene)

| Setting | Value |
|---------|-------|
| **Voice** | `Josh` atau `Adam` (Professional, calm dev-tool tone) |
| **Model** | Eleven Multilingual v2 |
| **Stability** | 55% |
| **Similarity** | 80% |
| **Style exaggeration** | 10% |
| **Speed** | 1.0 (normal) — Scene 7 turunkan ke 0.95 untuk GL-001 |
| **Format export** | MP3 per scene (`scene-01.mp3` … `scene-09.mp3`) |

**Tip sync:** Setiap scene generate audio **terpisah**. Di editor, drag audio ke timeline scene visual — potong/extend visual jika perlu.

---

## Timeline overview

| Scene | Durasi | Visual | Audio file |
|-------|--------|--------|------------|
| 01 Hook | 12s | Google Flow | `scene-01.mp3` |
| 02 AO Kanban | 42s | Screen record | `scene-02.mp3` |
| 03 Hero | 14s | Screen record | `scene-03.mp3` |
| 04 Naive merge | 10s | Screen record | `scene-04.mp3` |
| 05 GreenLie block | 14s | Screen record | `scene-05.mp3` |
| 06 Try It | 16s | Screen record | `scene-06.mp3` |
| 07 Terminal | 22s | Screen record | `scene-07.mp3` |
| 08 GitHub + AO PiP | 15s | Screen record | `scene-08.mp3` |
| 09 End card | 20s | Flow atau static | `scene-09.mp3` |
| **Total** | **165s** | | |

---

## Scene 01 — Hook (Google Flow)

**Durasi visual:** 12 detik  
**Durasi audio target:** 11 detik (1s tail silence)

### Visual — Google Flow

**Tool:** [Google Flow](https://labs.google/fx) · Model **Veo 3.1**

**Prompt:**
```
Cinematic close-up of a dark software engineering workspace at night. A green CI badge glows "PASS" on a monitor, then flickers red. Reflection in developer glasses. Shallow depth of field, moody teal and rust orange accent lighting, subtle screen glow, no readable text on screens, 4K film grain, slow push-in camera, dramatic but realistic.
```

**Negative / avoid:** readable code, logos, faces looking at camera, cartoon style

**Export:** 12s, 16:9, 1080p minimum

### Audio — ElevenLabs (Scene 01)

**Script (copy exact):**
```
CI passed. Auth was broken. The agent didn't fix the bug — it fixed the test.
```

| Metrik | Value |
|--------|-------|
| Kata | 16 |
| Target WPM | ~87 (deliberate, pauses on punctuation) |
| Emphasis | Pause 0.5s after "CI passed." dan after "broken." |

**Sync cue:** VO starts at **0:01** (1 detik after cut from black). Visual red flicker di **0:08–0:10**.

---

## Scene 02 — AO Kanban (Screen Record) ⭐ WAJIB

**Durasi visual:** 42 detik  
**Durasi audio target:** 38 detik (4s scroll tanpa VO di akhir)

### Visual — Screen Record

**Tool:** Screen Studio atau QuickTime · **Full screen AO app**

**Pre-flight:**
```bash
open -a "Agent Orchestrator"
```

**Action shot list:**

| Waktu relatif | Action |
|---------------|--------|
| 0:00–0:03 | Full screen AO project **GreenLie** — hold |
| 0:03–0:12 | Scroll perlahan: card `engine/backslide-detector` → Ready |
| 0:12–0:22 | Scroll ke `web/demo-bersebelahan` → In review |
| 0:22–0:32 | Scroll ke `api/fastapi-wrapper` + `samples/naive-agent-fix` → Working |
| 0:32–0:42 | Hold wide shot Kanban — jangan cut terlalu cepat |

**Catatan:** Cards harus **asli dari AO app**, bukan website mockup.

### Audio — ElevenLabs (Scene 02)

**Script:**
```
GreenLie was built with Agent Orchestrator as the workspace. Parallel agents shipped the Python engine, the API, the demo site, and the sample fixtures — all visible on this board.
```

| Metrik | Value |
|--------|-------|
| Kata | 32 |
| Target WPM | ~105 |
| Emphasis | Stress "Agent Orchestrator" dan "parallel agents" |

**Sync cue:**
- "GreenLie was built…" → mulai saat Kanban full screen (**0:02**)
- "Python engine…" → saat scroll ke engine card (**0:08**)
- "demo site…" → saat scroll ke web card (**0:18**)
- Last 4 detik: **no VO** — biarkan Kanban breathe

---

## Scene 03 — Website Hero (Screen Record)

**Durasi visual:** 14 detik  
**Durasi audio target:** 13 detik

### Visual — Screen Record

**URL:** https://web-flax-xi-10.vercel.app

| Waktu | Action |
|-------|--------|
| 0:00–0:05 | Load page — hero visible: "Your board says merge" |
| 0:05–0:10 | Hover badge "CI PASS \| 44/44 tests" |
| 0:10–0:14 | Slow scroll mulai turun ke problem section |

**Screen Studio:** enable zoom on green "merge" text at 0:06

### Audio — ElevenLabs (Scene 03)

**Script:**
```
Your Kanban says merge. Your tests say pass. Same agent fix — but two very different outcomes.
```

| Metrik | Value |
|--------|-------|
| Kata | 17 |
| Emphasis | Lower tone on "pass" · slight tension on "two very different outcomes" |

**Sync cue:** "Your Kanban says merge" sync dengan headline visible (**0:02**)

---

## Scene 04 — Naive Merge (Screen Record)

**Durasi visual:** 10 detik  
**Durasi audio target:** 9 detik

### Visual — Screen Record

**URL:** https://web-flax-xi-10.vercel.app/#demo

| Waktu | Action |
|-------|--------|
| 0:00–0:02 | Side-by-side demo visible |
| 0:02–0:04 | Click **Naive merge** button |
| 0:04–0:10 | Hold panel kanan: green "Ready to merge" · "44/44 tests passed" |

### Audio — ElevenLabs (Scene 04)

**Script:**
```
Naive merge: CI passes, board goes green, and nobody diffed the test file.
```

| Metrik | Value |
|--------|-------|
| Kata | 14 |
| Emphasis | Slight irony on "nobody diffed the test file" |

**Sync cue:** Click "Naive merge" exactly on word **"Naive"** (**0:02**)

---

## Scene 05 — GreenLie Block (Screen Record)

**Durasi visual:** 14 detik  
**Durasi audio target:** 13 detik

### Visual — Screen Record

**URL:** https://web-flax-xi-10.vercel.app/#demo

| Waktu | Action |
|-------|--------|
| 0:00–0:02 | Click **GreenLie block** button |
| 0:02–0:08 | Hold: **29%** integrity score + red panel |
| 0:08–0:14 | Scroll findings list GL-001 → GL-003 (minimal) |

### Audio — ElevenLabs (Scene 05)

**Script:**
```
GreenLie blocks the merge. Integrity score: twenty-nine percent. Five critical findings — the test was weakened, not the bug.
```

| Metrik | Value |
|--------|-------|
| Kata | 21 |
| Emphasis | Pause before "twenty-nine percent" · stress "weakened, not the bug" |

**Sync cue:** "twenty-nine percent" saat angka **29%** full visible (**0:04**)

---

## Scene 06 — Try It Live (Screen Record)

**Durasi visual:** 16 detik  
**Durasi audio target:** 15 detik

### Visual — Screen Record

**URL:** https://web-flax-xi-10.vercel.app/#try

| Waktu | Action |
|-------|--------|
| 0:00–0:02 | Scroll ke Try It section |
| 0:02–0:04 | Click **greenlie analyze** |
| 0:04–0:08 | Show "Scanning…" state |
| 0:08–0:16 | Hold results: `Integrity: 29% | 5 findings` + `Xms live via API` |

### Audio — ElevenLabs (Scene 06)

**Script:**
```
Run a live scan on the sample agent fix. Same backslide scenario — hit the API, get the verdict in milliseconds.
```

| Metrik | Value |
|--------|-------|
| Kata | 22 |
| Emphasis | "live scan" · "milliseconds" |

**Sync cue:** Click button on **"Run a live scan"** (**0:02**) · "milliseconds" saat result muncul (**0:10**)

---

## Scene 07 — Terminal GL-001 (Screen Record)

**Durasi visual:** 22 detik  
**Durasi audio target:** 21 detik

### Visual — Screen Record

**Tool:** Screen Studio · Terminal full screen · dark theme

```bash
cd /Users/mac/Development/GreenLie
./scripts/demo.sh
```

| Waktu | Action |
|-------|--------|
| 0:00–0:04 | Type command (or paste) · Enter |
| 0:04–0:10 | Output scrolling — hold on header `Integrity: 29%` |
| 0:10–0:18 | **Zoom** GL-001 block: `toBe(401)` → `toBeGreaterThan(0)` |
| 0:18–0:22 | Hold zoom 2 detik |

### Audio — ElevenLabs (Scene 07)

**Script:**
```
Command line confirms it. GL-001: expect status toBe four-oh-one became toBeGreaterThan zero. Status five-hundred also passes. That's the green lie.
```

| Metrik | Value |
|--------|-------|
| Kata | 24 |
| Speed | **0.95** (sedikit lebih lambat) |
| Emphasis | Pause 1s after "GL-001:" · stress "five-hundred also passes" |

**Sync cue:**
- "GL-001" → saat finding GL-001 visible (**0:11**)
- "toBe four-oh-one" → zoom line **Before** (**0:13**)
- "five-hundred also passes" → hold zoom (**0:18**)

---

## Scene 08 — GitHub + AO PiP (Screen Record)

**Durasi visual:** 15 detik  
**Durasi audio target:** 14 detik

### Visual — Screen Record (composite di editor)

**Layout:**
- **Main (80%):** https://github.com/adindamochamad/GreenLie — README visible
- **PiP bottom-right (20%):** Loop 5s dari Scene 02 AO footage (optional)

| Waktu | Action |
|-------|--------|
| 0:00–0:05 | GitHub repo README — scroll ke Live Demo links |
| 0:05–0:15 | Hold · PiP AO Kanban subtle |

### Audio — ElevenLabs (Scene 08)

**Script:**
```
Open source on GitHub. Built for The Orchestra hackathon with Agent Orchestrator.
```

| Metrik | Value |
|--------|-------|
| Kata | 12 |
| Emphasis | Warm tone · confident close of act 2 |

---

## Scene 09 — End Card (Google Flow atau Static)

**Durasi visual:** 20 detik  
**Durasi audio target:** 18 detik (2s outro silence)

### Visual — Option A: Google Flow

**Prompt:**
```
Minimal motion graphic end card, dark background #0D0F0C, elegant typography animation, subtle green and rust orange accent particles, professional SaaS product launch aesthetic, no fake logos, cinematic fade in, 4K.
```

Overlay text di editor (jangan minta Flow render text — sering salah):
```
GreenLie
web-flax-xi-10.vercel.app
github.com/adindamochamad/GreenLie
#agentorchestrator
```

### Visual — Option B: Static (CapCut)

Dark slide dengan text di atas — lebih aman untuk URL accuracy.

### Audio — ElevenLabs (Scene 09)

**Script:**
```
Try GreenLie at web-flax-xi-10 dot vercel dot app. CI passed. Tests lied.
```

| Metrik | Value |
|--------|-------|
| Kata | 14 |
| Emphasis | Slow on URL · punch "Tests lied." |

**Sync cue:** URL text appear saat "web-flax-xi-10" (**0:04**) · "Tests lied" on beat akhir (**0:16**)

---

## Assembly checklist (CapCut / Descript)

```
☐ Import scene-01 … scene-09 visuals
☐ Import scene-01 … scene-09 audio MP3
☐ Sync per scene (gunakan sync cues di atas)
☐ Crossfade 0.3s antar scene (optional)
☐ Subtitle auto-generate (English) — helps judges
☐ Export: 1080p · 30fps · H.264 · ~2:45
☐ Upload YouTube unlisted → paste URL ke docs/TIER-D-READY.md
```

---

## ElevenLabs — all scripts (single copy block)

Gunakan jika mau generate satu file dulu, lalu split di editor — **tidak disarankan**. Lebih baik **9 file terpisah**.

```
[Scene 01]
CI passed. Auth was broken. The agent didn't fix the bug — it fixed the test.

[Scene 02]
GreenLie was built with Agent Orchestrator as the workspace. Parallel agents shipped the Python engine, the API, the demo site, and the sample fixtures — all visible on this board.

[Scene 03]
Your Kanban says merge. Your tests say pass. Same agent fix — but two very different outcomes.

[Scene 04]
Naive merge: CI passes, board goes green, and nobody diffed the test file.

[Scene 05]
GreenLie blocks the merge. Integrity score: twenty-nine percent. Five critical findings — the test was weakened, not the bug.

[Scene 06]
Run a live scan on the sample agent fix. Same backslide scenario — hit the API, get the verdict in milliseconds.

[Scene 07]
Command line confirms it. GL-001: expect status toBe four-oh-one became toBeGreaterThan zero. Status five-hundred also passes. That's the green lie.

[Scene 08]
Open source on GitHub. Built for The Orchestra hackathon with Agent Orchestrator.

[Scene 09]
Try GreenLie at web-flax-xi-10 dot vercel dot app. CI passed. Tests lied.
```

---

## File naming convention

```
video-export/
  visual-01-flow-hook.mp4
  visual-02-ao-kanban.mp4
  visual-03-hero.mp4
  visual-04-naive.mp4
  visual-05-block.mp4
  visual-06-tryit.mp4
  visual-07-terminal.mp4
  visual-08-github.mp4
  visual-09-endcard.mp4
  scene-01.mp3 … scene-09.mp3
  GreenLie-final.mp4
```

---

## Prioritas jika waktu mepet

| Priority | Scene | Why |
|----------|-------|-----|
| P0 | 02 AO Kanban | Wajib rules |
| P0 | 05 GreenLie block | Wow moment |
| P0 | 07 Terminal GL-001 | Proof engine works |
| P1 | 04 + 06 | Side-by-side narrative |
| P2 | 01 + 09 Flow | Polish only |

Skip Flow (01, 09) → ganti static text slide · video tetap valid untuk submit.
