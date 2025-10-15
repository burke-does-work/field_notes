# Field Notes - Project Overview

PROJECT_OVERVIEW.md = what and why, ARCHITECTURE.md = how and technical details.

## Project Name

**Field Notebook**

## Project Description

Platform for writing and publishing field notes as markdown files converted to styled HTML pages.

## Purpose & Goals

### Platform goal

Simple system for efficient writing and regular publishing with minimal friction.

### Field notebook goal

Notes to my future self, publicly available. Each entry should be interesting six months later. Benefit to others is secondary.

All writing is focused here to use cognitive budget efficiently. No restriction on entry length.

## Key Features

**Publishing workflow:**
- Draft in `working/`, publish to `markdown/`, convert to HTML in `docs/`
- Interactive CLI with metadata validation
- Automatic image handling and path updates

**Styling:**
- Centered layout with Open Sans typography
- Raspberry-colored headings
- Responsive images with borders

**Technologies:**
- Python/Flask for workflow and development server
- Pandoc for markdown conversion
- GitHub Pages for hosting

## Project Status

- [x] Concept/Planning
- [x] Early Development
- [x] MVP Complete

**Completed:**
- Publishing workflow (working → markdown → docs)
- Flask routing and development server
- Styling system with responsive layout
- Image handling and path management
- Interactive CLI menu system

## Success Metrics

**Primary:**
- Publishing friction: Workflow enables quick note publishing
- Readability: Consistent formatting, no dead links, clean styling

**Achieved:**
- Single command publishing workflow
- Automated image and path management
- Professional, consistent styling
- Local preview before deployment

## Constraints & Limitations

- Static site only
- Single template design
- Requires local Pandoc installation
- GitHub Pages repository size limit (~1 GB)

## Style Guidelines

**Voice:** First-person ("I") and imperative (not "you")
**Commits:** Conventional Commits format
**Code:** PEP8 for Python
**Markdown:** See MARKDOWN_STYLE_GUIDE.md
**Language:** American English, Buzzfeed → AP → Chicago style hierarchy

## License

#TO BE COMPLETED: What license is this project under?

## Contact & Support

#TO BE COMPLETED: How can users get help or provide feedback?

Feedback accepted and in some cases solicitated, but no direct contributions