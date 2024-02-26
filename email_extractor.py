import argparse
import re
import os
from typing import Iterable

import pytesseract
from PIL import Image

EMAIL_REGEX = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")

parser = argparse.ArgumentParser(description="Extract emails from an image.")
parser.add_argument("--input", type=str, help="Local path to the input image", required=True)
parser.add_argument("--output", type=str, help="Local path to the output text file", required=True)


def parse_input_args():
    args = parser.parse_args()
    parser_errors = []

    input_path, output_path = args.input, args.output

    if not os.path.exists(input_path):
        parser_errors.append(f"The file {input_path} does not exist!")

    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        parser_errors.append(f"The directory {output_dir} does not exist for the output file!")

    if parser_errors:
        parser.error(";\t".join(parser_errors))

    return args


def extract_emails(img_path):
    image = Image.open(img_path)
    image_text = pytesseract.image_to_string(image)
    return EMAIL_REGEX.findall(image_text)


def save_extracted_emails(extracted_emails: Iterable[str], output_path):
    with open(output_path, "w") as file:
        file.writelines("\n".join(sorted(set(extracted_emails))))


if __name__ == "__main__":
    input_args = parse_input_args()

    emails = extract_emails(input_args.input)
    save_extracted_emails(emails, input_args.output)
