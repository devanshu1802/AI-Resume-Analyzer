import google.generativeai as genai

# ---------------- API KEY ---------------- #

GEMINI_API_KEY = "AIzaSyAHAbiA2aHqIgCyiHgfswE8l7ceIgV6N7k"

genai.configure(api_key=GEMINI_API_KEY)

# Lightweight model
model = genai.GenerativeModel(
    "models/gemini-2.0-flash-lite"
)

# ---------------- AI FEEDBACK ---------------- #

def get_resume_feedback(resume_text):

    prompt = f"""
    Analyze this resume professionally.

    Give:
    1. Summary
    2. Strengths
    3. Weaknesses
    4. Missing Skills
    5. ATS Tips

    Resume:
    {resume_text[:800]}
    """

    try:

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"Error Generating AI Feedback: {e}"