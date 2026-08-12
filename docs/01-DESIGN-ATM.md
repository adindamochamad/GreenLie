# GreenLie — Design ATM (Amati, Tiru, Modifikasi)

> Stage 2 visual research. Hackathon: The Orchestra · Aug 12-13, 2026

---

## Fase 1: AMATI — Tabel Referensi

| # | Nama & URL | Hero | Typography | Palette | Layout | Motion | Wow Element |
|---|-----------|------|------------|---------|--------|--------|-------------|
| 1 | **[Raycast](https://raycast.com)** | Product UI as hero, dark | Inter tight | `#FF6363` accent, `#0D0D0D` bg | Left text, product right | Command palette reveal | Show-don't-tell dengan UI nyata |
| 2 | **[Resend](https://resend.com)** | Code snippet hero | Inter + mono | Black + orange `#F97316` | Asymmetric whitespace | Code typing | Dev audience instant connect |
| 3 | **[Linear](https://linear.app)** | Minimal headline + mesh | Inter 600/700 | `#5E6AD2`, `#0A0A0B` | Center, asymmetric grid | Subtle fade-up | Premium dev tool feel |
| 4 | **[Stripe Press](https://press.stripe.com)** | Editorial serif headline | Serif + sans | Cream `#F6F1EB`, `#1A1A2E` | Magazine offset columns | Parallax | Unexpected editorial for dev tool |
| 5 | **[Vercel](https://vercel.com)** | Bold mono headline | Geist Sans/Mono | Black/white extreme | Bento grid | Triangle spin | High contrast instant premium |
| 6 | **[Sentry](https://sentry.io)** | Error monitoring aesthetic | System sans + mono | Dark + red alert | Split panels | Alert pulse | Red = danger signal (perfect for GreenLie) |

### Pilihan kombinasi GreenLie

| Ambil Dari | Elemen | Alasan |
|-----------|--------|--------|
| **Sentry** | Red alert panels + dark bg | GreenLie = fake green vs real danger |
| **Resend** | Code diff panels side-by-side | Before/after test diff natural fit |
| **Stripe Press** | Instrument Serif headline | Anti AI-slop typography |
| **Raycast** | Product-as-hero (demo centerpiece) | Side-by-side demo = hero |
| **Vercel** | Geist Mono for code | Assertion diff readability |

---

## Fase 2: TIRU — Design Tokens

```css
--bg-primary:     #0D0F0C;   /* olive-black */
--bg-panel:       #161A14;
--text-primary:   #E8E4DC;
--text-muted:     #8A8F82;
--green-fake:     #3DFF7A;   /* suspicious CI green */
--red-truth:      #FF3B30;   /* real danger */
--accent-rust:    #C44D2E;   /* brand accent */
--font-display:   'Instrument Serif', serif;
--font-mono:      'JetBrains Mono', monospace;
--font-body:      'Geist Sans', sans-serif;
```

---

## Fase 3: MODIFIKASI — Section List

1. **Hero** — "Your board says merge." + fake green pulse animation
2. **The Green Lie** — problem framing, bukan feature grid
3. **Side-by-Side Demo** — centerpiece: naive merge vs GreenLie block
4. **How It Reads a PR** — 3 langkah visual (diff, parse, verdict)
5. **Built with AO** — Kanban screenshot placeholder
6. **Try It** — trigger analyze, show golden report
7. **Footer** — GitHub, #agentorchestrator

### Signature elements

- **Fake green pulse** on "CI PASS" badge that flickers suspiciously
- **Diff highlight** — before red, after amber, verdict rust
- **Integrity counter** — animates 100 -> 29 with color shift
- **Custom crosshair cursor** on demo section only

---

## 3-Second Test checklist

- [ ] Bukan gradient ungu-pink
- [ ] Bukan Inter-only hero
- [ ] Ada asymmetric layout break
- [ ] Copy specific dengan angka (401, 29%, 5 findings)
- [ ] Demo interaktif visible above fold area
