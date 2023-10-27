def generate_k_shingles(document, k):
    shingles = set()

    # Check if the document length is less than k
    if len(document) < k:
        print("Document length is less than k. Cannot generate k-shingles.")
        return

    # Generate k-shingles by sliding a window of size k over the document
    for i in range(len(document) - k + 1):
        shingle = document[i:i + k]
        shingles.add(shingle)

    return shingles

def main():
    document = "The sky is blue and the sun is bright."
    k = 5  # You can change the value of k as needed

    # Construct k-shingles
    shingles = generate_k_shingles(document, k)

    # Print the k-shingles
    print(f"{k}-Shingles:")
    for shingle in shingles:
        print(shingle)

if __name__ == "__main__":
    main()
