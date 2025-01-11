import yt_dlp
from pytube import Playlist
import json

class VideoDownload:
    def __init__(self, url: str = None, in_project: bool = False):
        # Config file load
        config_json = json.load(open("src/config/config.json", "r", encoding="utf-8"))

        self.url: str = url

        # Set main path config
        if in_project:
            self.path: str = config_json["paths"]["project"]["bg_raw"]
        else:
            self.path: str = config_json["paths"]["system"]["bg_raw"]

    def downloadVideo(self, url: str = None, path: str = None, name: str = None):

        if url is not None:
            self.url = url

        ydl_opts = {
            "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",  # Selecciona MP4 para video y audio
            "outtmpl": f"{self.path}{name}.mp4",  # Define el nombre del archivo de salida
            "merge_output_format": "mp4",  # Fuerza el archivo final como MP4
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url])


    def get_videos_from_playlist(self, url) -> list:
        pl = Playlist(url)
        urls = []
        for _url in pl.video_urls:
            urls.append(_url)
        return urls

def main() -> None:
    # downloadVideo("https://www.youtube.com/watch?v=btnR609TeCg", "src/media/video/", "test")
    video_download = VideoDownload(in_project=False)

    urls = video_download.get_videos_from_playlist("https://youtube.com/playlist?list=PLmSs-0cFIbfVWhkZx0i4UMiZdr2C0Z8w7&si=LPW0z4t6EXixyQmF")

    index = 0

    for i in urls:
        video_download.downloadVideo(i, name= f"video_{index}")
        index += 1
    pass


if __name__ == "__main__":
    main()