
import random

WORD_BANK = [
    # Programming
    ("PYTHON",      "Programming Language"),
    ("VARIABLE",    "Programming Concept"),
    ("FUNCTION",    "Programming Concept"),
    ("ALGORITHM",   "Computer Science"),
    ("DATABASE",    "Computer Science"),
    ("COMPILER",    "Computer Science"),
    ("RECURSION",   "Programming Concept"),
    ("ITERATOR",    "Programming Concept"),
    ("EXCEPTION",   "Programming Concept"),
    ("BOOLEAN",     "Data Type"),
    # Engineering
    ("VOLTAGE",     "Electronics"),
    ("CIRCUIT",     "Electronics"),
    ("RESISTOR",    "Electronics"),
    ("TRANSISTOR",  "Electronics"),
    ("FREQUENCY",   "Physics"),
    ("AMPLITUDE",   "Physics"),
    # General
    ("KEYBOARD",    "Computer Hardware"),
    ("MONITOR",     "Computer Hardware"),
    ("NETWORK",     "Computer Science"),
    ("SOFTWARE",    "Computer Science"),
    ("HARDWARE",    "Computer Science"),
    ("INTERNET",    "Technology"),
    ("BROWSER",     "Technology"),
    ("FRAMEWORK",   "Programming"),
    ("LIBRARY",     "Programming"),
]

MAX_WRONG_ATTEMPTS = 6    
class HangmanGame:

    def start_new_game(self) -> dict:
        """Pick a random word and return a fresh game state."""
        word, category = random.choice(WORD_BANK)
        return self._build_initial_state(word, category)

    def process_guess(self, state: dict, letter: str) -> dict:

        state = dict(state)   

        if state["game_over"] or letter in state["guessed_letters"]:
            return state

        state["guessed_letters"].append(letter)

        if letter in state["word"]:
            state["correct_letters"].append(letter)
            state["last_guess_correct"] = True
        else:
            state["wrong_letters"].append(letter)
            state["wrong_count"] += 1
            state["last_guess_correct"] = False

        state["display_word"] = self._build_display_word(
            state["word"], state["correct_letters"]
        )

        state = self._check_game_over(state)
        return state