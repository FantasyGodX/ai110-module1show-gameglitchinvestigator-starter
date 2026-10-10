# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- Game Purpose
The game is a simple number‑guessing challenge where the user tries to guess a randomly generated secret number within a limited number of attempts. The game provides hints (“Too High” or “Too Low”), tracks score, and ends when the user wins or runs out of attempts.

- Bugs Found:

Hint messages contradicted the actual outcome.
Secret number switched between int and str, causing inconsistent comparisons.
Score increased on some wrong guesses due to parity‑based logic.
New Game reset the secret to a 1–100 range regardless of difficulty.
Attempts started at 0, breaking the “Attempts left” display.
Secret number sometimes changed mid‑game.
- Fixes Applied:

Refactored all logic into logic_utils.py for testability.
Rewrote check_guess to use consistent integer comparison and correct hint direction.
Simplified scoring to predictable rules.
Ensured secret number respects difficulty range.
Reset attempts, score, history, and status properly on New Game.
Updated UI text to reflect actual difficulty range.
Added comprehensive pytest tests.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User selects Normal difficulty (range 1–100, 8 attempts).
2. App displays the correct range and attempts left.
3. User enters 40.
   Secret is 50.
   Game returns: Too Low — 📈 Go HIGHER!
   Score: −5
4. User enters 70.
   Game returns: Too High — 📉 Go LOWER!
   Score: −10
5. User enters 50.
   Game returns: Win — 🎉 Correct!
   Balloons appear.
   Score: 100 − 10*(attempt−1) = 80
6. Game status becomes won, blocking further guesses.
7. User clicks New Game 🔁.
   Secret, attempts, score, and history reset correctly according to difficulty.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
============================= test session starts =============================
collected 8 items

tests/test_game_logic.py ........                                      [100%]

============================== 8 passed in 0.12s =============================

```
