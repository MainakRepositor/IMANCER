import streamlit as st
import numpy as np
from PIL import Image
import webbrowser
import cv2

def dodgeV2(x, y):
    return cv2.divide(x, 255 - y, scale=256)

def pencilsketch(inp_img):
    img_gray = cv2.cvtColor(inp_img, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
    final_img = dodgeV2(img_gray, img_smoothing)
    return(final_img)


st.title("PICASSO NET")
st.write("Convert you photos into lovely pencil sketches")

file_image = st.sidebar.file_uploader("Upload your Photos", type=['jpeg','jpg','png'])

if file_image is None:
    st.warning("You haven't uploaded any image file")

else:
    input_img = Image.open(file_image)
    final_sketch = pencilsketch(np.array(input_img))
    st.write("**Input Photo**")
    st.image(input_img, use_column_width=True)
    st.write("**Output Pencil Sketch**")
    st.image(final_sketch, use_column_width=True)
    if st.button("Download Sketch Images"):
        im_pil = Image.fromarray(final_sketch)
        im_pil.save('final_image.jpeg')
        st.success('Your download is completed!')
        
url = 'https://www.linkedin.com/in/mainak-chaudhuri-127898176/'
if st.button('Made with 💖 by Mainak Chaudhuri'):
    webbrowser.open_new_tab(url)