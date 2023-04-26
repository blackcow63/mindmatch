import openai
import os
import pandas as pd
import streamlit as st
from streamlit_chat import message
st.title('Virtual Therapist')

#st.set_page_config(
#    page_title="Streamlit Chat - Demo",
#    page_icon=":robot:"
#)

openai.api_key = st.secrets["OPENAI_API_KEY"]
#st.header("Streamlit Chat - Demo")
#st.markdown("[Github](https://github.com/ai-yash/st-chat)")

def generate_response(prompt):
    completions = openai.Completion.create(
        engine = "gpt-3.5-turbo",
        prompt_prefix = "Jesteś terpeutą. Odpowiedz na tą wiadomość tak aby dowiedzieć się jak najwięcej o objawach:" + "'" + prompt + "'",
        prompt = prompt,
        max_tokens = 400,
        n = 1,
        stop = None,
        temperature=0.7,
    )
    message = completions.choices[0].text
    print(message)
    return message

# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

#def query(payload):
#	response = requests.post(API_URL, headers=headers, json=payload)
#	return response.json()


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

