# API GreenLie — Tanpa Render

API sudah **built-in di Vercel** sebagai Next.js Route Handlers. Tidak perlu deploy terpisah.

| Endpoint | Method | Deskripsi |
|----------|--------|-----------|
| `/api/health` | GET | Health check |
| `/api/analyze` | POST | Analisis sample `naive-agent` |

## Contoh

```bash
curl https://web-flax-xi-10.vercel.app/api/health

curl -X POST https://web-flax-xi-10.vercel.app/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"sample":"naive-agent"}'
```

## Lokal

```bash
cd web && pnpm dev
# http://localhost:3000/api/health
# POST http://localhost:3000/api/analyze
```

Engine TypeScript mirror ada di `web/lib/greenlie/` — output match Python CLI untuk sample yang sama.

## FastAPI (opsional)

Python API di `api/` tetap ada untuk development lokal:

```bash
cd engine && source .venv/bin/activate && pip install -e .
pip install -r api/requirements.txt
cd ../api && PYTHONPATH="../engine:." uvicorn app.main:app --reload --port 8000
```

## Render (tidak wajib)

Jika tetap ingin Python API di Render:
1. Buat API key: https://dashboard.render.com/u/settings#api-keys
2. Jalankan `render login` di terminal
3. Atau set `RENDER_API_KEY` dan gunakan Blueprint dari `render.yaml`

Untuk hackathon, **Vercel `/api/analyze` sudah cukup**.
