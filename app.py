from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from frontend_utils import add_custom_css
from pdf_utils import extract_text_from_pdf
from gemini_utils import get_llm_feedback_and_score
from ml_model_utils import train_ml_model, get_ml_format_score
from prompts import input_prompt3

st.set_page_config(page_title="Hybrid ATS Resume Checker", page_icon="📝", layout="centered")
add_custom_css()

st.markdown("<h1 style='text-align:center;color:#4f46e5;'>Hybrid ATS Resume Checker</h1>", unsafe_allow_html=True)

# Load ML model
ml_model, vectorizer = train_ml_model()

jd_option = st.radio("Job Description Input", ["Type JD", "Upload JD PDF"])

if jd_option == "Type JD":
    jd_text = st.text_area("Paste the Job Description here", height=200)
else:
    jd_pdf = st.file_uploader("Upload JD PDF", type=["pdf"])
    jd_text = ""
    if jd_pdf is not None:
        jd_text = extract_text_from_pdf(jd_pdf)
        st.success("Job Description extracted successfully!")

uploaded_resume = st.file_uploader("Upload Your Resume (PDF)", type=["pdf"])

if st.button("Check ATS Score"):
    if uploaded_resume is not None and jd_text.strip() != "":
        user_resume_text = extract_text_from_pdf(uploaded_resume)

        # ML Format Score (structure, sections, formatting)
        ml_format_score = get_ml_format_score(user_resume_text, ml_model, vectorizer)

        # LLM JD Match Score (semantic matching)
        llm_score, llm_feedback = get_llm_feedback_and_score(user_resume_text, jd_text, input_prompt3)

        # Hybrid Score
        final_score = round((0.2 * ml_format_score) + (0.8 * llm_score), 2)

        st.subheader(f"Final ATS Score: {final_score} / 100")
        st.markdown(llm_feedback, unsafe_allow_html=True)

    else:
        st.error("Please upload both Resume and Job Description.")
