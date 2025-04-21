# backend/pdf_reader.py
import fitz  # PyMuPDF

def extract_text_from_pdf(filepath):
    text = ""
    with fitz.open(filepath) as doc:
        for page in doc:
            text += page.get_text()
    return text

from PyPDF2 import PdfReader

def extract_text_from_pdf(filepath):
    reader = PdfReader(filepath)
    text = ''
    for page in reader.pages:
        text += page.extract_text() or ''
    return text
