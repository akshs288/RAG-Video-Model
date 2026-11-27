import requests

req = requests.post("http://localhost:11434/api/embeddings",json={
    "model":"bge-m3",
    "prompt":"Aksh sharma doing consistent work"
})

embedding = req.json()["embedding"][:15]
print(embedding)