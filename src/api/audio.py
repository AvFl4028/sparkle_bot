from elevenlabs.client import ElevenLabs
from elevenlabs import play
import json
import uuid
from random import randint

json_file = open('src/api/history_test.json', "r", encoding="utf-8")
json_data = json.load(json_file)

num_random = randint(0, 19)

print(json_data[f"{num_random}"]["reddit_history"]["part1"]["content"])

client = ElevenLabs(api_key="API_KEY")

audio = client.text_to_speech.convert(
    text=json_data[f"{num_random}"]["reddit_history"]["part1"]["content"],
    voice_id="FXGrCtY3PEyfqczBAlqm",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",  # mp3_44100_128
    optimize_streaming_latency=0
)

save_file_name = f"src/media/audio/temp/{uuid.uuid4()}.mp3"

with open(save_file_name, "wb") as f:
    for chunk in audio:
      if chunk:
        f.write(chunk)
    f.close()