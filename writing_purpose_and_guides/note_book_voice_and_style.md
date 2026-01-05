# Voice and style

## TL;DR

For field_notes, use a combination of first-person ("I") and the imperative. Don't use second-person("you").

Use "recommend" when there are multiple, viable options but one is preferred but till don't use "you".

Don't use passive voice.

## Directions to my future self

I'm comfortable using the imperative for my future self. Even if "you" can be directed at my future self, I'd rather avoid the confusion if others read the email and interpret it as telling them what to do.

### Recommend

I use "recommend" when there are multiple, viable options but one is preferred. When using "recommends", use it in a declarative sentence. A declarative sentence is a sentence that states a fact, opinion, or an idea and is the most common sentence type in English.

For example: "I recommend using the latest version of Flask". Grammar breakdown:

- Subject = We
- Verb = recommend
- Object = using the latest version of Flask

### Alternatives to "you"

When avoiding "you" but can't use "I" or the imperative, don't replace it with formal tone like "one". I can't always just speak to and about future self. "A person" works well enough instead of "you". Other reasonable options:

"Anyone..."

- Most conversational and good for tutorials or blog-style docs
- For example: "Anyone setting this up for the first time might run into permission errors."

"People.."

- Very conversational and feels like I'm explaining something out loud
- Example: "People usually install Flask with pip, not from source."

"<role based>"

In certain context, addressing a user group works too, such as "developers", "software users", etc.


- Works well in certain contexts when the group is specific
- Examples: "the user...", "most devs..."

### Usage in technical documentation

In technical documentation it's common to use "you". For example, in the Flask documentation on the installation: "Create a project folder and a `.venv` folder within..."

They also use "we recommend". "We recommend" appears to be used when there are options, even if one options is best. For example: "We recommend using the latest version of Python. Flask supports Python 3.9 and newer."

And then they mix it up with "you may choose", a combo of the two: "You may choose to use `gevent` or `eventlet` with your application. In this case, `greenlet>=1.0` is required. When using `PyPy`, `PyPy>=7.3.7` is required."

## Conjunctions

I prefer conjunctions, unless there's a good reason not to use one.

## Passive voice

Don't use passive voice, even if this softens the directions. I'm not writing to others so I don't need to keep it soft.

## Acronyms

Always include the full word or phrase in parenthesis, unless the acronym is well known to the general population.

- Example of when to include the full word or phrase: when using the acronym SDLC, write: "SDLC (Software Development Life Cycle)" or "Software Development Life Cycle (SDLC)".
- Example when full word or phrase isn't included: when using the acronym JFK, no need to write "JFK (John F. Kennedy)", just write "JFK".

## Style guides

### Prose

We use the following style guides in the order provided:

1. [Buzzfeed style guide](https://www.buzzfeed.com/buzzfeednews/buzzfeed-style-guide)
2. Associated Press Style Book
3. The Chicago Manual of Style

### Code

- Python: [Python PEP 8](https://peps.python.org/pep-0008/) using an 80 character limit
- SQL: Mozilla
- Chinese language: [The China Story Style Guide](https://www.thechinastory.org/submission-guide/style-guide/)

Markdown: See [Field Notebook - Markdown Style Guide](MARKDOWN_STYLE_GUIDE.md)

### Documentation

Function doc strings: [Google Python Style Guide: Comments and Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)

Commits: [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)

### Language

Use these style guides in the following order:

- [Buzzfeed Style Guide](https://www.buzzfeed.com/buzzfeednews/buzzfeed-style-guide)
- [Associated Press Stylebook](https://www.apstylebook.com/)
- [Chicago Manual of Style](https://www.chicagomanualofstyle.org/home.html)

Use American English but vocabulary is flexible (e.g. Australian-isms are not flagged in the style check).

## Styling

See CSS file for specifics. Summary:

- Centered layout with Open Sans typography
- Raspberry-colored headings
- Responsive images with borders
