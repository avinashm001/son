import streamlit as st
import pandas as pd
import base64
from PIL import Image

st.title("HELLO SEXY")
st.header("media files")


st.markdown('''
This the video source of porn collection :[meganz](https://mega.nz/fm/7lFmQRha)''')


import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('t.jpg') 

