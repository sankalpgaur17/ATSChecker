
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from frontend_utils import add_custom_css
from pdf_utils import extract_text_from_pdf, input_pdf_setup
from gemini_utils import get_gemini_response
from prompts import input_prompt1, input_prompt3
from resume_reference_utils import load_reference_resumes, check_resume_format

st.set_page_config(page_title="ATS Resume Checker", page_icon="📝", layout="centered")
add_custom_css()

# Load reference resumes for format checking
reference_patterns = load_reference_resumes()

# App Title
st.markdown("""
    <div class="main-card">
        <h1 style="text-align: center; color: #4f46e5; margin-bottom: 30px;">ATS Resume Checker</h1>
""", unsafe_allow_html=True)

# Job Description Input
st.markdown("""
    <div class="section-title">Job Description</div>
""", unsafe_allow_html=True)

jd_option = st.radio("Select Input Method", ["Type JD", "Upload JD PDF"])

if jd_option == "Type JD":
    jd_text = st.text_area("Paste the Job Description here", height=200)
else:
    jd_pdf = st.file_uploader("Upload JD PDF", type=["pdf"])
    jd_text = ""
    if jd_pdf is not None:
        jd_text = extract_text_from_pdf(jd_pdf)
        st.success("Job Description extracted successfully!")

# Resume Upload
st.markdown("""
    <div class="section-title">Resume Upload</div>
""", unsafe_allow_html=True)

uploaded_resume = st.file_uploader("Upload Your Resume (PDF)", type=["pdf"])

# Action Buttons
col1, col2 = st.columns(2)

with col1:
    check_score = st.button("Resume Score Checker")

with col2:
    tell_about_resume = st.button("Tell me about the Resume")

st.markdown("</div>", unsafe_allow_html=True)  # Close main-card

# Processing Logic
if uploaded_resume is not None and jd_text.strip() != "":
    resume_text = extract_text_from_pdf(uploaded_resume)
    user_pdf_content = input_pdf_setup(uploaded_resume)

    if check_score:
        # Format score from reference resumes
        format_score = check_resume_format(resume_text, reference_patterns)

        # JD match score from LLM
        llm_response = get_gemini_response(jd_text, user_pdf_content, [], input_prompt3)

        st.subheader("ATS Match Result")
        st.write(f"**Formatting Score:** {format_score} / 100")
        st.markdown(llm_response, unsafe_allow_html=True)

    if tell_about_resume:
        llm_response = get_gemini_response(jd_text, user_pdf_content, [], input_prompt1)
        st.subheader("Resume Insights")
        st.markdown(llm_response, unsafe_allow_html=True)
else:
    if check_score or tell_about_resume:
        st.error("Please upload both Resume and Job Description.")