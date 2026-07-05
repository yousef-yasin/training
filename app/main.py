from retrieval.retriever import retrieve_relevant_chunks
from llm.gemini import generate_answer


def main():

    question = input("Ask your question: ")

    retrieved_chunks = retrieve_relevant_chunks(question)

    if not retrieved_chunks:
        print("\nThe information is not available in the Knowledge Base.")
        return

    print(f"\nRetrieved {len(retrieved_chunks)} relevant chunks.\n")

    answer = generate_answer(question, retrieved_chunks)

    print("=" * 60)
    print("Answer:")
    print("=" * 60)
    print(answer)


if __name__ == "__main__":
    main()