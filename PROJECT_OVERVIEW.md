# Field Notes - Project Overview

## Project Name
**Field Notebook**

## Project Description

The project contains the workflow for the development of the Field Notebook.

## Purpose & Goals

The project serves both as a platform for writing and the writing itself.

### Platform goal

The platform goal is to serve as a platform for writing - the end game is a simple system to enable concise and efficient writing to be published regulary.

### Field notebook goal

Notes to my future self, publicly available.

The entry should be interesting to me, if I read it 6 months from now. I'd like others to benefit from reading the entries, but this is a secondary goal.

This is the platform for writing - all writing is focused here, not sprawled elsewhere to use cognitive budget efficiently.

There's no restriction on entry length (long or short).

## Key Features

Workflow generally follows "docs as code" concepts.

### Current features and workflow

- Write notebook entries in Markdown in the `working` directory.
- Use Markdown heading structure and one journal template defined in the HTML template and CSS file.
- Convert Markdown to HTML via a Python script and is previewed with Flask.
- Copy final draft files to the pages directory.
- Push to Github pages for hosting and sharing.

### Core Technologies

- **Language:** Python 3.x
- **Web Framework:** Flask
- **Templating:** Pandoc
- **Styling:** CSS

### Dependencies

- Flask
- Pandoc (external)

## Project Status

- [x] Concept/Planning
- [ ] Early Development
- [ ] MVP Complete

## Success Metrics

- Limited friction to publishing - measure by number of times the workflow (not the writing itself) limits publishing
- Published entries are readable without basic distractions - measure by no dead links, font, heading consistency, no "placeholders"

## Constraints & Limitations

### Known Limitations

- Dynamic webpage behavior
- Template choices for entries

### Technical Constraints

- Static webpages only on Github pages
- Repo size (~ 1 GB) on Github with a free account

## Future Vision

[TO BE COMPLETED: Where do you see this project in 6-12 months?]

## License

#TO BE COMPLETED: What license is this project under?

## Contact & Support

#TO BE COMPLETED: How can users get help or provide feedback?

Feedback accepted and in some cases solicitated, but no direct contributions