import pdfplumber
import io
import base64
from PIL import Image
import pdf2image


def extract_text_from_pdf(uploaded_pdf):
    text = ""
    with pdfplumber.open(uploaded_pdf) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text()
    return text


def input_pdf_setup(uploaded_file):
    images = pdf2image.convert_from_bytes(uploaded_file.read())
    first_page = images[0]
    img_byte_arr = io.BytesIO()
    first_page.save(img_byte_arr, format='JPEG')
    img_byte_arr = img_byte_arr.getvalue()

    return [{
        "mime_type": "image/jpeg",
        "data": base64.b64encode(img_byte_arr).decode(),
    }]
