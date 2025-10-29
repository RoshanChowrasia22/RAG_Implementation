from src.data_loader import load_all_documents
from src.embedding import EmbeddingPipeline
from src.vectorstore import FaissVectorStore
# from src.search import RAGSearch

# Example usage
if __name__ == "__main__":
    
    # docs = load_all_documents("data")
    # print(docs[:1])
    # embed=EmbeddingPipeline()
    # chunks=embed.chunk_documents(docs)
    # embeddings=embed.embed_chunks(chunks=chunks)
    # print("[INFO] Example embedding:", embeddings[0] if len(embeddings) > 0 else None)
    store = FaissVectorStore("faiss_store")
    # store.build_from_documents(docs)
    store.load()
    print(store.query("What is attention mechanism?", top_k=3))
    # rag_search = RAGSearch()
    # query = "What is attention mechanism?"
    # summary = rag_search.search_and_summarize(query, top_k=3)
    # print("Summary:", summary)
