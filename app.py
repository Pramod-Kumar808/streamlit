import streamlit as st
import os
import shutil
import PIL
from PIL import Image

image = st.file_uploader("Upload an image")
if image is not None:
    os.makedirs("temp", exist_ok=True)
    picture = Image.open(image)
    picture = picture.save(f'temp/{image.name}')
    image_file = f"temp/{image.name}" 
    data_image = Image.open(image_file)
    st.image(data_image)
else:
    st.warning("Please upload a file for test")



