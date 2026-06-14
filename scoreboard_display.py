import streamlit as st
from fetch_score import fetch_live_score


st.set_page_config(
    page_title="IoT Cricket Scoreboard",
    page_icon="🏏",
    layout="centered"
)

st.title("🏏 IoT Cricket Scoreboard")
st.write("Real-time cricket scoreboard simulation using Python and API-style data.")

match = fetch_live_score()

st.subheader(f"{match['team_1']} vs {match['team_2']}")

st.write(f"**Venue:** {match['venue']}")
st.write(f"**Status:** {match['status']}")

score = match["score"]

st.metric(
    label=f"{score['team']} Score",
    value=f"{score['runs']}/{score['wickets']}",
    delta=f"{score['overs']} overs"
)

st.subheader("Current Batsmen")

for batsman in match["batsmen"]:
    st.write(f"**{batsman['name']}** - {batsman['runs']} runs from {batsman['balls']} balls")

st.subheader("Current Bowler")

bowler = match["bowler"]

st.write(f"**{bowler['name']}**")
st.write(f"Overs: {bowler['overs']}")
st.write(f"Wickets: {bowler['wickets']}")

st.subheader("IoT Explanation")

st.write(
    """
    In a real IoT scoreboard, this data can be sent to an LCD display,
    LED matrix, Raspberry Pi display, or Arduino-connected screen.
    This project simulates the API and display logic using Python.
    """
)
