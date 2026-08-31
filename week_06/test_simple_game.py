"""
Unit-test simple_game with pytest.

simple_game reads input, uses random.randint, and prints its result, so we
combine two techniques: monkeypatch to supply predictable input and a
predictable secret number, and the capsys fixture to capture what the game
printed. Each fake input pops its answers from a list, so every call to
input returns the next answer in order. The three tests cover the three
branches: a correct guess, a guess that is too low, and a guess that is
too high.
"""

from week_06.simple_game import simple_game


def test_simple_game_correct_guess(monkeypatch, capsys):
    answers = ["1", "10", "5"]

    def fake_input(prompt=""):
        return answers.pop(0)

    def fake_randint(low, high):
        return 5

    monkeypatch.setattr("builtins.input", fake_input)
    monkeypatch.setattr("random.randint", fake_randint)
    simple_game()
    assert capsys.readouterr().out == "You're right!\n"


def test_simple_game_guess_too_low(monkeypatch, capsys):
    answers = ["1", "10", "5"]

    def fake_input(prompt=""):
        return answers.pop(0)

    def fake_randint(low, high):
        return 6

    monkeypatch.setattr("builtins.input", fake_input)
    monkeypatch.setattr("random.randint", fake_randint)
    simple_game()
    assert capsys.readouterr().out == "Too low, the number was 6\n"


def test_simple_game_guess_too_high(monkeypatch, capsys):
    answers = ["1", "10", "5"]

    def fake_input(prompt=""):
        return answers.pop(0)

    def fake_randint(low, high):
        return 4

    monkeypatch.setattr("builtins.input", fake_input)
    monkeypatch.setattr("random.randint", fake_randint)
    simple_game()
    assert capsys.readouterr().out == "Too high, the number was 4\n"
