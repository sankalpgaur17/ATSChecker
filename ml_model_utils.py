import os
import pdfplumber
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

def extract_resume_text(folder):
    texts = []
    for file in os.listdir(folder):
        if file.endswith(".pdf"):
            path = os.path.join(folder, file)
            with pdfplumber.open(path) as pdf:
                text = ""
                for page in pdf.pages:
                    if page.extract_text():
                        text += page.extract_text()
                texts.append(text)
    return texts

def train_ml_model():
    pos_texts = extract_resume_text("Resumes")   # Good Resumes
    neg_texts = extract_resume_text("ResumeB")   # Bad Resumes

    X = pos_texts + neg_texts
    y = [1]*len(pos_texts) + [0]*len(neg_texts)

    vectorizer = TfidfVectorizer(stop_words='english', max_features=500)
    model = LogisticRegression(max_iter=1000)

    X_vect = vectorizer.fit_transform(X)
    model.fit(X_vect, y)

    return model, vectorizer

def get_ml_format_score(resume_text, model, vectorizer):
    X_test = vectorizer.transform([resume_text])
    prob = model.predict_proba(X_test)[0][1]  # Probability of being 'good'

    # Apply soft calibration to reduce strictness
    boosted_prob = min(1.0, prob * 1.2 + 0.1)  # Push scores higher but cap at 1.0

    ml_score = round(boosted_prob * 100, 2)

    # Print ML score in console
    print(f"[ML Model] Formatting/Structure Score (Boosted): {ml_score}/100")

    return ml_score

