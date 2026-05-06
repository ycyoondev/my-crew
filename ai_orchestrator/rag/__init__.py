"""
RAG (Retrieval-Augmented Generation) package.

Defines the interfaces for retrieving context from external knowledge bases.
"""
from abc import ABC, abstractmethod
from typing import List, Dict, Any


class Retriever(ABC):
    """Interface for document retrieval systems."""

    @abstractmethod
    def retrieve(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """
        Retrieves relevant documents for a query.

        Args:
            query: The search query.
            top_k: The number of documents to retrieve.

        Returns:
            A list of relevant document snippets or objects.
        """
        pass


class MockRetriever(Retriever):
    """A mock retriever for development."""

    def retrieve(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        return [{"content": "Mock document relevant to: " + query}]
