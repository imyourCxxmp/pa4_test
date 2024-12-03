import streamlit as st
import pandas as pd
import openai

# Sidebar for API key
st.sidebar.title("API Key")
api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")

# Input options
st.title("Smart Passage Analyzer")
input_text = st.text_area("Enter your passage here:")

if st.button("Analyze"):
    if not api_key:
        st.error("Please enter your API key.")
    else:
        openai.api_key = api_key

        # Process input and call OpenAI Completion API
        if input_text:
            prompt = (
                f"Analyze the following text: {input_text}\n"
                "1. Create 3 Cloze Test questions with answers and explanations.\n"
                "2. Extract vocabulary with part of speech, translations, and difficulty levels."
            )
            try:
                response = openai.Completion.create(
                    engine="text-davinci-003",  # หรือ model ที่คุณต้องการ
                    prompt=prompt,
                    max_tokens=1000,
                    temperature=0.7
                )
                result = response.choices[0].text.strip()
                st.write("**Analysis Result:**")
                st.text(result)

            except Exception as e:
                st.error(f"Error occurred: {e}")
