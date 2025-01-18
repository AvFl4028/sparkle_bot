import json
import pysrt
import textwrap
from moviepy import VideoFileClip, AudioFileClip
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy import CompositeVideoClip
from moviepy.video.VideoClip import TextClip


class VideoEditor:
    def __init__(self):
        self.config = json.load(open("src/config/config.json", "r", encoding="utf-8"))
        self.output_path = self.config["paths"]["video"]["system"]["output"]
        self.video_name = "test.mp4"
        self.subtitles: list[tuple]

    def create_video(self, bg_path: str, audio_path: str, subtitles_path: str):
        video = VideoFileClip(bg_path)
        audio = AudioFileClip(audio_path)

        self.__load_subtitles(subtitles_path)

        def subtitle_generator(txt):
            return TextClip(
                text=txt,
                font_size=24,  # Tamaño del texto
                color="white",  # Color del texto
                font="arial",  # Fuente del texto (asegúrate de que está instalada)
            )

        # Cargar los subtítulos desde un archivo SRT
        subtitles = SubtitlesClip(
            self.subtitles, make_textclip=subtitle_generator, encoding="utf-8"
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

    def __load_subtitles(self, subtitles_path: str) -> None:
        subtitles_file = pysrt.open(subtitles_path)
        subtitles = []

        for chunk in subtitles_file:
            start_time = chunk.start.seconds
            end_time = chunk.end.seconds
            text_wraped = textwrap.wrap(chunk.text, width=30)
            final_text: str = ""
            for i in text_wraped:
                final_text += i + "\n"
            subtitles.append(((start_time, end_time), final_text))
        self.subtitles = subtitles