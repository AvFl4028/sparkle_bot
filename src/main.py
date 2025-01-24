from api.audio import Audio
from api.gemini import GeminiAPI, HistoryType
from keys import GEMINI_API_KEY, ELEVENLABS_API_KEY
from video_edition.BgGenerator import BgGenerator
from video_edition.video import VideoEditor

audio_generator = Audio(ELEVENLABS_API_KEY)
gemini = GeminiAPI(GEMINI_API_KEY)
video_editor = VideoEditor()


test_subtitles_file: str = "src\\media\\audio\\subtitles\\El Reloj de Arena de la Abuela Emilia_part2.srt"
test_audio_file: str = "src\\media\\audio\\temp\\El Reloj de Arena de la Abuela Emilia_part2.mp3"
test_bg_file: str = BgGenerator().get_random_clip()


def main() -> None:
    # Some simple test
    # test_subtitles_video()
    # test_gemini()
    # test_whisper()
    # test_bg()
    # test_final_video()
    test_video_generator()
    return


def test_gemini() -> None:
    response = gemini.response(HistoryType.REDDIT, True)
    print("Starting Generative Text, Text to Speech and Subtitles generator")
    print("--------------------------------------------------------------------")

    print(response["reddit_history"]["part1"]["content"])
    audio_generator.text_to_speech(
        response["reddit_history"]["title"]
        + "...parte 1..."
        + response["reddit_history"]["part1"]["content"],
        is_temp=True,
        file_name=response["reddit_history"]["title"] + "_part1.mp3",
    )
    audio_generator.subtitles()

    print("--------------------------------------------------------------------")


#    print(response["reddit_history"]["part2"]["content"])
#    audio_generator.text_to_speech(response["reddit_history"]["part2"]["content"], is_temp=True)
#    audio_generator.subtitles()

#    print("--------------------------------------------------------------------")


def test_whisper():
    audio_path = "src/media/audio/temp/part2.mp3"
    audio_generator.subtitles(audio_path, "test")


def test_subtitles_video() -> None:
    video_editor.load_subtitles(test_subtitles_file)
    return

def test_bg():
    bg = BgGenerator()
    clip_files = bg.get_files()[6:-1]

    # print(clip_files)
    files_raw = [
        "D:\\Videos\\sparkle_bot\\media\\video\\background_raw\\video_2.mp4",
        "D:\\Videos\\sparkle_bot\\media\\video\\background_raw\\video_3.mp4",
        "D:\\Videos\\sparkle_bot\\media\\video\\background_raw\\video_4.mp4",
        "D:\\Videos\\sparkle_bot\\media\\video\\background_raw\\video_5.mp4",
    ]
    for i in files_raw:
        bg.bg_generate(i)
    # for clip in clip_files:
    #     bg.generate_clips(clip)

    # bg.generate_clips(
    #   "D:\\Videos\\sparkle_bot\\media\\video\\background_movil_size\\video_6.mp4"
    # )


def test_video_generator() -> None:
    history_title: str = "El Reloj de Arena de la Abuela Emilia_part2"
    video_editor.load_subtitles(test_subtitles_file)
    video_editor.create_video(
        BgGenerator().get_random_clip(),
        test_audio_file,
        test_subtitles_file,
        history_title + ".mp4",
    )

    return


def test_final_video():
    print("Generating History")
    response = gemini.response(HistoryType.REDDIT, True)
    print("Ready!")

    history_title: str = response["reddit_history"]["title"]
    history_content: list[str] = [
        response["reddit_history"]["part1"]["content"],
        response["reddit_history"]["part2"]["content"],
    ]
    history_part: int = 1

    print("Generating audio")

    for i in history_content:
        audio_generator.text_to_speech(
            history_title + f"...parte {history_part}..." + i,
            is_temp=True,
            file_name=f"{history_title}_part{history_part}",
        )

        print(f"Audio {history_part} ready!")

        print(f"Generating Subtitles file {history_part}...")

        audio_generator.subtitles()

        print("Ready!")
        print(f"Generating video {history_part}")

        video_editor.create_video(
            bg_path=BgGenerator().get_random_clip(),
            audio_path=audio_generator.audio_file_path,
            subtitles_path=audio_generator.subtitles_file_path,
            video_name=history_title + f" parte {history_part}",
        )

        print("Ready!")

        history_part += 1
    return


if __name__ == "__main__":
    main()
