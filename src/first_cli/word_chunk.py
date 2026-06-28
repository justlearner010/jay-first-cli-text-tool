from dataclasses import dataclass


def chunk_text(text, chunk_size):
    if chunk_size <= 0:
        raise ValueError("Chunk size is invalid")

    chunks = []

    for index, start in enumerate(range(0, len(text), chunk_size), start=1):
        end = min(start + chunk_size, len(text))
        chunks.append(
            {
                "chunk index": index,
                "chunk_start": start,
                "chunk_end": end,
                "chunk_text": text[start:end],
            }
        )

    return chunks


@dataclass
class Wordchunk:
    text: str
    chunk_size: int

    def text_chunk(self):
        return chunk_text(self.text, self.chunk_size)
