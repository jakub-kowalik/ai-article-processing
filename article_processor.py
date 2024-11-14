#!/usr/bin/env python3

import argparse
import sys
from pathlib import Path

import openai
import os


def read_article_from_txt(filepath):
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    return content


def process_article(article_text: str, api_key: str):
    pass


def configure_parser():
    argument_parser = argparse.ArgumentParser()

    argument_parser.add_argument(
        "-i",
        "--input-article",
        type=Path,
        required=True,
        help="Path to the input article",
    )

    argument_parser.add_argument(
        "-ak",
        "--api-key",
        type=str,
        required=False,
        help="Specify API key for OpenAI (overrides -ek argument)",
    )

    argument_parser.add_argument(
        "-ek",
        "--env-key",
        action=argparse.BooleanOptionalAction,
        type=bool,
        required=False,
        default=False,
        help="Use OPENAI_API_KEY environment variable",
    )

    return argument_parser


def configure_api_key(api_key, use_env_key):
    if api_key:
        openai.api_key = api_key or os.environ.get("OPENAI_API_KEY")
    elif use_env_key:
        if "OPENAI_API_KEY" in os.environ:
            openai.api_key = os.environ.get("OPENAI_API_KEY")
        else:
            sys.exit("OPENAI_API_KEY environment variable not set")
    else:
        sys.exit("Can't proceed without API key")


if __name__ == "__main__":
    parser = configure_parser()
    args = parser.parse_args()

    configure_api_key(args.api_key, args.env_key)

    print(read_article_from_txt(args.input_article))
