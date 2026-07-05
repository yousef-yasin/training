from pathlib import Path
import chromadb
from sentence_transformers import SentenceTransformer


CHROMA_DB_DIR = Path("chroma_db")
COLLECTION_NAME = "knowledge_base"
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"


model = SentenceTransformer(EMBEDDING_MODEL_NAME)


def get_chroma_collection():
    client = chromadb.PersistentClient(path=str(CHROMA_DB_DIR))

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )

    return collection


def store_chunks(chunks_with_metadata):
    collection = get_chroma_collection()

    documents = []
    metadatas = []
    ids = []

    for index, item in enumerate(chunks_with_metadata):
        documents.append(item["content"])
        metadatas.append({
            "file_name": item["file_name"],
            "chunk_index": item["chunk_index"]
        })
        ids.append(f"{item['file_name']}_{item['chunk_index']}")

    embeddings = model.encode(documents).tolist()

    collection.upsert(
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids
    )

    print(f"Stored {len(documents)} chunks in ChromaDB")