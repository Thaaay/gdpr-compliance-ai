import fitz
import logging

logger = logging.getLogger("PDF-Handler")

class PDFProcessor:
    def extract_text(self, pdf_path: str) -> str:
        """Extracts text from a PDF file."""
        try:
            doc = fitz.open(pdf_path)
            text = "".join([page.get_text() for page in doc])
            doc.close()
            return text
        except Exception as e:
            logger.error(f"Error reading PDF: {e}")
            raise

    def create_report_pdf(self, report_text: str, output_path: str):
        """Generates a PDF using a more robust text insertion method."""
        try:
            doc = fitz.open()
            page = doc.new_page()

            page.insert_text((50, 50), "GDPR COMPLIANCE AUDIT REPORT", fontsize=16, color=(0, 0, 0.5))
            html_content = f"<div style='font-family:sans-serif;font-size:11px;'>{report_text.replace('\n', '<br>')}</div>"
            rect = fitz.Rect(50, 80, 550, 800)
            page.insert_htmlbox(rect, html_content)

            doc.save(output_path)
            doc.close()
            logger.info("PDF Report generated successfully.")
        except Exception as e:
            logger.error(f"PDF Creation Error: {e}")
            raise

class GDPRScanner:
    def __init__(self):
        self.llm = OllamaLLM(model="llama3")

    def analyze_with_rag(self, vector_db):
        """Busca o contexto no FAISS e analisa."""
        # Buscamos os trechos que falam de dados, retenção e riscos
        query = "What are the data types, retention periods, and security risks in this policy?"
        docs = vector_db.similarity_search(query, k=4) # Pega os 4 trechos mais relevantes

        context = "\n".join([d.page_content for d in docs])

        prompt = f"""
        [Role: Senior DPO]
        Using ONLY the context below, analyze the GDPR compliance:

        Context:
        {context}

        Report:
        """
        return self.llm.invoke(prompt)