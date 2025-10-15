"""
Field Notes - Main Application

Workflow:
1. Publish all staged markdown files
2. Rebuild website from all published markdown
3. Start Flask development server

Run: python app.py
"""

import sys
from flask import Flask, render_template
from helper_scripts.convert_markdown import convert_all_markdown_files
from helper_scripts.publish_note import (
    find_markdown_files,
    parse_yaml_front_matter,
    find_image_references,
    publish_note
)
from helper_scripts.generate_index import main as generate_index

# Initialize the Flask application
app = Flask(__name__, template_folder='docs', static_folder='docs/static', static_url_path='/static')


def main():
    """
    Main workflow: Publish staged files, rebuild website, start server
    """
    print("\n" + "=" * 70)
    print("Field Notes - Publishing and Development Server")
    print("=" * 70)

    # Step 1: Find and publish staged files
    print("\n" + "━" * 70)
    print("Step 1: Publishing staged markdown files")
    print("━" * 70 + "\n")

    staged_files = find_markdown_files("working/pages_markdown_staged")

    if not staged_files:
        print("No files found in working/pages_markdown_staged/")
        print("Skipping publish step.\n")
    else:
        print(f"Found {len(staged_files)} file(s) to publish:\n")

        # Show what will be published
        for file_path in staged_files:
            yaml_data = parse_yaml_front_matter(file_path)
            title = yaml_data.get('title', '[No title]')
            date = yaml_data.get('date', '[No date]')

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                image_refs = find_image_references(content)
                image_count = len(image_refs)
            except:
                image_count = 0

            print(f"  • {file_path.name}")
            print(f"    Title: {title}")
            print(f"    Date: {date}")
            print(f"    Images: {image_count}")

        print()

        # Publish all staged files
        published_files = []
        total_images_moved = 0
        total_images_copied = 0
        all_warnings = []

        for file_path in staged_files:
            print(f"Publishing: {file_path.name}...")

            result = publish_note(file_path)

            if result['success']:
                published_files.append(result['destination_path'])
                total_images_moved += len(result['images_moved'])
                total_images_copied += len(result['images_copied'])

                print(f"  ✓ Published to: {result['destination_path']}")

                # Show image processing
                if result['images_moved']:
                    for img in result['images_moved']:
                        print(f"  ✓ Moved image: {img}")

                if result['images_copied']:
                    for img, count in result['images_copied']:
                        print(f"  ✓ Copied image: {img} (used in {count} files)")

                if result['paths_updated'] > 0:
                    print(f"  ✓ Updated {result['paths_updated']} image path(s)")

                # Collect warnings
                if result['warnings']:
                    all_warnings.extend(result['warnings'])
                    for warning in result['warnings']:
                        print(f"  ⚠ Warning: {warning}")

                print()
            else:
                print(f"  ✗ Error: {result['error']}\n")

        # Publish summary
        if published_files:
            print("━" * 70)
            print("Publish Summary")
            print("━" * 70)
            print(f"Files published: {len(published_files)}")
            print(f"Images moved: {total_images_moved}")
            print(f"Images copied: {total_images_copied}")
            if all_warnings:
                print(f"Warnings: {len(all_warnings)}")
            print()

    # Step 2: Rebuild website
    print("━" * 70)
    print("Step 2: Rebuilding website")
    print("━" * 70 + "\n")

    print("Converting all markdown files to HTML...")
    converted_count = convert_all_markdown_files()
    print(f"✓ Converted {converted_count} file(s)\n")

    print("Generating index.html...")
    generate_index()
    print()

    # Step 3: Start development server
    print("━" * 70)
    print("Step 3: Starting Flask development server")
    print("━" * 70 + "\n")
    print("Server starting at http://127.0.0.1:5000/")
    print("Press CTRL+C to stop the server\n")
    print("=" * 70 + "\n")

    try:
        app.run(debug=True, use_reloader=False)
    except KeyboardInterrupt:
        print("\n\n" + "=" * 70)
        print("Server stopped")
        print("=" * 70 + "\n")


# Flask routes

@app.route("/")
def home():
    """Homepage route - serves the index page"""
    return render_template('index.html')


@app.route("/<path:year>/<path:filename>")
def serve_note(year, filename):
    """Serve individual field note HTML files"""
    return render_template(f'{year}/{filename}')


if __name__ == "__main__":
    main()