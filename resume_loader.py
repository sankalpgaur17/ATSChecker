import os
import pdfplumber

def load_sample_resumes(folder_path="Resumes"):
    sample_texts = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            with pdfplumber.open(file_path) as pdf:
                text = ""
                for page in pdf.pages:
                    if page.extract_text():
                        text += page.extract_text()
                sample_texts.append(text)
    return sample_texts
