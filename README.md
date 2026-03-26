# ConvoPro — ChatGPT-style Chat UI

ConvoPro is a lightweight ChatGPT-style interface that lets users chat with Groq-hosted models while persisting conversations to MongoDB.

## Problem Solved

Enables a fast, local-first chat experience with selectable LLMs and conversation history persistence for easy retrieval.

## Tech Stack

- Python 3.13
- Streamlit
- Groq (via LlamaIndex)
- LlamaIndex
- MongoDB (PyMongo)
- Pydantic + pydantic-settings
- python-dotenv

## How to Run (Local)

### 1) Clone and set up a virtual environment

```bash
git clone https://github.com/Jaisheesh-2006/ConvoPro.git
cd ConvoPro
python -m venv .venv
```

Activate the virtual environment:

- Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

- macOS/Linux

```bash
source .venv/bin/activate
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Configure environment variables

```bash
copy .env.example .env
```

On macOS/Linux, use:

```bash
cp .env.example .env
```

Edit `.env` as needed (MongoDB URL, DB name, Groq API key, and models list).

### 4) Ensure services are running

- **MongoDB** should be running locally (default: `mongodb://localhost:27017/`).
- **Groq** requires a valid `GROQ_API_KEY` in your `.env` file.

### 5) Run the app

```bash
streamlit run main.py
```

## Project Structure (Quick Look)

- `main.py` — Streamlit UI and chat flow
- `services/` — model list, titles, and chat utilities
- `db/` — MongoDB connection and conversation persistence
- `config/` — environment-driven settings

## Pre-Deployment Checklist

- Python version is `3.10+`
- `.env` is configured with valid `GROQ_API_KEY`
- `GROQ_MODELS` contains at least one valid Groq model
- MongoDB is reachable from deployment environment
- Start command works: `streamlit run main.py --server.port $PORT --server.address 0.0.0.0`

## Free Deployment Options

### 1) Streamlit Community Cloud (best for this project)

- Free for public GitHub repos
- Native Streamlit support
- Simple setup from repo

Steps:

1. Push this repo to GitHub.
2. Go to share.streamlit.io and connect your GitHub.
3. Select repo and set entrypoint to `main.py`.
4. Add secrets (`GROQ_API_KEY`, `MONGO_DB_URL`, `MONGO_DB_NAME`, `GROQ_MODELS`) in app settings.
5. Deploy.

### 2) Render (free web service)

- Works with Streamlit
- Better control over runtime settings

Suggested settings:

- Build command: `pip install -r requirements.txt`
- Start command: `streamlit run main.py --server.port $PORT --server.address 0.0.0.0`

### 3) Hugging Face Spaces (free)

- Good for demo apps
- Supports Streamlit SDK directly

Note: For all platforms, use MongoDB Atlas free tier instead of local MongoDB.

---
