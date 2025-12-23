# 🏛️ Financial AI Architect - Portfolio Showcase

### _From Quant Analysis to Autonomous Agents_

![Python](https://img.shields.io/badge/Python-3.11-blue)
![AI](https://img.shields.io/badge/GenAI-Gemini%202.5-orange)
![Quant](https://img.shields.io/badge/Quant-Backtesting.py%20%26%20XGBoost-green)
![Docker](https://img.shields.io/badge/Deployment-Docker-blue)
![License](https://img.shields.io/badge/License-MIT-green)

**Zbiór zaawansowanych projektów inżynierskich łączących Quantitative Finance, Machine Learning oraz Generative AI (LLM Agents).**

To repozytorium stanowi **Portfolio Showcase** – zawiera wybrane, finalne projekty ("The Best Of") zrealizowane podczas intensywnego 12-tygodniowego bootcampu inżynierskiego. Każdy plik to działający, samodzielny moduł rozwiązujący konkretny problem biznesowy.

---

## 📂 Zawartość Portfolio (Highlights)

Poniżej znajdują się kluczowe projekty zawarte w tym repozytorium:

| Moduł                | Projekt                    | Plik                                     | Technologie                       |
| -------------------- | -------------------------- | ---------------------------------------- | --------------------------------- |
| **LLM RAG**          | Analityk PDF (OCR + AI)    | `06_project_pdf_analyst.ipynb`           | `OpenAI/Gemini`, `PDF Parsing`    |
| **LLM RAG**          | 10-K Report Analyzer       | `06_project_10k_analyzer.ipynb`          | `LangChain`, `ChromaDB`, `Tables` |
| **Machine Learning** | Demand Forecasting         | `06_project_demand_forecasting.ipynb`    | `XGBoost`, `Feature Engineering`  |
| **Quant Finance**    | Risk Manager Dashboard     | `06_project_risk_dashboard.ipynb`        | `VaR`, `Sharpe`, `Portfolio Opt`  |
| **Time Series**      | Hybrid Volatility Forecast | `06_project_volatility_forecaster.ipynb` | `GARCH`, `NHITS (Deep Learning)`  |
| **AI Agents**        | Autonomous Researcher      | `06_project_autonomous_analyst.ipynb`    | `LangGraph`, `Multi-Agent`        |
| **Fine-Tuning**      | Sentiment Model (QLoRA)    | `02_local_finetuning.ipynb`              | `PyTorch`, `PEFT`, `Llama/Qwen`   |
| **MLOps**            | Cloud Deployment           | `06_project_cloud_deploy.ipynb`          | `Docker`, `FastAPI`, `Streamlit`  |
| **Graph ML**         | AML Fraud Detection        | `04_fraud_detection.ipynb`               | `NetworkX`, `Graph Algorithms`    |
| **Algo Trading**     | Momentum Strategy Bot      | `06_project_trading_bot.ipynb`           | `Backtesting.py`, `Optimization`  |
| **Full App**         | **Hedge Fund CLI**         | `hedge_fund.py`                          | _Integrated System_               |

---

## 📚 Pełna Mapa Drogowa (Full Bootcamp Roadmap)

Poniżej znajduje się pełny plan szkolenia, które doprowadziło do powstania powyższych rozwiązań. Repozytorium zawiera esencję tych 12 tygodni.

---

## 🚀 FAZA 1: FUNDAMENTY (Data & AI Basics)

### **Tydzień 1: Fundamenty**

Ikona do wstawienia dla potwierdzenia statusu: ✅

| Dzień  | Temat Główny    | Co robimy (Notebook)                           | Tech Stack          | Status |
| ------ | --------------- | ---------------------------------------------- | ------------------- | ------ |
| **D1** | Python & ETL    | Klasy, czyszczenie danych, podstawy inżynierii | `uv, Python`        |        |
| **D2** | Pandas & NumPy  | Wektoryzacja, analiza szeregów czasowych       | `pandas, numpy`     |        |
| **D3** | Security & Logs | Pliki .env, bezpieczne logowanie zdarzeń       | `python-dotenv`     |        |
| **D4** | API & Walidacja | Serwer FastAPI, Modele Pydantic                | `fastapi, pydantic` |        |
| **D5** | LLM Intro       | Tokenizacja, Embeddings, Lokalne modele        | `transformers`      |        |
| **D6** | PROJEKT #1      | Analityk PDF (Gemini + OCR)                    | `gemini, pypdf`     |        |
| **D7** | Odpoczynek      | Reset                                          | ☕                  |        |

---

## 🧠 FAZA 2: LLM ENGINEERING (RAG & Agents)

### **Tydzień 2: LLM Core**

| Dzień  | Temat Główny     | Co robimy (Notebook)                      | Tech Stack       | Status |
| ------ | ---------------- | ----------------------------------------- | ---------------- | ------ |
| **D1** | Vector DBs       | ChromaDB, Wyszukiwanie Semantyczne        | `chromadb`       |        |
| **D2** | RAG Architecture | Chunking, łączenie bazy z Gemini          | `langchain`      |        |
| **D3** | Advanced RAG     | Re-ranking (naprawa błędów wyszukiwania)  | `cross-encoder`  |        |
| **D4** | LangChain        | Budowa łańcuchów (Chains) i LCEL          | `langchain-core` |        |
| **D5** | Data Ingestion   | Parsowanie tabel z PDF                    | `pdfplumber`     |        |
| **D6** | PROJEKT #2       | 10-K Analyzer (RAG na raportach rocznych) | `langchain`      |        |
| **D7** | Odpoczynek       | Reset                                     | ☕               |        |

### **Tydzień 3: ML Basics**

| Dzień  | Temat Główny   | Co robimy (Notebook)                      | Tech Stack | Status |
| ------ | -------------- | ----------------------------------------- | ---------- | ------ |
| **D1** | EDA & Cleaning | Czyszczenie "brudnych" danych finansowych | `seaborn`  |        |
| **D2** | Regresja       | Przewidywanie ceny (Liniowa, Ridge)       | `sklearn`  |        |
| **D3** | Klasyfikacja   | Decyzja KUP/SPRZEDAJ (Logistic, Trees)    | `sklearn`  |        |
| **D4** | Ensemble       | Random Forest & XGBoost                   | `xgboost`  |        |
| **D5** | Feature Eng.   | Tworzenie wskaźników i Pipeline'y         | `sklearn`  |        |
| **D6** | PROJEKT #3     | Demand Forecasting (Prognoza Sprzedaży)   | `xgboost`  |        |
| **D7** | Odpoczynek     | Reset                                     | ☕         |        |

---

## 📉 FAZA 3: QUANT FINANCE & TRADING

### **Tydzień 4: Quant Stats**

| Dzień  | Temat Główny | Co robimy (Notebook)                          | Tech Stack   | Status |
| ------ | ------------ | --------------------------------------------- | ------------ | ------ |
| **D1** | Statystyka   | Rozkłady, Skośność, Grube Ogony (Fat Tails)   | `scipy`      |        |
| **D2** | Korelacja    | Macierze korelacji, Rolling Correlation       | `seaborn`    |        |
| **D3** | Metryki      | Sharpe, Sortino, Beta, Alpha                  | `numpy`      |        |
| **D4** | Ryzyko (VaR) | Value at Risk, CVaR (Historyczny/Monte Carlo) | `scipy`      |        |
| **D5** | Portfel      | Teoria Markowitza (Efficient Frontier)        | `scipy`      |        |
| **D6** | PROJEKT #4   | Risk Manager Dashboard                        | `matplotlib` |        |
| **D7** | Odpoczynek   | Reset                                         | ☕           |        |

### **Tydzień 5: Time Series**

| Dzień  | Temat Główny  | Co robimy (Notebook)               | Tech Stack       | Status |
| ------ | ------------- | ---------------------------------- | ---------------- | ------ |
| **D1** | Klasyka       | ARIMA, Stacjonarność               | `statsmodels`    |        |
| **D2** | Modern TS     | Time-Series Transformers (NHITS)   | `neuralforecast` |        |
| **D3** | Volatility    | Modele GARCH (prognoza zmienności) | `arch`           |        |
| **D4** | Backtesting 1 | Szybki Backtesting wektorowy       | `vectorbt`       |        |
| **D5** | Backtesting 2 | Walk-Forward Validation            | `vectorbt`       |        |
| **D6** | PROJEKT #5    | Volatility Forecaster              | `arch`           |        |
| **D7** | Odpoczynek    | Reset                              | ☕               |        |

---

## 🤖 FAZA 4: ADVANCED AI & PRODUCTION

### **Tydzień 6: Agents**

| Dzień  | Temat Główny | Co robimy (Notebook)                | Tech Stack  | Status |
| ------ | ------------ | ----------------------------------- | ----------- | ------ |
| **D1** | Tools        | Function Calling (AI używa Pythona) | `gemini`    |        |
| **D2** | LangGraph 1  | Agenty stanowe (Stateful Agents)    | `langgraph` |        |
| **D3** | Web Search   | Agent szukający newsów w sieci      | `tavily`    |        |
| **D4** | Multi-Agent  | Zespół agentów (Analityk + Krytyk)  | `langgraph` |        |
| **D5** | Memory       | Dodawanie pamięci do agenta         | `langgraph` |        |
| **D6** | PROJEKT #6   | Autonomous Market Researcher        | `langgraph` |        |
| **D7** | Odpoczynek   | Reset                               | ☕          |        |

### **Tydzień 7: Fine-Tuning**

| Dzień  | Temat Główny | Co robimy (Notebook)                        | Tech Stack | Status |
| ------ | ------------ | ------------------------------------------- | ---------- | ------ |
| **D1** | Teoria       | LoRA, PEFT, Quantization (jak to działa?)   | `peft`     |        |
| **D2** | Data Prep    | Formatowanie danych finansowych do treningu | `datasets` |        |
| **D3** | Trening      | Dostrajanie Qwena 1.5B (Local QLoRA)        | `trl`      |        |
| **D4** | Ewaluacja    | LLM-as-a-Judge (Sędzia ocenia studenta)     | `gemini`   |        |
| **D5** | Local RAG    | RAG na własnym modelu (prywatność)          | `ollama`   |        |
| **D6** | PROJEKT #7   | Fine-Tuned Sentiment Trader                 | `peft`     |        |
| **D7** | Odpoczynek   | Reset                                       | ☕         |        |

---

## 🚀 FAZA 5: MLOps & CAPSTONE

### **Tydzień 8: MLOps**

| Dzień  | Temat Główny   | Co robimy (Notebook / Code)    | Tech Stack       | Status |
| ------ | -------------- | ------------------------------ | ---------------- | ------ |
| **D1** | Docker         | Konteneryzacja aplikacji       | `docker`         |        |
| **D2** | Docker-Compose | Multi-container Apps           | `docker-compose` |        |
| **D3** | Frontend       | Budowa UI w Streamlit          | `streamlit`      |        |
| **D4** | Monitoring     | Śledzenie LLMów (LangSmith)    | `langsmith`      |        |
| **D5** | CI/CD          | Automatyczne testy na GitHubie | `github-actions` |        |
| **D6** | PROJEKT #8     | Deploy Aplikacji Finansowej    | `docker`         |        |
| **D7** | Odpoczynek     | Reset                          | ☕               |        |

---

## 🕸️ FAZA 6: ADVANCED DATA STRUCTURES

### **Tydzień 9: Graphs (GNN)**

| Dzień  | Temat Główny     | Co robimy (Notebook)                       | Tech Stack  | Status |
| ------ | ---------------- | ------------------------------------------ | ----------- | ------ |
| **D1** | Graph Theory     | Węzły, Krawędzie i Relacje w finansach     | `networkx`  |        |
| **D2** | Knowledge Graphs | Budowa grafu zależności (Supply Chain)     | `langchain` |        |
| **D3** | Graph RAG        | Łączenie bazy wektorowej z grafem wiedzy   | `networkx`  |        |
| **D4** | Fraud Detection  | Wykrywanie prania brudnych pieniędzy       | `networkx`  |        |
| **D5** | GNN Intro        | Wstęp do PyTorch Geometric                 | `pyg`       |        |
| **D6** | PROJEKT #9       | AML Detective (System wykrywania anomalii) | `networkx`  |        |
| **D7** | Odpoczynek       | Reset                                      | ☕          |        |

---

## 📈 FAZA 7: ALGOTRADING SIMULATION

### **Tydzień 10: Algo-Trading**

| Dzień  | Temat Główny    | Co robimy (Notebook)                         | Tech Stack       | Status |
| ------ | --------------- | -------------------------------------------- | ---------------- | ------ |
| **D1** | Backtesting 101 | Jak symulować historię (Look-ahead bias)     | `backtesting.py` |        |
| **D2** | Strategy Logic  | Optymalizacja parametrów strategii (RSI/SMA) | `backtesting.py` |        |
| **D3** | Position Sizing | Kelly Criterion (Zarządzanie kapitałem)      | `pandas`         |        |
| **D4** | Portfolio Opt.  | Rebalansowanie portfela w czasie             | `pandas`         |        |
| **D5** | Execution Sim   | Symulacja poślizgów (Slippage) i prowizji    | `backtesting.py` |        |
| **D6** | PROJEKT #10     | AI Trading Bot Backtest                      | `backtesting.py` |        |
| **D7** | Odpoczynek      | Reset                                        | ☕               |        |

---

## 🏆 FAZA 8: CAPSTONE PROJECT

**Finał.** Budujesz **"Hedge Fund in a Box"**.

### **Tydzień 11: Capstone I** _(Budowa Rdzenia)_

| Dzień  | Temat Główny    | Co zrobiliśmy (Notebook)              | Status |
| ------ | --------------- | ------------------------------------- | ------ |
| **D1** | Architektura    | DataManager (Pobieranie Cen i Newsów) |        |
| **D2** | Quant Engine    | Mózg Matematyczny (Markowitz, VaR)    |        |
| **D3** | Sentiment Agent | Mózg Analityczny (Gemini 2.5)         |        |
| **D4** | Strategy Engine | Logika Decyzyjna (Wagi, Kill Switch)  |        |
| **D5** | Integration     | LangGraph Agent + Tools               |        |
| **D6** | MVP Demo        | Aplikacja CLI (Hedge Fund App)        |        |
| **D7** | Odpoczynek      | Reset ☕                              |        |

### **Tydzień 12: Capstone II** _(Polerowanie)_

| Dzień  | Temat Główny  | Co robimy                                        | Status |
| ------ | ------------- | ------------------------------------------------ | ------ |
| **D1** | Frontend      | Budowa profesjonalnego Dashboardu (Streamlit)    |        |
| **D2** | Optimization  | Session State, Caching, Fix Warningów            |        |
| **D3** | Documentation | Pisanie README i dokumentacji technicznej        |        |
| **D4** | Video Demo    | Nagranie 2-minutowego filmu "Jak to działa"      |        |
| **D5** | Review & CV   | Dodanie projektu do CV, LinkedIn, GitHub Profile |        |
| **D6** | PUBLIKACJA    | Wielki Finał! Code Freeze i Release v1.0.        |        |
| **D7** | ŚWIĘTOWANIE   | 🍾🥂                                             |        |

---

## **Author:** Krzysztof Pika
