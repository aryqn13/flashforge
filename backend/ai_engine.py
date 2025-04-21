import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_flashcards(text):
    prompt = f"Generate flashcards from this study material:\n{text}\nInclude: MCQs, True/False, and Explanatory Questions."
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You generate flashcards for students."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response['choices'][0]['message']['content']
