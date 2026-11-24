import whisper
import json
import os

model = whisper.load_model("medium")


all_files = os.listdir(r"D:\All Coding files\RAG-Video-Model\Audios_mp3")

for audio in all_files:
    # print(audio)
    number = audio.split("_")[0]
    title = audio.split("_")[1][:-4]
    print(number,title)

    transcribe_obj = model.transcribe(
        r"D:\All Coding files\RAG-Video-Model\Audios_mp3\output.mp3",
        task="translate",
    )

    print(transcribe_obj)

