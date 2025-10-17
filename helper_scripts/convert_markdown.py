"""Markdown to HTML Converter.

Converts markdown files to HTML using Pandoc with custom templating.
Supports both batch conversion of all files and selective file conversion.
"""

import subprocess
from pathlib import Path


# Define the base directories used for conversion
MARKDOWN_DIR = "docs/pages_markdown"
DOCS_DIR = "docs"
HTML_TEMPLATE_FILE = "docs/static/template.html"


def convert_markdown_to_html_with_pandoc(markdown_file, html_output_file):
    """Convert a single markdown file to HTML using Pandoc.

    Args:
        markdown_file: Path to the input markdown file.
        html_output_file: Path where the output HTML file will be saved.
    """
    command = [
        "pandoc",
        markdown_file,
        f"--template={HTML_TEMPLATE_FILE}",
        f"--output={html_output_file}",
        "--standalone"
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Converted {markdown_file} to {html_output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error: Pandoc command failed with error: {e}")


def convert_markdown_files(file_list=None):
    """Convert markdown files to HTML.

    Args:
        file_list: Optional list of markdown file paths (str or Path).
                   If None, converts all files in MARKDOWN_DIR.
                   If provided, converts only the specified files.

    Returns:
        Number of files successfully converted.
    """
    if file_list is None:
        markdown_dir = Path(MARKDOWN_DIR)

        if not markdown_dir.exists():
            print(f"Markdown directory not found: {MARKDOWN_DIR}")
            return 0

        converted_count = 0

        for markdown_file in markdown_dir.rglob('*.md'):
            output_dir = Path(DOCS_DIR) / "pages"
            output_dir.mkdir(parents=True, exist_ok=True)

            html_output_path = output_dir / markdown_file.stem
            html_output_path = html_output_path.with_suffix('.html')

            convert_markdown_to_html_with_pandoc(
                str(markdown_file),
                str(html_output_path)
            )
            converted_count += 1

        return converted_count

    else:
        if not file_list:
            print("No files to convert")
            return 0

        converted_count = 0

        for markdown_file in file_list:
            markdown_file = Path(markdown_file)

            if not markdown_file.exists():
                print(f"Warning: File not found: {markdown_file}")
                continue

            if not str(markdown_file).startswith(MARKDOWN_DIR):
                print(
                    f"Warning: File not in {MARKDOWN_DIR}/ directory: "
                    f"{markdown_file}"
                )
                continue

            output_dir = Path(DOCS_DIR) / "pages"
            output_dir.mkdir(parents=True, exist_ok=True)

            html_output_path = output_dir / markdown_file.stem
            html_output_path = html_output_path.with_suffix('.html')

            convert_markdown_to_html_with_pandoc(
                str(markdown_file),
                str(html_output_path)
            )
            converted_count += 1

        return converted_count


if __name__ == "__main__":
    convert_markdown_files()