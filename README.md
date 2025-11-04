Aamantran Portal RAG Assistant
Your Local AI Guide for Republic Day & Independence Day Ticket Booking
https://img.shields.io/badge/Python-3.10%2B-blue
https://img.shields.io/badge/License-MIT-green
https://img.shields.io/badge/Runs-Locally-orange

Project Overview
Feature  Description
Portal,Aamantran Portal – Official ticketing for Republic Day & Independence Day
Purpose,"Help citizens book tickets, understand policies, download e-tickets"
AI Model,llama3.2:latest via Ollama (runs on your laptop)
RAG,Answers from official Citizen User Manual only
UI,"Modern, responsive Streamlit interface"
Privacy,100% offline – no data leaves your machine

Tech Stack
Layer,Technology
LLM,llama3.2:latest (Ollama)
Embeddings,nomic-embed-text
RAG Framework,LangChain
Vector DB,Chroma (local)
UI,Streamlit + Custom CSS
Language,Python 3.10+
PDF Parser,pypdf

chatbot/
│
├── knowledge_base/                 # Extracted manual
│   ├── user_manual.txt             # Full text from PDF
│   └── summary.txt                 # Key points
│
├── rag/                            # RAG Logic
│   ├── __init__.py
│   ├── retriever.py                # Vector store + embeddings
│   └── chain.py                    # Prompt + LLM + RAG chain
│
├── ui/                             # Frontend
│   ├── app.py                      # Streamlit UI
│   └── assets/
│       ├── logo.png                # Aamantran logo
│       └── style.css               # Custom styling
│
├── data/                           # Raw files
│   └── CitizenUserManual.pdf       # Official manual
│
├── .vscode/                        # VS Code config
│   └── settings.json
│
├── extract_pdf.py                  # Convert PDF → TXT
├── requirements.txt
├── run.bat                         # Windows launcher
├── run.sh                          # Mac/Linux launcher
└── README.md                       # This file



































LayerTechnologyLLMllama3.2:latest (Ollama)Embeddingsnomic-embed-textRAG FrameworkLangChainVector DBChroma (local)UIStreamlit + Custom CSSLanguagePython 3.10+PDF Parserpypdf
