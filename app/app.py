import streamlit as st
import random
import copy

from home import home
from crossword import render_crossword
from sudoku import render_sudoku


st.set_page_config(page_title="Anniverary", page_icon="", layout="wide")

# ---------------------------
# ----- MAIN APP LAYOUT -----
# ---------------------------

def main():
    st.title("Anniversary Games")
    st.caption("Play them now.")

    tab1, tab2, tab3 = st.tabs(["Home", "Crossword", "Sudoku"])

    with tab1:
        home()
    with tab2:
        render_crossword()
    with tab3:
        render_sudoku()


if __name__ == "__main__":
    main()
