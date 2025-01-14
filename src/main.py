from api.audio import Audio
from api.gemini import GeminiAPI, HistoryType
from keys import GEMINI_API_KEY, ELEVENLABS_API_KEY
from video_edition.BgGenerator import BgGenerator

# TODO - Bug Se imprime el history_test.json sin razon alguna

audio_generator = Audio(ELEVENLABS_API_KEY)
gemini = GeminiAPI(GEMINI_API_KEY)


def main():
    # test_gemini()
    # test_whisper()
    test_bg()
    pass


def test_gemini():
    response = gemini.response(HistoryType.REDDIT, True)
    print("Starting Generative Text, Text to Speech and Subtitles generator")
    print("--------------------------------------------------------------------")

    print(response["reddit_history"]["part1"]["content"])
    audio_generator.text_to_speech(response["reddit_history"]["part1"]["content"], is_temp=True)
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
    bg.generate_clips("D:\\Videos\\sparkle_bot\\media\\video\\background_movil_size\\video_6.mp4")

if __name__ == "__main__":
    main()
