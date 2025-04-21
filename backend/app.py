# backend/app.py
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from flask_cors import CORS
from pdf_reader import extract_text_from_pdf
from ai_engine import generate_flashcards

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'pdf' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['pdf']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        try:
            flashcards = generate_flashcards(filepath)  # 👈 YOUR MAIN FUNCTION
            return jsonify({'flashcards': flashcards})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
