from typing import List #to import the List type from the typing module, which is used for type hinting in Python. 


#the second step to make chunk


def split_text(text: str, chunk_size: int = 700, chunk_overlap: int = 150) -> List[str]:
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]

    chunks = []
    current_chunk = ""

    for paragraph in paragraphs: #to make sure that the current chunk does not exceed the specified chunk size. If adding the current paragraph would exceed the chunk size, the current chunk is added to the list of chunks, and a new chunk is started with the overlap text and the current paragraph.
        if len(current_chunk) + len(paragraph) <= chunk_size:
            current_chunk += paragraph + "\n\n"
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())

            overlap_text = current_chunk[-chunk_overlap:] if current_chunk else ""
            current_chunk = overlap_text + paragraph + "\n\n"

    if current_chunk: #it checks if there is any remaining text in the current chunk after processing all paragraphs.
        chunks.append(current_chunk.strip())

    return chunks