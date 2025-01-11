import json
from moviepy import VideoFileClip, CompositeVideoClip

config = json.load(open("src/config/config.json", "r", encoding="utf-8"))

def bg_generate():
    if config["project_type"] == "system":
        path = config["paths"]["video"]["system"]["bg_raw"]
    else:
        path = config["paths"]["video"]["project"]["bg_raw"]

    video_path = path + "video_8.mp4"

    video = VideoFileClip(video_path)

    # Dimensiones para videos verticales
    vertical_width = 1080
    vertical_height = 1920

    # Recortar el video desde el centro
    x_center = video.size[0] // 2  # Centro del video en el eje X
    y_center = video.size[1] // 2  # Centro del video en el eje Y

    # TODO - El recorte es al revez :c
    # Calcular los bordes del recorte
    x1 = x_center - vertical_width // 2
    x2 = x_center + vertical_width // 2
    y1 = y_center - vertical_height // 2
    y2 = y_center + vertical_height // 2

    # Recortar el video
    cropped_video = video.cropped(x1=x1, x2=x2, y1=y1, y2=y2)

    # Guardar el resultado
    output_path = config["paths"]["video"]["system"]["bg_m_s"] + "video.mp4"
    cropped_video.write_videofile(output_path, codec="libx264", fps=60)
