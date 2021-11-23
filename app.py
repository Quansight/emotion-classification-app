import streamlit as st
import numpy as np
import en_textcat_goemotions

@st.cache(allow_output_mutation=True)
def load_model():
    return en_textcat_goemotions.load()

def classify(text):
    out = nlp(text)
    keys = list(out.cats.keys())
    values = list(out.cats.values())
    max_val = np.argmax(values)
    return keys[max_val]

nlp = load_model()

title = st.title('Classify text')
text = st.text_area('write a sentence to classify', key='text_content')

if text is not None:
    category = classify(text)
    st.markdown(f'This is {category} text')

