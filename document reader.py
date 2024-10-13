import streamlit as st
from PIL import Image
import google.generativeai as genai

GOOGLE_API_KEY = "google-api-key"
genai.configure(api_key=GOOGLE_API_KEY)
model= genai.GenerativeModel('gemini-1.5-flash')


def get_gemini_response(input,image,user_prompt):
    responce=model.generate_content([input,image[0],user_prompt])
    return responce.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("no file uploaded")

st.set_page_config(page_title="multilanguage invoice extractor")
st.header("multilanguage invoice extractor")
input=st.text_input("input prompt : " , key="input")
uploaded_file = st.file_uploader("choose an image of the invoice ...",type=["jpg","jpeg","png","webp"])



submit=st.button("tell me about the invoice")
input_prompt="""
     you are an expert in understanding invoices. we will upload a image as invoice and you will have to answer any questions based on the uploaded invoice image
"""

if submit:
    image_data=input_image_details(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("the response is")
    st.write(response)


    





