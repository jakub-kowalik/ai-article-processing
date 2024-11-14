#!/usr/bin/env python3

from argparse import ArgumentParser
from pathlib import Path

from openai import OpenAI


def read_text_from_file(filepath: Path) -> str:
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    return content


def save_text_to_file(article_text: str, filepath: Path) -> None:
    with open(filepath, "w", encoding="UTF-8") as file:
        file.write(article_text)


def configure_parser() -> ArgumentParser:
    argument_parser = ArgumentParser()

    argument_parser.add_argument(
        "-i",
        "--input-article",
        type=Path,
        required=True,
        help="Path to the input article",
    )

    argument_parser.add_argument(
        "-o",
        "--output-path",
        type=Path,
        default=Path("artykul.html"),
        required=False,
        help="Path for output file",
    )

    argument_parser.add_argument(
        "-ak",
        "--api-key",
        type=str,
        required=False,
        help="Specify API key for OpenAI (overrides -ek argument)",
    )

    argument_parser.add_argument(
        "-m",
        "--model",
        type=str,
        required=False,
        default="gpt-3.5-turbo",
        help="Specify which OpenAI model to use",
    )

    argument_parser.add_argument(
        "-pf",
        "--prompt-file",
        type=Path,
        required=False,
        default="prompt.txt",
        help="Path for prompt file",
    )

    return argument_parser


def process_article(
    article_text: str, prompt_text: str, model: str, api_key: str = None
) -> str:
    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": prompt_text},
            {"role": "user", "content": article_text},
        ],
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    parser = configure_parser()
    args = parser.parse_args()

    article = read_text_from_file(args.input_article)
    prompt = read_text_from_file(args.prompt_file)

    processed_article = process_article(article, prompt, args.model, args.api_key)
    save_text_to_file(processed_article, args.output_path)
