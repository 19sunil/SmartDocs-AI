import faiss
import numpy as np
from embedder import create_embedding

documents = []
index = None

def load_documents():
    global index

    with open("data.txt", "r") as f:
        docs = [line.strip() for line in f.readlines()]

    vectors = []

    for doc in docs:
        documents.append(doc)
        vectors.append(create_embedding(doc))

    vectors = np.array(vectors).astype("float32")

    dimension = vectors.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(vectors)