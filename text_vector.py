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

id_embed = 0
main_embeddings = {}

main_number = []
main_title= []
main_id_embed = []
main_embedin = []
id_embed = []

for i in file_path:
    c= 1
    with open(i) as f:
        i = i.stem     # stem attribute returns filename without extension
        refined_file_name = i.split(".")[0].split(" ")[1]
        all_data = json.load(f)  # Fetched as List of dictionary
        for data in all_data:
            id_embed += 1
            text_chunk = data["text"]    # Separate text 

            req = requests.post("http://localhost:11434/api/embeddings",json={
                "model":"bge-m3",
                "prompt":text_chunk
            })
            final_embedding = req.json()["embedding"]
            number = []
            title = []
            id_embed_list = []
            embedding_list = []
            embedding_list.append(final_embedding)
            number.append(c)
            title.append(refined_file_name)
            id_embed_list.append(id_embed)

            # Appending results to big list  (Means list of list)
            main_embedin.append(final_embedding)
            main_number.append(number)
            main_id_embed.append(id_embed_list)
            main_title.append(title)

    c+=1

main_embeddings["Number"] = main_number
main_embeddings["Title"] = main_title
main_embeddings["Embeddings"] = main_embedin
main_embeddings["Id_embeddings"] = main_id_embed

print(main_embeddings)
            

