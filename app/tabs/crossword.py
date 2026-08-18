import streamlit as st
import streamlit.components.v1 as components
import json

# ---------------------
# ----- CROSSWORD -----
# ---------------------

SOLUTION_GRID = [
    [None, None, None, None, None, "C", "A", "N", "C", "U", "N"],
    [None, None, None, None, "T", "A", "X", "E", "S", None, "U"],
    [None, None, None, "C", "A", "R", "L", None, "G", "E", "M"],
    [None, "W", "O", "O", None, "M", "E", "M", "O", None, "E"],
    ["P", "A", "D", "D", "L", "E", "S", None, None, None, "R"],
    ["A", "M", None, "Y", "E", "N", None, None, "O", "R", "A"],
    ["D", "O", "T", None, "B", None, "C", "O", "R", "A", "L"],

]
 
CLUES = {
    "CANCUN": "mexico",
    "TAXES": "pay",
    "CARL": "middle name",
    "GEM": "your initials",
    "WOO": "wine zoo",
    "MEMO": "law thing",
    "PADDLES": "pickleball tools",
    "AM": "not PM",
    "YEN": "japan currency",
    "ORA": "Rita",
    "DOT": "gummy candy",
    "CORAL": "Reef",
    "PAD": "thai",
    "WAMO": "self driving car",
    "OD": "overdose",
    "CODY": "____ simpson",
    "LEB": "your company",
    "CARMEN": "Playa Del _____",
    "AXLES": "Wheel and _____",
    "TA": "my georgetown job",
    "NE": "where noah kahans sings about",
    "CSGO": "game I play",
    "NUMERAL": "romans use to count",
    "OR": "surgery location",
    "RA": "residant advisor",
}
 
 
def build_crossword_words(grid):
    """Derive numbered across/down words from a solution grid."""
    rows, cols = len(grid), len(grid[0])
 
    def is_letter(r, c):
        return 0 <= r < rows and 0 <= c < cols and grid[r][c] is not None
 
    numbers = [[None] * cols for _ in range(rows)]
    words = []
    num = 1
 
    for r in range(rows):
        for c in range(cols):
            if not is_letter(r, c):
                continue
            starts_across = not is_letter(r, c - 1) and is_letter(r, c + 1)
            starts_down = not is_letter(r - 1, c) and is_letter(r + 1, c)
            if not (starts_across or starts_down):
                continue
 
            numbers[r][c] = num
 
            if starts_across:
                cells = []
                cc = c
                while is_letter(r, cc):
                    cells.append([r, cc])
                    cc += 1
                answer = "".join(grid[rr][cc_] for rr, cc_ in cells)
                words.append({
                    "id": f"{num}A", "number": num, "direction": "across",
                    "answer": answer, "clue": CLUES.get(answer, answer),
                    "cells": cells,
                })
 
            if starts_down:
                cells = []
                rr = r
                while is_letter(rr, c):
                    cells.append([rr, c])
                    rr += 1
                answer = "".join(grid[rr_][cc] for rr_, cc in cells)
                words.append({
                    "id": f"{num}D", "number": num, "direction": "down",
                    "answer": answer, "clue": CLUES.get(answer, answer),
                    "cells": cells,
                })
 
            num += 1
 
    return numbers, words
 
 
