# Aamantran Portal RAG Assistant  
### *Your Local AI Guide for Republic Day & Independence Day Ticket Booking*  
![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Ollama](https://img.shields.io/badge/Ollama-Llama3.2-orange) ![LangChain](https://img.shields.io/badge/LangChain-RAG-green) ![Streamlit](https://img.shields.io/badge/UI-Streamlit-red) ![Local](https://img.shields.io/badge/100%25-Local%20AI-lightgrey)

---

> A **beautiful, offline, RAG-powered chatbot** that helps citizens book tickets on the **Aamantran Portal** using **Ollama + Llama 3.2 + LangChain**.

---

## Live Demo  
![Chatbot UI](https://img.shields.io/badge/See%20Live%20Demo-Click%20Run%20Locally-success?style=for-the-badge)  
*100% local • No internet required after setup*

---

## Project Overview

| Feature | Description |
|--------|-------------|
| **Portal** | [Aamantran Portal](https://www.aamantran.mod.gov.in/ticketing) – Official ticketing for **Republic Day & Independence Day** |
| **Purpose** | Help citizens book tickets, add guests, pay, and download e-tickets |
| **AI Model** | `llama3.2:latest` via **Ollama** (runs on your laptop) |
| **RAG Source** | Official **Citizen User Manual (PDF)** |
| **UI** | Modern **Streamlit** with gradient theme & chat bubbles |
| **Privacy** | **Zero cloud** – all data stays on your machine |

---

## Features

- **Natural Language Queries**  
  > *"How do I add a guest using Aadhaar?"*  
  > *"Can I cancel my ticket?"*  
  > *"Where do I download the e-ticket?"*

- **Step-by-Step Guidance**  
  Registration → Guest List → Payment → Download

- **Policy Enforcement**  
  > Tickets are **non-cancellable & non-transferable**

- **Multilingual**  
  Answers in **English & Hindi** (auto-detected)

- **Beautiful UI**  
  Custom CSS, logo, responsive chat

---

## Tech Stack

| Layer | Tool |
|------|------|
| **LLM** | `llama3.2:latest` (Ollama) |
| **Embeddings** | `nomic-embed-text` |
| **RAG** | **LangChain** |
| **Vector DB** | **Chroma** (local) |
| **UI** | **Streamlit** + CSS |
| **PDF Parser** | `pypdf` |

> **No Spring AI** – We use **LangChain** (faster, flexible, production-ready)

---

## Project Structure

```bash
chatbot/
│
├── knowledge_base/                 # Extracted manual
│   ├── user_manual.txt             # From PDF
│   └── summary.txt
│
├── rag/                            # RAG Core
│   ├── __init__.py
│   ├── retriever.py                # Vector DB
│   └── chain.py                    # LLM + Prompt
│
├── ui/                             # Frontend
│   ├── app.py                      # Streamlit UI
│   └── assets/
│       ├── logo.png
│       └── style.css
│
├── data/                           # Source
│   └── CitizenUserManual.pdf
│
├── .vscode/                        # VS Code
│   └── settings.json
│
├── extract_pdf.py                  # PDF → TXT
├── requirements.txt
├── run.bat                         # Windows
├── run.sh                          # Mac/Linux
└── README.md                       # You are here
