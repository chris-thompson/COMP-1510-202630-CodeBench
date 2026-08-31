"""
Demonstrate how to dump JSON into a string.

We use dump(s) which is easy to remember because of the s for string.

We do this when we want to create a JSON object in string-format. We
often need to do this when passing JSON information from server to client
on the web!

Note the last line of output. Python writes None, but JSON has no None: it
uses null instead. The json module translates between the two for us in
both directions, so we never have to think about it.
"""

import json


def main():
    """
    Drive the program.
    """
    word_count = {'the': 42, 'and': 37}
    string_version = json.dumps(word_count)
    print(type(string_version))
    print(string_version)

    # Python's None becomes JSON's null on the way out.
    cat = {'name': 'Zofia', 'isCat': True, 'miceCaught': 0, 'felineIQ': None}
    print(json.dumps(cat))


if __name__ == "__main__":
    main()
