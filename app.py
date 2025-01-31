import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Load the chatbot pipeline
chatbot = pipeline("text-generation", model="gpt2")

def main():
    # Title at the top
    st.title("Healthcare Assistant Chatbot")
    
    # User input
    user_input = st.text_input("How can I assist you today?")
    
    # Button to submit input
    if st.button("Submit"):
        if user_input:
            st.write("User:", user_input)
        else:
            st.write("Please enter a message to get a response")

# Run the app
if __name__ == "__main__":
    main()
