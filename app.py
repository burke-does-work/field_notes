"""
Field Notes - Main Application

This is the main entry point for the Field Notes application.
It provides an interactive menu for publishing and converting markdown files,
and serves the generated HTML pages via Flask.
"""

import sys
from flask import Flask, render_template
from helper_scripts.convert_markdown import convert_all_markdown_files, convert_specific_files
from helper_scripts.publish_note import (
    find_markdown_files,
    parse_yaml_front_matter,
    find_image_references,
    publish_note
)

# Initialize the Flask application
app = Flask(__name__, template_folder='pages', static_folder='pages/static', static_url_path='/static')


def display_file_list_with_metadata(working_files):
    """
    Display a formatted list of markdown files with metadata

    Args:
        working_files: List of Path objects for markdown files

    Returns:
        None (prints to console)
    """
    print("\nFound {} markdown file(s) in working/:\n".format(len(working_files)))

    for idx, file_path in enumerate(working_files, 1):
        # Parse YAML to get metadata
        yaml_data = parse_yaml_front_matter(file_path)

        # Get title and date
        title = yaml_data.get('title', '[No title found]')
        date = yaml_data.get('date', '[No date found]')

        # Count images
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            image_refs = find_image_references(content)
            image_count = len(image_refs)
        except:
            image_count = 0

        # Display file info
        print(f"[{idx}] {file_path}")
        print(f"    Title: {title}")
        print(f"    Date: {date}")
        print(f"    Images: {image_count} found")

        # Show warnings for missing required fields
        warnings = []
        if 'title' not in yaml_data or not yaml_data['title']:
            warnings.append("Missing 'title'")
        if 'date' not in yaml_data or not yaml_data['date']:
            warnings.append("Missing 'date'")

        if warnings:
            print(f"    ⚠ Warning: {', '.join(warnings)} in YAML front matter")

        print()  # Blank line between entries


def get_user_selection(num_files):
    """
    Get user selection for files to publish

    Args:
        num_files: Total number of files available

    Returns:
        List of indices (0-based) or None if user quit
    """
    print("Select file(s) to publish:")
    print("  - Single file: 1")
    print("  - Multiple files: 1,3")
    print("  - All files: all")
    print("  - Back to main menu: b")
    print("  - Quit: q")
    print()

    while True:
        choice = input("Your choice: ").strip().lower()

        if choice == 'q':
            return None
        if choice == 'b':
            return []

        if choice == 'all':
            return list(range(num_files))

        # Parse comma-separated numbers
        try:
            selections = [int(x.strip()) for x in choice.split(',')]

            # Validate selections are in range
            if all(1 <= s <= num_files for s in selections):
                # Convert to 0-based indices
                return [s - 1 for s in selections]
            else:
                print(f"Error: Please enter numbers between 1 and {num_files}")

        except ValueError:
            print("Error: Invalid input. Please enter numbers separated by commas, 'all', 'b', or 'q'")


