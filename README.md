<<<<<<< HEAD
# India-market-analyzer
"A professional-grade FastAPI backend that automates Indian market research. Uses Tavily AI for real-time scraping and Gemini 2.5 Flash for structured report generation. Features rate-limiting, Jinja2 templating, and Markdown export functionality."
=======
# India Market AI Analyzer

A production-ready FastAPI backend that scrapes real-time Indian market data and generates structured, AI-driven trade opportunity reports using **Google Gemini 2.5 Flash**.

## 🚀 Overview
This project is a full-stack AI agent designed to bridge the gap between raw web data and actionable investment insights. It automates the process of searching for sector-specific news, cleaning the data, and using Large Language Models (LLMs) to synthesize professional market reports.

## ✨ Key Features
- **Real-Time Data Sourcing:** Integrated with **Tavily AI** for high-precision, AI-optimized web scraping of the Indian financial landscape.
- **LLM Intelligence:** Leverages **Gemini 2.5 Flash** for advanced context window processing and structured report generation.
- **Dual-Mode Delivery:** - **Article Mode:** A polished, CSS-styled web interface for human readers.
    - **Export Mode:** Instant `.md` file download functionality for data portability.
- **Enterprise-Grade Middleware:** - **Rate Limiting:** Implemented via `SlowAPI` to prevent API abuse and manage costs.
    - **Environment Security:** Full `.env` integration to protect sensitive API credentials.
    - **Jinja2 Templating:** Decoupled Frontend and Backend logic for better maintainability.

## 🛠️ Tech Stack
| Component | Technology |
| :--- | :--- |
| **Language** | Python 3.10+ |
| **Framework** | FastAPI |
| **AI/LLM** | Google GenAI (Gemini 2.5 Flash) |
| **Search Engine** | Tavily Search API |
| **Templating** | Jinja2 & HTML5/CSS3 |
| **Rate Limiter** | SlowAPI |

## ⚙️ Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/sai002/india-market-analyzer.git](https://github.com/sai002/india-market-analyzer.git)
   cd india-market-analyzer/Main



2.Set up Virtual Environment:

python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate


3.Install Dependencies: 

python -m pip install -r requirements.txt

4. Configuration:

Create a .env file in the Main directory:

TAVILY_API_KEY=your_tavily_key_here
GEMINI_API_KEY=your_google_gemini_key_here

5.Run the Server:

python -m uvicorn main:app --reload

📈 Usage
Web View: Navigate to http://127.0.0.1:8000/analyze/{sector} (e.g., /analyze/pharmaceuticals)

Download Report: Click the "Download .md File" button on the article page or append ?download=true to the URL.

API Documentation: Interactive Swagger UI available at http://127.0.0.1:8000/docs.

Developed by SAIKIRAN BANDI | MCA Graduate 2025
>>>>>>> 89898f6 (Initial commit: AI Market Analyzer with FastAPI and Gemini)
