import streamlit as st
# import os
# import shutil
# import PIL
# from PIL import Image

# image = st.file_uploader("Upload an image")
# if image is not None:
#     os.makedirs("temp", exist_ok=True)
#     picture = Image.open(image)

#     width, height = picture.size
#     left = 155
#     top = 65
#     right = 360
#     bottom = 270

#     im1 = picture.crop((left, top, right, bottom))
#     im1.save(f"temp/result.png")

#     # image_file = f"temp/{im1}" 
#     # data_image = Image.open(im1)
#     # picture = data_image.save(f"temp/{data_image.name}")
    
# else:
#     st.warning("Please upload a file for test")

st.session_state['answer'] = ''

st.write(st.session_state)

realans = ['', 'abc', 'edf']

if  st.session_state['answer'] in realans:
    answerStat = "correct"
elif st.session_state['answer'] not in realans:
    answerStat = "incorrect"

st.write(st.session_state)
st.write(answerStat)


