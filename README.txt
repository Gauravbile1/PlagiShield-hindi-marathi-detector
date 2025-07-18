PlaguShield - Hindi/Marathi Plagiarism Detection System ????

PlaguShield is a professional-grade plagiarism detection system tailored specifically for “Hindi” and “Marathi” languages. It uses TF-IDF vectorization, Cosine Similarity, and Unicode-compatible PDF reporting to help detect and highlight sentence-level plagiarism with precision.

---

 ?? Features

? Supports Hindi and Marathi language detection  
? Sentence-level plagiarism detection  
? Color-coded PDF report generation (?? plagiarized / ?? original)  
? Unicode Devanagari font support  
? Clean and professional report layout  
? Easy to integrate Flask API backend  
? Threshold-based matching control

---












?? Project Structure

PlaguShield/
?
??? backend/
?   ??? app.py                         # Main Flask backend application
?
?   ??? data/                          # Sample datasets
?   ?   ??? hindi_dataset.txt
?   ?   ??? marathi_dataset.txt
?
?   ??? fonts/                         # Devanagari Unicode font
?   ?   ??? NotoSansDevanagari-Regular.ttf
?
?   ??? reports/                       # Output folder for generated reports
?   ?   ??? plagiarism_report.pdf      # (generated dynamically)
?
?   ??? uploads/                       # Stores temporarily uploaded input files
?
?   ??? utils/                         # Utility modules for core functionality
?       ??? preprocessing.py           # Normalize text, split sentences
?       ??? plagiarism.py              # TF-IDF & Cosine similarity logic
?       ??? report_generator.py        # PDF generation logic (colored output)
?
??? README.txt                         # Project documentation (you’ll paste this manually)
??? requirements.txt                   # List of Python dependencies
??? .gitignore                         # To ignore uploads/reports in Git
---




? How to Run

1. ? Install dependencies:

pip install -r requirements.txt

2. ? Run the Flask server:

python backend/app.py

3. ? Open frontend (you can use HTML/Streamlit/custom UI) and call:
- POST /check ? to check plagiarism and generate PDF
- GET /download ? to download the report

---

?? Technologies Used

- Python
- Flask
- Scikit-learn (TF-IDF, Cosine Similarity)
- ReportLab (PDF generation)
- Unicode fonts (NotoSansDevanagari)

---

?? About

PlaguShield helps educational institutions, content creators, and students detect plagiarism in Hindi and Marathi content at a sentence level. With clean PDF reporting and a flexible backend, it is built for *real-world usage* and professional deployment.
---

?? Contact

Made with ? by Gaurav Bile  
?? gaurav.bile.cs@gmail.com
