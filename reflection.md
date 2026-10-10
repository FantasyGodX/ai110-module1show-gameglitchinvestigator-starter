# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The first time I ran the game, it looked playful and polished, but the behavior was clearly off. The hint messages were misleading: when my guess was higher than the secret, the game sometimes told me to go “HIGHER” instead of “LOWER.” The score also changed in strange ways, sometimes increasing after a wrong guess and sometimes decreasing unpredictably. On top of that, the secret number was occasionally treated as a string, which caused inconsistent comparisons and made the game feel random rather than logical. The attempt counter and “Attempts left” display also didn’t line up with how many guesses I had actually made.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess: 60, Secret: 50 | Hint: "Too High" and message telling me to go LOWER | Outcome said "Too High" but message told me to go HIGHER | none |
| Guess: 40, Secret: 50 | Hint: "Too Low" and message telling me to go HIGHER | Outcome said "Too Low" but message told me to go LOWER | none |
| New Game button on Hard difficulty | Secret and attempts reset using Hard range and limit | Secret reset to a 1–100 range and attempts started at 0, breaking the difficulty settings | none |
| Multiple wrong guesses | Score should steadily decrease by a predictable amount | Score sometimes increased on certain attempts due to parity-based scoring | none |

---

## 2. How did you use AI as a teammate?

I used Claude as my main AI teammate on this project, both inside VS Code and in chat. One helpful suggestion was to move the core game logic functions (`get_range_for_difficulty`, `parse_guess`, `check_guess`, and `update_score`) out of `app.py` into `logic_utils.py` so they could be tested independently. I accepted that suggestion and verified it by running pytest and confirming that the tests passed and the Streamlit app still behaved correctly.

Another suggestion from the AI was to keep the original parity-based scoring logic, where some “Too High” guesses added points and others subtracted them. I decided not to accept that as written because it made the game feel unfair and hard to reason about. Instead, I simplified the scoring to subtract 5 points for every wrong guess and award a decreasing but bounded amount for a win. I verified my version by running the game manually, watching the score change after each guess, and confirming the behavior with targeted pytest cases.

---

## 3. Debugging and testing your fixes

I considered a bug “really fixed” only after both the automated tests and the live game behavior matched my expectations. For example, after fixing the hint logic in `check_guess`, I wrote tests that checked both the outcome (“Too High” or “Too Low”) and the text of the hint message to ensure they were consistent. I also played through several full games at different difficulties to confirm that the secret stayed in range, the attempts counter behaved correctly, and the score updated predictably. AI helped me design some of these tests by suggesting edge cases, like winning on a very late attempt and validating that the minimum score bonus still applied.

---

## 4. What did you learn about Streamlit and state?

I learned that Streamlit reruns the script from top to bottom on almost every user interaction, which means you can’t rely on normal global variables to track game progress. Instead, you use `st.session_state` to store values like the secret number, attempts, score, and game status so they persist across reruns. To explain this to a friend, I’d say: “Every time you click a button, Streamlit replays your code, but `session_state` is like a backpack that carries your important variables from one run to the next.” Understanding this made it much easier to reason about when and how to reset the game.

---

## 5. Looking ahead: your developer habits

One habit I want to reuse in future projects is writing small, focused tests immediately after fixing a bug, especially for logic that looks deceptively simple. It forced me to think clearly about inputs, outputs, and edge cases instead of just trusting that the code “felt right.” Next time I work with AI on a coding task, I’ll be more deliberate about asking for explanations of proposed changes rather than just accepting large refactors, so I stay in control of the design. This project made me see AI-generated code as a starting point rather than a finished product: it can be fast and creative, but it still needs human judgment, testing, and sometimes rejection to become reliable.
