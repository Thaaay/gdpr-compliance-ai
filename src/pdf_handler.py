import fitz  # PyMuPDF
import logging

logger = logging.getLogger("PDF-Handler")

class PDFProcessor:
    def extract_text(self, pdf_path: str) -> str:
        """Extrai todo o texto de um arquivo PDF."""
        logger.info(f"Extracting text from: {pdf_path}")
        try:
            doc = fitz.open(pdf_path)
            text = ""
            for page in doc:
                text += page.get_text()

            if not text:
                logger.warning("No text found in PDF. It might be an image/scan.")

            return text
        except Exception as e:
            logger.error(f"Failed to read PDF: {str(e)}")
            raise

def create_report_pdf(self, report_text: str, output_path: str):
        """Generates a professional PDF report."""
        doc = fitz.open()
        page = doc.new_page()
        where = fitz.Point(50, 50)

        page.insert_text(where, "GDPR COMPLIANCE AUDIT REPORT", fontsize=18, color=(0, 0, 0.5))

        page.insert_textbox(fitz.Rect(50, 80, 550, 800), report_text, fontsize=11)
        doc.save(output_path)
        doc.close()