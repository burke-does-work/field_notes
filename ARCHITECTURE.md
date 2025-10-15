# Field Notes - Technical Architecture

PROJECT_OVERVIEW.md = what and why, ARCHITECTURE.md = how and technical details.

## System Overview

Flask-based web application that manages markdown field notes through a publishing workflow, converting them to styled HTML pages served via development server or deployable to GitHub Pages.

## Directory Structure

```
field_notes/
├── app.py                      # Flask app with publishing workflow
├── requirements.txt            # Flask 3.0.0
├── helper_scripts/
│   ├── convert_markdown.py     # Pandoc conversion functions
│   └── publish_note.py         # Publishing workflow helpers
├── working/                    # Draft markdown files
│   └── YYYY/
│       ├── [note].md          # Draft field notes
│       └── media/             # Draft images
├── markdown/                   # Published markdown files
│   └── YYYY/                  # Organized by year
│       └── [note].md          # Published field notes
└── docs/                      # Deployment folder (GitHub Pages)
    ├── index.html             # Homepage listing all notes
    ├── YYYY/
    │   └── [note].html        # Converted HTML files
    └── static/
        ├── template.html      # Pandoc HTML template
        ├── styles.css         # Site styling
        └── media/             # Published images
```

## Core Components

### Flask Application (`app.py`)

**Purpose:** Interactive CLI for publishing workflow and development server

**Routes:**
- `GET /` - Serves homepage (`docs/index.html`)
- `GET /<year>/<filename>` - Serves individual field notes from `docs/`

**Flask Configuration:**
- `template_folder='docs'` - Serves HTML from docs directory
- `static_folder='docs/static'` - Serves static assets from docs/static
- `static_url_path='/static'` - Static files accessible at `/static`

**Menu Options:**
1. Publish and convert field notes (integrated workflow)
2. Convert all markdown to HTML
3. Start Flask development server
4. Exit

### Publishing Workflow (`helper_scripts/publish_note.py`)

**Process:** `working/` → `markdown/` → `docs/` (HTML)

**Steps:**
1. Parse YAML front matter for metadata validation
2. Find image references in markdown
3. Copy markdown file to `markdown/` directory
4. Move images to `docs/static/media/` (or copy if shared)
5. Update image paths to `/static/media/[filename]`

**Image Handling:**
- Unique images: Moved from `working/YYYY/media/` to `docs/static/media/`
- Shared images: Copied (remain in working for other notes)

### Markdown Conversion (`helper_scripts/convert_markdown.py`)

**Tool:** Pandoc with custom HTML template

**Configuration:**
- Template: `docs/static/template.html`
- Input: `markdown/YYYY/[note].md`
- Output: `docs/YYYY/[note].html`
- Maintains directory structure

**YAML Front Matter:**
- `title` - Required, page title
- `date` - Required, publication date
- `tags` - Optional, list of tags
- `author` - Optional
- `description` - Optional

### HTML Template (`docs/static/template.html`)

Pandoc template with conditional metadata rendering.

**Variables:**
- `$title$` - Page title
- `$body$` - Converted markdown content
- `$author$` - Author metadata
- `$date$` - Publication date
- `$description$` - Meta description

### Styling (`docs/static/styles.css`)

**Layout:**
- Centered 800px max-width container
- 20px padding, auto margins

**Typography:**
- Font: Open Sans (Google Fonts)
- H1: Raspberry background (#8B1538), white text
- H2-H5: Raspberry text, H2 with bottom border

**Images:**
- Max-width 95%, centered
- Dark gray borders (#333) top and bottom
- Maintains aspect ratio

## Data Flow

### Publishing Workflow

```
1. Write draft → working/YYYY/note.md
2. Add images → working/YYYY/media/
3. Run app.py → Menu option 1
4. Select files to publish
5. Files copied → markdown/YYYY/
6. Images moved/copied → docs/static/media/
7. HTML generated → docs/YYYY/
8. View in browser via Flask server
```

## Configuration

### Constants

**`helper_scripts/convert_markdown.py`:**
- `MARKDOWN_DIR = "markdown"`
- `DOCS_DIR = "docs"`
- `HTML_TEMPLATE_FILE = "docs/static/template.html"`

**`helper_scripts/publish_note.py`:**
- `WORKING_DIR = "working"`
- `MARKDOWN_DIR = "markdown"`
- `STATIC_MEDIA_DIR = "docs/static/media"`

## Dependencies

**Python:**
- Flask 3.0.0

**External:**
- Pandoc (document conversion)

## Development Workflow

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

### Adding New Field Notes

1. Create `working/YYYY/note.md` with YAML front matter
2. Add images to `working/YYYY/media/`
3. Run `python app.py` (interactive menu)
4. Select option 1 (Publish and convert)
5. Select files to publish
6. Preview at `http://127.0.0.1:5000/`

### Command Line Options

```bash
python app.py              # Interactive menu (default)
python app.py --serve      # Start server directly
python app.py --convert-all # Convert all markdown
python app.py --help       # Show help
```

## Deployment

**Target:** GitHub Pages

**Process:**
1. Push `docs/` directory contents to GitHub
2. Configure GitHub Pages to serve from root or docs folder
3. Static HTML files served directly by GitHub

**Benefits:**
- No server maintenance
- Free hosting
- Automatic HTTPS
- Version control integration

## Known Limitations

- Static site only (no dynamic content)
- Manual publishing workflow required
- Single template design
- No search functionality
- Image processing requires local workflow