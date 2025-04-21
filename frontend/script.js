document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('upload-form');
    const result = document.getElementById('result');
  
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const fileInput = document.getElementById('pdf');
      const file = fileInput.files[0];
  
      if (!file) {
        result.textContent = 'Please select a PDF file.';
        return;
      }
  
      const formData = new FormData();
      formData.append('pdf', file);
  
      result.textContent = 'Generating flashcards...';
  
      try {
        const response = await fetch('http://127.0.0.1:5000/upload', {
          method: 'POST',
          body: formData
        });
  
        if (!response.ok) {
          throw new Error('Failed to generate flashcards');
        }
  
        const data = await response.json();
  
        if (typeof data === 'string') {
          result.textContent = data; // If AI returns plain text
        } else {
          result.textContent = JSON.stringify(data, null, 2); // If it's a JSON object
        }
      } catch (error) {
        result.textContent = 'Error: ' + error.message;
      }
    });
  });
  