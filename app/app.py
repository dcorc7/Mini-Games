import streamlit as st

from app.pages.home import render_home
from app.pages.crossword import render_crossword
from app.pages.sudoku import render_sudoku
from app.pages.schedule import render_schedule


st.set_page_config(page_title="Anniverary", page_icon="", layout="wide")

# ---------------------------
# ----- MAIN APP LAYOUT -----
# ---------------------------

def main():
    st.title("Gwynn and David's 3rd Anniversary!!!", text_alignment = "Center")
    st.caption("Anniversary schedule and games - Play them now.", text_alignment = "Center")

    tab1, tab2, tab3, tab4 = st.tabs(["Home", "Crossword", "Sudoku"])

    with tab1:
        render_home()
    with tab2:
        render_schedule()
    with tab3:
        render_crossword()
    with tab4:
        render_sudoku()


if __name__ == "__main__":
    main()
