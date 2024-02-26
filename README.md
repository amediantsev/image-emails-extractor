# Email Extractor from Image

This service is designed to extract email addresses from an image file. It is implemented as a Python script and utilizes Tesseract-OCR, 
an open-source OCR engine, to recognize text within the image, and then applies regular expressions to identify and extract email addresses.

## Features

- Extract email addresses from an image file.
- Save the extracted email addresses to a specified text file.
- Does not require internet access or the use of external services for text recognition.

## Prerequisites

Before you can use this script, you need to have Python installed on your system (Python 3.6 or newer is recommended). Additionally, you must install Tesseract-OCR and the Python libraries `pytesseract` and `Pillow`.

### Installing Tesseract-OCR

Tesseract-OCR needs to be installed separately from the Python environment. The installation process varies depending on your operating system:

- **Windows:** Download the installer from [the official Tesseract GitHub repository](https://github.com/tesseract-ocr/tesseract/wiki) and follow the installation instructions.
- **Linux:** Use your package manager to install Tesseract. For example, on Ubuntu or Debian, you can run `sudo apt-get install tesseract-ocr`.
- **macOS:** Install using Homebrew with the command `brew install tesseract`.

### Python Environment Setup

After installing Tesseract-OCR, set up your Python environment by installing the required Python libraries. Run the following command in your terminal:

```bash
pip install pytesseract Pillow
```

## Usage

To use the script, you need to provide two arguments: `--input`, the path to the input image, and `--output`, the path to the output text file where the extracted email addresses will be saved.

Example command:

```bash
python email_extractor.py --input /path/to/image.png --output /path/to/output.txt
```

## Script Arguments

- `--input`: Specifies the path to the input image file.
- `--output`: Specifies the path to the text file where extracted email addresses will be saved.

## License

This script is released under the MIT License.

## Acknowledgments

This script uses the following open-source software:
- [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract) for optical character recognition.
- [Pytesseract](https://pypi.org/project/pytesseract/) as a Python wrapper for Tesseract-OCR.
- [Pillow](https://python-pillow.org/) for image processing.
