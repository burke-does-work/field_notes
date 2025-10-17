"""Publishing Helper Functions for Field Notes.

This module provides functions to publish markdown files from the working/
directory to the markdown/ directory, handling image references and path updates.
"""

import re
import shutil
from pathlib import Path


# Configuration
WORKING_STAGED_DIR = "working/pages_markdown_staged"
MARKDOWN_DIR = "docs/pages_markdown"
STATIC_MEDIA_DIR = "docs/static/media"


def find_markdown_files(working_dir=WORKING_STAGED_DIR):
    """Find all markdown files in the working directory.

    Args:
        working_dir: Path to working directory.

    Returns:
        List of Path objects for all .md files found.
    """
    working_path = Path(working_dir)

    if not working_path.exists():
        return []

    markdown_files = []
    for md_file in working_path.rglob('*.md'):
        if not any(part.startswith('.') for part in md_file.parts):
            markdown_files.append(md_file)

    return sorted(markdown_files)


def parse_yaml_front_matter(file_path):
    """Parse YAML front matter from a markdown file.

    Args:
        file_path: Path to markdown file.

    Returns:
        Dict with YAML fields (title, date, tags, etc.) or empty dict if
        no YAML found.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if not content.startswith('---'):
            return {}

        parts = content.split('---', 2)
        if len(parts) < 3:
            return {}

        yaml_content = parts[1].strip()

        yaml_data = {}
        for line in yaml_content.split('\n'):
            line = line.strip()
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")

                if value.startswith('[') and value.endswith(']'):
                    value = [
                        item.strip().strip('"').strip("'")
                        for item in value[1:-1].split(',')
                    ]

                yaml_data[key] = value

        return yaml_data

    except Exception as e:
        print(f"Warning: Could not parse YAML from {file_path}: {e}")
        return {}


def find_image_references(markdown_content):
    """Find all image references in markdown content.

    Args:
        markdown_content: String containing markdown text.

    Returns:
        List of tuples: (alt_text, image_path).
    """
    pattern = r'!\[(.*?)\]\((.*?)\)'
    matches = re.findall(pattern, markdown_content)

    html_pattern = r'<img\s+[^>]*src=["\']([^"\']+)["\']'
    html_matches = re.findall(html_pattern, markdown_content)

    image_refs = []

    for alt_text, path in matches:
        image_refs.append((alt_text, path))

    for path in html_matches:
        image_refs.append(('', path))

    return image_refs


def extract_image_filename(image_path):
    """Extract just the filename from an image path.

    Args:
        image_path: Path string (e.g., "./media/image.jpg").

    Returns:
        Filename string (e.g., "image.jpg").
    """
    return Path(image_path).name


def count_image_usage(image_filename, working_dir=WORKING_STAGED_DIR):
    """Count how many markdown files reference a specific image.

    Args:
        image_filename: Image filename to search for (e.g., "image.jpg").
        working_dir: Path to working directory.

    Returns:
        Integer count of files that reference this image.
    """
    working_path = Path(working_dir)
    count = 0

    for md_file in working_path.rglob('*.md'):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            if image_filename in content:
                count += 1

        except Exception as e:
            print(f"Warning: Could not read {md_file}: {e}")
            continue

    return count


def replace_markdown_image_path(match):
    """Helper function to replace markdown image paths.

    Args:
        match: Regex match object.

    Returns:
        Replacement string with updated path.
    """
    alt_text = match.group(1)
    old_path = match.group(2) + match.group(3)

    filename = extract_image_filename(old_path)
    new_path = f"../static/media/{filename}"

    return f"![{alt_text}]({new_path})"


def replace_html_image_path(match):
    """Helper function to replace HTML image paths.

    Args:
        match: Regex match object.

    Returns:
        Replacement string with updated path.
    """
    attributes = match.group(1)
    old_path = match.group(2)

    filename = extract_image_filename(old_path)
    new_path = f"../static/media/{filename}"

    return f'<img {attributes}src="{new_path}"'


def update_image_paths(content):
    """Update image paths in markdown content for publishing.

    Changes:
        - ./media/image.jpg → ../static/media/image.jpg
        - media/image.jpg → ../static/media/image.jpg
        - ../media/image.jpg → ../static/media/image.jpg

    Args:
        content: Markdown content string.

    Returns:
        Updated content string with rewritten paths.
    """
    content = re.sub(
        r'!\[(.*?)\]\((\.\/media\/|media\/|\.\.\/media\/)(.*?)\)',
        replace_markdown_image_path,
        content
    )

    content = re.sub(
        r'<img\s+([^>]*)src=["\'](?:\.\/media\/|media\/|\.\.\/media\/)(.*?)["\']',
        replace_html_image_path,
        content
    )

    return content


def publish_note(source_path, dry_run=False):
    """Publish a single markdown file from working/ to markdown/.

    Process:
        1. Validate source file exists and is in working/
        2. Read markdown content
        3. Parse YAML front matter
        4. Find image references
        5. Copy markdown to markdown/ directory
        6. Handle images (move if unique, copy if shared)
        7. Update image paths in copied markdown

    Args:
        source_path: Path to markdown file in working/ (str or Path).
        dry_run: If True, show what would happen without making changes.

    Returns:
        Dict with results containing the following keys:
            success: Whether the operation succeeded.
            source_path: Original source file path.
            destination_path: Published destination path or None.
            images_moved: List of filenames that were moved.
            images_copied: List of (filename, usage_count) tuples.
            images_missing: List of filenames that could not be found.
            paths_updated: Number of image paths updated.
            warnings: List of warning messages.
            error: Error message or None.
    """
    result = {
        'success': False,
        'source_path': str(source_path),
        'destination_path': None,
        'images_moved': [],
        'images_copied': [],
        'images_missing': [],
        'paths_updated': 0,
        'warnings': [],
        'error': None
    }

    try:
        source_path = Path(source_path)

        if not source_path.exists():
            result['error'] = f"Source file not found: {source_path}"
            return result

        if not str(source_path).startswith(WORKING_STAGED_DIR):
            result['error'] = (
                f"Source file must be in {WORKING_STAGED_DIR}/ directory"
            )
            return result

        with open(source_path, 'r', encoding='utf-8') as f:
            original_content = f.read()

        yaml_data = parse_yaml_front_matter(source_path)

        if 'title' not in yaml_data or not yaml_data['title']:
            result['warnings'].append("Missing 'title' in YAML front matter")
        if 'date' not in yaml_data or not yaml_data['date']:
            result['warnings'].append("Missing 'date' in YAML front matter")

        image_refs = find_image_references(original_content)

        filename = source_path.name
        dest_path = Path(MARKDOWN_DIR) / filename
        result['destination_path'] = str(dest_path)

        if dry_run:
            print(f"[DRY RUN] Would copy: {source_path} → {dest_path}")
        else:
            dest_path.parent.mkdir(parents=True, exist_ok=True)

        for alt_text, image_path in image_refs:
            filename = extract_image_filename(image_path)

            source_image = Path("working/static/media") / filename

            if not source_image.exists():
                result['images_missing'].append(filename)
                result['warnings'].append(f"Image not found: {source_image}")
                continue

            staged_count = count_image_usage(filename, WORKING_STAGED_DIR)
            working_count = count_image_usage(
                filename, "working/pages_markdown"
            )
            usage_count = staged_count + working_count

            dest_image = Path(STATIC_MEDIA_DIR) / filename

            if dry_run:
                if usage_count == 1:
                    print(
                        f"[DRY RUN] Would move: {source_image} → {dest_image}"
                    )
                    result['images_moved'].append(filename)
                else:
                    print(
                        f"[DRY RUN] Would copy: {source_image} → "
                        f"{dest_image} (used in {usage_count} files)"
                    )
                    result['images_copied'].append((filename, usage_count))
            else:
                dest_image.parent.mkdir(parents=True, exist_ok=True)

                if usage_count == 1:
                    shutil.move(str(source_image), str(dest_image))
                    result['images_moved'].append(filename)
                else:
                    shutil.copy2(str(source_image), str(dest_image))
                    result['images_copied'].append((filename, usage_count))

        updated_content = update_image_paths(original_content)

        result['paths_updated'] = len(image_refs)

        if dry_run:
            print(
                f"[DRY RUN] Would update {result['paths_updated']} "
                f"image path(s)"
            )
        else:
            with open(dest_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)

        result['success'] = True
        return result

    except Exception as e:
        result['error'] = str(e)
        return result


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python publish_note.py <path_to_markdown_file>")
        print("Example: python publish_note.py working/2025/my-note.md")
        sys.exit(1)

    file_path = sys.argv[1]
    result = publish_note(file_path)

    if result['success']:
        print(f"✓ Published: {result['destination_path']}")
        if result['images_moved']:
            print(f"  Images moved: {', '.join(result['images_moved'])}")
        if result['images_copied']:
            for img, count in result['images_copied']:
                print(f"  Images copied: {img} (used in {count} files)")
        if result['warnings']:
            for warning in result['warnings']:
                print(f"  ⚠ {warning}")
    else:
        print(f"✗ Error: {result['error']}")
        sys.exit(1)
