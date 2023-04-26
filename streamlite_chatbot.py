import openai
import os
import pandas as pd
import streamlit as st
from streamlit_chat import message
st.title('Virtual Therapist')


openai.api_key = st.secrets["OPENAI_API_KEY"]

def generate_response(input):
    completions = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {
                "role": "user",
                "content": "Jesteś terpeutą. Odpowiedz na tą wiadomość tak aby dowiedzieć się jak najwięcej o objawach:" + "'" + input + "'",
            }
        ]
    )
    message = "a" #completions.choices[0].text
    return message

# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

#TEST
# We will get the user's input by calling the get_text function
def get_text():
    input_text = st.text_input("Ty:","Ostatnio nie czuję się najlepiej", key="input")
    return input_text

user_input = get_text()

if user_input:
    output = generate_response(user_input)
    # store the output 
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)


if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

