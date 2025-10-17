"""Generate Index Page from Published HTML Files.

This script scans the docs/ directory for published field notes and
generates an index.html page listing all available notes.
"""

import re
from pathlib import Path


DOCS_DIR = "docs"
INDEX_FILE = "docs/index.html"


def extract_metadata_from_html(html_file):
    """Extract title and date from HTML file.

    Args:
        html_file: Path to HTML file.

    Returns:
        Dict with title and date keys.
    """
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        title_match = re.search(r'<title>(.*?)</title>', content)
        title = title_match.group(1) if title_match else html_file.stem

        date_match = re.search(r'<meta name="date" content="(.*?)"', content)
        date = date_match.group(1) if date_match else 'No date'

        return {
            'title': title,
            'date': date
        }

    except Exception as e:
        print(f"Warning: Could not extract metadata from {html_file}: {e}")
        return {
            'title': html_file.stem,
            'date': 'No date'
        }


def find_published_notes():
    """Find all published HTML files and extract metadata.

    Returns:
        List of dicts with note information (url, title, date, file).
    """
    docs_dir = Path(DOCS_DIR)

    if not docs_dir.exists():
        print(f"Docs directory not found: {DOCS_DIR}")
        return []

    notes = []

    for html_file in sorted(docs_dir.rglob('*.html'), reverse=True):
        if html_file.name in ['index.html', 'template.html']:
            continue

        metadata = extract_metadata_from_html(html_file)

        relative_path = html_file.relative_to(DOCS_DIR)
        url_path = '/' + str(relative_path).replace('\\', '/')

        notes.append({
            'title': metadata['title'],
            'date': metadata['date'],
            'url': url_path,
            'file': html_file
        })

    return notes


def generate_index_html(notes):
    """Generate index.html content.

    Args:
        notes: List of note dictionaries.

    Returns:
        String containing complete HTML.
    """
    html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Field Notes</title>
    <link rel="stylesheet" href="static/styles.css">
</head>
<body>
    <h1>Field Notes</h1>
    <p>Welcome to the field notes.</p>

    <h2>Available notes</h2>
    <ul>
'''

    for note in notes:
        date_display = (
            note['date'] if note['date'] != 'No date' else '(Draft)'
        )
        relative_url = note["url"].lstrip('/')
        html += (
            f'        <li><a href="{relative_url}">{note["title"]}</a> - '
            f'{date_display}</li>\n'
        )

    html += '''    </ul>
</body>
</html>'''

    return html


def main():
    """Generate index.html from all published notes."""
    print("Generating index.html...")

    notes = find_published_notes()

    if not notes:
        print("No published notes found")
        return

    print(f"Found {len(notes)} published note(s)")

    html_content = generate_index_html(notes)

    index_path = Path(INDEX_FILE)
    index_path.parent.mkdir(parents=True, exist_ok=True)

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"✓ Generated: {INDEX_FILE}")

    for note in notes:
        print(f"  - {note['title']} ({note['date']})")


if __name__ == "__main__":
    main()
