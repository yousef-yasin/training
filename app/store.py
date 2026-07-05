from ingestion.reader import load_documents
from ingestion.chunker import split_text
from retrieval.vector_store import store_chunks


def main():

    documents = load_documents()

    all_chunks = []

    for document in documents:

        chunks = split_text(document["content"])

        for index, chunk in enumerate(chunks):

            all_chunks.append({
                "content": chunk,
                "file_name": document["file_name"],
                "chunk_index": index
            })

    store_chunks(all_chunks)


if __name__ == "__main__":
    main()