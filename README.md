# Document Q&A Assistant

An agentic RAG-based assistant that allows users to upload documents and ask contextual questions via a conversational UI. Built using **LangChain**, **FAISS**, **Hugging Face Transformers**, and **Gradio**.

---

## Overview

This assistant extracts knowledge from uploaded `.txt` documents and uses a **Retrieval-Augmented Generation (RAG)** pipeline to answer questions.

Features:
- Multi-document upload  
- Conversational memory  
- FAISS-based semantic retrieval  
- Real-time Q&A with `flan-t5-base`  
- Clear chat history/reset support

---

## Setup Instructions

### Prerequisites

- Python 3.8+
- Git
- (Optional) CUDA-compatible GPU for faster model execution

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/thisarakaushan/agentic-qna-assistant
cd agentic-qna-assistant

# 2. Create a virtual environment
python -m venv venv

# 3. Activate the environment
venv\Scripts\activate           # Windows
# source venv/bin/activate      # macOS/Linux

# 4. Install all required packages
pip install -r requirements.txt

# 5. Launch the Gradio app
python src/ui/gradio_app.py

# Once started, the app will be available at:
http://127.0.0.1:7860 

```

---

## Project Structure

```
agentic-qna-assistant/
├── data/                     # Saved FAISS vector index and sample_documents
├── src/
│   ├── agent/
│   │   ├── document_processor.py    # Handles embedding documents
│   │   └── rag_agent.py             # Manages RAG pipeline and memory
│   └── ui/
│       └── gradio_app.py            # Gradio interface
├── requirements.txt

```

---

## How It Works

1. Upload one or more `.txt` files.
2. The assistant:
   - Splits the text into chunks
   - Embeds them using `sentence-transformers/all-MiniLM-L6-v2`
   - Stores embeddings using FAISS in `data/embeddings`
3. When a question is asked:
   - FAISS retrieves relevant chunks
   - `flan-t5-base` generates the answer
   - LangChain memory maintains conversational history

---

## 📘 Example Use Cases

- Analyze job role descriptions (e.g., ML Engineer)
- Ask questions from Python tutorials or lecture notes
- Explore content in technical guidelines or manuals

---

## Sample Questions

With example files:

- `sample_document1.txt` — about machine learning engineers  
- `sample_document2.txt` — about Python programming

Try questions like:
- “What tools are used in MLOps?”
- “What are the responsibilities of an ML engineer?”
- “What is a for loop in Python?”
- “List Python data structures.”

---

## Tech Stack

| Tool         | Purpose                           |
|--------------|-----------------------------------|
| LangChain    | RAG orchestration and memory      |
| FAISS        | Vector similarity search engine   |
| HuggingFace  | Embeddings + `flan-t5-base` model |
| Gradio       | Web UI frontend                   |

---

## Evaluation Checklist

- Well-structured, modular code  
- Clear setup instructions  
- Multi-document upload & chat memory  
- End-user ready Gradio UI  
- Usage guide provided
