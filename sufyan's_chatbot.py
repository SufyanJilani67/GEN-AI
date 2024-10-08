# import streamlit as st
# import google.generativeai as genai

# # Configure the API key
# GOOGLE_API_KEY = "AIzaSyDma9KsEXzewUDnLTErjwVIyR3qwcRVlD8"
# genai.configure(api_key=GOOGLE_API_KEY)

# # Initialize the Generative Model
# # model = genai.GenerativeModel('gemini-pro')
# model = genai.GenerativeModel('gemini-1.5-flash')
# # Function to get response from the model
# def get_chatbot_response(user_input):
#     response = model.generate_content(user_input)
#     return response.text

# # Streamlit interface
# st.set_page_config(page_title="Sufyan's ChatBot", layout="centered")

# st.title("✨ Sufyan's ChatBot ✨")
# st.write("Powered by Google Generative AI")

# if "history" not in st.session_state:
#     st.session_state["history"] = []

# # Display chat history
# for user_message, bot_message in st.session_state.history:
#     st.markdown(f"""
#     <div style="
#         background-color: #2e4854; 
#         border-radius: 15px; 
#         padding: 10px 15px; 
#         margin: 5px 0; 
#         max-width: 70%; 
#         text-align: left; 
#         display: inline-block;
#     ">
#         <p style="margin: 0; font-size: 16px; line-height: 1.5;"><b>You:</b> {user_message} 😊</p>
#     </div>
#     """, unsafe_allow_html=True)
    
#     st.markdown(f"""
#     <div style="
#         background-color: #2e4854; 
#         border-radius: 15px; 
#         padding: 10px 15px; 
#         margin: 5px 0; 
#         max-width: 70%; 
#         text-align: left; 
#         display: inline-block;
#     ">
#         <p style="margin: 0; font-size: 16px; line-height: 1.5;"><b>Bot:</b> {bot_message} 🤖</p>
#     </div>
#     """, unsafe_allow_html=True)
    
# # user_input = input("Enter your Prompt = ")
# # output = get_chatbot_response(user_input)

# # print(output)

# with st.form(key="chat_form", clear_on_submit=True):
#     user_input = st.text_input("", max_chars=2000)
#     submit_button = st.form_submit_button("Submit")

#     if submit_button:
#         if user_input:
#             response = get_chatbot_response(user_input)
#             st.session_state.history.append((user_input, response))
#         else:
#             st.warning("Please Enter A Prompt")

import streamlit as st
import google.generativeai as genai

# Configure the API key
GOOGLE_API_KEY = "AIzaSyDma9KsEXzewUDnLTErjwVIyR3qwcRVlD8"
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the Generative Model
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to get response from the model
def get_chatbot_response(user_input):
    response = model.generate_content(user_input)
    return response.text

# Streamlit interface
st.set_page_config(page_title="Sufyan's ChatBot", layout="centered")

st.title("✨ Sufyan's ChatBot ✨")
st.write("Powered by Google Generative AI")

if "history" not in st.session_state:
    st.session_state["history"] = []

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("", max_chars=2000)
    submit_button = st.form_submit_button("Submit")

    if submit_button and user_input:
        # Generate response immediately
        response = get_chatbot_response(user_input)
        # Append the user input and bot response to the chat history
        st.session_state.history.append((user_input, response))

# Display chat history
for user_message, bot_message in st.session_state.history:
    st.markdown(f"""
    <div style="
        background-color: #2e4854; 
        border-radius: 15px; 
        padding: 10px 15px; 
        margin: 5px 0; 
        max-width: 70%; 
        text-align: left; 
        display: inline-block;
    ">
        <p style="margin: 0; font-size: 16px; line-height: 1.5;"><b>You:</b> {user_message} 😊</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="
        background-color: #2e4854; 
        border-radius: 15px; 
        padding: 10px 15px; 
        margin: 5px 0; 
        max-width: 70%; 
        text-align: left; 
        display: inline-block;
    ">
        <p style="margin: 0; font-size: 16px; line-height: 1.5;"><b>Bot:</b> {bot_message} 🤖</p>
    </div>
    """, unsafe_allow_html=True)
