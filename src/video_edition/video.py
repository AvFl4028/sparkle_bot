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

    def create_video(
        self, bg_path: str, audio_path: str, subtitles_path: str, video_name: str
    ) -> None:
        video = VideoFileClip(bg_path)
        audio = AudioFileClip(audio_path)
        # self.subtitles = subtitles_path
        self.video_name = video_name
        self.__load_subtitles(subtitles_path)

        def subtitle_generator(txt):
            text_clip: TextClip = TextClip(
                text=txt,
                method="caption",  # Tamaño del texto
                size=(int(round(float(self.video_size[0]) * 0.9)), None),
                color="white",  # Color del texto
                font="src/media/fonts/OugkehRegular-DYYrW.otf",  # Fuente del texto (asegúrate de que está instalada)
                text_align="center",
                font_size=60,
                # bg_color=(0, 0, 0, 75),
                stroke_color = "black",
                stroke_width = 5
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
        return

    def __load_subtitles(self, subtitles_path: str) -> None:
        subtitles_file = pysrt.open(subtitles_path)
        subtitles = []
        subtitles_width: int = 20

        for chunk in subtitles_file:
            start_time = chunk.start.seconds + (chunk.start.minutes * 60)
            end_time = chunk.end.seconds + (chunk.end.minutes * 60)
            text_wraped = textwrap.wrap(chunk.text, width=subtitles_width)

            num_subtitles: int = len(text_wraped)

            print(f"Start time: {start_time}\nEnd Time: {end_time}")

            duration = end_time - start_time
            duration_promedio = duration / num_subtitles

            print("Duracion promedio: " + str(duration_promedio))

            for text_chunk in text_wraped:
                final_end_time = start_time + duration_promedio

                if final_end_time > end_time:
                    final_end_time = end_time

                subtitles.append(((start_time, final_end_time), text_chunk))
                start_time += duration_promedio

        for i in subtitles:
            print(i)
        self.subtitles = subtitles
        return
