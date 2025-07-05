def save_embeddings(vector_store):
    """Save embeddings to disk."""
    vector_store.save_local("data/embeddings")