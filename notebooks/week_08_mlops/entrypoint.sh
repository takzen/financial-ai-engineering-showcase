#!/bin/bash

# 1. Uruchom Backend w tle (&)
# --host 0.0.0.0 jest krytyczny w chmurze
# --port 8000 to standardowy port API
echo "🚀 Uruchamiam Backend (FastAPI)..."
uvicorn app:app --host 0.0.0.0 --port 8000 &

# 2. Czekaj chwilę, aż API wstanie (opcjonalne, ale dobra praktyka)
sleep 5

# 3. Uruchom Frontend na głównym wątku
# Render/Railway udostępnia tylko jeden port publiczny (zazwyczaj ten zdefiniowany w zmiennej PORT lub domyślnie 10000/8080)
# Streamlit musi nasłuchiwać na tym porcie.
echo "🚀 Uruchamiam Frontend (Streamlit)..."
streamlit run frontend/app.py --server.port 8501 --server.address 0.0.0.0