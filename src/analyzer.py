import logging
from langchain_ollama import OllamaLLM

logger = logging.getLogger("GDPR-Scanner")

class GDPRScanner:
    def __init__(self):
        logger.info("Initializing Local Llama 3 model...")
        self.llm = OllamaLLM(model="llama3")

    # Mantenha a função antiga se quiser, mas adicione esta NOVA:
    def analyze_with_rag(self, vector_db):
        """Searches context in FAISS and analyzes it via RAG."""
        logger.info("Performing RAG analysis with FAISS context...")
        
        # Query para buscar os trechos mais importantes
        query = "Identify data types, retention periods, and potential GDPR risks."
        
        # Busca os 4 blocos de texto mais relevantes no PDF
        docs = vector_db.similarity_search(query, k=4)
        context = "\n".join([d.page_content for d in docs])
        
        prompt = f"""
        [Role: Senior Data Protection Officer]
        Using the provided context from the privacy policy, generate a GDPR compliance report.
        
        Context:
        {context}
        
        Audit Report:
        """
        try:
            return self.llm.invoke(prompt)
        except Exception as e:
            logger.error(f"RAG Analysis Error: {e}")
            return "Error during RAG processing."