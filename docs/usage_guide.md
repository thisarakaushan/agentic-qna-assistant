# Usage Guide — Document Q&A Assistant

This guide explains how to use the Document Q&A Assistant after launching the application.

---

## Starting the Application

After completing the setup in `README.md`, launch the app with:

```bash
python src/ui/gradio_app.py
or
python -m src.ui.gradio_app

Then open your browser and go to:
http://127.0.0.1:7860

```

---

## Uploading Documents

- Use the **“Upload Document”** field to select one or more `.txt` files.
- All uploaded files will be processed and **merged into the assistant's knowledge base**.

Example files:
- `sample_document1.txt` — about machine learning roles  
- `sample_document2.txt` — about Python fundamentals

**Only `.txt` format is supported.** Ensure your files are UTF-8 encoded.

---

## Asking Questions

1. Enter a natural language question in the input box.
2. Click the **“Ask”** button.
3. The assistant will:
   - Retrieve relevant document chunks
   - Generate an answer using the `flan-t5-base` model
   - Display the answer in the output box
   - Append the interaction to chat history

Example questions:
- “What tools are used in MLOps?”
- “What is a for loop in Python?”
- “List the responsibilities of an ML engineer.”

---

## Resetting the Chat

- Click **“Reset Chat”** to clear all chat history.
- This does **not** remove uploaded documents — it only resets memory.
- Use this when:
  - Starting a new topic
  - Testing new queries without previous context

---

## Chat Memory

- The assistant remembers previous questions and responses.
- You can ask **follow-up questions** for better contextual answers.

🗣️ Example:
- “What are the responsibilities?” → “And what tools are needed?”

Resetting chat **clears** this memory context.

---

## Best Practices

- Keep questions short and focused.
- Upload well-structured `.txt` documents.
- Use **Reset Chat** if switching to unrelated topics.
- Uploaded documents persist during the session.

---

## Notes

- Only `.txt` files are supported (PDF/DOCX not yet available).
- Documents remain active until:
  - You close the session  
  - Or restart the app
- Embeddings are stored in `data/embeddings/` using FAISS, and reused across sessions.

---
