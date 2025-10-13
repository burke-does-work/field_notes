from flask import Flask, render_template
import subprocess
from pathlib import Path

# Initialize the Flask application
app = Flask(__name__)

# Define the base directories used in the app
MARKDOWN_DIR = "markdown"
PAGES_DIR = "pages"
HTML_TEMPLATE_FILE = "static/template.html"

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

# TODO: Determine the routing structure for serving multiple field notes
# TODO: Create an index page that lists all available field notes
# Define the root ("/") route
@app.route("/")
def home():
    # Convert all markdown files to HTML before serving the page
    convert_all_markdown_files()

    # TODO: Update to serve the actual homepage (pages/index.html)
    # Render the homepage
    return render_template('index.html')

if __name__ == "__main__":
    # Convert all markdown files to HTML when the app starts
    convert_all_markdown_files()

    # Run the Flask application in debug mode
    app.run(debug=True)