def publish_and_convert_workflow():
    """
    Integrated workflow: publish from working/ to markdown/, then convert to HTML

    This is the main publishing workflow that:
    1. Finds markdown files in working/
    2. Displays interactive menu with metadata
    3. Gets user selection
    4. Publishes selected files (working/ → markdown/)
    5. Converts published files (markdown/ → HTML in pages/)
    6. Displays summary
    """
    print("\n" + "=" * 60)
    print("Publishing Workflow")
    print("=" * 60)

    # Step 1: Find working files
    working_files = find_markdown_files("working")

    if not working_files:
        print("\nNo markdown files found in working/ directory.")
        print("Add .md files to working/YYYY/ to get started.\n")
        input("Press Enter to return to main menu...")
        return

    # Step 2: Display menu with metadata
    display_file_list_with_metadata(working_files)

    # Step 3: Get user selection
    selected_indices = get_user_selection(len(working_files))

    if selected_indices is None:
        print("\nExiting...")
        sys.exit(0)

    if not selected_indices:
        return  # User chose to go back

    # Step 4: Publish selected files
    print("\n" + "━" * 60)
    print("Step 1: Publishing markdown files")
    print("━" * 60 + "\n")

    published_files = []
    total_images_moved = 0
    total_images_copied = 0
    warnings = []

    for idx in selected_indices:
        source_path = working_files[idx]
        print(f"Publishing: {source_path}")

        result = publish_note(source_path)

        if result['success']:
            published_files.append(result['destination_path'])
            total_images_moved += len(result['images_moved'])
            total_images_copied += len(result['images_copied'])

            print(f"✓ Copied to: {result['destination_path']}\n")

            # Show image processing details
            if result['images_moved'] or result['images_copied']:
                print("  Images processed:")
                for img in result['images_moved']:
                    print(f"  ✓ Moved: {img} → pages/static/media/")
                    print(f"    (unique to this file)")
                for img, count in result['images_copied']:
                    print(f"  ✓ Copied: {img} → pages/static/media/")
                    print(f"    (shared - used in {count} files, kept in working/)")
                print()

            if result['paths_updated'] > 0:
                print(f"  ✓ Updated {result['paths_updated']} image path(s)\n")

            # Collect warnings
            if result['warnings']:
                warnings.extend(result['warnings'])
                for warning in result['warnings']:
                    print(f"  ⚠ {warning}")
                print()

        else:
            print(f"✗ Error: {result['error']}\n")

    # Step 5: Convert published files to HTML
    if published_files:
        print("━" * 60)
        print("Step 2: Converting to HTML")
        print("━" * 60 + "\n")

        converted_count = convert_specific_files(published_files)

        # Step 6: Display summary
        print("\n" + "━" * 60)
        print("Summary")
        print("━" * 60)
        print(f"Files published: {len(published_files)}")
        print(f"Files converted to HTML: {converted_count}")
        print(f"Images moved: {total_images_moved}")
        print(f"Images copied: {total_images_copied}")

        if warnings:
            print(f"\nWarnings: {len(warnings)}")

        print("\n✓ Complete!\n")

    input("Press Enter to return to main menu...")


def display_main_menu():
    """
    Display the main menu and handle user choice

    Menu options:
    1. Publish and convert field notes
    2. Convert all markdown to HTML
    3. Start Flask development server
    4. Exit

    Returns:
        User's choice (str)
    """
    print("\n" + "=" * 60)
    print("Field Notes Manager")
    print("=" * 60)
    print("\nWhat would you like to do?\n")
    print("1. Publish and convert field notes")
    print("2. Convert all markdown to HTML")
    print("3. Start Flask development server")
    print("4. Exit")
    print()

    while True:
        choice = input("Your choice (1-4): ").strip()
        if choice in ['1', '2', '3', '4']:
            return choice
        print("Error: Please enter 1, 2, 3, or 4")


def main_menu_loop():
    """
    Main menu loop - runs until user exits

    Handles:
    - Publishing and converting workflow
    - Converting all markdown files
    - Starting Flask server
    - Exiting application
    """
    while True:
        choice = display_main_menu()

        if choice == '1':
            # Publish and convert workflow
            publish_and_convert_workflow()

        elif choice == '2':
            # Convert all markdown to HTML
            print("\n" + "━" * 60)
            print("Converting all markdown files to HTML")
            print("━" * 60 + "\n")

            count = convert_all_markdown_files()

            print(f"\n✓ Converted {count} file(s)\n")
            input("Press Enter to return to main menu...")

        elif choice == '3':
            # Start Flask server
            print("\n" + "━" * 60)
            print("Starting Flask development server")
            print("━" * 60 + "\n")
            print("Server will start at http://127.0.0.1:5000/")
            print("Press CTRL+C to stop the server and return to menu\n")

            try:
                # Convert all markdown before starting server
                convert_all_markdown_files()

                # Start Flask server
                app.run(debug=True, use_reloader=False)

            except KeyboardInterrupt:
                print("\n\nServer stopped.\n")
                input("Press Enter to return to main menu...")

        elif choice == '4':
            # Exit
            print("\nGoodbye!\n")
            sys.exit(0)


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
    # Check for command-line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == '--serve':
            # Skip menu, start server directly
            print("Starting Flask development server...")
            convert_all_markdown_files()
            app.run(debug=True)

        elif sys.argv[1] == '--convert-all':
            # Skip menu, convert all files
            print("Converting all markdown files to HTML...")
            count = convert_all_markdown_files()
            print(f"✓ Converted {count} file(s)")

        elif sys.argv[1] == '--help':
            print("Field Notes Manager")
            print("\nUsage:")
            print("  python app.py              # Interactive menu (default)")
            print("  python app.py --serve      # Start Flask server directly")
            print("  python app.py --convert-all # Convert all markdown to HTML")
            print("  python app.py --help       # Show this help message")

        else:
            print(f"Unknown option: {sys.argv[1]}")
            print("Use --help for usage information")

    else:
        # No arguments - show interactive menu
        main_menu_loop()