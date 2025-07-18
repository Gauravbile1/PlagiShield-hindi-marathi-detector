from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .preprocessing import normalize_text, split_sentences

def load_dataset(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return [normalize_text(line.strip()) for line in lines if line.strip()]

def check_plagiarism(input_text, dataset_sentences):
    input_sentences = split_sentences(input_text)
    print("📝 Input sentences:", input_sentences)

    if not input_sentences or not dataset_sentences:
        return [], 0.0

    all_sentences = dataset_sentences + input_sentences

    # ✅ Fit TF-IDF once on full data
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(all_sentences)

    results = []
    total_score = 0.0

    for i, sentence in enumerate(input_sentences):
        input_vector = tfidf[len(dataset_sentences) + i]
        similarities = cosine_similarity(input_vector, tfidf[:len(dataset_sentences)]).flatten()
        max_score = round(float(similarities.max()) * 100, 2) if similarities.size > 0 else 0.0
        results.append((sentence, max_score))
        total_score += max_score

    average_score = round(total_score / len(input_sentences), 2)
    print("✅ Plagiarism score calculated:", average_score)
    return results, average_score
