"""
File-to-Markdown converter using Microsoft's MarkItDown library.

Supported input formats: PDF, Word (.docx), Excel (.xlsx), PowerPoint (.pptx),
HTML, CSV, JSON, XML, ZIP archives, images (with OCR), audio (with transcription),
and plain text files.

Usage:
    python testing.py <input_file> [output_file]

    If output_file is omitted, the result is printed to stdout.
    If output_file is provided, the markdown is written to that path.

Examples:
    python testing.py report.pdf
    python testing.py data.xlsx output.md
    python testing.py slides.pptx converted/slides.md
"""

import sys
from pathlib import Path
from markitdown import MarkItDown


def convert_to_markdown(input_path: str, output_path: str | None = None) -> str:
    """
    Convert a file to Markdown using MarkItDown.

    Args:
        input_path: Path to the source file.
        output_path: Optional path to write the Markdown output.

    Returns:
        The converted Markdown text.

    Raises:
        FileNotFoundError: If the input file does not exist.
        ValueError: If conversion fails or produces no content.
    """
    source = Path(input_path)
    if not source.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    md = MarkItDown()
    result = md.convert(str(source))

    if not result or not result.text_content:
        raise ValueError(f"Conversion produced no content for: {input_path}")

    markdown_text = result.text_content

    if output_path:
        dest = Path(output_path)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(markdown_text, encoding="utf-8")
        print(f"Saved: {dest}")

    return markdown_text


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) >= 3 else None

    try:
        markdown = convert_to_markdown(input_file, output_file)
        if not output_file:
            print(markdown)
    except (FileNotFoundError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
