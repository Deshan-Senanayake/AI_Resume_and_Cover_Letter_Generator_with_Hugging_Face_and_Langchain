import streamlit as st
from chains.generate_letter import generate_cover_letter
from utils.pdf_utils import extract_text_from_pdf
from chains.summarize import summarize_resume
from chains.skill_gap import get_skill_overlap, calculate_similarity  # ✅ NEW
from utils.pdf_writer import generate_pdf

st.set_page_config(page_title="AI Resume & Cover Letter Generator", layout="centered")
st.title("📄 AI Resume & Cover Letter Generator")

# === PHASE 1: Upload & Extract Resume ===
uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")
job_desc = st.text_area("Paste the Job Description")

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)
    if resume_text:
        st.session_state['resume_text'] = resume_text
        st.success("✅ Resume text extracted!")
        st.subheader("Extracted Resume Text")
        st.write(resume_text)
    else:
        st.error("❌ Failed to extract text from PDF.")

# === Restore from session if available ===
resume_text = st.session_state.get('resume_text', None)
summary = st.session_state.get('summary', None)
cover_letter = st.session_state.get('cover_letter', None)

# === PHASE 2: Summarize Resume ===
if resume_text and st.button("🔍 Summarize Resume"):
    summary = summarize_resume(resume_text)
    st.session_state['summary'] = summary

# === Show Resume Summary & Cover Letter UI ===
if summary:
    st.subheader("Resume Summary")
    st.write(summary)

    style = st.selectbox("Select Cover Letter Style", ["Formal", "Creative", "Concise"])

    if st.button("✉️ Generate Cover Letter"):
        if not job_desc:
            st.warning("⚠️ Please paste a job description to generate a tailored cover letter.")
        else:
            with st.spinner("Generating cover letter..."):
                cover_letter = generate_cover_letter(summary, job_desc, style)
                st.session_state['cover_letter'] = cover_letter
                st.success("✅ Cover letter generated!")

# === PHASE 2: Display Generated Cover Letter ===
if cover_letter:
    st.subheader("Generated Cover Letter")
    st.write(cover_letter)

    if st.button("📥 Download as PDF"):
        pdf_path = generate_pdf(cover_letter)
        with open(pdf_path, "rb") as file:
            st.download_button(
                label="⬇️ Download Cover Letter PDF",
                data=file,
                file_name="cover_letter.pdf",
                mime="application/pdf"
            )

# === PHASE 2.3: Skill Gap Analysis ===
from chains.skill_gap import get_skill_overlap, calculate_similarity

# After generating the cover letter:
if summary and job_desc:
    matched_skills, missing_skills = get_skill_overlap(summary, job_desc)
    similarity_score = calculate_similarity(summary, job_desc)

    # Display Skill Match Report
    st.markdown("### 📊 Skill Match Report")
    st.markdown(f"**Similarity Score:** {similarity_score}%")

    st.markdown("#### 🟢 Matched Skills:")
    if matched_skills:
        st.write(matched_skills)
    else:
        st.markdown("_None_")

    st.markdown("#### 🔴 Missing Skills:")
    if missing_skills:
        st.write(missing_skills)
    else:
        st.markdown("_None_")


