import streamlit as st
import os
import google.generativeai as genai
genai.configure(api_key=os.getenv('gemini_api'))
st.title('Analyze Image with Google Gemini')
model=genai.GenerativeModel('gemini-pro-vision')
from PIL import Image
resim=st.file_uploader("Bir resim sec", type=(['jpg','jpeg','png']))
if resim is not None:
    img=Image.open(resim)
    st.image(img)
    #response=model.generate_content(img)
    #st.write(response.text)
soru=st.text_input('Soru')
if st.button('soru sor'):
    response=model.generate_content([soru,img], stream=True)
    response.resolve()
    st.write(response.text)
