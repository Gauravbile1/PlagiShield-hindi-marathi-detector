import pandas as pd
import os

csv_path = r"C:\Users\Gaurav Bile\Videos\1Study\SKY internship\hindi_marathi_plagiarism_checker\backend\data\marathi.csv"
df = pd.read_csv(csv_path)

# Show available columns
print("📌 Available columns:", df.columns.tolist())

# Try common column names — adjust if needed
if "Marathi" in df.columns:
    marathi_column = "Marathi"
elif "marathi" in df.columns:
    marathi_column = "marathi"
elif "target" in df.columns:
    marathi_column = "target"
else:
    raise ValueError("⚠️ Marathi column not found. Please check the column names above.")

# Save clean text
output_path = os.path.join(os.path.dirname(csv_path), "marathi_dataset.txt")
df[marathi_column].dropna().to_csv(output_path, index=False, header=False, encoding="utf-8")

print("✅ marathi_dataset.txt created at:", output_path)
