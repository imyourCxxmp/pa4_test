import streamlit as st
import openai

st.title('Reading Exam Generator')
st.markdown(
    'AI ช่วยแต่งข้อสอบพาร์ต Reading เพียงแค่เขียน keyword ที่จะต้องการ \n'
    'Article จะมีความยาว 400-500 คำ ความยากระดับ B2-C1 และมีข้อสอบทั้งหมด 10 ข้อ'
)

user_api_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")

if not user_api_key:
    st.warning("Please provide your OpenAI API key to proceed.")
else:
    openai.api_key = user_api_key  # Set OpenAI API key

user_input = st.text_area('Enter your keyword(s) here:', 'e.g., Christmas Day')

prompt = (
    "Act as an English exam writer who wants undergraduate students to develop their reading comprehension skills.\n"
    "1. Your task is to generate a reading comprehension exam from the keyword(s) provided by the user.\n"
    "2. You have to fact-check and verify information before using it.\n"
    "3. The article should be 400-500 words long, use vocabulary at the B2-C1 CEFR level, and contain grammatically correct sentences.\n"
    "4. Create 10 challenging multiple-choice questions requiring deeper comprehension and interpretation.\n"
    "5. Provide an answer key with proper reasoning for each question in a table format."
)

if st.button('Generate Exam'):
    if not user_input.strip():
        st.error("Please provide keywords to generate the exam.")
    else:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": user_input}
                ]
            )

            answer = response['choices'][0]['message']['content']
            st.markdown('**Generated Reading Exam:**')
            st.write(answer)
        except openai.error.OpenAIError as e:
            st.error(f"An error occurred: {e}")


