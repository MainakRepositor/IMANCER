# Core Pkgs
import streamlit as st 
import cv2
from PIL import Image,ImageEnhance,ImageOps
import numpy as np 
import os

@st.cache
def load_image(img):
	im = Image.open(img)
	return im





def cartonize_image(our_image):
	new_img = np.array(our_image.convert('RGB'))
	img = cv2.cvtColor(new_img,1)
	gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
	# Edges
	gray = cv2.medianBlur(gray, 5)
	edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
	#Color
	color = cv2.bilateralFilter(img, 9, 300, 300)
	#Cartoon
	cartoon = cv2.bitwise_and(color, color, mask=edges)

	return cartoon


def cannize_image(our_image):
	new_img = np.array(our_image.convert('RGB'))
	img = cv2.cvtColor(new_img,1)
	img = cv2.GaussianBlur(img, (11, 11), 0)
	canny = cv2.Canny(img, 100, 150)
	return canny

def main():
	

	st.title("📷 IMANCER 🖼")
	st.markdown('''***Your personal image enhancer***''')
	

	activities = ["Enhancer","Documentation","About"]
	choice = st.sidebar.selectbox("Navigator",activities)

	if choice == 'Enhancer':
		st.subheader("Enhanced Imaging")

		image_file = st.file_uploader("Upload Image",type=['jpg','png','jpeg'])

		if image_file is not None:
			col1,col2 = st.beta_columns(2)
			our_image = Image.open(image_file)
			col1.header("Original Image")
			# st.write(type(our_image))
			col1.image(our_image)
			
			enhance_type = st.sidebar.radio("Enhancement Type ",["Original","Gray-Scale","Contrast","Brightness","Blurring","Negative"])
			if enhance_type == 'Gray-Scale':
				new_img = np.array(our_image.convert('RGB'))
				img = cv2.cvtColor(new_img,1)
				gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
				# st.write(new_img)
				col2.header('Gray-scale Image')
				col2.image(gray)
			elif enhance_type == 'Contrast':
				c_rate = st.sidebar.slider("Contrast",0.5,3.5)
				enhancer = ImageEnhance.Contrast(our_image)
				img_output = enhancer.enhance(c_rate)
				col2.header('Contrast Modulated Image')
				col2.image(img_output)

			elif enhance_type == 'Brightness':
				c_rate = st.sidebar.slider("Brightness",0.5,3.5)
				enhancer = ImageEnhance.Brightness(our_image)
				img_output = enhancer.enhance(c_rate)
				col2.header('Brightness Editted Image')
				col2.image(img_output)

			elif enhance_type == 'Blurring':
				new_img = np.array(our_image.convert('RGB'))
				blur_rate = st.sidebar.slider("Brightness",0.5,3.5)
				img = cv2.cvtColor(new_img,1)
				blur_img = cv2.GaussianBlur(img,(11,11),blur_rate)
				col2.header('Blur Modulated Image')
				col2.image(blur_img)
    
			elif enhance_type == 'Negative':
       			
				new_img = np.array(our_image.convert('RGB'))
				img = cv2.cvtColor(new_img,1)
				neg = 255 - (cv2.cvtColor(img,cv2.COLOR_BGR2GRAY))
				# st.write(new_img)
				col2.header('Negative-Filmed Image')
				col2.image(neg)

			
			elif enhance_type == 'Original':
				col2.header('Original Image')
				col2.image(our_image)
			else:
				col2.header('Original Image')
				col2.image(our_image)


	
		task = ["Pencil Sketch","Cannize","Cartonize"]
		feature_choice = st.sidebar.selectbox("Generator 🎨",task)
		if st.button("Process"):

			if feature_choice == 'Pencil Sketch':
				st.markdown('''**Pencil Sketch**''')
			
				new_img = np.array(our_image.convert('RGB'))
				img = cv2.cvtColor(new_img,1)
				gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
				inv_gr_img = 255 - gray
				bi = cv2.GaussianBlur(inv_gr_img, (21,21), 0)
				inv_bl = 255 - bi
				pencil_sk = cv2.divide(gray, inv_bl, scale = 256.0)
				result_img = pencil_sk
				st.image(result_img,width=260)
			
				
			elif feature_choice == 'Cartonize':
				st.markdown('''**Cartonized**''')
				result_img = cartonize_image(our_image)
				st.image(result_img,width=260)

			elif feature_choice == 'Cannize':
				st.markdown('''**Cannized**''')
				result_canny = cannize_image(our_image)
				st.image(result_canny,width=260)

	elif choice == 'Documentation':
		st.subheader('Know how it works')
		st.markdown('''IMANCER is a best in class image enhancer and pencil sketch maker. It is made using two powerful Python libaries, Streamlit and OpenCV. IMANCER ensures to provide it's users with fast image enhancement, pencil sketch generation  and much more features.''')
		st.markdown('''It is quite simple to work with IMANCER. Just upload your favourite image in the app, choose your favourable image operations like gray-scaling, manipulating contrast, brightness, blur etc. and let IMANCER do it's job. To make a pencil sketch, select pencil sketch from Generator menu and click Process. You will get the thing ready. Take a screenshot or download your sketch and show to the world! ''')
     


	elif choice == 'About':
		st.subheader("About Face Detection App")
		st.markdown("Built with Streamlit by [Mainak Chaudhuri](https://www.github.com/MainakRepositor)")
		st.success("</Developer.Coder.Data Science Enthusiast>")



if __name__ == '__main__':
		main()	