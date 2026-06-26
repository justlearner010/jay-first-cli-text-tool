
import logging
import sys
from pathlib import Path

from .cli import parse_args
from .summarize import summarize_text
from .word_freq import word_freq_cnt
from .create_json import create_json
from .text_status import TextStats
from .word_freq import count_words
from .args_function import load_input_text
from .args_function import validate_args
def main():
    args =parse_args()
    return run(args)
    
def run(args):
    validate_args(args)

    fname = args.filename
    chunk_size = args.chunk_size
    top = args.top

    text = load_input_text(fname)
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s:%(name)s:%(message)s"
    )
    logger = logging.getLogger(__name__)

    # 传入文件名、词块大小
    logger.info("Program started. input_file=%s chunk_size=%s", fname, chunk_size)
    

    logger.info("Input file loaded. input_length=%s", len(text))
    
    
    if args.summary:
        handle_summary(text)
    if args.freq:
        handle_freq(fname,top)
        
        
    if args.status:
        handle_status(fname)
        
    if args.createjson:    
        #输出json文件
        handle_json(fname,text)
        

    if args.word:
        handle_word(text, args.word)
        print("运行完毕")
    
    return 0




def handle_summary(text):
    summ = summarize_text(text, mode="brief")
    print(summ)
def handle_freq(fname,top):
    try:
        freq_result = word_freq_cnt(fname, top)
    except ValueError as exc:
        sys.exit(str(exc))
    print("Top 10 words in this text!")
    print(freq_result)#打印词频最高的十个单词



def handle_status(filename):
    stats = TextStats(filename)
    lines = stats.line_check()
    words = stats.word_check()
    space = stats.space_check()
    digit = stats.digit_check()

    print(f"行数为{lines}行")#打印行
    print(f"单词数为{words}个单词")#打印单词数
    print(f"数字的个数为{digit}")#打印数字数
    print(f"空格数为{space}")#打印空格数

def handle_json(fname,text):
    output_file = (
            Path("output")
            / f"{Path(fname).stem}.json"
            )
    json_result = {
            "summary": summarize_text(text, mode="brief"),
            "mode": "brief",
            "input_chars": len(text),
        }
    create_json(json_result, output_file)
    print("Successfully create the json")


def handle_word(text, word):
    target_word = word.strip().lower()
    count = count_words(text, target_word)
    print(f"{target_word}: {count}")



if __name__ == "__main__":
    raise SystemExit(main())
