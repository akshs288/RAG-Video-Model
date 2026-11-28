import requests
import os
import json
from pathlib import Path

json_folder = Path(r"D:\All Coding files\RAG-Video-Model\All_JSON_chunks")
all_json_file = os.listdir(json_folder)

file_path = []
for i in all_json_file:
    path_file = json_folder / i
    file_path.append(path_file)

main_embeddings = {}
number = []
title = []
embedding_list = []
for i in file_path:
    c= 1
    with open(i) as f:
        i = i.stem     # stem attribute returns filename without extension
        refined_file_name = i.split(".")[0].split(" ")[1]
        all_data = json.load(f)  # Fetched as List of dictionary
        for data in all_data:
            text_chunk = data["text"]    # Separate text 

            req = requests.post("http://localhost:11434/api/embeddings",json={
                "model":"bge-m3",
                "prompt":text_chunk
            })
            final_embedding = req.json()["embedding"]

            embedding_list.append(final_embedding)
            number.append(c)
            title.append(refined_file_name)
        c+=1


main_embeddings["Number"] = number
main_embeddings["Title"] = title
main_embeddings["Embeddings"] = embedding_list
print(main_embeddings)
            

