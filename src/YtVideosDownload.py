import yt_dlp
from pytube import Playlist

def downloadVideo(url: str, path: str, name: str):
    ydl_opts = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",  # Selecciona MP4 para video y audio
        "outtmpl": f"{path}{name}.mp4",  # Define el nombre del archivo de salida
        "merge_output_format": "mp4",  # Fuerza el archivo final como MP4
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def get_videos_from_playlist(url) -> list:
    pl = Playlist(url)
    urls = []
    for _url in pl.video_urls:
        urls.append(_url)
    return urls

def main() -> None:
    # This path is for download the videos in the video folder in this project
    path = "src/media/video/background_raw/"

    # This path is for download the videos in another path in the system
    main_path = "D:\\Videos\\sparkle_bot\\media\\video\\background_raw\\"

    # downloadVideo("https://www.youtube.com/watch?v=btnR609TeCg", "src/media/video/", "test")
    urls = get_videos_from_playlist("https://youtube.com/playlist?list=PLmSs-0cFIbfVWhkZx0i4UMiZdr2C0Z8w7&si=LPW0z4t6EXixyQmF")

    index = 0

    for i in urls:
        downloadVideo(i, main_path, f"video_{index}")
        index += 1
    pass


if __name__ == "__main__":
    main()