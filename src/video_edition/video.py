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
        self.video_name: str
        self.subtitles: list[tuple]
        self.subtitles_size: tuple
        self.video_size: tuple = (608, 1080)

    def create_video(self, bg_path: str, audio_path: str, subtitles_path: str, video_name: str):
        video = VideoFileClip(bg_path)
        audio = AudioFileClip(audio_path)
        self.subtitles = subtitles_path
        self.video_name = video_name
        # self.__load_subtitles(subtitles_path)

        def subtitle_generator(txt):
            text_clip: TextClip = TextClip(
                text=txt,
                method="caption",  # Tamaño del texto
                size=(int(round(float(self.video_size[0]) * 0.9)), None),
                color="white",  # Color del texto
                font="src\\media\\fonts\\OugkehRegular-DYYrW.otf",  # Fuente del texto (asegúrate de que está instalada)
                text_align="center",
                font_size=60,
                bg_color=(0, 0, 0, 75),
            )

            self.subtitles_size = text_clip.size

            return text_clip

        # Cargar los subtítulos desde un archivo SRT
        subtitles = SubtitlesClip(
            self.subtitles, make_textclip=subtitle_generator, encoding="utf-8"
        )

        video = video.with_audio(audio)

        width, height = self.subtitles_size

        subtitles = subtitles.with_position(
            (
                (self.video_size[0] / 2) - (width / 2),
                (self.video_size[1] / 2) - (height / 2),
            )
        )

        output = CompositeVideoClip([video, subtitles])
        output = output.with_duration(audio.duration)
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
            text_wraped = textwrap.wrap(chunk.text, width=25)
            final_text: str = ""
            for i in text_wraped:
                final_text += i + "\n"
            subtitles.append(((start_time, end_time), final_text))
        self.subtitles = subtitles
