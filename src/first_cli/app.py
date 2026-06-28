import logging
from pathlib import Path

from .args_function import load_input_text, validate_args
from .cli import parse_args
from .create_json import create_json
from .summarize import summarize_text
from .text_status import TextStats
from .word_freq import count_words, word_freq_cnt


def main():
    args = parse_args()

    try:
        return run(args)
    except (FileNotFoundError, PermissionError, UnicodeDecodeError, ValueError) as exc:
        raise SystemExit(str(exc)) from exc


def run(args):
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s:%(name)s:%(message)s",
    )
    logger = logging.getLogger(__name__)

    validate_args(args)

    filename = args.filename
    text = load_input_text(filename)

    logger.info(
        "Program started. input_file=%s chunk_size=%s",
        filename,
        args.chunk_size,
    )
    logger.info("Input file loaded. input_length=%s", len(text))

    if args.summary:
        handle_summary(text)

    if args.freq:
        handle_freq(text, args.top)

    if args.status:
        handle_status(text)

    if args.createjson:
        handle_createjson(filename, text)

    if args.word:
        handle_word(text, args.word)

    logger.info("Program finished.")
   
    return 0

def build_summary(text):
    return summarize_text(text, mode="brief")


def handle_summary(text):
    print(build_summary(text))


def build_freq(text, top):
    freq_result = word_freq_cnt(text, top)

    return freq_result


def handle_freq(text, top):
    print("Top 10 words in this text!")
    print(build_freq(text, top))


def build_status(text):
    stats = TextStats(text)
    lines = stats.line_check()
    words = stats.word_check()
    space = stats.space_check()
    digit = stats.digit_check()
    stats_result = {
        "lines": lines,
        "words": words,
        "space": space,
        "digit": digit,
    }
    return stats_result


def handle_status(text):
    stats = build_status(text)

    print(f"行数为{stats['lines']}行")
    print(f"单词数为{stats['words']}个单词")
    print(f"数字的个数为{stats['digit']}")
    print(f"空格数为{stats['space']}")


def handle_createjson(filename, text):
    output_file = Path("output") / f"{Path(filename).stem}.json"
    json_result = {
        "summary": summarize_text(text, mode="brief"),
        "mode": "brief",
        "input_chars": len(text),
    }

    create_json(json_result, output_file)
    print("Successfully create the json")


def build_word(text, word):
    target_word = word.strip().lower()
    count = count_words(text, target_word)

    return target_word, count


def handle_word(text, word):
    target_word, count = build_word(text, word)

    print(f"{target_word}: {count}")


if __name__ == "__main__":
    raise SystemExit(main())
