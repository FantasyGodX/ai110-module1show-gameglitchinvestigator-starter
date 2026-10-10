# logic_utils.py

def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    # Default to Normal range if something unexpected happens
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        # Allow decimal input but convert to int
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # Core logic refactored from app.py with fixed hints.
    # AI initially mixed up the hint messages and tried to
    # compare strings and ints; this version keeps it simple
    # and testable.
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        # Guess is higher than secret → user should go LOWER
        return "Too High", "📉 Go LOWER!"
    else:
        # Guess is lower than secret → user should go HIGHER
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """
    Update score based on outcome and attempt number.

    - Win: start at 100 and subtract 10 per attempt, but never below 10.
    - Wrong guesses: subtract 5 points per attempt.
    """
    # AI originally had asymmetric scoring and odd parity rules.
    # This version is simpler, predictable, and easy to test.
    if outcome == "Win":
        points = 100 - 10 * (attempt_number - 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome in ("Too High", "Too Low"):
        return current_score - 5

    return current_score
