import os
import sys

# Esse comando força o Python a olhar para a pasta atual
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from src.pdf_handler import PDFProcessor
from src.analyzer import GDPRScanner

# Configuração da Página
st.set_page_config(page_title="EU GDPR AI Analyzer", page_icon="🇪🇺")

st.title("🇪🇺 GDPR Compliance AI Agent")
st.markdown("Arraste sua Política de Privacidade para uma análise instantânea via Llama 3.")

# Inicializa as classes
processor = PDFProcessor()
scanner = GDPRScanner()

# Componente de Upload
uploaded_file = st.file_uploader("Escolha um arquivo PDF", type="pdf")

if uploaded_file is not None:
    # Salva temporariamente o arquivo na pasta data/
    temp_path = os.path.join("data", "temp_upload.pdf")
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("Lendo PDF e consultando IA local..."):
        # Pipeline que você já criou
        text = processor.extract_text(temp_path)
        report = scanner.analyze_text(text[:4000]) # Limitamos para ser mais rápido

        st.subheader("Relatório de Conformidade")
        st.info(report)

    # Limpa o arquivo temporário
    os.remove(temp_path)