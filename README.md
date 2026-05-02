# Hangman Game — MNU AIE

> A web-based Hangman game built with **Python + Flask** for the  


# Team Members

| # |Name                | Student ID |
|---|--------------------|------------|
| 1 | [Loai-Fouda]       | [24040190] |
| 2 | [Karim-Mohamed]    | [24040800] | 
| 3 | [Ahmed-aboelmaged] | [24040814] | 
| 4 | [Mohamed-yasser]   | [24040247] | 
| 5 | [Kareem-Elgamal]   | [24040390] | 
| 6 | [Mahmoud-Sameh]    | [24040423] | 
| 7 | [Ahmed-mohamed]    | [24040325] |


#  Project Description

A fully-featured Hangman game where players guess a hidden word letter by letter before the hangman is drawn.  
The word bank is themed around **programming and engineering** vocabulary — great for AIE students!

#  Features
-  Random word selection from 25+ curated words
-  Clean, responsive terminal-aesthetic UI
-  On-screen keyboard + physical keyboard support
-  Animated SVG hangman figure (6 stages)
-  Hint system (2 hints per game)
-  Category clue shown for each word
-  Win/Lose overlay with play-again option

---

#  Technologies Used

| Technology | Purpose |
|------------|---------|
| Python     | Core game logic |
| Flask      | Web server & routing |
| HTML       | Page structure |
| CSS3       | Styling, animations |
| JavaScript | UI interactivity, API calls |

---

##  How to Run

```bash
git clone https://github.com/YOUR_USERNAME/hangman-mnu-2026.git
```


###  Install dependencies
```bash
pip install -r requirements.txt
```

###  Run the app
```bash
python app.py
```

###  Open in browser
```bash
http://localhost:5000
```

---

##  Project Structure

```
hangman_project/
│
├── app.py                  Flask routes & session
├── game.py                 Game logic & word engine
├── requirements.txt        Python dependencies
├── README.md               Documentation
│
├── templates/
│   └── index.html          HTML structure
│
└── static/
    ├── css/
    │   └── style.css       Styling
    └── js/
        └── game.js         Interactivity
```


## How to Play

1. Click **NEW GAME** to start
2. Guess letters by clicking the on-screen keyboard (or type on your physical keyboard)
3. You have **6 wrong attempts** before the game ends
4. Use the **HINT** button (max 2 per game) to reveal a random letter
5. The **category** shown above the word gives you a clue

