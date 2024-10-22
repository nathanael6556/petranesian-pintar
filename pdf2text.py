# importing required modules
from pypdf import PdfReader

# creating a pdf reader object
reader = PdfReader('./samples/Lecture04/DS-Lct04-Communication.pdf')

with open("pdf_text.txt", "a") as f:
    for page in reader.pages:
        # extracting text from page
        text = page.extract_text()
        f.write(text)
        f.write("\n\n")