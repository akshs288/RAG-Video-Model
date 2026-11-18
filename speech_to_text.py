import whisper
import json

# model = whisper.load_model("medium")

# transcribe_obj = model.transcribe(
#     r"D:\All Coding files\RAG-Video-Model\Audios_mp3\output.mp3",
#     task="translate",
# )

with open(r"D:\All Coding files\RAG-Video-Model\testing.json") as g:
    transcribe_obj = json.load(g)

refined_data = []

for i in transcribe_obj["segments"]:
    start_obj  = i["start"]
    end_obj = i["end"]
    text_obj = i['text']
    new_d = {"Start":start_obj,"End":end_obj,"Text":text_obj}
    refined_data.append(new_d)

print(refined_data)


with open("testing2.json","w") as f:
    json.dump(refined_data,f)



