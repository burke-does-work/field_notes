
## Voice

### TL;DR

For field_notes, use a combination of first-person ("I") and the imperative. Don't use second-person("you").

Use "recommend" when there are multiple, viable options but one is preferred but till don't use "you".

Don't use passive voice.

### My psychology

I prefer not being told what to do, and so I don't want to tell others what to do.

I'm comfortable using the imperative for my future self. Even if "you" can be directed at my future self, I'd rather avoid the confusion if others read the email and interpret it as telling them what to do.

### Usage in technical documentation

In technical documentation it's common to use "you". For example, in the Flask documentation on the installation: "Create a project folder and a .venv folder within..."

They also use "we recommend". "We recommend" appears to be used when there are options, even if one options is best. For example: "We recommend using the latest version of Python. Flask supports Python 3.9 and newer."

And then they mix it up with "you may choose", a combo of the two: "You may choose to use gevent or eventlet with your application. In this case, greenlet>=1.0 is required. When using PyPy, PyPy>=7.3.7 is required."

### My preferences

Don't use passive voice, even if this softens the directions. I'm not writing to others so I don't need to keep it soft.

When using "recommends", use it in a declarative sentence. A declarative sentence is a sentence that states a fact, opinion, or an idea and is the most common sentence type in English. For example: "I recommend using the latest version of Flask". Grammar breakdown:

- Subject = We
- Verb = recommend
- Object = using the latest version of Flask

When avoiding "you", don't replace it with formal tone, from most formal to still formal: "one", "a person", or "those who". Good options (not sure which I want to use yet":

"Anyone..."

- Most conversational and good for tutorials or blog-style docs
- For example: "Anyone setting this up for the first time might run into permission errors."

"People.."

- Very conversational and feels like I'm explaining something out loud
- Example: "People usually install Flask with pip, not from source."

"<role based>"

- Clear and context specific
- Examples: "the user...", "most devs..."

## Style guides

### Code

Python: PEP8
Markdown: [Field Notebook - Markdown Style Guide](MARKDOWN_STYLE_GUIDE.md)

#TO BE COMPLETED: linters and spell checkers

### Documentation

Function doc strings: [Google Python Style Guide: Comments and Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)

Commits: [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)

### Language

Use these style guides in the following order:

- [Buzzfeed Style Guide](https://www.buzzfeed.com/buzzfeednews/buzzfeed-style-guide)
- [Associated Press Stylebook](https://www.apstylebook.com/)
- [Chicago Manual of Style](https://www.chicagomanualofstyle.org/home.html)

Use American English but vocabulary is flexible (e.g. Australianisms are not flagged in the style check).

