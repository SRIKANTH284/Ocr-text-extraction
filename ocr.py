import easyocr as ocr
import streamlit as st
from PIL import Image
import numpy as np

# Title
st.title("Easy OCR - Extract Text from Images")
st.markdown("## Optical Character Recognition - Using `easyocr`, `streamlit'")
st.markdown("")

# Function to load the OCR model
@st.cache_data()
def load_model():
    reader = ocr.Reader(['en', 'hi'], model_storage_directory='.')
    return reader

# Main function to run the OCR app
def main():
    # Load the OCR model
    reader = load_model()

    # Image uploader
    image = st.file_uploader(label="Upload your image here", type=['png', 'jpg', 'jpeg'])

    if image is not None:
        # Read the uploaded image
        input_image = Image.open(image)

        # Display the image
        st.image(input_image)

        # Button to perform OCR
        if st.button("Perform OCR"):
            with st.spinner("🤖 AI is at Work!"):
                result = reader.readtext(np.array(input_image))

                result_text = []

                for text in result:
                    result_text.append(text[1])

                # Display the extracted text
                if result_text:
                    st.success("Text Extracted Successfully!")
                    st.write("\n".join(result_text))
                else:
                    st.warning("No Text Detected in the Image.")

                st.balloons()

    else:
        st.write("Upload an Image")

    st.caption("Made with ❤️ by @Srikanth284")

if __name__ == "__main__":
    main()
