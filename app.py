import streamlit as st
import joblib
import pickle

# Load model and vectorizer
model = joblib.load("sentiment_model.pkl")
tfidf_vectorizer = joblib.load("vectorizer.pkl")

st.title("📰 News Sentiment Analysis")
st.write("Enter a news headline or short article to predict its sentiment.")

# Input
user_input = st.text_area("📝 Enter news text here:")

if st.button("Predict Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        transformed_input = tfidf_vectorizer.transform([user_input])
        prediction = model.predict(transformed_input)

        sentiment = "Positive 😊" if prediction[0] == 1 else "Negative 😞"
        st.success(f"Predicted Sentiment: **{sentiment}**")
