import streamlit as st
import os
import shutil
import PIL
from PIL import Image

image = st.file_uploader("Upload an image")
if image is not None:
    os.makedirs("temp", exist_ok=True)
    picture = Image.open(image)

    width, height = picture.size
    left = 5
    top = height / 4
    right = 164
    bottom = 3 * height / 4

    im1 = picture.crop((left, top, right, bottom))
    picture = picture.save(f"temp/{im1}")

    # image_file = f"temp/{im1}" 
    # data_image = Image.open(image_file)
    # st.image(data_image)
    
else:
    st.warning("Please upload a file for test")



