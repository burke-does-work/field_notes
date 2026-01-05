# Field Notes - Project Overview

**Doc purpose:** Overview of scripts (for writing, see [writing_guides](./writing_guides/)

PROJECT_OVERVIEW.md = what and why, ARCHITECTURE.md = how and technical details.

## Project name

**Field Notes**

## Project description

Field notes are notes to myself, made publicly available.

This is a platform for writing and publishing field notes. Field notes are written as markdown files, converted to styled HTML pages, and published to Github Pages.

## Purpose & goals

### Platform goal

Simple system for efficient writing and regular publishing with minimal friction.

### Field notes goal

Each note is to still be of interest to me in 6 months, while any benefit from publishing is secondary.

Focuses writing here to use my cognitive budget efficiently and to track productivity.

## Key features

### Publishing workflow

- Draft in `working/`, publish to `markdown/`, convert to HTML in `docs/`
- Interactive CLI with metadata validation
- Automatic image handling and path updates

### Technologies

- Python/Flask for workflow and development server
- Pandoc for markdown conversion
- GitHub Pages for hosting

## Project status

MVP complete.

- Publishing workflow (working → markdown → docs)
- Flask routing and development server
- Styling system with responsive layout
- Image handling and path management
- Interactive CLI menu system

## Success metrics

- Publishing friction: Workflow enables quick note publishing
- Readability: Consistent formatting, no dead links, clean styling, etc.

### Achieved

- Single command publishing workflow
- Automated image and path management
- Local preview before deployment

## Constraints & limitations

- Static site
- Single template design
- GitHub Pages repository size limit (~1 GB)
- Unordered index (e.g. no use of tags)

## License

#TODO: What license is this project under?
