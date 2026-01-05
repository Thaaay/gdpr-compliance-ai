import logging
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

logger = logging.getLogger("Vector-Store")

class VectorManager:
    def __init__(self):

        self.embeddings = OllamaEmbeddings(model="llama3")
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100
        )

    def create_index(self, text: str):
        """Transforma o texto em pedaços e salva no FAISS."""
        logger.info("Splitting text and creating FAISS index...")
        chunks = self.text_splitter.split_text(text)

        vector_db = FAISS.from_texts(chunks, self.embeddings)
        return vector_db