# rag/retriever.py
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
import os

def get_retriever():
    # Load
    loader = TextLoader("knowledge_base/user_manual.txt")
    docs = loader.load()

    # Split
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    # Embed + Store
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = Chroma.from_documents(
        chunks, embeddings, collection_name="aamantran", persist_directory="./chroma_db"
    )
    return vectorstore.as_retriever(search_kwargs={"k": 4})