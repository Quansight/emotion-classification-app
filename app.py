import streamlit as st
import numpy as np
import en_textcat_goemotions

# emojis for the fans
emojis = {
    'admiration': ':raised_hands:',
    'amusement': ':koala:',
    'anger': ':bomb:',
    'annoyance': ':sweat:',
    'approval': ':watermelon:',
    'caring': ':pineapple:',
    'confusion': ':bowtie:',
    'curiosity': ':banana:',
    'desire': ':wink:',
    'disgust': ':fries:',
    'embarressment': ':lemon:',
    'excitement': ':beer:',
    'fear': ':tiger2:',
    'gratitude': ':evergreen_tree:',
    'grief': ':snowflake:',
    'joy': ':meat_on_bone:',
    'love': ':sunflower:',
    'nervousness': ':ocean:',
    'optimism': ':crocodile:',
    'pride': ':grapes:',
    'realization': ':christmas_tree:',
    'relief': ':guitar:',
    'remorse': ':rose:',
    'sadness': ':purple_heart:',
    'surprise': ':cactus:',
    'neutral': ':camel:',
}

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

title = st.title(':watermelon: Emotion Detection :watermelon:')
text = st.text_area('write a sentence to classify', key='text_content')

if text is not None:
    category = classify(text)
    st.markdown(f'{emojis[category]} {category} {emojis[category]}')

