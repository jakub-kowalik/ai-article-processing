import argparse
from pathlib import Path


def read_article_from_txt(filepath):
    file = open(filepath, "r", encoding="utf-8")
    content = file.read()
    file.close()
    return content


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-i",
        "--input-article",  # named argument
        type=Path,  # ensures the file can be opened for reading
        required=True,  # makes this argument required
        help="Path to the input article",
    )

    args = parser.parse_args()

    print(read_article_from_txt(args.input_article))
