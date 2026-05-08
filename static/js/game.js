
const ALPHABET   = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const BODY_PARTS = ["hm-head","hm-body","hm-larm","hm-rarm","hm-lleg","hm-rleg"];


const wordDisplay   = document.getElementById("word-display");
const keyboard      = document.getElementById("keyboard");
const newGameBtn    = document.getElementById("new-game-btn");
const hintBtn       = document.getElementById("hint-btn");
const statusMsg     = document.getElementById("status-msg");
const wrongCount    = document.getElementById("wrong-count");
const hintLeft      = document.getElementById("hint-left");
const categoryBadge = document.getElementById("category-badge");
const attemptBubbles= document.getElementById("attempt-bubbles");
const overlay       = document.getElementById("overlay");
const overlayTitle  = document.getElementById("overlay-title");
const overlayWord   = document.getElementById("overlay-word");
const overlayEmoji  = document.getElementById("overlay-emoji");
const overlayBtn    = document.getElementById("overlay-btn");


let gameActive = false;


buildKeyboard();
startNewGame();   


newGameBtn.addEventListener("click", startNewGame);
overlayBtn.addEventListener("click", () => { hideOverlay(); startNewGame(); });
hintBtn.addEventListener("click", useHint);


document.addEventListener("keydown", (e) => {
  if (!gameActive) return;
  const letter = e.key.toUpperCase();
  if (letter.length === 1 && ALPHABET.includes(letter)) {
    const btn = document.getElementById(`key-${letter}`);
    if (btn && !btn.disabled) btn.click();
  }
});


function buildKeyboard() {
  keyboard.innerHTML = "";
  for (const letter of ALPHABET) {
    const btn = document.createElement("button");
    btn.textContent  = letter;
    btn.id           = `key-${letter}`;
    btn.className    = "key-btn";
    btn.setAttribute("aria-label", `Guess letter ${letter}`);
    btn.addEventListener("click", () => handleGuess(letter));
    keyboard.appendChild(btn);
  }
}


async function startNewGame() {
  gameActive = false;
  setStatus("", "");

  const state = await apiPost("/new_game");
  if (!state) return;

  gameActive = true;
  resetKeyboard();
  renderState(state);
}

async function handleGuess(letter) {
  if (!gameActive) return;

  disableKey(letter, null);

  const state = await apiPost("/guess", { letter });
  if (!state) return;

  renderState(state);


  disableKey(letter, state.correct_letters.includes(letter) ? "correct" : "wrong");

  if (state.last_guess_correct) {
    setStatus(`✔  "${letter}" is in the word!`, "correct");
  } else {
    setStatus(`✘  "${letter}" is not in the word.`, "wrong");
  }
}


async function useHint() {
  if (!gameActive) return;
  const state = await apiPost("/hint");
  if (!state) return;

  renderState(state);

  if (state.hint_letter) {
    disableKey(state.hint_letter, "correct");
    setStatus(`💡 Hint: the letter "${state.hint_letter}" was revealed!`, "hint");
  }


  const remaining = 2 - state.hints_used;
  hintLeft.textContent = `(${remaining} left)`;
  if (remaining <= 0) hintBtn.disabled = true;
}


function renderState(state) {
  renderWordDisplay(state.display_word, state.correct_letters);
  renderHangman(state.wrong_count);
  renderAttemptBubbles(state.wrong_count, state.max_wrong);
  categoryBadge.textContent = `Category: ${state.category}`;
  wrongCount.textContent    = state.wrong_count;

  const remaining = 2 - state.hints_used;
  hintLeft.textContent = `(${remaining} left)`;
  hintBtn.disabled = (remaining <= 0 || state.game_over);

  if (state.game_over) {
    gameActive = false;
    disableAllKeys();
    hintBtn.disabled = true;

    setTimeout(() => {
      if (state.player_won) {
        showOverlay("🎉", "YOU WIN!", `The word was: ${state.word}`, true);
      } else {
        showOverlay("💀", "GAME OVER", `The word was: ${state.word}`, false);
      }
    }, 600);
  }
}


function renderWordDisplay(displayWord, correctLetters) {
  wordDisplay.innerHTML = "";
  displayWord.forEach(ch => {
    const tile = document.createElement("div");
    tile.className = "letter-tile";
    if (ch !== "_") {
      tile.textContent = ch;
      tile.classList.add("revealed");
    }
    wordDisplay.appendChild(tile);
  });
}


function renderHangman(wrongCount) {
  BODY_PARTS.forEach((id, index) => {
    const el = document.getElementById(id);
    if (!el) return;
    if (index < wrongCount) {
      el.classList.remove("hidden");
    } else {
      el.classList.add("hidden");
    }
  });
}


function renderAttemptBubbles(wrongCount, maxWrong) {
  attemptBubbles.innerHTML = "";
  for (let i = 0; i < maxWrong; i++) {
    const b = document.createElement("div");
    b.className = "attempt-bubble" + (i < wrongCount ? " used" : "");
    attemptBubbles.appendChild(b);
  }
}



function setStatus(text, cls) {
  statusMsg.textContent = text;
  statusMsg.className   = "status-msg" + (cls ? ` ${cls}` : "");
}

function disableKey(letter, cls) {
  const btn = document.getElementById(`key-${letter}`);
  if (!btn) return;
  btn.disabled = true;
  if (cls) btn.classList.add(cls);
}

function disableAllKeys() {
  document.querySelectorAll(".key-btn").forEach(b => b.disabled = true);
}

function resetKeyboard() {
  document.querySelectorAll(".key-btn").forEach(btn => {
    btn.disabled = false;
    btn.className = "key-btn";
  });
  hintBtn.disabled = false;
  hintLeft.textContent = "(2 left)";
}

function showOverlay(emoji, title, wordMsg, won) {
  overlayEmoji.textContent   = emoji;
  overlayTitle.textContent   = title;
  overlayTitle.style.color   = won ? "var(--accent2)" : "var(--danger)";
  overlayWord.textContent    = wordMsg;
  overlay.classList.remove("hidden");
}

function hideOverlay() {
  overlay.classList.add("hidden");
}


async function apiPost(endpoint, body = {}) {
  try {
    const res = await fetch(endpoint, {
      method:  "POST",
      headers: { "Content-Type": "application/json" },
      body:    JSON.stringify(body),
    });
    if (!res.ok) {
      const err = await res.json();
      console.error("API error:", err);
      return null;
    }
    return await res.json();
  } catch (e) {
    console.error("Network error:", e);
    return null;
  }
}
