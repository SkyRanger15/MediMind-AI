import streamlit as st
from chat import analyze_image

st.set_page_config(page_title="Medical Image Analysis Chatbot", layout="wide")

st.title("MediMind: Your Personal Medical Image Analysis Chatbot")

st.header("Image Upload and Analysis")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

submit_button = st.button("Analyze Image")

if submit_button and uploaded_file is not None:
    image, analysis = analyze_image(uploaded_file)
    
    # Display the image
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Display the response
    st.write("Analysis:")
    st.write(analysis)

st.sidebar.header("About")
st.sidebar.info("PBL Project By Soumyajit")
