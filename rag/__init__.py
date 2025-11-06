# rag/__init__.py
"""
Aamantran RAG module.
Contains the retriever (vector store) and the full RAG chain.
"""

# Optional: expose the public API at package level
from .retriever import get_retriever   # noqa: F401
from .chain import answer             # noqa: F401

__all__ = ["get_retriever", "answer"]