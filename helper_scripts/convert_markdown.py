import subprocess
from pathlib import Path

# Define the base directories used for conversion
MARKDOWN_DIR = "markdown"
PAGES_DIR = "pages"
HTML_TEMPLATE_FILE = "pages/static/template.html"

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

def convert_all_markdown_files():
    '''Find all markdown files in the markdown directory and convert them to HTML'''

    # Get the markdown directory as a Path object
    markdown_dir = Path(MARKDOWN_DIR)

    # Find all markdown files recursively
    for markdown_file in markdown_dir.rglob('*.md'):
        # Calculate the relative path from the markdown directory
        relative_path = markdown_file.parent.relative_to(markdown_dir)

        # Create corresponding output directory in pages folder
        output_dir = Path(PAGES_DIR) / relative_path
        output_dir.mkdir(parents=True, exist_ok=True)

        # Change file extension from .md to .html
        html_output_path = output_dir / markdown_file.stem
        html_output_path = html_output_path.with_suffix('.html')

        # Convert the markdown file to HTML (convert Path objects to strings for subprocess)
        convert_markdown_to_html_with_pandoc(str(markdown_file), str(html_output_path))

if __name__ == "__main__":
    # Allow this script to be run directly for testing or standalone conversion
    convert_all_markdown_files()
