import subprocess
from pathlib import Path

# Define the base directories used for conversion
MARKDOWN_DIR = "docs/pages_markdown"
DOCS_DIR = "docs"
HTML_TEMPLATE_FILE = "docs/static/template.html"

def convert_markdown_to_html_with_pandoc(markdown_file, html_output_file):
    '''Convert a single Markdown file to HTML using Pandoc'''

    # Build the pandoc command
    command = [
        "pandoc",
        markdown_file,
        f"--template={HTML_TEMPLATE_FILE}",
        f"--output={html_output_file}",
        "--standalone"
    ]

    try:
        # Run the Pandoc command with subprocess
        subprocess.run(command, check=True)
        print(f"Converted {markdown_file} to {html_output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error: Pandoc command failed with error: {e}")

def convert_markdown_files(file_list=None):
    '''Convert markdown files to HTML

    Args:
        file_list: Optional list of markdown file paths (str or Path).
                   If None, converts all files in MARKDOWN_DIR.
                   If provided, converts only the specified files.

    Returns:
        int: Number of files successfully converted
    '''

    if file_list is None:
        # Convert all markdown files in the directory
        markdown_dir = Path(MARKDOWN_DIR)

        if not markdown_dir.exists():
            print(f"Markdown directory not found: {MARKDOWN_DIR}")
            return 0

        converted_count = 0

        # Find all markdown files recursively
        for markdown_file in markdown_dir.rglob('*.md'):
            # Output all HTML to docs/pages/ (flat structure)
            output_dir = Path(DOCS_DIR) / "pages"
            output_dir.mkdir(parents=True, exist_ok=True)

            # Change file extension from .md to .html
            html_output_path = output_dir / markdown_file.stem
            html_output_path = html_output_path.with_suffix('.html')

            # Convert the markdown file to HTML
            convert_markdown_to_html_with_pandoc(str(markdown_file), str(html_output_path))
            converted_count += 1

        return converted_count

    else:
        # Convert specific files from the provided list
        if not file_list:
            print("No files to convert")
            return 0

        converted_count = 0

        for markdown_file in file_list:
            markdown_file = Path(markdown_file)

            # Validate file exists
            if not markdown_file.exists():
                print(f"Warning: File not found: {markdown_file}")
                continue

            # Validate file is in markdown directory
            if not str(markdown_file).startswith(MARKDOWN_DIR):
                print(f"Warning: File not in {MARKDOWN_DIR}/ directory: {markdown_file}")
                continue

            # Output all HTML to docs/pages/ (flat structure)
            output_dir = Path(DOCS_DIR) / "pages"
            output_dir.mkdir(parents=True, exist_ok=True)

            # Change file extension from .md to .html
            html_output_path = output_dir / markdown_file.stem
            html_output_path = html_output_path.with_suffix('.html')

            # Convert the markdown file to HTML
            convert_markdown_to_html_with_pandoc(str(markdown_file), str(html_output_path))
            converted_count += 1

        return converted_count


if __name__ == "__main__":
    # Allow this script to be run directly for testing or standalone conversion
    convert_markdown_files()