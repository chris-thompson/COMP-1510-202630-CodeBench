"""
Unit-test a function that prints, using pytest.

my_printer writes to standard output with print. To check what it printed,
we use the built-in capsys fixture ("capture system output"). After the
function runs, capsys.readouterr() hands back an object whose .out attribute
holds everything that was printed, so we can assert on it.
"""

from week_06.function_that_uses_print import my_printer


def test_my_printer_writes_value_and_newline(capsys):
    my_printer("Hello world!")
    captured = capsys.readouterr()
    assert captured.out == "Hello world!\n"
