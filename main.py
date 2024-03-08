import streamlit as st
import glob
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


analyzer=SentimentIntensityAnalyzer()

#get the filepaths of the each txt files
filepaths=sorted(glob.glob("diary/*.txt"))

#created two empty list to store the sentiment analysis scores
positivity=[]
negativity=[]

#read the contents of the file and get the positivity and negativity scores of each day
for filepath in filepaths:
    with open(f"{filepath}","r") as file:
        content= file.read()
        scores=analyzer.polarity_scores(content)
        positivity.append(scores['pos'])
        negativity.append(scores['neg'])

#extract the dates

st.title("Diary Tone")
st.subheader("Positivity")
st.subheader("Negativity")


