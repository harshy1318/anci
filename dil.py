import streamlit as st
from PIL import Image
import pytesseract
from googletrans import Translator

st.set_page_config(
    page_title="Image Translator",
    page_icon="🖼️",
    layout="centered"
)

st.title("🖼️ Image to Hindi Translator")
st.write("Upload an image containing English text and get Hindi translation")

translator = Translator()

uploaded_image = st.file_uploader(
    "Upload Image (English Text)",
    type=["png", "jpg", "jpeg"]
)

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("Reading text from image..."):
        extracted_text = pytesseract.image_to_string(image)

    st.subheader("📄 Extracted English Text")
    st.write(extracted_text if extracted_text else "No text detected")

    if extracted_text.strip():
        with st.spinner("Translating to Hindi..."):
            translated = translator.translate(extracted_text, src="en", dest="hi")

        st.subheader("🇮🇳 Hindi Translation")
        st.success(translated.text)
