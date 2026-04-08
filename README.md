# ConvoPro

ConvoPro is a Streamlit-based conversational AI application that provides a ChatGPT-style interface using Groq-hosted LLMs, with persistent conversation history stored in MongoDB.

## Overview

This project is designed for fast, practical chat workflows where users can:

- select from configured LLM models,
- exchange multi-turn messages in a clean UI,
- preserve and retrieve conversation history,
- keep configuration environment-driven for local or hosted use.

## Core Features

- Chat interface built with Streamlit
- Groq model integration through LlamaIndex
- MongoDB-backed conversation persistence
- Automatic conversation title generation
- Centralized settings via environment variables

## Technology Stack

- Python 3.10+
- Streamlit
- LlamaIndex
- Groq API
- PyMongo
- Pydantic + pydantic-settings
- python-dotenv

## Project Structure

- `main.py`: Application entrypoint and UI flow
- `config/`: Environment configuration and settings management
- `db/`: MongoDB connection and conversation data operations
- `services/`: Chat helpers, model listing, and title generation
- `llm_factory/`: LLM initialization and provider wiring

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Jaisheesh-2006/ConvoPro.git
cd ConvoPro
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file based on your template and provide values for:

- `GROQ_API_KEY`
- `MONGO_DB_URL`
- `MONGO_DB_NAME`
- `GROQ_MODELS`

### 5. Run the application

```bash
streamlit run main.py
```

## Configuration Notes

- Ensure MongoDB is reachable before launching the app.
- Ensure `GROQ_MODELS` contains valid model names available to your Groq account.
- Keep secrets in `.env` and never commit them to source control.

## Intended Use

ConvoPro is suitable for local development, rapid prototyping, and internal conversational workflows where quick setup and persistent chat history are important.
