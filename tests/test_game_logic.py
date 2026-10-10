# tests/test_game_logic.py

from logic_utils import check_guess, update_score, parse_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_update_score_win_first_attempt():
    # Winning on the first attempt should give 100 points
    new_score = update_score(current_score=0, outcome="Win", attempt_number=1)
    assert new_score == 100


def test_update_score_win_late_attempt_minimum():
    # Winning late should still give at least 10 points
    new_score = update_score(current_score=0, outcome="Win", attempt_number=20)
    assert new_score == 10


def test_update_score_wrong_guess():
    # Wrong guesses should subtract 5 points
    new_score = update_score(current_score=50, outcome="Too High", attempt_number=3)
    assert new_score == 45


def test_parse_guess_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None


def test_parse_guess_invalid_input():
    ok, value, err = parse_guess("not-a-number")
    assert ok is False
    assert value is None
    assert err == "That is not a number."
