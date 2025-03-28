import streamlit as st


st.markdown("""
    <style>
        .stTextInput>div>div>input {
            background-color: #f0f8ff;
            color: #333;
            border-radius: 10px;
            padding: 10px;
            font-size: 16px;
        }
        .stNumberInput>div>div>input {
            background-color: #f0f8ff;
            color: #333;
            border-radius: 10px;
            padding: 10px;
            font-size: 16px;
        }
        .stTextArea>div>textarea {
            background-color: #f0f8ff;
            color: #333;
            border-radius: 10px;
            padding: 10px;
            font-size: 16px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            border-radius: 10px;
            padding: 10px 20px;
            border: none;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Form for feedback")
st.write('write your impression to give us a the opportunity to improuve.')

with st.form(key='feedback form'):
    name=st.text_input('Enter your name: ')
    grade=st.slider('Enter your mark (o to 5):',0,5,3)
    feedback=st.text_area('Enter your feedback (max 500 charts):',
                           max_chars= 500)
    button=st.form_submit_button(label='Submit')

if button:
    st.write('Your grade is: ',grade)
    if grade<=2:
        st.write('Warning the app need to be refined')
    elif grade>=4:
        st.write('You do a great job')
    else:
        st.write('Good, but you can improve')

