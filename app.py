import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="AI Sentiment Analyzer", page_icon="🧠")

st.title("🧠 AI Sentiment Analyzer")
st.write("This app uses Natural Language Processing (NLP) to detect the mood of your text.")

user_input = st.text_area("Enter text to analyze:", "I am having a great day working on my AI project!")

if st.button("Analyze Sentiment"):
    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity
    
    if polarity > 0:
        st.success(f"Positive Sentiment (Score: {round(polarity, 2)}) 😊")
    elif polarity < 0:
        st.error(f"Negative Sentiment (Score: {round(polarity, 2)}) 😡")
    else:
        st.warning(f"Neutral Sentiment (Score: {polarity}) 😐")

st.info("Technical Note: This uses the TextBlob library for lexicon-based sentiment analysis.")