import streamlit as st
import random
import copy
import streamlit.components.v1 as components
import json

# ------------------
# ----- SUDOKU -----
# ------------------

def make_solved_sudoku():
    base = 3
    side = base * base
 
    def pattern(r, c):
        return (base * (r % base) + r // base + c) % side
 
    def shuffle(s):
        return random.sample(s, len(s))
 
    r_base = range(base)
    rows = [g * base + r for g in shuffle(r_base) for r in shuffle(r_base)]
    cols = [g * base + c for g in shuffle(r_base) for c in shuffle(r_base)]
    nums = shuffle(range(1, side + 1))
 
    board = [[nums[pattern(r, c)] for c in cols] for r in rows]
    return board
 
 
def make_sudoku_puzzle(difficulty="Easy"):
    if difficulty == "Easy":
        difficulty_holes = 45
    elif difficulty == "Medium":
        difficulty_holes = 50
    else:
        difficulty_holes = 60

    solution = make_solved_sudoku()
    puzzle = copy.deepcopy(solution)
    cells = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(cells)

    for r, c in cells[:difficulty_holes]:
        puzzle[r][c] = 0

    return puzzle, solution
 
 
SUDOKU_TEMPLATE = r"""
<div id="sk-root">
  <style>
    #sk-root { font-family: -apple-system, Segoe UI, Roboto, sans-serif; }
    #sk-grid {
      display: grid;
      grid-template-columns: repeat(9, __CELLPX__px);
      grid-template-rows: repeat(9, __CELLPX__px);
      border: 3px solid #1a1a1a;
      width: max-content;
    }
    .sk-cell {
      position: relative;
      border-right: 1px solid #ccc;
      border-bottom: 1px solid #ccc;
      box-sizing: border-box;
    }
    .sk-cell.box-right { border-right: 3px solid #1a1a1a; }
    .sk-cell.box-bottom { border-bottom: 3px solid #1a1a1a; }
    .sk-cell input {
      width: 100%; height: 100%; border: none; text-align: center;
      font-size: 19px; font-weight: 500; background: transparent;
      outline: none; box-sizing: border-box; caret-color: transparent;
    }
    .sk-cell input:disabled {
      font-weight: 800; color: #111; background: #ececec; opacity: 1;
    }
    .sk-cell input.correct { background: #b7e4b7 !important; }
    .sk-cell input.incorrect { background: #f3b3b3 !important; }
    .sk-cell input.revealed { background: #cfe3fb !important; }
    .sk-cell input:focus { background: #fff3b0; }
    #sk-controls { margin-top: 12px; display: flex; gap: 8px; }
    #sk-controls button {
      font-size: 13px; padding: 6px 12px; border-radius: 6px; border: 1px solid #ccc;
      background: #f6f6f6; cursor: pointer;
    }
    #sk-controls button:hover { background: #eaeaea; }
    #sk-status { margin-top: 8px; font-size: 13px; font-weight: 600; }
  </style>
 
  <div id="sk-grid"></div>
  <div id="sk-controls">
    <button onclick="checkSudoku()">Check Solution</button>
    <button onclick="revealSudoku()">Reveal Puzzle</button>
    <button onclick="clearSudoku()">Clear My Entries</button>
  </div>
  <div id="sk-status"></div>
</div>
 
<script>
const SK = __DATA_JSON__;
const grid = document.getElementById("sk-grid");
const inputs = {};
 
for (let r = 0; r < 9; r++) {
  for (let c = 0; c < 9; c++) {
    const cell = document.createElement("div");
    let cls = "sk-cell";
    if (c === 2 || c === 5) cls += " box-right";
    if (r === 2 || r === 5) cls += " box-bottom";
    cell.className = cls;
 
    const inp = document.createElement("input");
    inp.maxLength = 1;
    inp.autocomplete = "off";
    inp.dataset.r = r; inp.dataset.c = c;
 
    const given = SK.puzzle[r][c];
    if (given !== 0) {
      inp.value = given;
      inp.disabled = true;
    } else {
      inp.addEventListener("input", (e) => handleInput(e, r, c));
      inp.addEventListener("keydown", (e) => handleKeydown(e, r, c));
    }
 
    cell.appendChild(inp);
    grid.appendChild(cell);
    inputs[r + "," + c] = inp;
  }
}
 
function focusCell(r, c) {
  if (r < 0 || r > 8 || c < 0 || c > 8) return;
  const inp = inputs[r + "," + c];
  if (inp && !inp.disabled) inp.focus();
  else if (inp) inp.blur();
}
 
function handleInput(e, r, c) {
  let v = e.target.value.replace(/[^1-9]/g, "");
  e.target.value = v.slice(-1);
  e.target.classList.remove("correct", "incorrect", "revealed");
  if (v && c < 8) focusCell(r, c + 1);
  else if (v && c === 8 && r < 8) focusCell(r + 1, 0);
}
 
function handleKeydown(e, r, c) {
  if (e.key === "Backspace" && !e.target.value && c > 0) focusCell(r, c - 1);
  else if (e.key === "ArrowRight") { e.preventDefault(); focusCell(r, c + 1); }
  else if (e.key === "ArrowLeft") { e.preventDefault(); focusCell(r, c - 1); }
  else if (e.key === "ArrowDown") { e.preventDefault(); focusCell(r + 1, c); }
  else if (e.key === "ArrowUp") { e.preventDefault(); focusCell(r - 1, c); }
}
 
function checkSudoku() {
  let total = 0, correct = 0, filled = 0;
  for (let r = 0; r < 9; r++) {
    for (let c = 0; c < 9; c++) {
      if (SK.puzzle[r][c] !== 0) continue;
      total++;
      const inp = inputs[r + "," + c];
      inp.classList.remove("correct", "incorrect", "revealed");
      const val = inp.value ? parseInt(inp.value, 10) : 0;
      if (val) {
        filled++;
        if (val === SK.solution[r][c]) { inp.classList.add("correct"); correct++; }
        else inp.classList.add("incorrect");
      }
    }
  }
  const status = document.getElementById("sk-status");
  if (correct === total) status.textContent = "🎉 Solved it!";
  else if (filled === 0) status.textContent = "Fill in some cells first.";
  else status.textContent = correct + "/" + filled + " filled cells correct (" + (total - filled) + " still empty).";
}
 
function revealSudoku() {
  for (let r = 0; r < 9; r++) {
    for (let c = 0; c < 9; c++) {
      if (SK.puzzle[r][c] !== 0) continue;
      const inp = inputs[r + "," + c];
      inp.value = SK.solution[r][c];
      inp.classList.remove("correct", "incorrect");
      inp.classList.add("revealed");
    }
  }
  document.getElementById("sk-status").textContent = "Solution revealed.";
}
 
function clearSudoku() {
  for (let r = 0; r < 9; r++) {
    for (let c = 0; c < 9; c++) {
      if (SK.puzzle[r][c] !== 0) continue;
      const inp = inputs[r + "," + c];
      inp.value = "";
      inp.classList.remove("correct", "incorrect", "revealed");
    }
  }
  document.getElementById("sk-status").textContent = "";
}
</script>
"""
 
 
def sudoku_component_html(puzzle, solution, cell_px=42):
    data = {"puzzle": puzzle, "solution": solution}
    html = SUDOKU_TEMPLATE.replace("__CELLPX__", str(cell_px))
    html = html.replace("__DATA_JSON__", json.dumps(data))
    return html
 
 
def render_sudoku():
    st.subheader("Sudoku")

    difficulty = st.selectbox(
        "Difficulty",
        options=("Easy", "Medium", "Hard")
    )
 
    if "sudoku_puzzle" not in st.session_state:
        puzzle, solution = make_sudoku_puzzle(difficulty)
        st.session_state.sudoku_puzzle = puzzle
        st.session_state.sudoku_solution = solution
 
    if st.button("New Puzzle", key="sudoku_new"):
        puzzle, solution = make_sudoku_puzzle(difficulty)
        st.session_state.sudoku_puzzle = puzzle
        st.session_state.sudoku_solution = solution
        st.rerun()


 
    st.caption("Click a box to type a digit 1-9. Check Solution highlights right (green) vs wrong (red) cells; Reveal Puzzle fills in the answer.")
 
    html = sudoku_component_html(st.session_state.sudoku_puzzle, st.session_state.sudoku_solution)
    components.html(html, height=460, scrolling=True)