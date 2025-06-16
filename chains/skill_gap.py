import re
import inflect
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from rapidfuzz import fuzz

# ✅ Define commonly used skills
COMMON_SKILLS = [
    "python", "sql", "machine learning", "deep learning", "data science",
    "data analysis", "data scientist", "tensorflow", "pandas", "numpy", "matplotlib",
    "nlp", "big data", "excel", "communication", "leadership"
]

# ✅ For potential future use (not used directly right now)
p = inflect.engine()
def normalize_word(word):
    if p.singular_noun(word):
        return p.singular_noun(word)
    return word

# ✅ Normalize text for consistent matching
def normalize_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)  # replace punctuation with space
    text = re.sub(r"\s+", " ", text).strip()
    return text

# ✅ Use fuzzy logic to extract matching skills
def extract_skills(text, skills_list=COMMON_SKILLS, threshold=85):
    text = normalize_text(text)
    found = []
    for skill in skills_list:
        score = fuzz.partial_ratio(skill, text)
        if score >= threshold:
            found.append(skill)
    return list(set(found))

# ✅ Get matched and missing skills
def get_skill_overlap(resume_summary, job_description):
    resume_skills = set(extract_skills(resume_summary))
    job_skills = set(extract_skills(job_description))

    matched = sorted(resume_skills & job_skills)
    missing = sorted(job_skills - resume_skills)

    return matched, missing

# ✅ Calculate cosine similarity
def calculate_similarity(resume_summary, job_description):
    resume_summary = normalize_text(resume_summary)
    job_description = normalize_text(job_description)

    vectorizer = CountVectorizer().fit_transform([resume_summary, job_description])
    vectors = vectorizer.toarray()
    similarity = cosine_similarity(vectors)[0][1]
    return round(similarity * 100, 2)
