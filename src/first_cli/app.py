
import logging
import sys
from pathlib import Path

from .cli import parse_args
from .summarize import summarize_text
from .word_freq import word_freq_cnt
from .word_chunk import Wordchunk
from .create_json import create_json
from .text_status import TextStats


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s:%(name)s:%(message)s"
    )
    logger = logging.getLogger(__name__)


    args = parse_args()


    # 传入文件名、词块大小
    fname = args.filename
    chunk_size = args.chunk_size

    logger.info("Program started. input_file=%s chunk_size=%s", fname, chunk_size)

    try:
        with open(fname) as f:
            text = f.read()
    except FileNotFoundError:
        logger.error("Input file does not exist. input_file=%s", fname)
        sys.exit("File does not exist")

    if not text.strip():
        logger.error("Input file is empty. input_file=%s", fname)
        sys.exit("Input file is empty")

    logger.info("Input file loaded. input_length=%s", len(text))

    if(chunk_size <= 0):
        logger.error("Chunk size is invalid. chunk_size=%s", chunk_size)
        sys.exit("Chunk size is invalid")

    stats = TextStats(fname)



    chunk1 = Wordchunk(fname,chunk_size)

    chunks = chunk1.text_chunk()


    lines = stats.line_check()
    words = stats.word_check()
    space = stats.space_check()
    digit = stats.digit_check()

    output_file = (
    Path("output")
    / f"{Path(fname).stem}.json"
    )



    if args.summary:
        summ = summarize_text(text, mode="brief")
        print(summ)
        logging.info(summ)
    if args.freq:
        freq_result = word_freq_cnt(fname)
        print("Top 10 words in this text!")
        print(freq_result)#打印词频最高的十个单词

    if args.status:
        print(f"行数为{lines}行")#打印行
        print(f"单词数为{words}个单词")#打印单词数
        print(f"数字的个数为{digit}")#打印数字数
        print(f"空格数为{space}")#打印空格数
    if args.createjson:
        json_result = {
            "summary": summarize_text(text, mode="brief"),
            "mode": "brief",
            "input_chars": len(text),
        }
        create_json(json_result, output_file)#输出json文件
        logger.info("JSON output created. output_path=%s", output_file)
        print("Successfully create the json")

    logger.info("Program finished.")
    print("运行完毕")
if __name__ == "__main__":
    main()
