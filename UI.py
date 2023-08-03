import streamlit as st

# pip install streamlit-chat  
from streamlit_chat import message

import ProtocolDev as pd

#Creating the chatbot interface
st.title("ProtocolDev")
st.subheader("Find and generate lab protocol for any biological experiment instantly!")

# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

# We will get the user's input by calling the get_text function
def get_text():
    input_text = st.text_input("Hello and welcome! What lab protocol would you like to start today?\n", key="input")
    return input_text

user_input = get_text()

if user_input:
    output = pd.generate_response(user_input)
    # store the output 
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')