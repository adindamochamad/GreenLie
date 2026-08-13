# GreenLie — Self-Record Script (Detail Lengkap)

> **Durasi target:** 2:00–2:30 (boleh 90 detik versi pendek)  
> **Bahasa narasi:** English — **ramah, non-teknis** (layar boleh tetap nunjuk kode)  
> **Rules AO:** Kanban asli **≥30 detik** full screen

### Gaya bicara
- Jelaskan **masalah nyata**, bukan istilah dev: "tes dibuat mudah lolos" bukan "assertion weakened"
- **Agent Orchestrator** tetap disebut (nama produk hackathon)
- Saat layar nunjuk kode, **arahkan dengan jari/cursor** — narasi tetap plain English

---

## Quick start

```bash
./scripts/record-demo.sh
```

**Rekam dengan:** Loom · QuickTime · OBS

---

## Ringkasan scene

| Scene | Waktu | Layar | Ngomong tentang |
|-------|-------|-------|-----------------|
| 1 Hook | 0:00–0:15 | Website hero | Masalah: semua hijau, tapi bug masih ada |
| 2 AO Kanban ⭐ | 0:15–0:50 | Agent Orchestrator | Cara bikin GreenLie pakai AO |
| 3 Demo | 0:50–1:15 | Website demo | Dua jalan: percaya ceklis vs cek ulang |
| 4 Try It | 1:15–1:35 | Website try | Coba langsung di browser |
| 5 Terminal | 1:35–2:00 | Terminal | Bukti konkret di layar |
| 6 Close | 2:00–2:20 | GitHub | Link + penutup |

---

# SCENE 1 — Hook (0:00 – 0:15)

## Buka apa
- https://web-flax-xi-10.vercel.app — paling atas (hero)

## Tunjuk di layar
- Headline *"Your board says merge"*
- Badge hijau **CI PASS | 44/44 tests**

## Action + narasi (non-teknis)

| Waktu | Layar | Ngomong |
|-------|-------|---------|
| 0:00 | Hero full screen | *"Hi — I'm Adinda. I built GreenLie for The Orchestra hackathon."* |
| 0:05 | Hover badge hijau | *"Imagine this: every check looks green, your board says ship it —"* |
| 0:12 | Hold | *"but login is still broken. The AI didn't fix the app. It made the test easier to pass."* |
| 0:15 | Switch ke AO | |

## Script Scene 1
```
Hi — I'm Adinda. I built GreenLie for The Orchestra hackathon.

Imagine this: every check looks green, your board says ship it —
but login is still broken. The AI didn't fix the app.
It made the test easier to pass.
```

---

# SCENE 2 — AO Kanban ⭐ (0:15 – 0:50)

## Buka apa
- Agent Orchestrator → klik **GreenLie** → **Board Kanban**

## Tunjuk di layar
- Header **GreenLie**
- 4 kartu: **engine**, **web**, **api**, **samples**
- Kolom board (Working / Needs you)

## Action + narasi (non-teknis)

| Waktu | Layar | Ngomong |
|-------|-------|---------|
| 0:15 | Wide shot board | *"I built GreenLie using Agent Orchestrator — a tool that runs several AI coding assistants in parallel."* |
| 0:22 | Hover **engine** | *"One helper worked on the core checker,"* |
| 0:26 | Hover **web** | *"one on the website,"* |
| 0:28 | Hover **api** | *"one on the online service,"* |
| 0:30 | Hover **samples** | *"and one on example files."* |
| 0:33 | Wide shot lagi | *"You can see all four jobs on this board — this is the real Agent Orchestrator, not a fake screenshot."* |
| 0:45 | Hold | |
| 0:50 | Switch browser | |

## Script Scene 2
```
I built GreenLie using Agent Orchestrator —
a tool that runs several AI coding assistants in parallel.

One helper worked on the core checker,
one on the website,
one on the online service,
and one on example files.

You can see all four jobs on this board.
This is the real Agent Orchestrator, not a fake screenshot.
```

---

# SCENE 3 — Demo Naive vs GreenLie (0:50 – 1:15)

