# Field Notes - Technical Architecture

## System Overview
[TO BE COMPLETED: Provide a high-level description of how the system works]

This is a Flask-based web application that converts markdown field notes into HTML pages for viewing in a browser.

## Architecture Diagram
[TO BE COMPLETED: Consider adding a diagram showing the system components and their relationships]

```
[User] --> [Flask App] --> [Pandoc] --> [HTML Pages]
                |
                v
          [Static Assets]
```

## Directory Structure

```
field_notes/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── markdown/                   # Source markdown files
│   └── 2025/                  # Organized by year
│       └── [field-notes].md   # Individual field notes
├── pages/                      # Generated HTML output
│   └── 2025/                  # Mirrors markdown structure
│       └── [field-notes].html # Converted HTML files
├── static/                     # Static assets
│   ├── template.html          # Pandoc HTML template
│   ├── styles.css             # Application styles
│   └── media/                 # Images and other media
└── working/                    # [TO BE COMPLETED: What is this for?]
```

## Core Components

### 1. Flask Application (`app.py`)

**Purpose:** [TO BE COMPLETED: Describe the role of the Flask app]

**Key Functions:**
- `convert_markdown_to_html_with_pandoc(markdown_file, html_output_file)`
  - [TO BE COMPLETED: Add more details about what this does]

- `convert_all_markdown_files()`
  - Recursively finds all `.md` files in `markdown/` directory
  - Maintains directory structure in `pages/` output
  - [TO BE COMPLETED: Add more details]

**Routes:**
- `GET /` - Homepage
  - [TO BE COMPLETED: What should this display?]
  - Current Status: TODO - needs implementation

[TO BE COMPLETED: Add more routes as they are implemented]

### 2. Markdown Processing

**Input:** Markdown files in `markdown/` directory

**Process:**
1. [TO BE COMPLETED: Describe the conversion process step-by-step]
2. Pandoc converts markdown to HTML using `static/template.html`
3. Output is written to corresponding path in `pages/` directory

**YAML Front Matter Support:**
- `title` - Page title
- `author` - Author name
- `date` - Publication date
- `description` - Meta description
- [TO BE COMPLETED: Add any custom fields]

### 3. HTML Template (`static/template.html`)

**Purpose:** Provides consistent structure for all generated pages

**Features:**
- Responsive meta viewport
- Conditional metadata from YAML front matter
- Links to `styles.css` for styling
- [TO BE COMPLETED: Add more features]

**Variables:**
- `$title$` - From YAML front matter
- `$body$` - Converted markdown content
- `$author$` - Optional author metadata
- `$date$` - Optional date metadata
- `$description$` - Optional description metadata

### 4. Styling (`static/styles.css`)

**Current Status:** [TO BE COMPLETED: Is this file populated?]

**Planned Styles:**
- [TO BE COMPLETED: What styling approach will you use?]
- Typography
- Layout
- Responsive design
- [Add more]

## Data Flow

### Content Publishing Flow
```
1. Write markdown file → markdown/YYYY/filename.md
2. Start Flask app (or reload)
3. app.py runs convert_all_markdown_files()
4. Pandoc processes each .md file
5. HTML output → pages/YYYY/filename.html
6. User accesses via Flask route
```

[TO BE COMPLETED: Add more detail to each step if needed]

## Technology Decisions

### Why Flask?
[TO BE COMPLETED: Why did you choose Flask over other frameworks?]

### Why Pandoc?
[TO BE COMPLETED: Why Pandoc instead of a Python markdown library?]

### Why Static Generation?
[TO BE COMPLETED: Why generate HTML files instead of converting on-the-fly?]

## Configuration

### Environment Variables
[TO BE COMPLETED: List any environment variables]
- Variable 1: Purpose
- Variable 2: Purpose

### Constants (in `app.py`)
- `MARKDOWN_DIR = "markdown"` - Source directory for field notes
- `PAGES_DIR = "pages"` - Output directory for HTML
- `HTML_TEMPLATE_FILE = "static/template.html"` - Pandoc template path

## Dependencies

### Python Dependencies
- **Flask 3.0.0** - Web framework
  - [TO BE COMPLETED: Why this version?]

### External Dependencies
- **Pandoc** - Document converter
  - [TO BE COMPLETED: Minimum version required?]
  - [TO BE COMPLETED: Installation instructions?]

## Development Workflow

### Local Development
[TO BE COMPLETED: How do you run this locally?]
```bash
# Example:
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

### Adding New Field Notes
[TO BE COMPLETED: What's the process for adding a new note?]
1. Create markdown file in `markdown/YYYY/`
2. Add YAML front matter
3. Write content
4. Restart Flask app (in development mode)

## Deployment

### Deployment Strategy
[TO BE COMPLETED: How will this be deployed?]
- [ ] Local only
- [ ] Heroku
- [ ] AWS
- [ ] Other: ___________

### Build Process
[TO BE COMPLETED: Are there any build steps before deployment?]

### Environment Configuration
[TO BE COMPLETED: How do you configure for production vs development?]

## Testing Strategy

### Current Testing
[TO BE COMPLETED: What testing is in place?]
- [ ] Unit tests
- [ ] Integration tests
- [ ] Manual testing

### Testing TODO
[TO BE COMPLETED: What testing needs to be added?]

## Performance Considerations

### Current Performance
[TO BE COMPLETED: How does it perform now?]

### Optimization Opportunities
[TO BE COMPLETED: What could be improved?]
- Caching converted HTML
- Only convert changed files
- [Add more]

## Security Considerations

### Current Security Measures
[TO BE COMPLETED: What security is in place?]

### Security TODO
[TO BE COMPLETED: What security needs to be added?]
- Input validation
- XSS prevention
- [Add more]

## Error Handling

### Current Error Handling
[TO BE COMPLETED: How are errors handled?]
- Pandoc conversion errors are caught and logged
- [Add more]

### Error Handling TODO
[TO BE COMPLETED: What error handling needs to be added?]

## Logging & Monitoring

### Current Logging
[TO BE COMPLETED: What is logged?]
- Successful conversions
- Pandoc errors
- [Add more]

### Monitoring TODO
[TO BE COMPLETED: What monitoring should be added?]

## Outstanding TODOs (from code)

1. **Routing Structure** - Determine how to serve multiple field notes
   - [TO BE COMPLETED: Document the planned approach]

2. **Index Page** - Create homepage that lists all field notes
   - [TO BE COMPLETED: Document the design]

3. **Homepage Template** - Update to serve actual homepage
   - [TO BE COMPLETED: What should it contain?]

## Future Architecture Changes

### Short-term (1-3 months)
[TO BE COMPLETED: What architectural changes are planned soon?]

### Long-term (6-12 months)
[TO BE COMPLETED: What major architectural changes might be needed?]

## Maintenance & Support

### Maintenance Tasks
[TO BE COMPLETED: What regular maintenance is needed?]

### Known Issues
[TO BE COMPLETED: Document any known bugs or issues]

## References & Resources

### Documentation
[TO BE COMPLETED: Links to relevant documentation]
- Flask: https://flask.palletsprojects.com/
- Pandoc: https://pandoc.org/
- [Add more]

### Similar Projects
[TO BE COMPLETED: Any projects that inspired this or that you reference?]
