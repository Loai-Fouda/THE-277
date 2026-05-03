
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
    
    def use_hint(self, state: dict) -> dict:

        state = dict(state)

        if state["game_over"] or state["hints_used"] >= 2:
            return state 

        hidden = [
            ch for ch in state["word"]
            if ch not in state["correct_letters"]
            and ch not in state["wrong_letters"]
            and ch.isalpha()
        ]
        if not hidden:
            return state

        hint_letter = random.choice(hidden)
        state["hints_used"] += 1

        state["correct_letters"].append(hint_letter)
        state["guessed_letters"].append(hint_letter)
        state["display_word"] = self._build_display_word(
            state["word"], state["correct_letters"]
        )
        state["hint_letter"] = hint_letter
        state = self._check_game_over(state)
        return state
    


    def _build_initial_state(self, word: str, category: str) -> dict:
        return {
            "word":              word,
            "category":          category,
            "display_word":      self._build_display_word(word, []),
            "guessed_letters":   [],
            "correct_letters":   [],
            "wrong_letters":     [],
            "wrong_count":       0,
            "max_wrong":         MAX_WRONG_ATTEMPTS,
            "game_over":         False,
            "player_won":        False,
            "last_guess_correct": None,
            "hints_used":        0,
            "hint_letter":       None,
        }

    @staticmethod
    def _build_display_word(word: str, correct_letters: list) -> list:

        return [ch if ch in correct_letters else "_" for ch in word]

    @staticmethod
    def _check_game_over(state: dict) -> dict:

        all_revealed = "_" not in state["display_word"]

        if all_revealed:
            state["game_over"] = True
            state["player_won"] = True
        elif state["wrong_count"] >= state["max_wrong"]:
            state["game_over"] = True
            state["player_won"] = False

        return state