# Prompt ChatGPT — Poster Alur GreenLie (LinkedIn · Detail)

Copy-paste ke **ChatGPT → Generate image**.  
Kalau teks blur, lanjut prompt **Refine #1** di bawah.

---

## Prompt utama — LinkedIn scroll-stopper (copy semua)

```
Design a premium LinkedIn carousel-style infographic poster for a developer product launch.

CANVAS
- Aspect ratio: 16:9 landscape (1920×1080 px)
- Optimized for LinkedIn feed: bold headline readable on mobile, high contrast, clear visual hierarchy
- Safe margins: 80px padding all sides — no text touching edges

BRAND — GreenLie
- Background: deep charcoal #0d0f0c with subtle radial green glow top-left (very soft, 5% opacity)
- Primary accent: neon green #3dff7a (false success / CI pass)
- Truth accent: red #ff3b30 (blocked merge / warning)
- Brand accent: rust orange #c44d2e (GreenLie logo, step 3 hero)
- Text primary: #e8e4dc · muted: #8a8f82
- Typography: elegant serif for headlines (like Instrument Serif), clean geometric sans for body (like Inter), monospace for badges

HEADER (top 18% of canvas)
- Center: wordmark "GreenLie" large serif rust orange
- Tagline under it: "CI passed. Tests lied." monospace small green
- Top-right corner pill badge: "THE ORCHESTRA HACKATHON · #agentorchestrator" small caps gray-green
- One-line hook below title, centered, white serif italic:
  "Your board says merge — but did the AI fix the bug, or just the test?"

MAIN VISUAL — horizontal story flow (middle 62%)
Four equal columns connected by thick minimal green chevron arrows. Each column is a card with rounded corners, dark panel #161a14, thin border.

Each card structure (top to bottom):
1) Small label "LANGKAH 01" etc in green caps
2) Custom flat icon (48px) — unique per step, line-art style, 2px stroke
3) Bold Indonesian title (serif, 28px)
4) 2-line description (sans, 17px, gray) — plain language, no jargon
5) Status pill badge at bottom

─── CARD 1 · LANGKAH 01 ───
Icon: green dashboard with checkmarks, everything glowing green
Title: "Semua terlihat OK"
Body: "CI lulus. Board bilang siap merge. Semua checklist hijau."
Badge (green outline): "✓ Siap merge · 44/44 tests"
Mood: deceptive calm, slightly too perfect

─── CARD 2 · LANGKAH 02 ───
Icon: robot/AI hand editing a document, eraser on test line
Title: "The green lie"
Body: "AI nggak benerin produk — tes-nya dilonggarkan supaya lulus."
Badge (red outline): "Login masih broken"
Visual detail: tiny before/after — strict test → loose test (abstract, not code)

─── CARD 3 · LANGKAH 03 — HERO CARD (slightly larger or orange border glow) ───
Icon: shield with magnifying glass scanning a file
Title: "GreenLie stop merge"
Body: "Skor kepercayaan tes + daftar masalah. Merge diblokir sebelum bug lolos."
Badge (red filled subtle): "29% integrity · 5 findings · BLOCKED"
Large number "29%" as subtle watermark behind icon in red 15% opacity
This card should visually POP as the solution

─── CARD 4 · LANGKAH 04 ───
Icon: Kanban board with 4 mini cards labeled engine, web, api, samples
Title: "Dibangun pakai AO"
Body: "Empat AI helper paralel di Agent Orchestrator — Kanban asli, bukan mockup."
Badge (rust outline): "Agent Orchestrator"
Small subtitle: "Engine · Web · API · Samples"

CONNECTORS
- Between cards: clean → arrows in #3dff7a, not cartoonish
- Optional thin timeline line running through card centers

BOTTOM STRIP (footer 12%)
- Dark bar with top border 1px white/10%
- Left: green arrow + "web-flax-xi-10.vercel.app" monospace
- Center: "Coba live · Scan sample agent fix"
- Right: "github.com/adindamochamad/GreenLie"

STYLE RULES
- Flat modern SaaS infographic — think Linear, Vercel, Stripe developer posts
- NO: 3D, glossy gradients, stock photos, human faces, emoji, cartoon mascots, cyberpunk neon, cluttered code blocks, illegible tiny text, watermarks
- YES: whitespace, crisp alignment, professional, trustworthy, slightly editorial
- Must feel like a real shipped devtool, not a generic AI slop image
- All visible text in INDONESIAN except: GreenLie, Agent Orchestrator, CI, merge, Kanban, AO, integrity, findings, engine, web, api, samples

MOOD
Smart, calm, slightly unsettling in step 1-2, confident resolution in step 3-4.
Tell a story: false green → hidden bug → guardrail → built credibly with AO.
```

---

## Refine #1 — kalau teks blur / layout berantakan

```
Regenerate the same GreenLie LinkedIn 16:9 flow poster. Keep identical 4-step story and Indonesian copy.

Fix: sharper readable text, perfect alignment, equal card heights, larger font sizes for mobile LinkedIn feed.

Prioritize legibility over decoration. Flat dark SaaS style. No typos in Indonesian text.
```

---

## Refine #2 — kalau terlalu polos

```
Same layout but add subtle visual polish:
- Soft card shadows (very subtle)
- Step 3 hero card with rust orange #c44d2e border glow
- Small green radial glow behind step 1 badge only
- Slightly richer icons (still flat line-art)

Keep minimal and professional — not flashy.
```

---

## Refine #3 — versi lebih “LinkedIn viral”

```
Add a bold top banner strip above the title:
"When every check is green — who checks the tests?"

Keep 4-step flow below. Make step 3 "29% BLOCKED" the visual focal point with largest typography on the poster.

LinkedIn feed optimized: someone scrolling should understand the story in 2 seconds.
```

---

## Prompt alternatif — diagram + ikon besar (lebih visual, less text)

```
LinkedIn infographic 16:9, dark #0d0f0c, premium devtool launch.

Center: large horizontal pipeline diagram with 4 nodes.

Node 1 icon: green traffic light all green — label "Semua hijau"
Node 2 icon: AI editing test paper with eraser — label "Tes dilonggarkan"  
Node 3 icon: red stop hand + 29% gauge — label "GreenLie blokir merge"
Node 4 icon: Kanban 4 columns — label "Built with Agent Orchestrator"

Title top: GreenLie (rust serif)
Hook: "CI passed. Tests lied." (green mono)
Footer: web-flax-xi-10.vercel.app · #agentorchestrator

Indonesian subtitles under each node (1 short sentence each).
Flat vector, Figma/Notion quality, whitespace, no photos, 1920x1080.
```

---

## Setelah dapat gambar

1. Download PNG → simpan `docs/assets/linkedin-poster.png`
2. Attach ke LinkedIn post
3. Caption dari `docs/LINKEDIN-POST.md`
4. Paste link video: https://youtu.be/RmDVxPWPBzU (auto embed)

**LinkedIn tips:**
- Poster = **hook visual**, caption = **cerita lengkap**
- Post jam kerja (Sel–Kam 8–10 pagi atau 5–7 sore) untuk reach
- Tag **Agent Orchestrator** company page
- First comment: link demo + GitHub (boost engagement)

---

## Negative prompt (append di akhir prompt utama)

```
Avoid: cartoon, anime, cyberpunk, neon overload, realistic people, stock office photos, 
lorem ipsum, English-only body text, messy code screenshots, blurry typography, 
competing logos, watermark, DALL-E artifacts, misaligned columns, emoji.
```
