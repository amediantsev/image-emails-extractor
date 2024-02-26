import argparse
import re
from typing import Iterable

import pytesseract
from PIL import Image


EMAIL_REGEX = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")

parser = argparse.ArgumentParser(description="Extract emails from an image.")
parser.add_argument("--input", type=str, help="Local path to the input image", required=True)
parser.add_argument("--output", type=str, help="Local path to the output text file", required=True)


def extract_emails(img_path):
    image = Image.open(img_path)
    image_text = pytesseract.image_to_string(image)
    return EMAIL_REGEX.findall(image_text)


def save_extracted_emails(extracted_emails: Iterable[str], output_path):
    with open(output_path, "w") as file:
        file.writelines("\n".join(sorted(set(extracted_emails))))


if __name__ == "__main__":
    args = parser.parse_args()

    emails = extract_emails(args.input)
    save_extracted_emails(emails, args.output)
