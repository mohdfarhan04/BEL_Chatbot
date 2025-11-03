# extract_pdf.py
from pypdf import PdfReader

reader = PdfReader("data/CitizenUserManual.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

with open("knowledge_base/user_manual.txt", "w", encoding="utf-8") as f:
    f.write(text)