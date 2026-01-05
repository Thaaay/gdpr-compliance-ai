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