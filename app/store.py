from ingestion.reader import load_documents #to import the load_documents function from the reader module in the ingestion package, 
from ingestion.chunker import split_text #to import the load_documents function from the reader module in the ingestion package, 
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