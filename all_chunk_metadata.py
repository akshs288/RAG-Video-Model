import json
import os

# model = whisper.load_model("medium")

# transcribe_obj = model.transcribe(
#     r"D:\All Coding files\RAG-Video-Model\Audios_mp3\output.mp3",
#     task="translate",
# )

all_files = os.listdir(r"D:\All Coding files\RAG-Video-Model\Audios_mp3")


all_chunks = []
k = 0
for file in all_files:
    k+=1
    with open(r"D:\All Coding files\RAG-Video-Model\testing.json") as g:
        transcribe_obj = json.load(g)

    refined_data = []
    for i in transcribe_obj:
        start_obj  = i['segments']["start"]
        end_obj = i['segments']["end"]
        text_obj = i['segments']['text']
        whole_text = i['text']
        new_d = {"Start":start_obj,"End":end_obj,"Chunked_Text":text_obj}
        refined_data.append(new_d)

    chunk_dict = {f"Chunk{k}":refined_data}
    all_chunks.append(chunk_dict)

print(all_chunks)
