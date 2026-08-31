"""
GET requests fetch a page. POST requests submit data to it, e.g. from an
HTML form. This file shows both sides: the form, and the route that
reads what the form sends.

To use this: run the app, visit http://127.0.0.1:5000/ in a browser,
type a name, and press the button.
"""

from flask import Flask, request

app = Flask(__name__)

FORM_PAGE = '''
<form method="post" action="/greet">
    <label>Your name: <input type="text" name="name"></label>
    <button type="submit">Greet me</button>
</form>
'''


@app.route('/')
def show_form() -> str:
    """
    Serve the HTML form.

    This is the GET half: the browser asks for the page, and we hand back
    the form for the user to fill in.

    :precondition: this function must be called by Flask while it is
                   handling a request
    :return: the HTML of the form as a string
    """
    return FORM_PAGE


@app.route('/greet', methods=['POST'])
def greet() -> str:
    """
    Greet the name the form submitted.

    This is the POST half. The submitted values arrive in request.form
    rather than in the query string, because a POST carries its data in
    the body of the request instead of in the URL.

    :precondition: this function must be called by Flask while it is
                   handling a request
    :return: a greeting, which Flask sends back as the page
    """
    name = request.form.get('name', 'World')
    return f'Hello, {name}! That came from a POST request.'


if __name__ == '__main__':
    app.run(debug=True)
