import streamlit as st
from src.pdf_extractor import extract_text_from_pdf
from src.preprocessing import preprocess
from src.skill_extractor import load_skills, extract_skills

st.set_page_config(page_title="Resume Skill Extractor", layout="centered")

st.title("📄 Resume Skill Extractor")
st.write("Upload your resume and extract skills using NLP.")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file:
    with st.spinner("Processing..."):
        text = extract_text_from_pdf(uploaded_file)
        clean_text = preprocess(text)

        skills_list = load_skills("data/skills_list.txt")
        skills = extract_skills(clean_text, skills_list)

    st.success("Done!")

    st.subheader("✅ Extracted Skills")

    if skills:
        st.write(", ".join(skills))
    else:
        st.warning("No skills found.")

    with st.expander("Show processed text"):
        st.write(clean_text[:1000])
