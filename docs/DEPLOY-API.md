# Deploy API ke Render

1. Buka https://dashboard.render.com → **New** → **Blueprint**
2. Connect repo `adindamochamad/GreenLie`
3. Render akan baca `render.yaml` di root
4. Deploy selesai → catat URL (mis. `https://greenlie-api.onrender.com`)
5. Set env di Vercel:
   ```bash
   cd web && vercel env add NEXT_PUBLIC_API_URL production
   # isi: https://greenlie-api.onrender.com
   vercel --prod
   ```

## Lokal

```bash
cd engine && source .venv/bin/activate && pip install -e .
pip install -r api/requirements.txt
cd ../api && PYTHONPATH="../engine:." uvicorn app.main:app --reload --port 8000
```

Docs: http://localhost:8000/docs
