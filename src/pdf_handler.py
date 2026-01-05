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