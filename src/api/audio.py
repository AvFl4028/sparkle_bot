from elevenlabs.client import ElevenLabs
from elevenlabs import play
from faster_whisper import WhisperModel
from random import randint

import json
import uuid
import os
import math

# TODO - Documentar todo el codigo :'3

json_file = open('src/api/history_test.json', "r", encoding="utf-8")
json_data = json.load(json_file)

num_random = randint(0, 19)

# print(json_data[f"{num_random}"]["reddit_history"]["part1"]["content"])

class Audio:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = ElevenLabs(api_key=self.api_key)

        self.audio_file_path: str = ""

        self.audio_path: str = "src/media/audio/"
        self.audio_temp_path: str = "src/media/audio/temp/"
        self.subtitles_path: str = "src/media/audio/subtitles/"
        self.subtitles_file_path: str = f"{self.subtitles_path}test_sub.srt"


    def text_to_speech(self, text, save_file: bool = True, file_name: str = None, is_temp: bool = False):
        audio = self.client.text_to_speech.convert(
            text=text,
            voice_id="FXGrCtY3PEyfqczBAlqm",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",  # mp3_44100_128
            optimize_streaming_latency=0
        )

        if not save_file:
            play(audio)
            return

        if is_temp:
            file_path = self.audio_temp_path
        else:
            file_path = self.audio_path

        if file_name is None:
            self.audio_file_path = f"{file_path}{uuid.uuid4()}.mp3"
        else:
            self.audio_file_path =  f"{file_path}{file_name}.mp3"

        with open(self.audio_file_path, "wb") as f:
            for chunk in audio:
                if chunk:
                    f.write(chunk)
            f.close()
            print(f"Archivo guardado en {self.audio_file_path}")


    def subtitles(self, audio_file: str = None, subtitles_name: str = None):
        if audio_file is None:
            audio_file = self.audio_file_path

        if not os.path.isfile(audio_file):
            print("Archivo no encontrado")
            return

        file_transcribed = self.__generate_subtitle_file(audio_file, subtitles_name)

        print(f"---------------------------\n{file_transcribed}\n----------------------------")

    def __transcribe(self, audio_file: str) -> tuple:
        model = WhisperModel("small", device="cpu", compute_type="int8")
        segments, info = model.transcribe(audio_file)
        language = info.language
        print(f"Transcription language {language}")

        segments_start = {}
        segments_end = {}
        segments_text = {}

        index = 0

        for segment in segments:
            segments_start[str(index)]= "%.2f" % segment.start
            segments_end[str(index)] = "%.2f" % segment.end
            segments_text[str(index)] = segment.text

            index = index + 1

            print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))

        print(segments_start)
        print(segments_end)
        print(segments_text)

        return language, segments_start, segments_end, segments_text, index


    def __format_time(self, seconds: int):
        hours = math.floor(seconds / 3600)
        seconds %= 3600
        minutes = math.floor(seconds / 60)
        seconds %= 60
        milliseconds = round((seconds - math.floor(seconds)) * 1000)
        seconds = math.floor(seconds)
        formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:01d},{milliseconds:03d}"

        return formatted_time


    def __generate_subtitle_file(self, audio_file: str, subtitles_name: str = None):
        text = ""
        (language, segments_start, segments_end, segments_text, index) = self.__transcribe(audio_file)
        for i in range(index):
            segment_start = self.__format_time(round(float(segments_start[str(i)])))
            segment_end = self.__format_time(round(float(segments_end[str(i)])))
            text = text + f"{str(i + 1)} \n{segment_start} --> {segment_end} \n{segments_text[str(i)]} \n\n"

        print(text)

        if subtitles_name is not None:
            self.subtitles_file_path = self.subtitles_path + f"{subtitles_name}"

        f = open(self.subtitles_file_path, "w")
        f.write(text)
        f.close()

        return self.subtitles_file_path

