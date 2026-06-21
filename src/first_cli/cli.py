import argparse
def parse_args():
    parser = argparse.ArgumentParser(
    description="Analyze text files and generate chunk."
    )

    parser.add_argument("filename",
                        help="Input text file")
    parser.add_argument("--chunk_size", type=int, default=500,
                        help= "Words per chunk")


    parser.add_argument(
        "--summary",
        action="store_true",
        help="Show summary only"
    )

    parser.add_argument(
        "--freq",
        action="store_true",
        help="Show the most frequent 10 words in text"
    )

    parser.add_argument(
        "--status",
        action="store_true",
        help="Show the text status"
    )

    parser.add_argument(
        "--createjson",
        action="store_true",
        help="create json file of this text to show the chunks"
    )

    return parser.parse_args()