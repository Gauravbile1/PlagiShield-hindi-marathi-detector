function checkPlagiarism() {
    const fileInput = document.getElementById("fileInput");
    const language = document.getElementById("language").value;
    const resultDiv = document.getElementById("result");
    const downloadLink = document.getElementById("downloadLink");

    if (!fileInput.files[0]) {
        alert("Please upload a file!");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);
    formData.append("language", language);

    fetch("http://127.0.0.1:5000/check", {
        method: "POST",
        body: formData
    })
    .then(res => {
        if (!res.ok) {
            throw new Error("Network response was not ok");
        }
        return res.json();
    })
    .then(data => {
        if (data.score !== undefined) {
            resultDiv.innerHTML = `📊 Plagiarism Score: <b>${data.score}%</b>`;
            downloadLink.href = "http://127.0.0.1:5000/download";
            downloadLink.style.display = "inline-block";
        } else {
            throw new Error("Invalid response format");
        }
    })
    .catch(err => {
        console.error("❌ JS Fetch Error:", err);
        resultDiv.innerHTML = "❌ Something went wrong.";
        downloadLink.style.display = "none";
    });
}
