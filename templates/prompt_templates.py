def build_cover_letter_prompt(summary, job_desc, style):
    return f"""Write a {style.lower()} cover letter tailored to this job description and resume:

Job Description:
{job_desc}

Resume Summary:
{summary}
"""
