skills_db = [
    "python",
    "java",
    "c++",
    "html",
    "css",
    "javascript",
    "sql",
    "mysql",
    "machine learning",
    "data analysis",
    "power bi",
    "excel",
    "tableau",
    "streamlit",
    "ai",
    "nlp"
]

def extract_skills(text):

    found_skills = []

    text = text.lower()

    for skill in skills_db:

        if skill in text:
            found_skills.append(skill)

    return found_skills