import pytest
from first_cli.text_status import TextStats

@pytest.fixture
def sample_file(tmp_path):
    file = tmp_path /"test.txt"
    file.write_text(
        "hello world\n"
        "python 123\n"
        "456"
    )

    return file

@pytest.fixture
def stats(sample_file):
    return TextStats(sample_file)


def test_line_check(stats):
    assert stats.line_check() == 3


def test_word_check(stats):
    assert stats.word_check() == 5


def test_digit_check(stats):
    assert stats.digit_check() == 6


def test_space_check(stats):
    assert stats.space_check() == 4


@pytest.fixture
def empty_file(tmp_path):
    file = tmp_path / "empty.txt"

    file.write_text("")

    return file


@pytest.fixture
def empty_stats(empty_file):
    return TextStats(empty_file)

def test_empty_line_check(empty_stats):
    assert empty_stats.line_check() == 0

def test_empty_word_check(empty_stats):
    assert empty_stats.word_check() == 0

def test_empty_space_check(empty_stats):
    assert empty_stats.space_check() == 0

def test_empty_digit_check(empty_stats):
    assert empty_stats.digit_check() == 0

def test_file_not_found():
    stats = TextStats("not_exist.txt")

    with pytest.raises(FileNotFoundError):
        stats.word_check()

# 9 passed
