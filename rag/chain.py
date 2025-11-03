# rag/chain.py
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from .retriever import get_retriever

retriever = get_retriever()
llm = ChatOllama(model="llama3.2:latest", temperature=0.3)

template = """
You are Aamantran Assistant, an expert on the Aamantran Portal (Ministry of Defence).
Answer in clear, polite English or Hindi (match user language).
Use ONLY the context below. If unsure, say: "I don't have that information."

Context:
{context}

Question: {question}

Answer:
"""

prompt = ChatPromptTemplate.from_template(template)

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

def answer(query: str) -> str:
    return chain.invoke(query)