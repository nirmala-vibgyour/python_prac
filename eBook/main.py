import streamlit as st
import glob
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer


filepaths = sorted(glob.glob("diary/*.txt"))

analyzer = SentimentIntensityAnalyzer()

negativity = []
positivity = []
for filepath in filepaths:
    with open(filepath) as file:
        content = file.read()
    scores = analyzer.polarity_scores(content)
    positivity.append(scores["pos"])
    negativity.append(scores["neg"])

dates = [name.strip(".txt").strip(r"diary\\") for name in filepaths]

st.title("Diary Tone")
st.subheader("Positivity")
posFigure = px.line(x=dates, y=positivity,
                    labels={"X": "Date", "Y": "Positivity"})
st.plotly_chart(posFigure)

st.subheader("Negativity")
negFigure = px.line(x=dates, y=negativity,
                    labels={"X": "Dates", "Y": "Negativity"})
st.plotly_chart(negFigure)