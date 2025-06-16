📄 AI Resume & Cover Letter Generator
An AI-powered web application that analyzes your resume, summarizes your experience, and generates personalized cover letters — all in one place. Built with 💡 LangChain, 🤖 Hugging Face Transformers, and 🌐 Streamlit.

🚀 Features
📤 Upload your resume in PDF format

🔍 Extract and summarize your resume using an LLM

📄 Paste a job description to match against your profile

✍️ Generate tailored cover letters in 3 styles: Formal, Creative, or Concise

🧠 Skill match analysis (Matched vs Missing Skills)

📥 Download your cover letter as a professional PDF

🛠️ Tech Stack
Layer	                  Technology
👨‍💻 Frontend---------------Streamlit
🤖 AI/LLM Models----------Falcon-7B-Instruct / Hugging Face Pipelines
🔗 LLM Wrappers-----------LangChain
📄 PDF Handling-----------PyMuPDF (fitz), FPDF
🧠 Skill Matching---------Scikit-learn, RapidFuzz

resume-cover-gen/
├── app.py
├── chains/
│   ├── summarize.py
│   ├── generate_letter.py
├── utils/
│   ├── pdf_utils.py
│   ├── skill_gap.py
│   ├── pdf_writer.py
├── models/
│   └── model_loader.py



🧪 Setup Instructions
1. Clone this repo
git clone https://github.com/your-username/resume-cover-gen.git
cd resume-cover-gen

2. Create & activate a virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows

3.Install dependencies
pip install -r requirements.txt

4.Run the app
streamlit run app.py


🧾 Sample Usage
Upload your resume (PDF)

Paste any job description

Click "Summarize Resume" ➜ View extracted summary

Select cover letter style ➜ Click "Generate Cover Letter"

Download it as PDF 🎉


Dependencies

streamlit
langchain
transformers
huggingface_hub
scikit-learn
rapidfuzz
fpdf
PyMuPDF
inflect

🔧 Install all with:

pip install -r requirements.txt


📌 Future Enhancements
📊 Skill gap insights chart

🧠 Skill recommendations based on missing skills

📝 Resume optimizer suggestions

🌐 Multi-language support

🙌 Contributors
Deshan Senanayake – GitHub

Model credits: Hugging Face

📃 License
This project is licensed under the MIT License.

