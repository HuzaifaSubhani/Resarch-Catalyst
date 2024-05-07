import streamlit as st
from gtts import gTTS
import random

random_integer = random.randint(1, 1000)
def audio(data):

    language = "en"  
    speech = gTTS(text=str(data), lang=language)
    speech.save(f"output{str(random_integer)}.mp3")
    audio_bytes =open(f"output{str(random_integer)}.mp3", "rb").read()
    st.audio(audio_bytes, format="audio/mpeg")
