import json
import os
from moviepy import VideoFileClip


class BgGenerator:
    def __init__(self):
        self.config = json.load(open("src/config/config.json", "r", encoding="utf-8"))
        if self.config["project_type"] == "system":
            self.path = self.config["paths"]["video"]["system"]["bg_m_s"]
        else:
            self.path = self.config["paths"]["video"]["project"]["bg_m_s"]
        self.video_name = "test.mp4"
        self.video_file = self.path + self.video_name
        self.clip_duration = 120
        self.clip_path: str

    def bg_generate(self, video_path: str = None):

        if video_path is not None:
            self.video_file = video_path
            self.video_name = video_path.split("\\")[-1]

        print("Generating background video...")
        print("File: " + self.video_file)
        print("Name: " + self.video_name)

        video = VideoFileClip(self.video_file)

        # Dimensiones para videos verticales
        vertical_width = 608
        vertical_height = 1080

        # Recortar el video desde el centro
        x_center = video.size[0] // 2  # Centro del video en el eje X
        y_center = video.size[1] // 2  # Centro del video en el eje Y

        # Calcular los bordes del recorte
        x1 = x_center - vertical_width // 2
        x2 = x_center + vertical_width // 2
        y1 = y_center - vertical_height // 2
        y2 = y_center + vertical_height // 2

        # Recortar el video
        cropped_video = video.cropped(x1=x1, x2=x2, y1=y1, y2=y2)

        # Guardar el resultado
        output_path = self.path + self.video_name
        cropped_video.write_videofile(output_path, codec="libx264", fps=60)

    def get_files(self) -> list:
        final_list = []
        files = os.listdir(self.path)
        for i in files:
            final_list.append(self.path + i)
        return final_list

    def generate_clips(self, path: str = None):
        if path is not None:
            self.video_file = path
            self.video_name = path.split("\\")[-1]

        video = VideoFileClip(self.video_file)

        self.clip_path = (
            self.config["paths"]["video"]["system"]["clips"]
            + self.video_name.replace(".mp4", "")
            + "\\"
        )

        if not os.path.exists(self.clip_path):
            os.makedirs(self.clip_path)
        # Duracion del video
        duration = video.duration

        # Cantidad de clips a generar
        clips_amount = int(duration / self.clip_duration)

        print("Video duration: " + str(duration))
        print("Clip duration: " + str(self.clip_duration))
        print("Clips amount: " + str(clips_amount))

        for i in range(clips_amount):
            start_time = i * self.clip_duration
            end_time = (i + 1) * self.clip_duration

            # Recortar el video
            clip = video.subclipped(start_time, end_time)

            # Guardar el clip
            output_path = self.clip_path + f"clip_{i}.mp4"
            print("Saving clip: " + output_path)
            clip.write_videofile(output_path, codec="libx264", fps=60)

        return

    def get_clips_files() -> list[str]:
        pass
