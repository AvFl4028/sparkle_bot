import json
from moviepy import VideoFileClip

class BgGenerator():
    def __init__(self):
        self.config = json.load(open("src/config/config.json", "r", encoding="utf-8"))
        if self.config["project_type"] == "system":
            self.path = self.config["paths"]["video"]["system"]["bg_raw"]
        else:
            self.path = self.config["paths"]["video"]["project"]["bg_raw"]

    def bg_generate(self):
        video_path = self.path + "video_8.mp4"

        video = VideoFileClip(video_path)

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
        output_path = self.config["paths"]["video"]["system"]["bg_m_s"] + "video_8.mp4"
        cropped_video.write_videofile(output_path, codec="libx264", fps=60)


def generate_clips():
    pass