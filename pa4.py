import streamlit as st
import pandas as pd
import openai

# Sidebar for API key
st.sidebar.title("API Key")
user_api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")
client = openai.OpenAI(api_key=user_api_key)
# Input options
st.title("Smart Passage Analyzer")
input_text = st.text_area("Enter your passage here:")

if st.button("Analyze"):
        # Process input and call OpenAI Completion API
        if input_text:
            prompt = (
                f"Analyze the following text: {input_text}\n"
                "1. Create 3 Cloze Test questions with answers and explanations.\n"
                "2. Extract vocabulary with part of speech, translations, and difficulty levels."
            )
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini", 
                    prompt=prompt,
                    max_tokens=1000,
                    temperature=0.7
                )
                result = response.choices[0].text.strip()
                st.write("**Analysis Result:**")
                st.text(result)

            except Exception as e:
                st.error(f"Error occurred: {e}")
