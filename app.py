import streamlit as st
import plotly.express as px
import pandas as pd

from resume_parser import extract_text
from utils import extract_skills
from ats_score import calculate_ats
from jd_matcher import match_resume
from interview_questions import generate_questions
from gemini_ai import get_resume_feedback

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🚀",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

body {
    background-color: #0E1117;
}

.main {
    background: linear-gradient(to right, #0F172A, #111827);
}

.block-container {
    padding-top: 2rem;
}

h1, h2, h3 {
    color: white;
}

.skill-box {
    background: linear-gradient(135deg, #00FFA3, #03E1FF);
    color: black;
    padding: 10px 18px;
    border-radius: 25px;
    margin: 5px;
    display: inline-block;
    font-weight: bold;
    font-size: 14px;
}

.resume-box {
    background-color: rgba(255,255,255,0.05);
    backdrop-filter: blur(12px);
    padding: 25px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.1);
    color: white;
    line-height: 1.8;
    max-height: 400px;
    overflow-y: auto;
}

.metric-card {
    background-color: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
    border: 1px solid rgba(255,255,255,0.08);
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("🚀 AI Resume Analyzer")

st.sidebar.info(
    "Upload your resume and get AI-powered analysis, ATS scoring, job matching, and interview preparation."
)

st.sidebar.markdown("---")

st.sidebar.write("### Features")
st.sidebar.write("✅ ATS Score")
st.sidebar.write("✅ Skill Detection")
st.sidebar.write("✅ Job Matching")
st.sidebar.write("✅ AI Feedback")
st.sidebar.write("✅ Interview Questions")

# ---------------- TITLE ---------------- #

st.title("🚀 AI Resume Analyzer & Interview Coach")

st.write(
    "Analyze resumes using AI, NLP, ATS scoring, and Gemini-powered feedback."
)

# ---------------- FILE UPLOAD ---------------- #

uploaded_file = st.file_uploader(
    "📄 Upload Resume PDF",
    type=["pdf"]
)

# ---------------- MAIN ---------------- #

if uploaded_file is not None:

    st.success("✅ Resume Uploaded Successfully")

    # Extract text
    text = extract_text(uploaded_file)

    if text.strip():

        clean_text = " ".join(text.split())

        # ---------------- RESUME PREVIEW ---------------- #

        st.subheader("📑 Resume Preview")

        st.markdown(
            f"""
            <div class="resume-box">
            {clean_text}
            </div>
            """,
            unsafe_allow_html=True
        )

        # ---------------- SKILLS ---------------- #

        skills = extract_skills(clean_text)

        st.subheader("🛠 Detected Skills")

        if skills:

            skill_html = ""

            for skill in skills:
                skill_html += f'<span class="skill-box">{skill.upper()}</span>'

            st.markdown(skill_html, unsafe_allow_html=True)

        else:
            st.warning("No skills detected.")

        # ---------------- CHART ---------------- #

        st.subheader("📈 Skills Visualization")

        skill_data = pd.DataFrame({
            "Skill": skills,
            "Value": [1] * len(skills)
        })

        fig = px.bar(
            skill_data,
            x="Skill",
            y="Value",
            color="Skill",
            title="Detected Skills"
        )

        st.plotly_chart(fig, use_container_width=True)

        # ---------------- ATS SCORE ---------------- #

        score = calculate_ats(skills)

        st.subheader("📊 ATS Score")

        st.progress(int(score))

        # ---------------- DASHBOARD METRICS ---------------- #

        col1, col2, col3 = st.columns(3)

        col1.metric("Skills Found", len(skills))
        col2.metric("ATS Score", f"{score}%")
        col3.metric(
            "Resume Level",
            "Strong" if score >= 60 else "Average"
        )

        # ---------------- JOB DESCRIPTION ---------------- #

        st.subheader("💼 Job Description Matching")

        job_description = st.text_area(
            "Paste Job Description",
            height=200
        )

        if job_description:

            match_score = match_resume(
                clean_text,
                job_description
            )

            st.subheader("🎯 Resume Match Score")

            st.progress(int(match_score))

            st.success(f"Match Score: {match_score}%")

        # ---------------- GEMINI AI FEEDBACK ---------------- #

        st.subheader("🤖 Gemini AI Resume Review")

        if st.button("Generate AI Feedback"):

            with st.spinner("Analyzing Resume with Gemini AI..."):

                feedback = get_resume_feedback(clean_text)

                st.markdown(feedback)

        # ---------------- INTERVIEW QUESTIONS ---------------- #

        st.subheader("🎤 AI Interview Questions")

        questions = generate_questions(skills)

        if questions:

            for i, question in enumerate(questions, 1):
                st.write(f"{i}. {question}")

        else:
            st.warning("No interview questions generated.")

    else:
        st.warning("⚠ No readable text found in PDF.")

