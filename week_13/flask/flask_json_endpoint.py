"""
A web page doesn't have to return HTML. APIs usually return JSON instead,
so other programs (not browsers) can read the response.

To use this: run the app, then visit
http://127.0.0.1:5000/api/greeting?name=Ada in a browser, or fetch it
with requests.get(...).json() from another program.
"""

from flask import Flask, Response, jsonify, request

app = Flask(__name__)


@app.route('/api/greeting')
def greeting() -> Response:
    """
    Return a greeting as JSON rather than as a page.

    jsonify turns a dictionary into a JSON response and sets the content
    type, so whatever reads this knows it is receiving JSON and not HTML.

    :precondition: this function must be called by Flask while it is
                   handling a request
    :return: a Flask Response whose body is a JSON object with the
             keys "message" and "name"
    """
    name = request.args.get('name', 'World')
    return jsonify({'message': f'Hello, {name}!', 'name': name})


if __name__ == '__main__':
    app.run(debug=True)
