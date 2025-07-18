import pandas as pd
import os

csv_path = r"C:\Users\Gaurav Bile\Videos\1Study\SKY internship\hindi_marathi_plagiarism_checker\backend\data\Hindi_English_Truncated_Corpus.csv"
df = pd.read_csv(csv_path)

# Use correct column name directly
df["hindi_sentence"].dropna().to_csv(
    os.path.join(os.path.dirname(csv_path), "hindi_dataset.txt"),
    index=False, header=False, encoding="utf-8"
)

print("✅ hindi_dataset.txt created successfully!")
