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
prompt = (
                f"Analyze the following text: {input_text}\n"
                "1. Create 3 Cloze Test questions with answers and explanations.\n"
                "2. Extract vocabulary with part of speech, translations, and difficulty levels."
            )

if st.button("Analyze"):
        # Process input and call OpenAI Completion API
        if input_text:
            messages_so_far = [
        {"role": "system", "content": prompt},
        {'role': 'user', 'content': input_text},
            ]
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini", 
                    messages=messages_so_far,
                    temperature=1.1
                )
                result = response.choices[0].text.strip()
                st.write("**Analysis Result:**")
                st.text(result)

            except Exception as e:
                st.error(f"Error occurred: {e}")
