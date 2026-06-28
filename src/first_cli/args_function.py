def validate_args(args):
    if args.chunk_size <= 0:
        raise ValueError("Chunk size is invalid")

    if args.top < 0:
        raise ValueError("Top value is invalid")

    output_actions = [
        args.summary,
        args.status,
        args.createjson,
        args.word,
        args.freq,
    ]

    if not any(output_actions):
        raise ValueError("请至少选择一个功能进行输出，例如 --word, --freq, 详情见 --help")


def load_input_text(fname):
    try:
        with open(fname) as f:
            text = f.read()
    except FileNotFoundError as exc:
        raise FileNotFoundError("File does not exist") from exc
    except PermissionError as exc:
        raise PermissionError("File does not have permission to open") from exc
    except UnicodeDecodeError as exc:
        raise UnicodeDecodeError(
            exc.encoding,
            exc.object,
            exc.start,
            exc.end,
            "fail to unicode decode",
        ) from exc

    if not text.strip():
        raise ValueError("Input file is empty")

    return text
