import streamlit as st
import os
import shutil
import PIL
from PIL import Image

image = st.upload_file("Upload an image")
if None not in (image):
    os.makedirs("temp", exist_ok=True)
    picture = Image.open(image)
    picture = picture.save(f'temp/{image.name}')
    image_file = f"temp/{image.name}" 
    data_image = Image.open(image_file)
    st.image(data_image)



