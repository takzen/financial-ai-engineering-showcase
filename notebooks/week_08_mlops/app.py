import os
import time
from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob
from sqlalchemy import create_engine, Column, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Konfiguracja Bazy
DB_USER = os.getenv("POSTGRES_USER", "user")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")
DB_NAME = os.getenv("POSTGRES_DB", "sentiment_db")
DB_HOST = os.getenv("DB_HOST", "db")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 2. Tabela
class SentimentLog(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    score = Column(Float)
    label = Column(String)

# 3. Inicjalizacja z RETRY (Poprawka!)
def init_db():
    retries = 5
    while retries > 0:
        try:
            Base.metadata.create_all(bind=engine)
            print("✅ Połączono z bazą danych (Tabele utworzone).")
            return # Sukces, wychodzimy
        except Exception as e:
            print(f"⏳ Baza nie jest gotowa, czekam 5s... (Błąd: {e})")
            time.sleep(5)
            retries -= 1
    print("❌ Nie udało się połączyć z bazą po 5 próbach.")

# 4. App
app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

class NewsItem(BaseModel):
    text: str

@app.post("/analyze")
def analyze_sentiment(news: NewsItem):
    blob = TextBlob(news.text)
    sentiment = blob.sentiment.polarity

    label = "NEUTRAL"
    if sentiment > 0.1: label = "POSITIVE"
    if sentiment < -0.1: label = "NEGATIVE"

    # Zapis
    try:
        session = SessionLocal()
        log_entry = SentimentLog(text=news.text, score=sentiment, label=label)
        session.add(log_entry)
        session.commit()
        session.close()
        saved = True
    except Exception as e:
        print(f"Błąd zapisu: {e}")
        saved = False

    return {"text": news.text, "label": label, "saved_to_db": saved}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
