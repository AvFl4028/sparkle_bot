from api.audio import Audio
from api.gemini import GeminiAPI, HistoryType
from keys import GEMINI_API_KEY, ELEVENLABS_API_KEY
from video_edition.BgGenerator import BgGenerator
from video_edition.video import VideoEditor

audio_generator = Audio(ELEVENLABS_API_KEY)
gemini = GeminiAPI(GEMINI_API_KEY)


def main():
    # test_gemini()
    # test_whisper()
    # test_bg()
    test_final_video()
    pass


def test_gemini():
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
    audio_generator.subtitles(audio_path)


def test_bg():
    bg = BgGenerator()
    clip_files = bg.get_files()[6:-1]

    print(clip_files)

    for clip in clip_files:
        bg.generate_clips(clip)

    # bg.generate_clips(
    #   "D:\\Videos\\sparkle_bot\\media\\video\\background_movil_size\\video_6.mp4"
    # )


def test_final_video():
    clip_path = "D:\\Videos\\sparkle_bot\\media\\video\\clips\\video_11\\clip_1.mp4"
    video = VideoEditor()
    video.create_video(
        clip_path,
        "src/media/audio/temp/72d08f0c-6ae5-4bcc-b5e3-24967e9f1e32.mp3",
        "src/media/audio/subtitles/72d08f0c-6ae5-4bcc-b5e3-24967e9f1e32.srt",
    )
    return


if __name__ == "__main__":
    main()
