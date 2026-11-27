import requests

def embedding(prompt):
    req = requests.post("http://localhost:11434/api/embeddings",json={
        "model":"bge-m3",
        "prompt":prompt
    })

    embedding = req.json()["embedding"]
    return embedding
