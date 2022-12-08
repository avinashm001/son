import streamlit as st
import pandas as pd
import base64
from PIL import Image

st.title("HELLO SEXY")
st.header("media files")


st.markdown('''
This the video source of porn collection :[meganz](https://mega.nz/fm/7lFmQRha)''')


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://erowall.com/download_img.php?dimg=32974&raz=2560x1600.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