## Buka apa
- https://web-flax-xi-10.vercel.app/#demo

## Tunjuk di layar
- Tombol **Naive merge** → panel hijau "Ready to merge"
- Tombol **GreenLie block** → **29%** + daftar masalah merah

## Action + narasi (non-teknis)

| Waktu | Layar | Ngomong |
|-------|-------|---------|
| 0:50 | Section demo | *"Same fix from an AI — two ways to look at it."* |
| 0:53 | Klik **Naive merge** | *"If you only trust the green checkmarks,"* |
| 0:55 | Panel hijau | *"everything looks fine. Ready to merge. All tests passed."* |
| 1:03 | Klik **GreenLie block** | *"GreenLie looks deeper."* |
| 1:05 | Angka **29%** + merah | *"It gives your tests a trust score — only twenty-nine percent."* |
| 1:10 | Scroll ke GL-001 | *"It found five serious problems. The test was loosened so it would pass — the bug is still there."* |
| 1:15 | Scroll ke Try It | |

## Script Scene 3
```
Same fix from an AI — two ways to look at it.

If you only trust the green checkmarks,
everything looks fine. Ready to merge. All tests passed.

GreenLie looks deeper.
It gives your tests a trust score — only twenty-nine percent.
It found five serious problems.
The test was loosened so it would pass — the bug is still there.
```

## Saat layar nunjuk kode
Boleh bilang sambil tunjuk baris Before/After:
*"See this line? It used to check for a real login error. Now it accepts almost anything — even a server crash."*

---

# SCENE 4 — Try It (1:15 – 1:35)

## Buka apa
- https://web-flax-xi-10.vercel.app/#try

## Tunjuk di layar
- Klik **greenlie analyze**
- Hasil: **Integrity: 29%**, **5 findings**, teks **live via API**

## Action + narasi (non-teknis)

| Waktu | Layar | Ngomong |
|-------|-------|---------|
| 1:15 | Tomol analyze | *"You can try it yourself on the website."* |
| 1:18 | Klik analyze | |
| 1:20 | Hasil muncul | *"One click — it scans the sample fix and tells you straight:"* |
| 1:25 | Tunjuk 29% + findings | *"low trust score, five problems found. And this is a real scan, not a canned demo."* |
| 1:32 | Hold | |
| 1:35 | Switch terminal | |

## Script Scene 4
```
You can try it yourself on the website.

One click — it scans the sample fix and tells you straight:
low trust score, five problems found.

And this is a real scan, not a canned demo.
```

---

# SCENE 5 — Terminal (1:35 – 2:00)

## Buka apa
- Terminal full screen

```bash
cd /Users/mac/Development/GreenLie
./scripts/demo.sh
```

## Tunjuk di layar
- **Integrity: 29%**
- **GL-001** — baris Before (401) dan After (greater than 0)

## Action + narasi (non-teknis)

| Waktu | Layar | Ngomong |
|-------|-------|---------|
| 1:35 | Ketik command | *"Same story from the command line."* |
| 1:42 | Integrity 29% | *"Again — twenty-nine percent trust."* |
| 1:44 | Scroll ke GL-001 | *"Here's the smoking gun."* |
| 1:48 | Tunjuk Before / After | *"Before: the test checked for a proper login error. After: it accepts any response — even a five-hundred server error."* |
| 1:56 | Hold | *"The dashboard says green. The test says pass. That's the green lie."* |
| 2:00 | Switch GitHub | |

## Script Scene 5
```
Same story from the command line.
Again — twenty-nine percent trust.

Here's the smoking gun.
Before: the test checked for a proper login error.
After: it accepts any response — even a five-hundred server error.

The dashboard says green. The test says pass.
That's the green lie.
```

---

# SCENE 6 — Close (2:00 – 2:20)

## Buka apa
- https://github.com/adindamochamad/GreenLie

## Action + narasi (non-teknis)

| Waktu | Layar | Ngomong |
|-------|-------|---------|
| 2:00 | GitHub README | *"GreenLie is open source — code and demo are online."* |
| 2:08 | Live Demo links | *"Try the live site at web-flax-xi-ten dot vercel dot app."* |
| 2:14 | End card | *"GreenLie — when everything looks fine but the tests aren't telling the truth. Thank you."* |

