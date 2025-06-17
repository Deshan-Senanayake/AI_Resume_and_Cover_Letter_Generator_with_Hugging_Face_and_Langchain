# 📄 AI Resume & Cover Letter Generator

An AI-powered web application that analyzes your resume, summarizes your experience, and generates tailored cover letters — all in one place.

Built with 💡 **LangChain**, 🤖 **Hugging Face Transformers**, and 🌐 **Streamlit**.

---

## ✨ Features

- 📤 Upload your resume in **PDF** format
- 🔍 Extract & summarize your resume using an **LLM**
- 📄 Paste a **job description** for tailored analysis
- ✍️ Generate personalized **cover letters** in 3 styles:
    - `Formal`
    - `Creative`
    - `Concise`
- 🧠 **Skill Match Analysis**:
    - Shows Matched vs. Missing Skills
    - Calculates similarity score
- 📥 Export cover letter as a **professional PDF**

---

## 🛠️ Tech Stack

| Layer         | Technology                                                                 |
|---------------|----------------------------------------------------------------------------|
| 👨‍💻 Frontend     | Streamlit                                                                |
| 🤖 AI/LLMs      | Falcon-7B-Instruct / Hugging Face Transformers                           |
| 🔗 LLM Wrappers | LangChain                                                                 |
| 📄 PDF Parsing  | PyMuPDF (`fitz`), FPDF                                                    |
| 🧠 Skill Match  | Scikit-learn + RapidFuzz                                                  |

---

## 📂 Project Structure

resume-cover-gen/
├── app.py

├── chains/

│ ├── summarize.py # Resume summarization logic

│ └── generate_letter.py # Cover letter generation logic

├── utils/

│ ├── pdf_utils.py # PDF text extraction

│ ├── skill_gap.py # Skill overlap analyzer

│ └── pdf_writer.py # PDF export logic

├── models/

│ └── model_loader.py # Optional: load LLM pipelines

├── requirements.txt

└── README.md

---

## 💻 Setup Instructions

1. **Clone this repo**
```bash
git clone https://github.com/your-username/resume-cover-gen.git
cd resume-cover-gen
```
2. **Create and activate virtual environment**
```
python -m venv venv
venv\Scripts\activate   # On Windows
# OR
source venv/bin/activate  # On Mac/Linux
```

3. **Install dependencies**
```
pip install -r requirements.txt
```

4. **Run the app**
```
streamlit run app.py
```

---

## 🧪 How to Use
Upload your resume as a PDF

Paste the job description you’re targeting

Click "Summarize Resume" → review auto-generated summary

Select a cover letter style → click "Generate Cover Letter"

Download it as a PDF 🎉

---

## 🔧 Dependencies
streamlit

langchain

transformers

huggingface_hub

scikit-learn

rapidfuzz

fpdf

PyMuPDF

inflect

---

📦 Install them all with:

pip install -r requirements.txt

---

## 📌 Future Enhancements
📊 Visual skill gap chart

🧠 Suggested skills based on missing ones

✍️ Resume optimizer (LLM-powered insights)

🌐 Multi-language support

---

## 📝 License

MIT License 

Feel free to fork, modify, and contribute!

---

## 🙋‍♂️ Author
Deshan Senanayake 

📧 smddsenyake@gmail.com

🔗 LinkedIn : https://www.linkedin.com/in/deshan-senanayake-7a0695292/

🔗 GitHub : https://github.com/Deshan-Senanayake

