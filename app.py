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
st.sidebar.info(
     """
    **Steps to Analyze a Medical Image:**
    
    1. **Upload Image**: Click on 'Choose an image' and select a medical image (JPG, JPEG, or PNG format).
    2. **Analyze**: Once uploaded, click on the 'Analyze Image' button to get insights on the image.
    3. **Review Analysis**: The uploaded image and the chatbot's analysis will be displayed below.

    **Important Notes:**
    - Ensure the image is clear and in a proper resolution.
    - Supported file formats: JPG, JPEG, PNG.
    - Please avoid uploading unrelated or low-quality images for better results.
    """
)