## Script Scene 6
```
GreenLie is open source — code and demo are online.

Try the live site at web-flax-xi-ten dot vercel dot app.

GreenLie — when everything looks fine but the tests aren't telling the truth.
Thank you.
```

## End card
```
GreenLie
https://web-flax-xi-10.vercel.app
https://github.com/adindamochamad/GreenLie
#agentorchestrator · Built with Agent Orchestrator
```

---

# TELEPROMPTER — Non-teknis (copy ke monitor 2)

```
Hi — I'm Adinda. I built GreenLie for The Orchestra hackathon.

Imagine this: every check looks green, your board says ship it —
but login is still broken. The AI didn't fix the app.
It made the test easier to pass.

I built GreenLie using Agent Orchestrator —
a tool that runs several AI coding assistants in parallel.

One helper worked on the core checker,
one on the website,
one on the online service,
and one on example files.

You can see all four jobs on this board.
This is the real Agent Orchestrator, not a fake screenshot.

Same fix from an AI — two ways to look at it.

If you only trust the green checkmarks,
everything looks fine. Ready to merge. All tests passed.

GreenLie looks deeper.
It gives your tests a trust score — only twenty-nine percent.
It found five serious problems.
The test was loosened so it would pass — the bug is still there.

You can try it yourself on the website.
One click — it scans the sample fix and tells you straight:
low trust score, five problems found.
And this is a real scan, not a canned demo.

Same story from the command line.
Again — twenty-nine percent trust.

Here's the smoking gun.
Before: the test checked for a proper login error.
After: it accepts any response — even a five-hundred server error.

The dashboard says green. The test says pass.
That's the green lie.

GreenLie is open source — code and demo are online.
Try the live site at web-flax-xi-ten dot vercel dot app.

GreenLie — when everything looks fine but the tests aren't telling the truth.
Thank you.
```

---

# Versi pendek ~90 detik (non-teknis)

| Waktu | Layar | Ngomong |
|-------|-------|---------|
| 0:00 | Hero | *"All checks green — but the AI fixed the test, not the bug."* |
| 0:10 | AO 35s | *"Built with Agent Orchestrator — four AI helpers, one board."* |
| 0:45 | Demo | *"Trust the checkmarks? Everything passes. GreenLie? Only twenty-nine percent trust — merge blocked."* |
| 1:00 | Try It | *"Try it live on the website — real scan, same answer."* |
| 1:10 | Terminal | *"The test used to catch login errors. Now it accepts anything. That's the green lie."* |
| 1:25 | End card | *"Link below. GreenLie. Thank you."* |

---

# Glosarium — istilah teknis → kata ramah

| Di layar (boleh tetap) | Katakan ini |
|------------------------|-------------|
| CI PASS | "all checks look green" |
| Kanban / merge | "your board says ship it" |
| Agent / coding agent | "AI helper" / "AI assistant" |
| Assertion weakened | "the test was made easier to pass" |
| toBe(401) | "checked for a real login error" |
| toBeGreaterThan(0) | "accepts almost any response" |
| Integrity 29% | "trust score — only twenty-nine percent" |
| API / CLI | "on the website" / "from the command line" |
| Findings | "problems found" |
| Naive merge | "if you only trust the green checkmarks" |

---

# Checklist sebelum upload

- [ ] AO Kanban asli ≥30 detik
- [ ] Demo: hijau vs merah 29% keduanya terlihat
- [ ] Try It: hasil scan muncul
- [ ] Terminal: Before/After GL-001 terbaca (meski narasi non-teknis)
- [ ] End card + `#agentorchestrator`
- [ ] Upload → isi `[VIDEO_URL]` di `TIER-D-READY.md`

---

# Troubleshooting

| Masalah | Fix |
|---------|-----|
| AO bukan board | Klik **GreenLie** di sidebar |
| Try It error | Test klik analyze dulu sebelum rekam |
| Terminal panjang | Cmd+F → `GL-001` |
