import os
from pdf_utils import extract_text_from_pdf


def load_reference_resumes(folder_path="Resumes"):
    patterns = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            with open(os.path.join(folder_path, filename), "rb") as f:
                text = extract_text_from_pdf(f)
                sections = {
                    "has_summary": "Summary" in text or "Profile" in text,
                    "has_skills": "Skills" in text,
                    "has_projects": "Projects" in text,
                    "has_education": "Education" in text,
                    "length": len(text)
                }
                patterns.append(sections)
    return patterns


def check_resume_format(user_text, reference_patterns):
    format_score = 0
    total_checks = 4

    user_sections = {
    "has_summary": any(section in user_text for section in ["Summary", "summary", "Profile", "profile", "About Me", "about me", "Professional Summary", "professional summary"]),
    
    "has_skills": any(section in user_text for section in ["Skills", "skills", "Technical Skills", "technical skills", "Core Competencies", "core competencies", "Technologies", "technologies"]),
    
    "has_projects": any(section in user_text for section in ["Projects", "projects", "Project Experience", "project experience", "Technical Projects", "technical projects", "Relevant Projects", "relevant projects"]),
    
    "has_education": any(section in user_text for section in ["Education", "education", "Academic Background", "academic background", "Educational Qualifications", "educational qualifications", "Academics", "academics"]),
    
    "has_experience": any(section in user_text for section in ["Experience", "experience", "Work Experience", "work experience", "Professional Experience", "professional experience", "Employment History", "employment history"]),
    
    "has_certifications": any(section in user_text for section in ["Certifications", "certifications", "Licenses & Certifications", "licenses & certifications", "Certification", "certification"]),
    
    "has_achievements": any(section in user_text for section in ["Achievements", "achievements", "Awards", "awards", "Honors", "honors"]),
    
    "has_contact_info": any(section in user_text for section in ["Contact", "contact", "Contact Info", "contact info", "Personal Details", "personal details", "Details", "details"]),
}


    for sec in user_sections:
        match_count = sum(1 for ref in reference_patterns if ref[sec])
        if user_sections[sec] and match_count > 0:
            format_score += 1

    return round((format_score / total_checks) * 100, 2)
