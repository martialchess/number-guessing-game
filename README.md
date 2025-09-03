# Number Guessing Game

A simple Python console game where the player tries to guess a randomly chosen number between 1 and 100.  
The game provides hints ("Too high!" / "Too low!") and limits the number of guesses based on the selected difficulty.

---

## Features
- Randomly generated number between **1–100**.
- Two difficulty levels:
  - **Easy** → 10 guesses
  - **Hard** → 5 guesses
- Input validation (rejects invalid or out-of-range guesses).
- Feedback after every guess:
  - "Too high, try again!"
  - "Too low, try again!"
  - "Congratulations!" when guessed correctly.
- Game Over screen when guesses run out (reveals the correct number).
- Replay option at the end.

---

## Concepts Covered
- Functions and reusable logic
- While loops
- If/elif/else decision making
- Random number generation (`random.randint`)
- Dictionaries (for ASCII logo import)
- Input validation with `try/except`
- Recursion (restart game)

---

## How to Play
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/number-guessing-game.git

2. Navigate to the project folder:

cd number-guessing-game


3. Run the game:

python main.py


4. Choose your difficulty and start guessing!