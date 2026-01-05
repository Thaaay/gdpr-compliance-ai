import logging
from langchain_ollama import OllamaLLM

# Log Configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("GDPR-Scanner")

class GDPRScanner:
    def __init__(self):
        logger.info("Initializing Local Llama 3 model...")
        self.llm = OllamaLLM(model="llama3")

    def analyze_text(self, text):
        logger.info("Sending text for AI analysis...")
        prompt = f"""
        [Role: Senior Data Protection Officer]
        Analyze the following text for GDPR compliance.
        Identify data types, retention periods, and potential risks.
        Provide a professional audit report.

        Text:
        {text}
        """
        try:
            return self.llm.invoke(prompt)
        except Exception as e:
            logger.error(f"Error communicating with Ollama: {e}")
            return "Error processing the analysis. Please ensure Ollama is running locally."