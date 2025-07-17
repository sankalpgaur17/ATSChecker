import streamlit as st

def add_custom_css():
    st.markdown("""
    <style>
    .stButton>button {
        background-color: #4f46e5;
        color: white;
        padding: 12px 24px;
        border-radius: 10px;
        font-size: 16px;
        font-weight: 600;
        width: 100%;
    }

    .stTextArea textarea {
        background: #f3f4f6;
        color: #111827;
        border-radius: 12px;
        font-size: 14px;
        padding: 12px;
    }

    .stFileUploader>div>div>div {
        background: #f3f4f6;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
    }

    h1 {
        font-size: 30px;
        color: #4f46e5;
        text-align: center;
        margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True)
