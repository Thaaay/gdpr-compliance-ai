import logging
from langchain_ollama import OllamaLLM

# Configuração de Log
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("GDPR-Scanner")

class GDPRScanner:
    def __init__(self):
        logger.info("Iniciando o modelo Llama 3 local...")
        # Certifique-se de que o Ollama está rodando com 'llama3'
        self.llm = OllamaLLM(model="llama3")

    def analyze_text(self, text):
        logger.info("Enviando texto para análise da IA...")
        prompt = f"""
        Analyze the following text for GDPR compliance. 
        Identify data types, retention periods, and potential risks:
        
        {text}
        """
        try:
            return self.llm.invoke(prompt)
        except Exception as e:
            logger.error(f"Erro na comunicação com o Ollama: {e}")
            return "Erro ao processar a análise. Verifique se o Ollama está ativo."