import streamlit as st
import os
import shutil
import PIL
import random
from PIL import Image
import cv2

image = st.file_uploader("Upload an image")
if image is not None:
    picture = cv2.imerad(image)
    st.success("uplodaed")
    
else:
    st.warning("Please upload a file for test")

