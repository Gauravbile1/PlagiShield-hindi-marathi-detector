from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename
import os
from utils.preprocessing import normalize_text
from utils.plagiarism import check_plagiarism, load_dataset
from utils.report_generator import generate_pdf_report
from flask_cors import CORS

# Flask setup
app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = os.path.join("backend", "uploads")
REPORT_PATH = os.path.join("backend", "reports", "plagiarism_report.pdf")

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)

@app.route("/check", methods=["POST"])
def check_plagiarism_route():
    language = request.form["language"]
    print("✅ Request received!")
    print("📥 Language:", language)

    uploaded_file = request.files["file"]
    print("📄 Uploaded file:", uploaded_file.filename)

    filename = secure_filename(uploaded_file.filename)
    input_path = os.path.join(UPLOAD_FOLDER, filename)
    uploaded_file.save(input_path)

    # Dataset path
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    if language == "hindi":
        dataset_path = os.path.join(BASE_DIR, "data", "hindi_dataset.txt")
    elif language == "marathi":
        dataset_path = os.path.join(BASE_DIR, "data", "marathi_dataset.txt")
    else:
        return jsonify({"error": "Unsupported language"}), 400

    try:
        dataset_sentences = load_dataset(dataset_path)
        print("📚 Loaded dataset sentences:", dataset_sentences[:5])

        with open(input_path, "r", encoding="utf-8") as f:
            input_text = f.read()
        print("📝 Input sentences:", input_text)

        results, score = check_plagiarism(input_text, dataset_sentences)
        print("📊 Results preview:", results[:3])
        print("✅ Plagiarism score calculated:", score)

        try:
            print("🧾 Results to report:", results)

            generate_pdf_report(results, score, REPORT_PATH)
        except Exception as e:
            print("❌ Report generation error:", str(e))
            return jsonify({"error": "PDF generation failed"}), 500

        return jsonify({"score": round(score, 2)})

    except Exception as e:
        print("❌ Error:", str(e))
        return jsonify({"error": "Something went wrong"}), 500

@app.route("/download", methods=["GET"])
def download_report():
    if os.path.exists(REPORT_PATH):
        return send_file(REPORT_PATH, as_attachment=True)
    else:
        return "Report not found", 404

if __name__ == "__main__":
    print("📂 check_plagiarism loaded from correct plagiarism.py")
    app.run(debug=True)
