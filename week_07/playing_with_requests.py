"""
Playing with the requests module.

The requests module is not included when we install Python. We have to
install it separately. If you mouse over the import statement, you'll
notice requests is underlined in curly red. PyCharm will ask you if you
want it to install the requests module. Say yes.

The requests module makes HTTP requests. We will learn how to use it
properly in Week 9 -- this week it is our example of installing a
third-party package from PyPI with pip3.
"""

import requests


def download_page(url: str) -> str:
    """
    Download the document at url and return its text.

    :param url: a str containing a well-formed URL
    :precondition: url points to a reachable text document
    :postcondition: an HTTP GET request is sent to url
    :return: the body of the response as a str
    """
    response = requests.get(url)
    return response.text


def main():
    """
    Drive the program.
    """
    url = 'https://www.gutenberg.org/files/28054/28054-0.txt'
    contents = download_page(url)
    print('Number of characters downloaded:', len(contents))
    print(contents[:250])  # prints the first 250 characters


if __name__ == "__main__":
    main()
