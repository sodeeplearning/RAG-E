from langchain_community.document_loaders import UnstructuredFileLoader
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

from rage.rag.utils import *


class RAG:
    """Class build for RAG task."""
    def __init__(self, documents_path: str | list[str], extra_wishes: str = ""):
        """Constructor of RAG class.

        :param documents_path: Path (list of paths) to your knowledge base.
        :param extra_wishes: Wishes for prompts.
        """
        loader = UnstructuredFileLoader(documents_path)
        documents = loader.load()
        text_chunks = text_splitter.split_documents(documents)
        knowledge_base = FAISS.from_documents(text_chunks, embeddings)

        self.qa_chain = RetrievalQA.from_chain_type(
            llm,
            retriever=knowledge_base.as_retriever())

        self.wishes = ". " + extra_wishes

    def ask(self, question: str) -> str:
        """Ask question about database.

        :param question: Question to a model.
        :return: Model's answer.
        """
        return self.qa_chain.invoke({"query": question + self.wishes})["result"]

    def __call__(self, question: str, *args, **kwargs):
        """Ask question about database.

        :param question: Question to a model.
        :return: Model's answer.
        """
        return self.ask(question=question)
