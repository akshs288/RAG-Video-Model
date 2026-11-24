import whisper
import json
import os

model = whisper.load_model("medium")

all_refine_audio = os.listdir(r"D:\All Coding files\RAG-Video-Model\Refined Audios")

l = []
for audio_refine in all_refine_audio:
    transcribe_obj = model.transcribe(
        f"D:\All Coding files\RAG-Video-Model\Refined Audios\{audio_refine}",
        task="translate",
    )

    l.append(transcribe_obj)

with open(r"D:\All Coding files\RAG-Video-Model\ouput.json","w") as g:
    json.dump(l,g)

with open(r"D:\All Coding files\RAG-Video-Model\ouput.json") as f:
    Chunks_data = json.load(f)
    final_data = {}
    count = 0
    for chunk_index in range(len(Chunks_data)):
        l = []
        for i in Chunks_data[count]["segments"]:
            # Storing this in dictionary
            d = {}
            d["Start"] = i["start"]
            d["End"] = i["end"]
            d["text"] = i["text"]
            l.append(d)

        final_data[f"Chunk {chunk_index+1}"] = l
        
with open("result.json","w") as g:
    json.dump(final_data,g)


    
