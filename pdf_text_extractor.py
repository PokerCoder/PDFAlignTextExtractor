import sys
import argparse
import fitz  # PyMuPDF


def extract_text(pdf_path, output_path):
    """
    Extracts text from a PDF file and saves it to an output text file while preserving the alignment.

    :param pdf_path: str, path to the input PDF file
    :param output_path: str, path to the output text file
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as output_file:
            doc = fitz.open(pdf_path)
            for page_num in range(doc.page_count):
                page = doc[page_num]
                blocks = page.get_text("blocks")
                # Sort blocks by y-coordinate and then by x-coordinate
                blocks.sort(key=lambda block: (-block[1], block[0]))

                for block in blocks:
                    text = block[4].strip()
                    if text:
                        output_file.write(text + '\n')

            doc.close()

    except Exception as e:
        print(f"Error extracting text from '{pdf_path}': {e}")
        sys.exit(1)


def main(args):
    extract_text(args.input, args.output)
    print(f"Text extracted from '{args.input}' and saved in '{args.output}'")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Extract text from a PDF file and save it to a text file, preserving the alignment"
    )
    parser.add_argument("input", help="Path to the input PDF file")
    parser.add_argument("output", help="Path to the output text file")
    args = parser.parse_args()

    main(args)
