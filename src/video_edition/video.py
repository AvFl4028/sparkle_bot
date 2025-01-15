import json
import os
from moviepy import VideoFileClip, AudioFileClip
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy import CompositeVideoClip
from moviepy.video.VideoClip import TextClip


class VideoEditor:
    def __init__(self):
        self.config = json.load(open("src/config/config.json", "r", encoding="utf-8"))
        self.output_path = self.config["paths"]["video"]["system"]["output"]
        self.video_name = "test.mp4"

    def create_video(self, bg_path: str, audio_path: str, subtitles_path: str):
        video = VideoFileClip(bg_path)
        audio = AudioFileClip(audio_path)

        def subtitle_generator(txt):
            return TextClip(
                text=txt,
                font_size=24,  # Tamaño del texto
                color="white",  # Color del texto
                font="arial",  # Fuente del texto (asegúrate de que está instalada)
            )

        # Cargar los subtítulos desde un archivo SRT
        subtitles = SubtitlesClip(
            subtitles_path, make_textclip=subtitle_generator, encoding="utf-8"
        )

        output = CompositeVideoClip([video.with_audio(audio), subtitles]).with_duration(
            audio.duration
        )
        output.write_videofile(
            self.output_path + self.video_name,
            fps=video.fps,
            temp_audiofile="src/media/audio/temp/temp-audio.m4a",
            remove_temp=True,
            codec="libx264",
            audio_codec="aac",
        )
