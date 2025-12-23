import os
import pandas as pd
import numpy as np
import yfinance as yf
import warnings
import json
import time
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults
from colorama import Fore, Style, init

# Inicjalizacja
init(autoreset=True)
warnings.filterwarnings("ignore")

# Ładowanie kluczy (Szukamy .env dwa poziomy wyżej od folderu skryptu)
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
load_dotenv(os.path.join(project_root, ".env"))

# --- 1. DATA MANAGER ---
class DataManager:
    def get_data(self, ticker):
        print(f"{Fore.CYAN}📥 Pobieram dane rynkowe dla {ticker}...{Style.RESET_ALL}")
        try:
            df = yf.download(ticker, period="1y", progress=False, auto_adjust=True)
            if isinstance(df.columns, pd.MultiIndex):
                try: df = df.xs('Close', axis=1, level=0, drop_level=True)
                except: pass
            elif 'Close' in df.columns:
                df = df[['Close']]

            if isinstance(df, pd.Series):
                 df = df.to_frame(name=ticker)
            return df
        except Exception as e:
            print(f"❌ Błąd yfinance: {e}")
            return pd.DataFrame()

    def get_news(self, ticker):
        print(f"{Fore.CYAN}🌍 Szukam newsów o {ticker}...{Style.RESET_ALL}")
        if not os.getenv("TAVILY_API_KEY"):
            return []
        tavily = TavilySearchResults(k=3)
        try:
            return tavily.invoke(f"{ticker} stock news analysis current trends")
        except:
            return []

# --- 2. QUANT ENGINE ---
class QuantEngine:
    def analyze(self, df):
        if df.empty: return {}
        print(f"{Fore.YELLOW}🧮 Obliczam ryzyko i wskaźniki...{Style.RESET_ALL}")
        returns = np.log(df / df.shift(1)).dropna()

        if len(returns) < 2: return {}

        volatility = returns.std().iloc[0] * np.sqrt(252)
        mean_ret = returns.mean().iloc[0] * 252
        sharpe = (mean_ret - 0.04) / volatility if volatility != 0 else 0

        price = df.iloc[-1].item()
        sma_50 = df.rolling(50).mean().iloc[-1].item()

        # RSI
        delta = df.diff()
        gain = delta.where(delta > 0, 0).rolling(14).mean()
        loss = -delta.where(delta < 0, 0).rolling(14).mean()
        rs = gain / (loss + 1e-9)
        rsi = 100 - (100 / (1 + rs))
        current_rsi = rsi.iloc[-1].item()

        tech_score = 50
        if price > sma_50: tech_score += 20
        else: tech_score -= 20

        if current_rsi < 30: tech_score += 20
        elif current_rsi > 70: tech_score -= 20

        return {
            "volatility": volatility,
            "sharpe": sharpe,
            "rsi": current_rsi,
            "tech_score": tech_score
        }

# --- 3. SENTIMENT AGENT ---
class SentimentAgent:
    def __init__(self):
        if os.getenv("GOOGLE_API_KEY"):
            self.llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
        else:
            self.llm = None

    def analyze(self, news_list):
        if not self.llm or not news_list:
            return {"score": 0.0, "reason": "Brak danych/klucza"}

        print(f"{Fore.MAGENTA}🤖 AI analizuje sentyment...{Style.RESET_ALL}")
        context = "\n".join([f"- {n['content']}" for n in news_list if 'content' in n])

        prompt = f"""
        Jesteś analitykiem giełdowym. Przeanalizuj poniższe nagłówki.
        Oceń sentyment w skali od -1.0 (Tragiczny) do 1.0 (Euforia).
        Podaj TYLKO JSON w formacie: {{"score": float, "reason": "krótkie zdanie"}}

        NEWSY:
        {context}
        """
        try:
            response = self.llm.invoke(prompt)
            content = response.content.replace("```json", "").replace("```", "").strip()
            return json.loads(content)
        except Exception as e:
            return {"score": 0.0, "reason": "Błąd modelu"}

# --- 4. STRATEGY ENGINE ---
class StrategyEngine:
    def decide(self, quant_data, sent_data):
        print(f"{Fore.GREEN}⚖️ Podejmuję decyzję inwestycyjną...{Style.RESET_ALL}")
        w_tech, w_sent = 0.6, 0.4
        sent_score_norm = (sent_data.get('score', 0) + 1) * 50
        tech_score = quant_data.get('tech_score', 50)

        final_score = (tech_score * w_tech) + (sent_score_norm * w_sent)

        action = "HOLD"
        if final_score > 65: action = "BUY"
        elif final_score < 35: action = "SELL"

        return action, final_score

# --- MAIN APP LOOP ---
def run_hedge_fund():
    print(f"{Fore.YELLOW}{Style.BRIGHT}" + "="*40)
    print("   HEDGE FUND IN A BOX (v1.0 CLI)")
    print("="*40 + f"{Style.RESET_ALL}")

    dm = DataManager()
    qe = QuantEngine()
    sa = SentimentAgent()
    se = StrategyEngine()

    while True:
        try:
            ticker = input("\nPodaj ticker (np. BTC-USD, NVDA) lub 'q': ").upper().strip()
            if ticker == 'Q': break
            if not ticker: continue

            df = dm.get_data(ticker)
            if df.empty:
                print("❌ Nie znaleziono danych.")
                continue

            q_res = qe.analyze(df)
            news = dm.get_news(ticker)
            s_res = sa.analyze(news)
            action, score = se.decide(q_res, s_res)

            print("\n" + "-"*30)
            print(f"📊 RAPORT DLA: {Fore.CYAN}{ticker}{Style.RESET_ALL}")
            print("-" * 30)
            print(f"📉 Volatility: {q_res.get('volatility',0):.2%}")
            print(f"📈 RSI:        {q_res.get('rsi',0):.2f}")
            print(f"🤖 AI Score:   {s_res.get('score',0)}")
            print("-" * 30)

            color = Fore.GREEN if action == "BUY" else (Fore.RED if action == "SELL" else Fore.WHITE)
            print(f"🎯 DECYZJA:    {color}{Style.BRIGHT}{action}{Style.RESET_ALL} (Score: {score:.1f})")
            print("-" * 30)

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"❌ Błąd: {e}")

if __name__ == "__main__":
    run_hedge_fund()
