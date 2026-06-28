
import pytest

from first_cli.word_chunk import Wordchunk, chunk_text


def test_chunk_text_basic():
    result = chunk_text("abcdef", chunk_size=2)

    assert result == [
        {
            "chunk index": 1,
            "chunk_start": 0,
            "chunk_end": 2,
            "chunk_text": "ab",
        },
        {
            "chunk index": 2,
            "chunk_start": 2,
            "chunk_end": 4,
            "chunk_text": "cd",
        },
        {
            "chunk index": 3,
            "chunk_start": 4,
            "chunk_end": 6,
            "chunk_text": "ef",
        },
    ]


def test_wordchunk_wrapper_uses_text():
    chunker = Wordchunk("abcdef", chunk_size=2)

    result = chunker.text_chunk()

    assert result == [
        {
            "chunk index": 1,
            "chunk_start": 0,
            "chunk_end": 2,
            "chunk_text": "ab",
        },
        {
            "chunk index": 2,
            "chunk_start": 2,
            "chunk_end": 4,
            "chunk_text": "cd",
        },
        {
            "chunk index": 3,
            "chunk_start": 4,
            "chunk_end": 6,
            "chunk_text": "ef",
        },
    ]


def test_chunk_text_rejects_invalid_chunk_size():
    with pytest.raises(ValueError, match="Chunk size is invalid"):
        chunk_text("abcdef", chunk_size=0)
