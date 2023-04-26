import openai
import os
import pandas as pd
import streamlit as st
from streamlit_chat import message
st.title('Virtual Therapist')


openai.api_key = st.secrets["OPENAI_API_KEY"]

if 'messages' not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "Jesteś terpeutą. Odpowiadaj na wiadomoci tak aby dowiedzieć się jak najwięcej o objawach. Gdy zidentyfikujesz chorob krzyknij eureka! i powiedz jej nazwę.",
        }
    ]


def generate_response(messages):
    completions = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages,
    )
    message = completions.choices[0].message.content
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


    st.session_state.messages.append({
        "role": "user",
        "content": user_input,
    })

    #if already 5 messages, add system message
    if len(st.session_state.messages) == 6:
        st.session_state.messages.append({
            "role": "user",
            "content": "Podaj współrzędne w układzie kartezjańskim [depresja, lęk, agresja, anoreksja, bulimia, zaburzenia lękowe, zaburzenia osobowości, zaburzenia zachowania, zaburzenia seksualne, zaburzenia somatyczne, zaburzenia społeczne] np. [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1, 0.2] na podstawie wcześniejszych rozmów.",
        })

    output = generate_response(st.session_state.messages)
    #add output to the messages
    st.session_state.messages.append({
        "role": "assistant",
        "content": output,
    })
    # store the output \
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)


if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

