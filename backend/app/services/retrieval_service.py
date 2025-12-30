import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"
KB_PATH = "app/data/knowledge_base"

model = SentenceTransformer(MODEL_NAME)

documents = []
doc_metadata = []

for file in os.listdir(KB_PATH):
    with open(os.path.join(KB_PATH, file), "r", encoding="utf-8") as f:
        text = f.read()
        documents.append(text)
        doc_metadata.append(file.replace(".txt", ""))

embeddings = model.encode(documents)
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

def retrieve_context(query, top_k=1):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), top_k)

    return {
        "department": doc_metadata[indices[0][0]],
        "context": documents[indices[0][0]]
    }
