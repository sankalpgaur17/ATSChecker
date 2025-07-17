import pdfplumber

def extract_text_from_pdf(uploaded_pdf):
    text = ""
    with pdfplumber.open(uploaded_pdf) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text()
    return text
