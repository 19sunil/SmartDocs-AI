import numpy as np
from embedder import create_embedding
import endee_db   # import the module, not variables

def semantic_search(query):

    query_vector = create_embedding(query)
    query_vector = np.array([query_vector]).astype("float32")

    distances, indices = endee_db.index.search(query_vector, 3)

    for i in indices[0]:
        print("Result:", endee_db.documents[i])