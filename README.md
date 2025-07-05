# Document Q&A Assistant

## 📄 Overview
This agentic application uses Retrieval-Augmented Generation (RAG) to answer questions from uploaded documents via a Gradio-based interface. It supports:
- **Multi-document upload**
- **Conversational memory**
- **Automatic query box reset**
- **Clear chat functionality**

It’s ideal for querying job descriptions, research papers, or any domain-specific text with follow-up capabilities.

---

## ✅ Prerequisites

- Python 3.8 or higher (tested on Windows)
- Git (to clone the repository)
- (Optional) CUDA-compatible GPU for faster model inference

---

## 🛠 Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/thisarakaushan/agentic-qna-assistant
cd agentic-qna-assistant

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate      # On Windows
# Or use: source venv/bin/activate  # On Linux/Mac

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the Gradio interface
python src/ui/gradio_app.py
