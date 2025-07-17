import streamlit as st


def add_custom_css():
    st.markdown("""
    <style>
    .main-card {
        background-color: #ffffff;
        padding: 40px;
        margin: 40px auto;
        max-width: 800px;
        border-radius: 16px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }

    .section-title {
        font-size: 20px;
        font-weight: 600;
        color: #4f46e5;
        margin-bottom: 15px;
        margin-top: 25px;
    }

    .stTextArea textarea, .stFileUploader>div>div>div {
        background: #f3f4f6;
        color: #111827;
        border-radius: 12px;
        border: 1px solid #d1d5db;
        font-size: 14px;
    }

    .stButton>button {
        background-color: #4f46e5;
        color: white;
        padding: 10px 24px;
        border-radius: 10px;
        font-size: 16px;
        font-weight: 600;
        border: none;
    }

    .stButton>button:hover {
        background-color: #4338ca;
    }
    </style>
    """, unsafe_allow_html=True)
