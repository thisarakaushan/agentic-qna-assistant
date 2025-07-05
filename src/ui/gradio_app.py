import gradio as gr
from src.agent.document_processor import process_documents
from src.agent.rag_agent import initialize_agent, get_response

rag_chain = None  # Cache RAG chain after first upload


def process_query(files, query):
    """Process user query with document and return response."""

    global rag_chain

    if files:
        file_paths = [file.name for file in files]

        # 1. Process all uploaded documents
        process_documents(file_paths)

        try:
            rag_chain = initialize_agent()
        except RuntimeError as e:
            return str(e), ""

    if not rag_chain:
        return "Please upload a document first.", ""

    # 2. Get the response using the RAG agent
    response = get_response(query, rag_chain)

    # Return response and clear query
    return response, ""  
    
# Function to display chat history
def update_chat_history(query, response):
    """Update and return the chat history based on the latest interaction."""

    # Retrieve current chat history from memory
    if rag_chain and hasattr(rag_chain.memory, 'chat_memory'):
        messages = rag_chain.memory.chat_memory.messages

        history_lines = []
        for i in range(0, len(messages), 2):  # Step in pairs (Human, AI)
            human_msg = messages[i].content if i < len(messages) else ""
            ai_msg = messages[i+1].content if i+1 < len(messages) else ""
            history_lines.append(f"You: {human_msg}\nBot: {ai_msg}")

        return "\n\n".join(history_lines)
    
    return "No chat history available."

# Function to reset chat memory and UI components
def reset_chat():
    """Reset the chat memory and UI components."""
    if rag_chain and hasattr(rag_chain, "memory"):
        rag_chain.memory.clear()
    return "", "", ""  # clear response_output, query_input, chat_display


# Gradio UI
with gr.Blocks(title="Document Q&A Assistant with Memory") as interface:
    gr.Markdown("## Document Q&A Assistant with Memory")

    with gr.Row():
        doc_input = gr.File(label="Upload Documents", file_types=[".txt"], file_count="multiple")

    with gr.Row():
        query_input = gr.Textbox(label="Ask a Question", lines=2)
        ask_button = gr.Button("Ask")
        reset_button = gr.Button("Reset Chat", variant="stop")  # ✨ New button

    response_output = gr.Textbox(label="Response", lines=4)
    chat_display = gr.Textbox(label="Chat History", lines=10, interactive=False)

    # Ask button flow
    ask_button.click(
        fn=process_query,
        inputs=[doc_input, query_input],
        outputs=[response_output, query_input]
    ).then(
        fn=update_chat_history,
        inputs=[query_input, response_output],
        outputs=chat_display
    )

    # Reset button flow
    reset_button.click(
        fn=reset_chat,
        inputs=[],
        outputs=[response_output, query_input, chat_display]
    )

# Launch the Gradio interface
interface.launch()