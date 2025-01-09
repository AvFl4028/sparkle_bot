from keys import GEMINI_API_KEY, ELEVENLABS_API_KEY
from api.gemini import GeminiAPI, HistoryType
from api.audio import Audio

from faster_whisper import WhisperModel

# TODO - Bug Se imprime el history_test.json sin razon alguna

audio_generator = Audio(ELEVENLABS_API_KEY)
gemini = GeminiAPI(GEMINI_API_KEY)


def main():
    #test_gemini()
    test_whisper()


def test_gemini():
    response = gemini.response(HistoryType.REDDIT, True)
    print("--------------------------------------------------------------------")
    print(response["reddit_history"]["part1"]["content"])
    audio_generator.subtitles("src/media/audio/temps/part1.mp3")
    print("--------------------------------------------------------------------")
    print(response["reddit_history"]["part2"]["content"])
    print("--------------------------------------------------------------------")
    #audio_generator.text_to_speech(response["reddit_history"]["part2"]["content"], file_name="part2")


def test_whisper():
    audio_path = "src/media/audio/temp/part2.mp3"
    audio_generator.subtitles(audio_path)


if __name__ == "__main__":
    main()

