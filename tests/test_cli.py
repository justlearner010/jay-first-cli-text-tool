from first_cli.cli import parse_args

def test_parser_args_summary():
    args = parse_args(["sample.txt","--summary"])

    assert args.filename == "sample.txt"
    assert args.summary == True
