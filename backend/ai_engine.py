from pdf_reader import extract_text_from_pdf  # import the extractor

def generate_flashcards(filepath):
    text = extract_text_from_pdf(filepath)  # extract text from PDF
    # Now use `text` as usual
    return {
        "mcq": [
            {"question": "What is AI?", "options": ["Art", "Science", "Artificial Intelligence", "None"], "answer": "Artificial Intelligence"},
        ],
        "true_false": [
            {"statement": "AI stands for Artificial Intelligence.", "answer": True}
        ],
        "explanatory": [
            {"question": "Explain AI", "answer": "AI refers to the simulation of human intelligence in machines."}
        ]
    }
