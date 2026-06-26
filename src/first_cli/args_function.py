def validate_args(args):
    if args.chunk_size <= 0:
        raise ValueError("Chunk size is invalid")

    if args.top < 0:
        raise ValueError("Top value is invalid")
    
def load_input_text(fname):
    try:
        with open(fname) as f:
            text = f.read()
    except FileNotFoundError:
        raise FileNotFoundError("文件没找到")
    if not text.strip():
        raise ValueError("输入的文件是空文件")
    
    return text