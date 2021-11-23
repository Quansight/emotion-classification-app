import streamlit as st


@st.cache
def load_model():
    # loads the model
    pass

def classify(text):
    pass

model = load_model()

title = st.title('Classify text')
text = st.text_area('write a sentence to classify', key='text_content')

out = classify(text)

