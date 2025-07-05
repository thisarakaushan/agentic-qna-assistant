from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def process_documents(file_paths):
    """Process multiple document into embeddings and store in FAISS.
        Also return the combined vector store."""
    
    all_chunks = []

    # 1. Load and split each document
    for path in file_paths:
        loader = TextLoader(path, encoding="utf-8")
        documents = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
        )
        chunks = text_splitter.split_documents(documents)
        all_chunks.extend(chunks)

    # 2. Convert all text chunks into embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # 3. Store in a combined FAISS vector index
    vector_store = FAISS.from_documents(all_chunks, embeddings)

    # 4. Save the merged index
    vector_store.save_local("data/embeddings")

    return vector_store