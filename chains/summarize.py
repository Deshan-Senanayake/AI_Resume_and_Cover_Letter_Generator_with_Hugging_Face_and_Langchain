from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_resume(resume_text, max_len=300):
    if not resume_text or len(resume_text.strip()) == 0:
        return "No text to summarize."

    trimmed_text = resume_text[:3000]  # Trim for BART input length
    summary = summarizer(trimmed_text, max_length=max_len, min_length=60, do_sample=False)
    return summary[0]['summary_text']
