@echo off
echo Starting Ollama...
start "" "ollama" serve

timeout /t 5

echo Starting Chatbot UI...
streamlit run ui/app.py --server.port=8501