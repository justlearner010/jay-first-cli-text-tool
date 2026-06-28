from first_cli.text_status import TextStats

def sample_text():
    return (
        "hello world\n"
        "python 123\n"
        "456"
    )


def stats():
    return TextStats(sample_text())


def test_line_check():
    assert stats().line_check() == 3


def test_word_check():
    assert stats().word_check() == 5


def test_digit_check():
    assert stats().digit_check() == 6


def test_space_check():
    assert stats().space_check() == 4


def empty_stats():
    return TextStats("")


def test_empty_line_check():
    assert empty_stats().line_check() == 0


def test_empty_word_check():
    assert empty_stats().word_check() == 0


def test_empty_space_check():
    assert empty_stats().space_check() == 0


def test_empty_digit_check():
    assert empty_stats().digit_check() == 0
