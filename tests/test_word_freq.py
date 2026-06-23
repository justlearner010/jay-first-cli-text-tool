
import pytest

from first_cli.word_freq import count_words, word_freq_cnt



def test_word_freq_basic(tmp_path):
    test_file = tmp_path / "test.txt"

    test_file.write_text(
        "apple banana apple\nbanana orange apple"
    )

    result = word_freq_cnt(test_file,10)

    assert result == [
        ("apple", 3),
        ("banana", 2),
        ("orange", 1)
    ]


def test_word_freq_ignore_case(tmp_path):
    test_file = tmp_path / "test.txt"

    test_file.write_text(
        "Apple apple APPLE Banana"
    )

    result = word_freq_cnt(test_file,10)

    assert result == [
        ("apple", 3),
        ("banana", 1)
    ]


def test_word_freq_top_n(tmp_path):
    test_file = tmp_path / "test.txt"

    test_file.write_text(
        "a a a b b c"
    )

    result = word_freq_cnt(test_file,2)

    assert result == [
        ("a", 3),
        ("b", 2)
    ]


def test_word_freq_rejects_negative_top(tmp_path):
    test_file = tmp_path / "test.txt"

    test_file.write_text(
        "a a a b b c"
    )

    with pytest.raises(ValueError, match="Top value is invalid"):
        word_freq_cnt(test_file, -1)


def test_word_freq_top_larger_than_unique_words(tmp_path):
    test_file = tmp_path / "test.txt"

    test_file.write_text(
        "a a b"
    )

    result = word_freq_cnt(test_file, 10)

    assert result == [
        ("a", 2),
        ("b", 1)
    ]


@pytest.mark.parametrize(
    "target_word",
    [
        "apple",
        " Apple ",
        "APPLE",
    ],
)
def test_count_words_strips_space_and_ignores_case(target_word):
    text = "Apple apple APPLE banana"

    result = count_words(text, target_word)

    assert result == 3


def test_word_freq_empty_file(tmp_path):
    test_file = tmp_path / "empty.txt"

    test_file.write_text("")

    result = word_freq_cnt(test_file,10)

    assert result == []
