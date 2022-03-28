import streamlit as st
import os
import shutil
import PIL
import random
from PIL import Image

image = st.file_uploader("Upload an image")
if image is not None:
    os.makedirs("temp", exist_ok=True)
    picture = Image.open(image)
    width, height = picture.size
    left = 155
    top = 65
    right = 360
    bottom = 270

    im1 = picture.crop((left, top, right, bottom))
    save_name = random.random()
    im1.save(f"temp/{save_name}.jpg")

    for i in os.listdir("temp"):
        st.write(i)
    
else:
    st.warning("Please upload a file for test")

