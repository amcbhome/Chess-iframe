import streamlit as st

st.set_page_config(page_title="Lichess Study Viewer", layout="centered")

st.title("Lichess Study Viewer")
st.write("Embedded study:")

# Embed the Lichess study
st.components.v1.iframe(
    "https://lichess.org/study/embed/sgYuHjtP/jxQIk87O",
    width=600,
    height=371,
    scrolling=False
)
