---
name: markitdown-converter
description: >
  Convert any supported file (PDF, Word, Excel, PowerPoint, HTML, CSV, JSON,
  XML, ZIP, images, audio) to Markdown using Microsoft's MarkItDown Python
  library. Use this skill when asked to convert, transform, or extract content
  from a file into Markdown format.
---

# MarkItDown File-to-Markdown Converter

Convert virtually any document or media file to clean Markdown using
[Microsoft MarkItDown](https://github.com/microsoft/markitdown).

## When to Activate

- User asks to "convert", "transform", or "extract" a file to Markdown.
- User mentions PDF, Word, Excel, PowerPoint, HTML, CSV, JSON, XML, image, or audio files.
- User wants readable text output from a binary document.

## Supported Input Formats

| Format | Extension(s) |
|---|---|
| PDF | `.pdf` |
| Word | `.docx` |
| Excel | `.xlsx` |
| PowerPoint | `.pptx` |
| HTML | `.html`, `.htm` |
| CSV | `.csv` |
| JSON | `.json` |
| XML | `.xml` |
| ZIP archive | `.zip` |
| Images (OCR) | `.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`, `.tiff` |
| Audio (transcription) | `.mp3`, `.wav`, `.m4a` |
| Plain text | `.txt`, `.md` |

## Setup

### Install

```bash
pip install "markitdown[all]"
```

> `[all]` installs optional extras for image OCR, audio transcription, and
> Azure Document Intelligence support.

### Minimal install (no extras)

```bash
pip install markitdown
```

## Core Conversion Pattern

```python
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
        ValueError: If conversion produces no content.
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

    return markdown_text
```

## CLI Wrapper Pattern

```python
"""
Usage:
    python converter.py <input_file> [output_file]

    If output_file is omitted, the result is printed to stdout.
"""

import sys
from pathlib import Path
from markitdown import MarkItDown


def convert_to_markdown(input_path: str, output_path: str | None = None) -> str:
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
```

## Usage Examples

```python
from markitdown import MarkItDown

md = MarkItDown()

# Convert a PDF
result = md.convert("report.pdf")
print(result.text_content)

# Convert a Word document
result = md.convert("document.docx")
print(result.text_content)

# Convert an Excel spreadsheet
result = md.convert("data.xlsx")
print(result.text_content)

# Convert a PowerPoint presentation
result = md.convert("slides.pptx")
print(result.text_content)

# Convert an image (uses OCR)
result = md.convert("screenshot.png")
print(result.text_content)

# Convert from a URL
result = md.convert("https://example.com/page.html")
print(result.text_content)
```

## Azure Document Intelligence (optional)

For higher-quality PDF/image conversion, supply Azure credentials:

```python
from markitdown import MarkItDown

md = MarkItDown(
    docintel_endpoint="https://<your-resource>.cognitiveservices.azure.com/",
)
result = md.convert("scanned_report.pdf")
print(result.text_content)
```

## Key Rules

1. **Always validate** the input file exists before converting.
2. **Always check** `result.text_content` is non-empty before using it.
3. **Create parent directories** with `mkdir(parents=True, exist_ok=True)` when
   writing output files.
4. **Use `[all]` extras** when image OCR or audio transcription is needed.
5. **Avoid mutation** — treat `result.text_content` as read-only; write a new
   variable if you need to transform it.
