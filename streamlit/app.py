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
             background-image: url("https://photo.xmissy.nl/pictures/babescom1301/20180703-2835920_LanaRhoades_RickyJohnson_FitnessFinesse_pics_xm/033.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

