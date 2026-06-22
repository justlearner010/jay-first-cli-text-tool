
from first_cli.word_freq import word_freq_cnt



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


def test_word_freq_empty_file(tmp_path):
    test_file = tmp_path / "empty.txt"

    test_file.write_text("")

    result = word_freq_cnt(test_file,10)

    assert result == []
