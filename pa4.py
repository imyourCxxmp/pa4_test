import streamlit as st
import openai
import json
import pandas as pd

# Get the API key from the sidebar
user_api_key = st.sidebar.text_input("OpenAI API key", type="password")

if user_api_key:
    openai.api_key = user_api_key  # Set the OpenAI API key
    
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
        try:
            # Construct the messages for the API
            messages_so_far = [
                {"role": "system", "content": prompt},
                {"role": "user", "content": user_input},
            ]
            
            # Call OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=messages_so_far
            )
            
            # Extract and parse the response
            suggestion_text = response.choices[0].message["content"]
            st.markdown('**AI Response:**')
            
            # Try parsing the JSON suggestions
            try:
                suggestions = json.loads(suggestion_text)
                # Convert suggestions to a DataFrame
                suggestion_df = pd.DataFrame(suggestions)
                st.table(suggestion_df)
            except json.JSONDecodeError:
                st.error("Failed to parse AI response. Please check the response format.")
                st.text(suggestion_text)  # Display raw response for debugging
            
        except Exception as e:
            st.error(f"An error occurred: {e}")
else:
    st.warning("Please enter your OpenAI API key to proceed.")
