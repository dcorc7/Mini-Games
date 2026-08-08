import streamlit as st

# ---------------------
# ----- HOME PAGE -----
# ---------------------

def render_schedule():

    page_cols = st.columns([1, 1])

    with page_cols[0]:
        # Define your fixed daily schedule items
        schedule = [
            {
                "time": "08:00 AM", 
                "task": "Wake up and breakfast"
            },
            {
                "time": "09:30 AM", 
                "task": "Team sync meeting"
            },
            {
                "time": "11:00 AM", 
                "task": "Deep work / coding"
            },
            {
                "time": "01:00 PM", 
                "task": "Lunch break"
            },
            {
                "time": "02:00 PM", 
                "task": "Project review"
            },
            {
                "time": "04:30 PM", 
                "task": "Wrap up and emails"
             },
        ]

        # Rendering the vertical timeline using columns
        for item in schedule:
            schedule_col1, schedule_col2 = st.columns([1, 4])

            with schedule_col1:
                st.markdown(f"**{item['time']}**")
            with schedule_col2:
                st.info(item["task"])

            # small gap
            st.write("")

    with page_cols[1]:
        st.write("Menu Placeholder")