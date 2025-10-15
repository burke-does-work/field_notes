# Markdown Style Guide

Based on:

- [VS Code markdownlint extension](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md)
- [CommonMark](https://spec.commonmark.org/0.31.2/)

If not specified in the document, default to CommonMark, then to the markdownlint extension.

## Headings

### Capitalization

#### H1 (Title Case)

Capitalize each word, except for articles, conjunctions, or prepositions, unless they start the heading or are after a dash or semicolon.

Examples:

- Field Notes - Technical Architecture
- The Quick Brown Fox Jumps Over the Lazy Dog
- Publishing Workflow: A Guide for Writers

#### H2-H5 (Sentence Case)

Only capitalize the first word of the heading or any word after a dash or a semicolon.

Examples:

- Publishing workflow
- Core technologies
- Publishing workflow: A guide for writers
- Image handling and path management

### Formatting

- Use only the heading tags for headings. Do not use other formatting (such as bold) for a heading. Where I don't want a formatted heading, use plan text with a colon.
- Heading levels should only increment by one level at a time.
- The title in the YAML front matter is the same as heading 1

## Lists

- Single space between the list block and the text above and below.
- Unordered lists use "-" or a bullet. Do not mix in "*", for example.

## Additional

All documents should end with a new line.