from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def measure_similarity(documents):
    # Initialize a TF-IDF vectorizer
    tfidf_vectorizer = TfidfVectorizer()

    # Calculate TF-IDF vectors for all documents
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

    # Calculate cosine similarity between all pairs of documents
    similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

    return similarity_matrix

def find_reused_passages(documents, threshold=0.8):
    similarity_matrix = measure_similarity(documents)
    num_documents = len(documents)

    # Find reused passages based on the cosine similarity threshold
    reused_passages = []

    for i in range(num_documents):
        for j in range(i + 1, num_documents):
            if similarity_matrix[i][j] >= threshold:
                reused_passages.append((i, j))

    return reused_passages

def main():
    # Sample documents
    documents = [
        "This is the first document.",
        "This document is the second document.",
        "And this is the third one.",
        "Is this the first document?"
    ]

    # Set a similarity threshold (adjust as needed)
    threshold = 0.8

    # Find reused passages
    reused_passages = find_reused_passages(documents, threshold)

    if not reused_passages:
        print("No reused passages found.")
    else:
        print("Reused passages found:")
        for i, j in reused_passages:
            print(f"Document {i+1} and Document {j+1} are similar.")

if __name__ == "__main__":
    main()
