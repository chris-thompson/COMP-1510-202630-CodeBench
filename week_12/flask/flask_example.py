from flask import Flask, request

"""
To use this:

1. Ensure you have installed flask using pip3 or PyCharm
2. Run the app
3. Examine the output in the terminal and click the link to open your browser
4. You're using flask, a micro-framework, Harry!
5. Use control-C to shut down the server.
6. So easy.  You're a back-end programmer now, Harry!
"""

app = Flask(__name__)


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {name}!'

if __name__ == "__main__":
    # Start the dev server
    app.run(debug=True)
