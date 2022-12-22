from tkinter.ttk import Style
import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.title("Welcome to the page👋🏻 ")
st.caption("🥂")
###background image
from PIL import Image
image = Image.open('image.jpg')

st.image(image)