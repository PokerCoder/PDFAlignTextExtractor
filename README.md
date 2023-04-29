# PDF Text Extractor

PDF Text Extractor is a Python command-line application that extracts text from PDF files while preserving the alignment and saves the text to a plain text file.

## Prerequisites

To use PDF Text Extractor, you must have Python 3.6 or later installed on your system. Additionally, you'll need to install the PyMuPDF library:

```bash
pip install PyMuPDF
```

## Usage

Save the provided code as `pdf_text_extractor.py` and run the following command in your terminal:

```bash
python pdf_text_extractor.py <input_pdf_path> <output_txt_path>
```

Replace `<input_pdf_path>` with the path to your PDF file and `<output_txt_path>` with the path to the output text file.

For example:

```bash
python pdf_text_extractor.py sample.pdf extracted_text.txt
```

This command will extract text from `sample.pdf` and save the extracted text to `extracted_text.txt`.

## Important Notes

The PDF Text Extractor application is designed to work well for most PDF files with simple layouts. However, it may not be able to preserve the exact formatting and alignment in some cases, especially for complex PDF files.