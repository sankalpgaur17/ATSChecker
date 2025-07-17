import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(input_text, user_pdf_content, sample_resume_contents, prompt):
    model = genai.GenerativeModel("gemini-2.5-flash")

    input_parts = [input_text, user_pdf_content[0]]
    input_parts.extend(sample_resume_contents)  # Can be empty if not needed
    input_parts.append(prompt)

    response = model.generate_content(input_parts, generation_config={"temperature": 0})

    return response.text

