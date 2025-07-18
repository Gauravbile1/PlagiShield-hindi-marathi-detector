import re

def normalize_text(text):
    # Remove punctuation, normalize spaces, convert to lowercase
    text = re.sub(r'[^\w\s]', '', text)   # Remove punctuation
    text = re.sub(r'\s+', ' ', text)      # Replace multiple spaces with single space
    return text.strip().lower()

def split_sentences(text):
    # Split text into sentences using Devanagari danda and common punctuation
    sentences = re.split(r'[।!?]', text)
    return [s.strip() for s in sentences if s.strip()]
