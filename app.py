import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from src.pdf_handler import PDFProcessor
from src.analyzer import GDPRScanner

# Page Config
st.set_page_config(page_title="AI GDPR Analyzer", page_icon="🇪🇺")

st.title("AI-Powered GDPR Agent")
st.markdown("Upload your Privacy Policy for an instant compliance audit powered by Llama 3.")

# Initialize classes
processor = PDFProcessor()
scanner = GDPRScanner()

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    if not os.path.exists("data"):
        os.makedirs("data")

    temp_path = os.path.join("data", "temp_upload.pdf")
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("Processing PDF and consulting Local AI..."):
        text = processor.extract_text(temp_path)
        report = scanner.analyze_text(text[:4000])

        st.subheader("Compliance Analysis Report")
        st.info(report)

        report_filename = "gdpr_analysis_report.pdf"
        processor.create_report_pdf(report, report_filename)

        with open(report_filename, "rb") as pdf_file:
            st.download_button(
                label="📥 Download PDF Report",
                data=pdf_file,
                file_name="GDPR_Compliance_Report.pdf",
                mime="application/pdf"
            )

    if os.path.exists(temp_path):
        os.remove(temp_path)