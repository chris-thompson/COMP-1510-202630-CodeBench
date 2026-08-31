"""
Building HTML with f-strings gets messy fast. Jinja2 templates (the
templating engine Flask uses) keep HTML in its own file, with {{ }} for
values and {% %} for logic. Flask looks for templates in a "templates"
folder beside this file.

To use this: run the app, then visit
http://127.0.0.1:5000/greet/Ada in a browser.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/greet/<name>')
def greet(name: str) -> str:
    """
    Render the greeting template for a name taken from the URL.

    The <name> in the route is a placeholder, so visiting /greet/Ada
    calls this function with name set to "Ada".

    :param name: a string
    :precondition: name must be the string Flask captured from the URL
    :precondition: this function must be called by Flask while it is
                   handling a request
    :return: the rendered HTML of greeting.html as a string
    """
    return render_template('greeting.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
