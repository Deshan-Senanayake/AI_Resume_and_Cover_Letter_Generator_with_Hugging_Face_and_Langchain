from fpdf import FPDF
import tempfile

def generate_pdf(text, title="Generated Cover Letter"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Title
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, title, ln=True, align='C')

    # Content
    pdf.set_font("Arial", size=12)
    lines = text.split('\n')
    for line in lines:
        pdf.multi_cell(0, 10, line)

    # Save to temp file and return the path
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        pdf.output(tmp_file.name)
        return tmp_file.name
