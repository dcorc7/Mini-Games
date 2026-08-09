import streamlit as st

from tabs.home import render_home
from tabs.crossword import render_crossword
from tabs.sudoku import render_sudoku
from tabs.schedule import render_schedule


st.set_page_config(page_title="Anniverary", page_icon="", layout="wide")

# ---------------------------
# ----- MAIN APP LAYOUT -----
# ---------------------------

def main():
    st.markdown("<h1 style='text-align: center;'>Gwynn and David's 3rd Anniversary!!!</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Anniversary schedule and games - Play them now.</p>", unsafe_allow_html=True)

    tabs = st.tabs(["Home", "Schedule", "Crossword", "Sudoku"])

    with tabs[0]:
        render_home()
    with tabs[1]:
        render_schedule()
    with tabs[2]:
        render_crossword()
    with tabs[3]:
        render_sudoku()


if __name__ == "__main__":
    main()
