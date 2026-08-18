import streamlit as st

from tabs.home import render_home
from tabs.crossword import render_crossword
from tabs.sudoku import render_sudoku
from tabs.schedule import render_schedule

# ---------------------------
# ----- MAIN APP LAYOUT -----
# ---------------------------

st.set_page_config(page_title="Anniversary", page_icon="", layout="wide")

TABS = ["Home", "Schedule", "Crossword", "Sudoku"]

def main():
    st.markdown("<h1 style='text-align: center;'>Gwynn and David's 3rd Anniversary!!!</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Anniversary schedule and games - Play them now.</p>", unsafe_allow_html=True)

    # Nav bar styling — fixed size, color driven purely by primary/secondary kind
    st.markdown("""
    <style>
    .st-key-nav_bar div.stButton > button {
        height: 55px;
        width: 100%;
        font-size: 16px;
        font-weight: 600;
        border-radius: 10px;
        transition: all 0.15s ease;
        box-sizing: border-box;
    }
    .st-key-nav_bar div.stButton > button[kind="secondary"] {
        background-color: #f0f0f0;
        color: #333333;
        border: 2px solid #e0e0e0;
    }
    .st-key-nav_bar div.stButton > button[kind="secondary"]:hover {
        background-color: #e6e6e6;
        border: 2px solid #d0d0d0;
    }
    .st-key-nav_bar div.stButton > button[kind="primary"] {
        background: #ffb347;
        color: white;
        border: 2px solid #ff7b00;
        box-shadow: 0 2px 10px rgba(255, 123, 0, 0.4);
    }
    .st-key-nav_bar div.stButton > button[kind="primary"]:hover {
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)

    if "active_tab" not in st.session_state:
        st.session_state.active_tab = "Home"

    with st.container(key="nav_bar"):
        cols = st.columns(len(TABS))
        for col, name in zip(cols, TABS):
            with col:
                is_active = st.session_state.active_tab == name

                if st.button(name, key=f"nav_{name}", use_container_width=True,
                            type="primary" if is_active else "secondary"):
                    st.session_state.active_tab = name
                    st.rerun()

    st.divider()

    if st.session_state.active_tab == "Home":
        render_home()
    elif st.session_state.active_tab == "Schedule":
        render_schedule()
    elif st.session_state.active_tab == "Crossword":
        render_crossword()
    elif st.session_state.active_tab == "Sudoku":
        render_sudoku()

if __name__ == "__main__":
    main()