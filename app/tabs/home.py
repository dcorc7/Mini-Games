import streamlit as st
from tabs.pinboard import render_pinboard

# ---------------------
# ----- HOME PAGE -----
# ---------------------

RESTAURANT_NAME = "UCHI"

def render_home():
    st.markdown("<br>", unsafe_allow_html=True)

    with st.container(key="home_grid"):
        st.markdown("""
        <style>
        .st-key-home_grid div.stButton {
            display: flex;
            justify-content: center;
        }
        .st-key-home_grid div.stButton > button {
            height: 200px;
            width: 80%;
            font-size: 30px;
            font-weight: bold;
            border-radius: 16px;
            border: 2px solid #d0d0d0;
            color: #333333;
            background: #f0f0f0;
            transition: transform 0.15s ease;
        }
        .st-key-home_grid div.stButton > button:hover {
            transform: scale(1.03);
        }
        </style>
        """, unsafe_allow_html=True)


        # --------------------
        # ----- PINBOARD -----
        # --------------------

        render_pinboard(
            photo_paths=[
                "photo1.jpeg",
                "photo2.jpeg",
                "photo3.jpeg",
                "photo4.jpeg",
                "photo5.jpeg",
                "photo6.jpeg",
                "photo7.jpeg",
                "photo8.jpeg",
                "photo9.jpeg",
                "photo10.jpg",
                "photo11.jpg",
                "photo12.jpg",
            ],
            event_details={
                "title": "Gwynns Shrine Part 2",
                "names": "Anniversary",
                "date": "Tuesday, September 15th",
                "time": "7:30 PM",
                "location": "MYSTERY (Not Anymore)",
            }
        )

        st.markdown("<br><br>", unsafe_allow_html=True)

        # ----------------------------
        # ----- RESTAURANT REVEL -----
        # ----------------------------

        if "restaurant_revealed" not in st.session_state:
            st.session_state.restaurant_revealed = False

        if not st.session_state.restaurant_revealed:
            if st.button("Reveal Restaurant", key="btn_reveal", use_container_width=True):
                st.session_state.restaurant_revealed = True
                st.rerun()
        else:
            st.markdown(f"""
            <div style="
                height:200px;
                width: 80%;
                margin: 0 auto;
                border-radius:16px;
                background: linear-gradient(135deg, #9a3324 0%, #b56c62 100%);
                display:flex;
                align-items:center;
                justify-content:center;
                color:white;
                font-size:26px;
                font-weight:bold;
                text-align:center;
                padding:10px;
            ">
                {RESTAURANT_NAME}
            </div>
            """, unsafe_allow_html=True)