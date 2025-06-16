from transformers import pipeline
from templates.prompt_templates import build_cover_letter_prompt

generator = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_cover_letter(resume_summary, job_description, style="Formal"):
    prompt = build_cover_letter_prompt(resume_summary, job_description, style)
    result = generator(prompt, max_length=512)
    return result[0]['generated_text'].strip()