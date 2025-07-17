import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_llm_feedback_and_score(user_resume_text, jd_text, prompt):
    model = genai.GenerativeModel("gemini-2.5-flash")

    input_parts = [
        jd_text,
        user_resume_text,
        prompt
    ]

    response = model.generate_content(input_parts, generation_config={"temperature": 0})

    # Parse LLM Response
    output = response.text

    # Extract score from LLM output (look for first number out of 100)
    import re
    score_match = re.search(r'(\d+(\.\d+)?)\s*/\s*100', output)
    if score_match:
        score = float(score_match.group(1))
    else:
        score = 50.0  # fallback

    return score, output
