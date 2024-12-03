import streamlit as st
import openai
import json
import pandas as pd

# Get the API key from the sidebar
user_api_key = st.sidebar.text_input("OpenAI API key", type="password")
client = openai.OpenAI(api_key=user_api_key)
    
prompt = """Act as an AI writing tutor in English. You will receive a 
                piece of writing and you should give suggestions on how to improve it.
                List the suggestions in a JSON array, one suggestion per line.
                Each suggestion should have 4 fields:
                - "before" - the text before the suggestion
                - "after" - the text after the suggestion
                - "category" - the category of the suggestion, one of "grammar", "style", "word choice", "other"
                - "comment" - a comment about the suggestion
            """
    
st.title('Writing Tutor')
st.markdown('Input the writing that you want to improve. \n\
                The AI will give you suggestions on how to improve it.')

    # User input
user_input = st.text_area("Enter some text to correct:", "Your text here")

if st.button('Submit'):
    messages_so_far = [
                {"role": "system", "content": prompt},
                {"role": "user", "content": user_input},
    ]
    
    response = client.chat.completions.create(
                model="gpt-4",
                messages=messages_so_far
    )
    st.markdown('**AI Response:**')
    suggestion_text = response["choices"][0]["message"]["content"]
    suggestions = json.loads(suggestion_text)
    suggestion_df = pd.DataFrame(suggestions)
    st.table(suggestion_df)