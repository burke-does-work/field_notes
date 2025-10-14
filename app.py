from flask import Flask, render_template
from helper_scripts.convert_markdown import convert_all_markdown_files

# Initialize the Flask application
app = Flask(__name__)

# TODO: Determine the routing structure for serving multiple field notes
# TODO: Create an index page that lists all available field notes
# Define the root ("/") route
@app.route("/")
def home():
    # Convert all markdown files to HTML before serving the page
    convert_all_markdown_files()

    # TODO: Update to serve the actual homepage (pages/index.html)
    # Render the homepage
    return render_template('index.html')

if __name__ == "__main__":
    # Convert all markdown files to HTML when the app starts
    convert_all_markdown_files()

    # Run the Flask application in debug mode
    app.run(debug=True)
