import openai
import os
import pandas as pd
import streamlit as st
from streamlit_chat import message
st.title('Virtual Therapist')
api_key = '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'
openai.api_key = api_key
article_text = st.text_area("Enter your scientific texts to summarize")
output_size = st.radio( label = "What kind of output do you want?", 
                        options= ["To-The-Point", "Concise", "Detailed"]
                     )

def generate_response(prompt):
    return prompt
    completions = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message #bla bla bla

# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

#TEST
# We will get the user's input by calling the get_text function
def get_text():
    input_text = st.text_input("Wirtualny Terapeuta:","Co Ci lezy na sercu? Jak się czujesz?", key="input")
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

