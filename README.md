# 🇪🇺 GDPR Compliance AI Agent

An automated LegalTech solution for scanning privacy policies and identifying GDPR risks using Local LLMs (Llama 3).

## 🛡️ Why This Project?
In the European Union, data privacy is a priority. This tool demonstrates how to use **Agentic AI** to solve complex compliance problems while maintaining **Data Sovereignty** by running models 100% locally on Linux (Fedora).

## 🚀 Key Features
- **Privacy-First:** No data leaves the local infrastructure (GDPR-friendly).
- **PDF Intelligence:** Extracts and analyzes unstructured legal text from PDFs.
- **Local LLM:** Powered by Ollama and Llama 3 for high-quality legal reasoning.
- **Observability:** Full logging system for audit trails.

## 🛠️ Tech Stack
- **Language:** Python 3.14+
- **Orchestration:** LangChain
- **AI Backend:** Ollama (Llama 3)
- **UI:** Streamlit
- **OS:** Linux (Fedora)

## 📦 How to Run
1. Install [Ollama](https://ollama.com/) and run `ollama pull llama3`.
2. Activate venv: `source venv/bin/activate`.
3. Set path: `export PYTHONPATH=$PYTHONPATH:.`.
4. Launch UI: `streamlit run app.py`.

---
*Developed for a high-compliance European market mindset.*
