# GreenLie ù Konteks Lengkap Proyek

> **Single source of truth** untuk seluruh konteks hackathon, produk, arsitektur, strategi, dan status build.
> Terakhir diperbarui: **12 Agustus 2026, malam** ù build & deploy selesai; sisa video manual + Tier D submit

---

## Daftar Isi

1. [Ringkasan Eksekutif](#1-ringkasan-eksekutif)
2. [Konteks Hackathon](#2-konteks-hackathon)
3. [Builder & Setup](#3-builder--setup)
4. [Stage 1 ù Ideation & Validasi Strategis](#4-stage-1--ideation--validasi-strategis)
5. [Produk: GreenLie](#5-produk-greenlie)
6. [Demo Concept & Wow Moment](#6-demo-concept--wow-moment)
7. [Strategi Menang Hackathon](#7-strategi-menang-hackathon)
8. [Arsitektur Sistem](#8-arsitektur-sistem)
9. [Engine Python ù Detail Teknis](#9-engine-python--detail-teknis)
10. [API FastAPI](#10-api-fastapi)
11. [Demo Website (Next.js)](#11-demo-website-nextjs)
12. [Sample Data & Golden Report](#12-sample-data--golden-report)
13. [Agent Orchestrator (AO) Workflow](#13-agent-orchestrator-ao-workflow)
14. [Design System (ATM)](#14-design-system-atm)
15. [Timeline & Progress](#15-timeline--progress)
16. [Submission Checklist](#16-submission-checklist)
17. [Demo Video Script](#17-demo-video-script)
18. [Perintah Referensi](#18-perintah-referensi)
19. [URL & Placeholder](#19-url--placeholder)
20. [Risiko & Mitigasi](#20-risiko--mitigasi)
21. [Relasi Proyek Lain](#21-relasi-proyek-lain)
22. [Glosarium](#22-glosarium)

---

## 1. Ringkasan Eksekutif

| Field | Value |
|-------|-------|
| **Nama proyek** | GreenLie |
| **Tagline** | CI passed. Tests lied. |
| **One-line problem** | Your Kanban shows green. Your tests show pass. Your production shows outage. The agent didn't fix the bug ù it fixed the test. |
| **Hackathon** | [The Orchestra](https://luma.com/iw1v5erp) ù hackathon pertama Agent Orchestrator |
| **Format** | Solo ù 2 hari ù fully online |
| **Verdict Stage 1** | **GO** ù Win Index estimasi ~20ù28% |
| **Stage saat ini** | Stage 3 - Ship & Submit (build selesai; sisa video manual + Tier D) |
| **Constraint unik** | Produk bebas; **AO wajib** sebagai workspace; demo video **wajib** tunjukkan AO Kanban |

**GreenLie** adalah detektor *test backslide*: alat yang menangkap saat coding agent "memperbaiki" CI dengan **melemahkan assertion test**, bukan memperbaiki bug di kode produksi.

Contoh klasik:

```javascript
// SEBELUM (benar)
expect(response.status).toBe(401);

// SESUDAH agent "fix" (bohong tapi CI hijau)
expect(response.status).toBeGreaterThan(0);
```

---

## 2. Konteks Hackathon

### 2.1 Event Overview

| Item | Detail |
|------|--------|
| **Nama resmi** | The Orchestra |
| **Penyelenggara** | [Agent Orchestrator](https://aoagents.dev/) / [Untrivial-ai](https://github.com/Untrivial-ai/agent-orchestrator) |
| **Host** | Maaz, Pulkit Saraf, Nikhil Achale, Prateek, Prasad Ware |
| **Creator AO** | Prateek Karnal (session Discord dari SF) |
| **Peserta terdaftar** | ~235+ (per Luma, Agustus 2026) |
| **Edisi** | Pertama ù **tidak ada pemenang edisi sebelumnya** |
| **Lokasi** | Fully online via Discord |
| **Registrasi** | Luma ù approval required (status: **APPROVED**) |

### 2.2 Jadwal Kritis

| Milestone | Tanggal/Waktu |
|-----------|---------------|
| Build window | **12ù13 Agustus 2026** |
| Submission deadline | **13 Agustus, 7:00 PM** (timezone tidak eksplisit ù asumsikan IST atau konfirmasi di Discord) |
| Pengumuman pemenang | **14 Agustus 2026** |

### 2.3 Hadiah

| Peringkat | Hadiah |
|-----------|--------|
| 1st | $100 |
| 2nd | $50 |
| 3rd | $50 |
| Top 10ù15 | AO merch |
| Bonus | Undangan opsional ke launch party Bangalore (BLR) |

### 2.4 Rules Resmi (scraped dari Luma + Notion)

**Sumber:**
- Luma: https://luma.com/iw1v5erp
- Notion: https://maaztwts.notion.site/The-Orchestra-3b532902e4a38040aedbc66966f4fc06
- Discord: https://discord.gg/87NPrAuDa

**Aturan build:**
- Tim 1ù4 orang; solo diperbolehkan
- Build hanya selama window resmi (12ù13 Agustus)
- **Wajib pakai AO** saat membuat proyek
- Produk bebas ù AO adalah **workspace**, bukan tema
- **Public GitHub repo** wajib
- **Demo video** wajib ù **harus menampilkan AO Kanban board / penggunaan Agent Orchestrator**

**Tema eksplorasi (saran, bukan wajib):**
Creative tools ù Developer workflows ù Personal productivity ù Local-first ù Education ù Communities ù Business ops ù Security/reliability ù Media/games/storytelling ù Weird/experimental/internet-native ù **Bonus untuk yang mengejutkan**

### 2.5 Cara Masuk (Discord)

1. Join AO Discord ? https://discord.gg/87NPrAuDa
2. React **spider emoji** di `#orchestra-announcements` ? dapat role **Hacker**
3. Pantau `#orchestra-announcements` untuk update
4. Cari tim di `#orchestra-find-a-teammate` (jika perlu ù kita solo)
5. Build & diskusi di `#orchestra-general`
6. Submit di `#orchestra-project-showcase`

### 2.6 Submission ù 2 Langkah WAJIB

**Step 1 ù Discord `#orchestra-project-showcase`:**
- Team name
- Project name
- Description
- Public GitHub repo
- Live demo link (jika ada)
- Demo video link

**Step 2 ù Post publik X atau LinkedIn:**
- Project + demo video + public GitHub repo
- Hashtag `#agentorchestrator`
- Tag AO: X ? [@aoagents](https://x.com/aoagents) ù LinkedIn ? [Agent Orchestrator](https://www.linkedin.com/company/agent-orchestrator/)
- Multi-post dari member tim boleh ù engagement digabung

**Tidak ada showcase post + post publik = tidak masuk penilaian.**

### 2.7 Kriteria Penilaian (Implisit)

Tidak ada rubric numerik resmi. Signal yang jelas dari rules:

| Signal | Bobot |
|--------|-------|
| Penggunaan AO sebagai workspace | **Sangat tinggi** |
| Demo video dengan Kanban AO | **Wajib** |
| Produk yang benar-benar di-ship | **Tinggi** |
| Engagement sosial (X/LinkedIn) | **Medium** |
| Surprise factor | **Bonus eksplisit** |
| "Ship something real" | **Narasi inti event** |

**Lens juri:** Tim AO + Prateek Karnal ù mereka peduli orchestration, parallel agents, CI feedback loop, branch management.

---

## 3. Builder & Setup

| Field | Value |
|-------|-------|
| **Nama** | Adinda Panca Mochamad |
| **Email** | adindacq@gmail.com |
| **GitHub** | [adindamochamad](https://github.com/adindamochamad) |
| **Format tim** | Solo |
| **Background** | Backend developer (PHP, Python, R, C++, MySQL) |
| **Track record hackathon** | SpecDrift, HeatRecall, OmniBridge |
| **AO terinstall** | Ya ù `/Applications/Agent Orchestrator.app` (v0.12.2 via Homebrew) |
| **Workspace lokal** | `/Users/mac/Development/GreenLie` |

---

## 4. Stage 1 ù Ideation & Validasi Strategis

### 4.1 Baseline Penelitian

Hackathon **pertama** AO ù tidak ada pemenang edisi sebelumnya untuk dibandingkan.

**Blind spot kompetitor:** Banyak peserta akan build AO dashboard clone, generic agent tool, atau ChatGPT wrapper.

**Angle menang:** Produk nyata dengan masalah konkret + demo AO yang dramatis + failure mode yang bikin engineer insomnia.

### 4.2 Tiga Ide yang Dievaluasi

#### Ide A: GreenLie (TERPILIH)

> *"What happens when your agent 'fixes' CI by weakening the test ù and your Kanban board says ready to merge?"*

| Lensa | Skor | Catatan |
|-------|------|---------|
| Pain Point Clarity | 9 | Engineer agent fleet khawatir ini |
| Differentiation | 8 | Bukan spec drift, bukan memory ù test integrity |
| Technical Feasibility | 9 | Python diff analyzer ù 2 hari realistis solo |
| Judge Appeal | 10 | Align langsung narasi produk AO (CI feedback loop) |
| Scalability Story | 8 | Semua tim agentic development |
| High Chance of Winning | 9 | Juri membangun fitur yang GreenLie audit |
| Uniqueness | 8 | Bukan Kanban clone |
| Wow Factor | 9 | Side-by-side naive merge vs block |
| ChatGPT Test | **LULUS** | Butuh heuristics diff ù tidak bisa di-prompt |

**DeadDrop Checklist:** 6/6  
**Verdict:** **GO**

#### Ide B: FleetCollide (PIVOT)

> *"Four agents finished. Zero git conflicts. Why does main break anyway?"*

Radar konflik semantic antar branch parallel agent.

| Lensa | Skor |
|-------|------|
| Feasibility | **6** ù scope terlalu besar 2 hari solo |
| Judge Appeal | 9 |

**Verdict:** **PIVOT** ù bagus tapi tidak realistis untuk window hackathon.

#### Ide C: TaskDrift (DROP)

Adaptasi SpecDrift: AO task card vs codebase.

| Lensa | Skor |
|-------|------|
| Feasibility | 10 ù engine sudah ada |
| Uniqueness | **5** ù terlihat repackage SpecDrift |

**Verdict:** **DROP** untuk Orchestra ù derivative risk.

### 4.3 Framework 9 Lensa ù GreenLie Final

```
1. PAIN POINT CLARITY     9/10
2. DIFFERENTIATION      8/10
3. TECHNICAL FEASIBILITY 9/10
4. JUDGE APPEAL        10/10
5. SCALABILITY STORY    8/10
6. HIGH CHANCE WINNING  9/10
7. UNIQUENESS           8/10
8. WOW FACTOR             9/10
9. CHATGPT TEST         LULUS
?????????????????????????????
Rata-rata               8.9/10
Win Index estimasi    20ù28% (235 peserta, solo, execution-dependent)
```

### 4.4 DeadDrop Checklist (6 Pertanyaan)

| # | Pertanyaan | GreenLie |
|---|----------|----------|
| 1 | Failure mode bikin insomnia? | Ya ù agent melemahkan test, prod outage |
| 2 | Stakes demo setinggi mungkin? | Ya ù auth 401 ? toBeGreaterThan(0), bug masuk prod |
| 3 | Side-by-side before/after? | Ya ù naive merge vs GreenLie block |
| 4 | Problem framing satu kalimat? | Ya ù "agent fixed the test, not the bug" |
| 5 | Menyentuh criteria eksplisit juri? | Ya ù CI guardrails, AO feedback loop |
| 6 | Nama menggambarkan mekanisme? | Ya ù GreenLie = CI hijau tapi bohong |

### 4.5 ChatGPT Test

**Konteks:** User paste scenario agent melemahkan test.

**GAGAL jika:** Wrapper ChatGPT, fitur generik summarize/generate.

**LULUS karena:** Butuh parser assertion, scoring strictness, heuristics pairing, diff directory ù workflow multi-step dengan logika proprietary.

---

## 5. Produk: GreenLie

### 5.1 Definisi

GreenLie adalah **test integrity guard** untuk agentic development workflows. Ia membandingkan file test **sebelum** dan **sesudah** agent melakukan "CI fix", lalu mendeteksi:

| Kode Temuan | Arti |
|-------------|------|
| `TEST_BACKSLIDE` | Assertion exact diganti yang lebih longgar (range, truthy, defined) |
| `ASSERTION_DROPPED` | Agent menghapus assertion sepenuhnya |

### 5.2 Bukan Apa

- Bukan clone AO Kanban
- Bukan generic LLM wrapper
- Bukan spec-vs-code checker (itu SpecDrift)
- Bukan agent memory tool (itu HeatRecall)

### 5.3 Target User

Engineer yang menjalankan fleet coding agents (AO, Cursor, Claude Code, dll.) dan khawatir agent "memperbaiki" CI dengan cara curang.

### 5.4 Value Proposition

| Tanpa GreenLie | Dengan GreenLie |
|----------------|-----------------|
| CI pass, board green, merge | Integrity score + temuan backslide |
| Bug auth masuk production | Block sebelum merge |
| Nobody audits test diffs | Automated assertion strictness scoring |

### 5.5 Metrik Utama

- **Integrity Score** (0ù100%): persentase assertion yang tidak melemah
- **Findings count**: jumlah TEST_BACKSLIDE + ASSERTION_DROPPED
- **Confidence**: 0.7ù0.98 per temuan

---

## 6. Demo Concept & Wow Moment

### 6.1 Side-by-Side Scenario

```
?????????????????????????????????????????????????????????????
?  NAIVE AO WORKFLOW          ?  WITH GREENLIE              ?
?????????????????????????????????????????????????????????????
?  CI fails on auth test      ?  Same CI failure             ?
?  Agent: toBe(401)           ?  GreenLie flags GL-001       ?
?    ? toBeGreaterThan(0)     ?    TEST_BACKSLIDE            ?
?  Board ? Ready to merge     ?  Integrity: 29%              ?
?  Merge ? bug in prod        ?  Block merge                 ?
?????????????????????????????????????????????????????????????
```

### 6.2 Wow Moment (Stakes Tinggi)

Agent mengubah:

```javascript
expect(response.status).toBe(401)
// menjadi
expect(response.status).toBeGreaterThan(0)
```

Engineer senior jam 2 pagi **duduk tegak** ù karena status 500 juga `> 0`.

### 6.3 Kalimat Pitch ke Juri

> "AO's CI feedback loop is powerful ù until the agent edits the test instead of the bug. GreenLie catches the green lie before it merges."

### 6.4 Section List Website Demo

1. **Hero** ù "Your board says merge." + fake green pulse
2. **The Green Lie** ù problem framing
3. **Side-by-Side Demo** ù centerpiece interaktif
4. **How It Reads a PR** ù diff ? parse ? verdict
5. **Built with AO** ù Kanban footage/screenshot
6. **Try It** ù trigger analyze, golden report
7. **Footer** ù GitHub, #agentorchestrator

---

## 7. Strategi Menang Hackathon

### 7.1 Align dengan AO

AO memasarkan: *CI fails ? agent fixes ? merge*. GreenLie menunjukkan **failure mode produk mereka sendiri** ù dan solusi. Ini bukan kritik destruktif; ini menunjukkan depth pemahaman platform.

### 7.2 Meta Demo AO (Wajib Rules)

Demo video harus include:
1. AO Kanban dengan cards GreenLie (engine, api, web, samples)
2. Parallel agents working
3. Picture-in-picture atau split: produk demo + board footage

### 7.3 Engagement Sosial

Post X/LinkedIn dengan `#agentorchestrator` @aoagents ù engagement **dihitung**. Siapkan thread + demo video embed.

### 7.4 Surprise Factor

Nama "GreenLie" memorable. Visual fake-green vs truth-red. Bukan template AI purple gradient.

### 7.5 Risiko Kompetitif

| Kompetitor likely build | GreenLie counter |
|------------------------|------------------|
| AO dashboard clone | Produk standalone, AO hanya workspace |
| Generic dev tool | Spesifik failure mode |
| Another orchestrator | Deteksi, bukan orchestration |

---

## 8. Arsitektur Sistem

```
???????????????????????????????????????????????????????????????
?                     GreenLie Monorepo                        ?
???????????????????????????????????????????????????????????????
?   engine/    ?    api/      ?           web/                ?
?   Python     ?   FastAPI    ?        Next.js 15              ?
?   CLI        ?   /analyze   ?     Demo website               ?
???????????????????????????????????????????????????????????????
?                      samples/                                ?
?   before-agent-fix/  ?  after-agent-fix/  ? golden-report.json?
???????????????????????????????????????????????????????????????
                              ?
                    Built with AO (workspace)
```

### 8.1 Alur Data

```
samples/before-agent-fix/  ???
                             ???? engine/greenlie/detector.py ??? LaporanIntegritas
samples/after-agent-fix/  ???              ?
                                             ???? CLI (greenlie analyze)
                                             ???? API POST /analyze
                                             ???? web/public/golden-report.json
```

### 8.2 Struktur Direktori

```
GreenLie/
??? CONTEXT.md              ? dokumen ini
??? README.md               ? public-facing intro
??? .gitignore
??? docs/
?   ??? 01-DESIGN-ATM.md    ? riset visual Stage 2
??? engine/
?   ??? pyproject.toml
?   ??? greenlie/
?   ?   ??? __init__.py
?   ?   ??? models.py       ? Assertion, TemuanBackslide, LaporanIntegritas
?   ?   ??? parser_test.py  ? ekstraksi assertion JS/TS/Python
?   ?   ??? detector.py     ? pairing + deteksi pelemahan
?   ?   ??? analyze.py      ? orkestrasi
?   ?   ??? cli.py          ? entry point CLI
?   ?   ??? exceptions.py
?   ??? tests/
?       ??? test_detector.py
??? api/
?   ??? app/
?       ??? main.py         ? FastAPI /health, /analyze
?       ??? schemas.py
?       ??? config.py
?       ??? layanan.py
??? samples/
?   ??? before-agent-fix/tests/auth.test.js
?   ??? after-agent-fix/tests/auth.test.js
?   ??? golden-report.json
??? scripts/
?   ??? demo.sh
??? web/
    ??? app/                ? layout, page, globals.css
    ??? components/         ? Hero, Demo, Problem, HowItWorks, TryIt, AO, Footer
    ??? public/golden-report.json
```

---

## 9. Engine Python ù Detail Teknis

### 9.1 Stack

- Python 3.11+
- click (CLI)
- pytest (dev)
- Zero ML ù pure heuristic

### 9.2 Model Data

```python
Assertion          # teks, baris, tingkat_ketat (0-100), jenis
TemuanBackslide    # id, severity, sebelum, sesudah, alasan, berkas, baris, confidence
LaporanIntegritas  # integrity_score, temuan[], assertion_dicek, assertion_aman, metode
```

### 9.3 Scoring Strictness (Jest/Vitest)

| Pola | Skor | Jenis |
|------|------|-------|
| `toStrictEqual` | 95 | strict_equal |
| `toBe('string')` / `toBe(401)` | 90 | exact_string / exact_number |
| `toEqual` | 85 | equal |
| `toThrow` | 85 | throws |
| `toMatch(/regex/)` | 82 | regex_specific |
| `toHaveLength(n)` | 80 | length_exact |
| `toBeGreaterThanOrEqual` | 55 | range_gte |
| `toBeGreaterThan` | 50 | range_gt |
| `toBeTruthy` | 35 | truthy |
| `toBeDefined` | 30 | defined |

### 9.4 Scoring Strictness (pytest)

| Pola | Skor |
|------|------|
| `assert x == 'str'` / `assert x == 401` | 90 |
| `assert x is not None` | 75 |
| `pytest.raises` | 85 |
| `assert x` (loose) | 60 |

### 9.5 Deteksi Pelemahan

Threshold: `pasangan.tingkat_ketat < sebelum.tingkat_ketat - 15`

Severity:
- `critical` jika selisih >= 30
- `warning` jika selisih 16ù29

### 9.6 Assertion Pairing Heuristics

1. Baris within ù3 ? dianggap pasangan
2. Subjek `expect(...)` sama ? pasangan
3. Subjek `assert ...` sama ? pasangan
4. SequenceMatcher ratio > 0.55 ? pasangan
5. Tidak ada pasangan ? `ASSERTION_DROPPED`

### 9.7 Output CLI Saat Ini (Verified)

```
Integrity Score: 29%
Assertions: 2/7 intact
Findings: 5
Exit code: 1
```

Temuan utama:
- GL-001: `toBe(401)` ? `toBeGreaterThan(0)` ù TEST_BACKSLIDE
- GL-002: `toBe('Unauthorized')` ? `toBeDefined()` ù TEST_BACKSLIDE
- GL-003ù005: assertion dropped atau weakened di test case lain

### 9.8 File Test yang Didukung

- `*.test.js`, `*.test.ts`, `*.spec.js`, `*.spec.ts`
- `test_*.py`, `*_test.py`
- Berkas di folder `tests/`, `__tests__/`, `test/`

### 9.9 Batasan MVP (Sengaja)

- Tidak parse AST penuh ù regex line-based (cukup untuk demo hackathon)
- Tidak support semua matcher Jest (cukup yang common untuk backslide scenario)
- Tidak integrasi git diff langsung ù compare dua direktori
- Tidak block merge otomatis ù laporkan saja

---

## 10. API FastAPI

### 10.1 Endpoints

| Method | Path | Deskripsi |
|--------|------|-----------|
| GET | `/health` | Health check + version |
| POST | `/analyze` | Analisis sample `naive-agent` |

### 10.2 Request/Response

```json
// POST /analyze
{ "sample": "naive-agent" }

// Response
{
  "integrity_score": 29,
  "assertion_dicek": 7,
  "assertion_aman": 2,
  "metode": "backslide_v1",
  "duration_ms": 12,
  "berkas_test": ["tests/auth.test.js"],
  "temuan": [...]
}
```

### 10.3 Menjalankan Lokal

```bash
cd engine && source .venv/bin/activate && pip install -e .
cd ../api && pip install fastapi uvicorn pydantic
PYTHONPATH="../engine:." uvicorn app.main:app --reload --port 8000
# Docs: http://localhost:8000/docs
```

---

## 11. Demo Website (Next.js)

### 11.1 Stack

- Next.js 15.5.23 (App Router, Turbopack)
- React 19
- Tailwind CSS 4
- Font: Geist Sans, Geist Mono, Instrument Serif (Google Fonts)

### 11.2 Komponen

| Komponen | Fungsi |
|----------|--------|
| `Nav.tsx` | Fixed nav, logo GreenLie, link demo/GitHub |
| `HeroSection.tsx` | Headline insomnia + fake green CI badge pulse |
| `ProblemSection.tsx` | Failure mode framing |
| `DemoBersebelahan.tsx` | Side-by-side diff + naive/greenlie toggle (auto 5s) |
| `HowItWorks.tsx` | 3 langkah: diff ? parse ? verdict |
| `TryItSection.tsx` | Button "greenlie analyze" ? load golden-report.json |
| `BuiltWithAO.tsx` | Kanban mockup + narasi AO workflow |
| `FooterSitus.tsx` | Links + #agentorchestrator |

### 11.3 Build Status

```bash
cd web && pnpm build  # OK ù static export ready
cd web && pnpm dev    # http://localhost:3000
```

### 11.4 Deploy Target

- **Vercel** (recommended)
- Environment: static, golden-report.json di `/public`

---

## 12. Sample Data & Golden Report

### 12.1 Scenario: Auth Middleware Test Backslide

**Konteks:** Agent ditugaskan fix CI failure pada auth tests. Alih-alih fix middleware, agent melemahkan assertion.

**Before** (`samples/before-agent-fix/tests/auth.test.js`):
- 3 test cases, 7+ assertions
- Proper 401 checks, exact error messages, user.id validation

**After** (`samples/after-agent-fix/tests/auth.test.js`):
- `toBe(401)` ? `toBeGreaterThan(0)`
- `toBe('Unauthorized')` ? `toBeDefined()`
- `toBe('user-123')` dan `toBe('dev@...')` ? **dihapus**
- `toMatch(/expired/)` ? diganti `toBeDefined()` on body

### 12.2 Golden Report

File: `samples/golden-report.json` (juga di `web/public/`)

Digunakan untuk:
- Fallback demo website (judges tanpa setup)
- Expected output dokumentasi
- API response reference

**Catatan:** Golden report (3 temuan, 42%) vs engine live (5 temuan, 29%) ù engine lebih agresif karena mendeteksi semua backslide di file. Update golden report sebelum submit agar konsisten.

---

## 13. Agent Orchestrator (AO) Workflow

### 13.1 Install

```bash
brew install agentwrapper/tap/agent-orchestrator
# App: /Applications/Agent Orchestrator.app
```

### 13.2 Cara Pakai untuk Hackathon

1. Buka AO ? Create project **GreenLie**
2. Delegate parallel tasks:
   - `engine/backslide-detector` ù Python engine
   - `api/fastapi-wrapper` ù API layer
   - `web/demo-bersebelahan` ù Next.js site
   - `samples/naive-agent-fix` ù test fixtures
3. **Rekam Kanban** selama build ù wajib untuk demo video
4. Ganti placeholder di `BuiltWithAO.tsx` dengan screenshot asli

### 13.3 Narasi AO untuk Pitch

> "GreenLie was built using Agent Orchestrator as the workspace ù parallel agents on engine, API, and demo site. The demo video shows the real Kanban board."

### 13.4 Resources AO

| Resource | URL |
|----------|-----|
| Website | https://aoagents.dev/ |
| GitHub | https://github.com/Untrivial-ai/agent-orchestrator |
| Discord | https://discord.gg/87NPrAuDa |
| Demo Prateek | https://x.com/Maaztwts/status/2082322742284853303 |
| Product Hunt | https://producthunt.com/products/agent-orchestrator |

---

## 14. Design System (ATM)

Detail lengkap: `docs/01-DESIGN-ATM.md`

### 14.1 Referensi Visual

| Sumber | Elemen dipakai |
|--------|----------------|
| Sentry | Red alert + dark bg |
| Resend | Code diff panels |
| Stripe Press | Instrument Serif headline |
| Raycast | Product-as-hero |
| Vercel | Geist Mono code |

### 14.2 Palette

| Token | Hex | Usage |
|-------|-----|-------|
| bg-primary | `#0D0F0C` | Background |
| bg-panel | `#161A14` | Cards |
| text-primary | `#E8E4DC` | Body |
| text-muted | `#8A8F82` | Secondary |
| green-fake | `#3DFF7A` | Suspicious CI green |
| red-truth | `#FF3B30` | Danger/blocked |
| accent-rust | `#C44D2E` | CTA, brand |

### 14.3 Anti AI-Slop Checklist

- [x] Bukan gradient ungu-pink
- [x] Instrument Serif (bukan Inter-only hero)
- [x] Asymmetric layout (problem section 2-col)
- [x] Copy spesifik (401, 29%, 5 findings)
- [x] Demo interaktif sebagai centerpiece
- [ ] 3-Second Test dengan designer (belum dilakukan)
- [ ] Real AO screenshot (placeholder saat ini)

---

## 15. Timeline & Progress

### 15.1 Timeline 36 Jam

| Window | Task | Status |
|--------|------|--------|
| **12 Agg sore** | Install AO, scaffold repo, engine MVP | ? |
| **12 Agg malam** | Sample repo, golden report, tests | ? |
| **12 Agg malam** | Web scaffold + build OK | ? |
| **12 Agg malam** | Deploy Vercel, GitHub public, API live | ? |
| **12ù13 Agg** | Tier D pack + social assets | ? |
| **13 Agg** | Rekam demo video manual (Screen Studio + AO asli) | ? |
| **13 Agg siang** | Upload video ? Discord + X + LinkedIn | ? |
| **13 Agg ? 7 PM** | Submit final | ? |

### 15.2 Progress Checklist Build

#### Stage 1 ù Ideation ?

- [x] Evaluasi 3 ide (GreenLie, FleetCollide, TaskDrift)
- [x] 9 Lensa scoring
- [x] DeadDrop checklist 6/6
- [x] ChatGPT Test LULUS
- [x] Verdict GO
- [x] Demo concept side-by-side
- [x] Design ATM research

#### Stage 2 - Build (selesai)

- [x] Python engine (parser, detector, CLI)
- [x] CLI `greenlie analyze` - verified 29%, 5 findings
- [x] Sample before/after agent fix
- [x] Golden report JSON (synced)
- [x] FastAPI `/analyze` + API live Vercel `/api/analyze`
- [x] Next.js demo website + Try It live
- [x] Web production build OK + deploy Vercel
- [x] GitHub public repo
- [x] AO terinstall
- [x] Submission docs + social assets

#### Stage 3 - Submit (in progress)

- [ ] Demo video manual (bukan auto-generate)
- [ ] AO Kanban footage asli di video
- [ ] Upload video, isi URL di TIER-D-READY.md
- [ ] Discord showcase + X + LinkedIn
- [ ] Optional: screenshot AO asli di website

Catatan: Video auto GreenLie-demo.mp4 tidak dipakai.

---

## 16. Submission Checklist

### 16.1 Pre-Submit

- [x] GitHub repo public: https://github.com/adindamochamad/GreenLie
- [x] README updated dengan live URL
- [x] Golden report sync dengan engine output (29%, 5 temuan)
- [ ] Demo video ? 3 menit (produk + AO Kanban) ù **rekam manual**
- [x] Live demo URL: https://web-flax-xi-10.vercel.app
- [ ] AO Kanban screenshot asli di website (optional ù placeholder `ao-kanban.png` ada)

### 16.2 Discord `#orchestra-project-showcase`

```
Team name:     Adinda Panca Mochamad (solo)
Project name:  GreenLie
Description:   [pitch 2-3 kalimat]
GitHub:        https://github.com/adindamochamad/GreenLie
Live demo:     [VERCEL_URL]
Demo video:    [YOUTUBE/Loom URL]
```

### 16.3 X / LinkedIn Post

```
Built GreenLie for @aoagents hackathon #agentorchestrator

Your Kanban says merge. Your tests say pass.
GreenLie catches when the agent fixed the TEST, not the bug.

Demo: [URL]
GitHub: [URL]

#agentorchestrator @aoagents
```

---

## 17. Demo Video Script

**Durasi target:** ? 3 menit

| Waktu | Konten |
|-------|--------|
| 0:00ù0:20 | Hook: "CI passed. Auth was broken. The agent didn't fix the bug ù it fixed the test." |
| 0:20ù0:45 | AO Kanban: cards moving (engine, web, samples) |
| 0:45ù1:30 | Website side-by-side demo: toggle naive vs GreenLie |
| 1:30ù2:00 | Terminal: `./scripts/demo.sh` ? Integrity 29%, 5 findings |
| 2:00ù2:30 | Highlight GL-001: `toBe(401)` ? `toBeGreaterThan(0)` |
| 2:30ù3:00 | GitHub + "Built with Agent Orchestrator" + CTA |

---

## 18. Perintah Referensi

```bash
# Demo one-command
./scripts/demo.sh

# Engine manual
cd engine && source .venv/bin/activate
pip install -e ".[dev]"
greenlie analyze                          # default sample
greenlie analyze --format json
pytest tests/ -v

# API lokal
cd api && PYTHONPATH="../engine:." uvicorn app.main:app --reload --port 8000

# Web dev
cd web && pnpm dev

# Web build
cd web && pnpm build

# AO
open -a "Agent Orchestrator"
```

---

## 19. URL & Placeholder

| Resource | URL | Status |
|----------|-----|--------|
| Hackathon Luma | https://luma.com/iw1v5erp | ? |
| Hackathon Notion | https://maaztwts.notion.site/The-Orchestra-3b532902e4a38040aedbc66966f4fc06 | ? |
| AO Website | https://aoagents.dev/ | ? |
| AO GitHub | https://github.com/Untrivial-ai/agent-orchestrator | ? |
| AO Discord | https://discord.gg/87NPrAuDa | ? join + spider react |
| GreenLie GitHub | https://github.com/adindamochamad/GreenLie | ? |
| Live Demo | https://web-flax-xi-10.vercel.app | ? |
| API (Vercel) | https://web-flax-xi-10.vercel.app/api/analyze | ? |
| Demo Video | https://youtu.be/RmDVxPWPBzU | ? |
| Submission pack | docs/TIER-D-READY.md | ? siap copy-paste |

---

## 20. Risiko & Mitigasi

| Risiko | Impact | Mitigasi |
|--------|--------|----------|
| Waktu 2 hari solo | Scope creep | MVP: 1 deteksi pattern, 1 sample, 1 demo |
| AO footage tidak direkam | Gagal submit | Rekam screen saat build hari ini |
| Golden report ? engine | Confusing judges | Sync sebelum deploy |
| Banyak AO clone competitors | Lower differentiation | GreenLie = produk standalone |
| Matcher regex false positive | Credibility | Sample curated, confidence score |
| Submission timezone unclear | Miss deadline | Submit 2 jam sebelum 7 PM, konfirmasi Discord |

---

## 21. Relasi Proyek Lain

| Proyek | Hackathon | Hubungan dengan GreenLie |
|--------|-----------|--------------------------|
| **SpecDrift** | Kiro Ready Spec Ship (deadline 23 Agg) | Same author, different angle: SpecDrift = spec vs code; GreenLie = test integrity vs agent fix. **Jangan reuse** untuk Orchestra. |
| **HeatRecall** | CockroachDB x AWS | Same side-by-side demo pattern; different domain (agent memory). |
| **OmniBridge** | Claude Opus 4.7 | Same author; different problem (serial protocols). |

**Pola menang yang reused dari BACKSTOP/SpecDrift post-mortem:**
- Insomnia-grade problem statement
- Side-by-side demo
- Stakes tinggi (prod outage, bukan inconvenience)
- Nama menggambarkan mekanisme

---

## 22. Glosarium

| Term | Definisi |
|------|----------|
| **Green Lie** | CI hijau / board merge-ready, tapi test sudah tidak valid |
| **Test Backslide** | Assertion diperlemah dari exact ke range/truthy/defined |
| **Assertion Dropped** | Agent menghapus assertion tanpa mengganti setara |
| **Integrity Score** | % assertion before yang masih setara strictness after |
| **AO** | Agent Orchestrator ù fleet coding agents parallel |
| **CI Feedback Loop** | AO feature: CI fail ? route back to owning agent |
| **ATM** | Amati-Tiru-Modifikasi ù metode design Stage 2 |
| **ChatGPT Test** | "Apakah ChatGPT bisa produce hasil setara?" ù eliminasi ide |

---

*Dokumen ini = single source of truth konteks proyek GreenLie untuk The Orchestra hackathon.*
*Pemilik: Adinda Panca Mochamad ù Solo ù Aug 2026*