CROSSWORD_TEMPLATE = r"""
<div id="cw-root">
  <style>
    #cw-root { font-family: -apple-system, Segoe UI, Roboto, sans-serif; display: flex; gap: 28px; flex-wrap: wrap; }
    #cw-grid { display: grid; gap: 2px; background: #1a1a1a; padding: 2px; border-radius: 4px; }
    .cw-cell { position: relative; width: __CELLPX__px; height: __CELLPX__px; background: #fff; }
    .cw-cell.block { background: #1a1a1a; }
    .cw-cell input {
      width: 100%; height: 100%; border: none; text-align: center;
      font-size: 20px; font-weight: 600; text-transform: uppercase;
      background: transparent; outline: none; box-sizing: border-box;
      caret-color: transparent;
    }
    .cw-cell .num {
      position: absolute; top: 1px; left: 2px; font-size: 9px;
      color: #555; font-weight: 600; pointer-events: none;
    }
    .cw-cell.active-word input { background: #fff3b0; }
    .cw-cell.active-cell input { background: #ffca28; }
    .cw-cell input.correct { background: #b7e4b7 !important; }
    .cw-cell input.incorrect { background: #f3b3b3 !important; }
    #cw-clues { display: flex; gap: 24px; min-width: 260px; }
    #cw-clues h4 { margin: 0 0 6px 0; font-size: 14px; }
    #cw-clues ul { list-style: none; margin: 0; padding: 0; font-size: 13px; }
    #cw-clues li { padding: 4px 6px; border-radius: 4px; cursor: pointer; line-height: 1.35; }
    #cw-clues li:hover { background: #f0f0f0; }
    #cw-clues li.active-clue { background: #fff3b0; font-weight: 600; }
    #cw-clues .num { color: #666; margin-right: 2px; }
    #cw-controls { margin-top: 12px; display: flex; gap: 8px; }
    #cw-controls button {
      font-size: 13px; padding: 6px 12px; border-radius: 6px; border: 1px solid #ccc;
      background: #f6f6f6; cursor: pointer;
    }
    #cw-controls button:hover { background: #eaeaea; }
    #cw-status { margin-top: 8px; font-size: 13px; font-weight: 600; }
  </style>
 
  <div>
    <div id="cw-grid"></div>
    <div id="cw-controls">
      <button onclick="checkCrossword()">Check</button>
      <button onclick="revealCrossword()">Reveal</button>
      <button onclick="clearCrossword()">Clear</button>
    </div>
    <div id="cw-status"></div>
  </div>
 
  <div id="cw-clues">
    <div>
      <h4>Across</h4>
      <ul id="cw-across"></ul>
    </div>
    <div>
      <h4>Down</h4>
      <ul id="cw-down"></ul>
    </div>
  </div>
</div>
 
<script>
const DATA = __DATA_JSON__;
const rows = DATA.rows, cols = DATA.cols;
let currentR = 0, currentC = 0, currentDir = "across";
 
const cellWords = {};
for (const w of DATA.words) {
  for (const [r, c] of w.cells) {
    const k = r + "," + c;
    if (!cellWords[k]) cellWords[k] = {};
    cellWords[k][w.direction] = w.id;
  }
}
const wordById = {};
for (const w of DATA.words) wordById[w.id] = w;
 
function isLetter(r, c) {
  return r >= 0 && r < rows && c >= 0 && c < cols && !DATA.blocks[r][c];
}
 
const grid = document.getElementById("cw-grid");
grid.style.gridTemplateColumns = "repeat(" + cols + ", " + DATA.cellPx + "px)";
grid.style.gridTemplateRows = "repeat(" + rows + ", " + DATA.cellPx + "px)";
 
const acrossList = document.getElementById("cw-across");
const downList = document.getElementById("cw-down");
for (const w of DATA.words) {
  const li = document.createElement("li");
  li.dataset.id = w.id;
  li.innerHTML = '<span class="num">' + w.number + '.</span> ' + w.clue;
  li.onclick = () => selectWord(w.id);
  (w.direction === "across" ? acrossList : downList).appendChild(li);
}
 
const inputs = {};
 
for (let r = 0; r < rows; r++) {
  for (let c = 0; c < cols; c++) {
    const cell = document.createElement("div");
    cell.className = "cw-cell" + (DATA.blocks[r][c] ? " block" : "");
    cell.dataset.r = r; cell.dataset.c = c;
    if (!DATA.blocks[r][c]) {
      const num = DATA.numbers[r][c];
      if (num) {
        const numSpan = document.createElement("span");
        numSpan.className = "num";
        numSpan.textContent = num;
        cell.appendChild(numSpan);
      }
      const inp = document.createElement("input");
      inp.maxLength = 1;
      inp.autocomplete = "off";
      inp.dataset.r = r; inp.dataset.c = c;
      inp.addEventListener("click", () => selectCell(r, c, null));
      inp.addEventListener("focus", () => {
          currentR = r;
          currentC = c;
          updateHighlight();
      });
      inp.addEventListener("keydown", (e) => handleKeydown(e, r, c));
      inp.addEventListener("input", (e) => handleInput(e, r, c));
      cell.appendChild(inp);
      inputs[r + "," + c] = inp;
    }
    grid.appendChild(cell);
  }
}
 
function selectCell(r, c, preferDir) {
  if (!isLetter(r, c)) return;
  const cw = cellWords[r + "," + c] || {};
  let dir = preferDir || currentDir;
  if ((r === currentR && c === currentC) && !preferDir && cw.across && cw.down) {
    dir = currentDir === "across" ? "down" : "across";
  }
  if (!cw[dir]) dir = cw.across ? "across" : "down";
  currentR = r; currentC = c; currentDir = dir;
  updateHighlight();
  const inp = inputs[r + "," + c];
  if (inp) inp.focus();
}
 
function selectWord(wordId) {
  const w = wordById[wordId];
  if (!w) return;
  currentR = w.cells[0][0]; currentC = w.cells[0][1]; currentDir = w.direction;
  updateHighlight();
  const inp = inputs[currentR + "," + currentC];
  if (inp) inp.focus();
}
 
function updateHighlight() {
  const activeWordId = (cellWords[currentR + "," + currentC] || {})[currentDir];
  document.querySelectorAll(".cw-cell").forEach(cell => {
    cell.classList.remove("active-word", "active-cell");
  });
  if (activeWordId) {
    for (const [r, c] of wordById[activeWordId].cells) {
      const cell = grid.children[r * cols + c];
      cell.classList.add("active-word");
    }
  }
  const curCell = grid.children[currentR * cols + currentC];
  if (curCell) curCell.classList.add("active-cell");
 
  document.querySelectorAll("#cw-clues li").forEach(li => {
    li.classList.toggle("active-clue", li.dataset.id === activeWordId);
  });
}
 
function nextCellInWord(r, c, dir, delta) {
  return dir === "across" ? [r, c + delta] : [r + delta, c];
}
 
function handleInput(e, r, c) {
  let v = e.target.value.toUpperCase().replace(/[^A-Z]/g, "");
  e.target.value = v.slice(-1);
  e.target.classList.remove("correct", "incorrect");
  if (v) {
    const next = nextCellInWord(r, c, currentDir, 1);
    if (isLetter(next[0], next[1])) selectCell(next[0], next[1], currentDir);
  }
}
 
function handleKeydown(e, r, c) {
  if (e.key === "Backspace" && !e.target.value) {
    const prev = nextCellInWord(r, c, currentDir, -1);
    if (isLetter(prev[0], prev[1])) selectCell(prev[0], prev[1], currentDir);
  } else if (e.key === "ArrowRight") { e.preventDefault(); if (isLetter(r, c + 1)) selectCell(r, c + 1, "across"); }
  else if (e.key === "ArrowLeft") { e.preventDefault(); if (isLetter(r, c - 1)) selectCell(r, c - 1, "across"); }
  else if (e.key === "ArrowDown") { e.preventDefault(); if (isLetter(r + 1, c)) selectCell(r + 1, c, "down"); }
  else if (e.key === "ArrowUp") { e.preventDefault(); if (isLetter(r - 1, c)) selectCell(r - 1, c, "down"); }
}
 
function checkCrossword() {
  let total = 0, correct = 0;
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (DATA.blocks[r][c]) continue;
      total++;
      const inp = inputs[r + "," + c];
      const val = (inp.value || "").toUpperCase();
      inp.classList.remove("correct", "incorrect");
      if (val) {
        if (val === DATA.solution[r][c]) { inp.classList.add("correct"); correct++; }
        else inp.classList.add("incorrect");
      }
    }
  }
  const status = document.getElementById("cw-status");
  status.textContent = correct === total ? "🎉 Solved it!" : (correct + "/" + total + " correct");
}
 
function revealCrossword() {
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (DATA.blocks[r][c]) continue;
      inputs[r + "," + c].value = DATA.solution[r][c];
      inputs[r + "," + c].classList.remove("correct", "incorrect");
    }
  }
  document.getElementById("cw-status").textContent = "Answers revealed.";
}
 
function clearCrossword() {
  for (const k in inputs) {
    inputs[k].value = "";
    inputs[k].classList.remove("correct", "incorrect");
  }
  document.getElementById("cw-status").textContent = "";
}
 
selectCell(0, 0, "across");
</script>
"""
 
 
def crossword_component_html(grid, numbers, words, cell_px=42):
    rows, cols = len(grid), len(grid[0])
    blocks = [[grid[r][c] is None for c in range(cols)] for r in range(rows)]
 
    data = {
        "rows": rows,
        "cols": cols,
        "blocks": blocks,
        "solution": grid,
        "numbers": numbers,
        "words": words,
        "cellPx": cell_px,
    }
 
    html = CROSSWORD_TEMPLATE.replace("__CELLPX__", str(cell_px))
    html = html.replace("__DATA_JSON__", json.dumps(data))
    return html
 
 
def render_crossword():
    st.subheader("Mini Crossword")
    st.caption("Click a cell or clue to select a word. Type to fill letters; arrow keys to move; Backspace to erase and step back.")

    numbers, words = build_crossword_words(SOLUTION_GRID)
    html = crossword_component_html(SOLUTION_GRID, numbers, words)

    # Center the crossword by flanking it with empty columns
    left, center, right = st.columns([2.25, 8, 1])
    with center:
        components.html(html, height=420, scrolling=True)