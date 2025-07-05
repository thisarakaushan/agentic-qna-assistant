from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from langchain_community.llms import HuggingFacePipeline
import torch
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
import os


# Memory to hold chat history for contextual Q&A with explicit output key
memory = ConversationBufferMemory(memory_key="chat_history", output_key="answer", return_messages=True)

def initialize_agent():
    """Initialize the RAG agent with LLM and vector store."""

    # Load the same embeddings used for document vectorization 
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    try:
        vector_store = FAISS.load_local("data/embeddings", embeddings, allow_dangerous_deserialization=True)
    except Exception as e:
        raise RuntimeError(f"Failed to load vector store: {e}. Please upload a document first.")


    # Load a question-answering tuned model(text2text)
    model_id = "google/flan-t5-base"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
    pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer, device=0 if torch.cuda.is_available() else -1)
    
    llm = HuggingFacePipeline(pipeline=pipe)

    # Combine retriever, LLM, and memory into ConversationalRetrievalChain
    rag_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(),
        memory=memory,
        return_source_documents=True
    )
    return rag_chain

def get_response(query, rag_chain):
    """Get response with fallback if no context is found."""

    # Invoke the chain to answer the question
    result = rag_chain.invoke({"question": query})
    response = result["answer"]

    # If no relevant docs used, return fallback
    if not result["source_documents"]:
        response = "No relevant context found. Please rephrase your question or upload a different document."
    return response