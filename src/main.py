from api.audio import Audio, Engine
from api.gemini import GeminiAPI, HistoryType
from keys import GEMINI_API_KEY, ELEVENLABS_API_KEY
from video_edition.BgGenerator import BgGenerator
from video_edition.video import VideoEditor
from enum import Enum


class TestType(Enum):
    GEMINI = 0
    BACKGROUND = 1
    VIDEO_GENERATOR = 2
    WHISPER = 3
    SUBTITLES = 4
    FINAL_VIDEO = 5
    SUBTITLES_VIDEO = 6


class SparkleBot:
    def __init__(self):
        self.__history_type: HistoryType = HistoryType.REDDIT
        self.__audio_generator = Audio()
        self.__audio_generator.engine()
        self.__gemini = GeminiAPI(GEMINI_API_KEY)
        self.__video_editor = VideoEditor()

        self.__test_subtitles_file: str = (
            "src\\media\\audio\\subtitles\\La noche que el cielo cambió de color_part1.srt"
        )
        self.__test_audio_file: str = (
            "src\\media\\audio\\temp\\El Reloj de Arena de la Abuela Emilia_part2.mp3"
        )
        self.__generate_clip: str = BgGenerator().get_random_clip()

    def set_history_type(self, history: HistoryType) -> None:
        self.__history_type = history
        return

    def generate_video(self, videos_amount: int) -> None:
        print(f"Generando history de género {self.__history_type}")
        response = self.__gemini.response(self.__history_type, True)
        title: str = response["reddit_history"]["title"]
        history_content: list[str]
        history_num_parts: int

        match self.__history_type:
            case HistoryType.HORROR:
                history_content = [
                    response["reddit_history"]["part1"]["content"],
                    response["reddit_history"]["part2"]["content"],
                    response["reddit_history"]["part3"]["content"],
                    response["reddit_history"]["part4"]["content"],
                ]
            case HistoryType.REDDIT:
                history_content = [
                    response["reddit_history"]["part1"]["content"],
                    response["reddit_history"]["part2"]["content"],
                ]

        history_num_parts = len(history_content)

        if videos_amount > history_num_parts:
            print(
                f"Cantidad de videos mayor que la generada, se generaran {history_num_parts} videos"
            )

        return

    def set_audio_engine(self, engine: Engine, api_key: str) -> None:
        self.__audio_generator.engine(engine, api_key)
        return

    def test(self, test_type: TestType) -> None:
        match test_type:
            case TestType.GEMINI:
                self.__test_gemini()
            case TestType.BACKGROUND:
                self.__test_bg()
            case TestType.VIDEO_GENERATOR:
                self.__test_video_generator()
            case TestType.WHISPER:
                self.__test_whisper()
            case TestType.SUBTITLES:
                self.__test_whisper()
            case TestType.FINAL_VIDEO:
                self.__test_final_video()
            case TestType.SUBTITLES_VIDEO:
                self.__test_subtitles_video()
            case _:
                print("Error, test no encontrado")
        return

    def __test_gemini(self) -> None:
        response = self.__gemini.response(HistoryType.HORROR)
        print("Starting Generative Text, Text to Speech and Subtitles generator")
        print("--------------------------------------------------------------------")
        print(response)
        print("--------------------------------------------------------------------")

    def __test_whisper(self):
        audio_path = "src/media/audio/temp/part2.mp3"
        self.__audio_generator.subtitles(audio_path, "test")

    def __test_subtitles_video(self) -> None:
        self.__video_editor.load_subtitles(self.__test_subtitles_file)
        return

    def __test_bg(self):
        bg = BgGenerator()
        files_raw = [
            "D:\\Videos\\sparkle_bot\\media\\video\\background_movil_size\\video_5.mp4",
        ]
        for i in files_raw:
            bg.generate_clips(i)

    def __test_video_generator(self) -> None:
        history_title: str = "El Reloj de Arena de la Abuela Emilia_part2"
        self.__video_editor.load_subtitles(self.__test_subtitles_file)
        self.__video_editor.create_video(
            self.__generate_clip,
            self.__test_audio_file,
            self.__test_subtitles_file,
            history_title + ".mp4",
        )

        return

    def __test_final_video(self):
        print("Generating History")
        response = self.__gemini.response(HistoryType.REDDIT, True)
        print("Ready!")

        history_title: str = response["reddit_history"]["title"]
        history_content: list[str] = [
            response["reddit_history"]["part1"]["content"],
            response["reddit_history"]["part2"]["content"],
        ]
        history_part: int = 1

        print("Generating audio")

        for i in history_content:
            self.__audio_generator.text_to_speech(
                history_title + f"...parte {history_part}..." + i,
                is_temp=True,
                file_name=f"{history_title}_part{history_part}",
            )

            print(f"Audio {history_part} ready!")

            print(f"Generating Subtitles file {history_part}...")

            self.__audio_generator.subtitles()

            print("Ready!")
            print(f"Generating video {history_part}")

            self.__video_editor.create_video(
                bg_path=BgGenerator().get_random_clip(),
                audio_path=self.__audio_generator.audio_file_path,
                subtitles_path=self.__audio_generator.subtitles_file_path,
                video_name=history_title + f" parte {history_part}.mp4",
            )

            print("Ready!")

            history_part += 1
        return


def main() -> None:
    sparkle = SparkleBot()
    sparkle.test(TestType.SUBTITLES)
    return


if __name__ == "__main__":
    main()
