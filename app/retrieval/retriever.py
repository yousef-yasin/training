from retrieval.vector_store import get_chroma_collection, model #to import the get_chroma_collection function and the model object from the vector_store module

MAX_DISTANCE = 1.2


def retrieve_relevant_chunks(question: str, top_k: int = 3):

    collection = get_chroma_collection()

    question_embedding = model.encode([question]).tolist()[0]

    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=top_k,
        include=["documents", "metadatas", "distances"]
    )

    retrieved_chunks = []

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0] #to retrieve the distances between the question embedding and the embeddings of the retrieved chunks. 


    for document, metadata, distance in zip(documents, metadatas, distances):

        if distance <= MAX_DISTANCE:# to check if the distance is less than or equal to the maximum distance threshold. 
            retrieved_chunks.append({
                "content": document,
                "file_name": metadata["file_name"],
                "chunk_index": metadata["chunk_index"],
                "distance": distance
            })

    return retrieved_chunks