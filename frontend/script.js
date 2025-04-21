document.getElementById("uploadForm").addEventListener("submit", async function (e) {
    e.preventDefault();
    
    const formData = new FormData();
    const fileInput = document.getElementById("pdf");
    formData.append("pdf", fileInput.files[0]);
  
    const response = await fetch("http://127.0.0.1:5000/upload", {
      method: "POST",
      body: formData
    });
  
    const data = await response.json();
    document.getElementById("result").textContent = JSON.stringify(data, null, 2);
  });
  
  