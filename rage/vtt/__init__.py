from os import remove

from transformers import pipeline

from rage.config import use_gpu, stt_model, delete_files
from rage.vtt.utils import *


class SpeechRecognition:
    """Class made for Speech-To-Text task."""
    def __init__(self, use_cuda: bool = use_gpu, model_name: str = stt_model):
        """Constructor of a SpeechRecognition class.

        :param use_cuda: 'True' if you need to use GPU.
        :param model_name: STT model's name.
        """
        self.device = "cuda" if use_cuda else "cpu"
        self.model = pipeline(
            task="automatic-speech-recognition",
            model=model_name,
            device=self.device
        )

    def __call__(self, audio_file: str, *args, **kwargs) -> str:
        """Get brief from audio file

        :param audio_file: Audio file path.
        :return: Text of audio file.
        """
        return self.model(audio_file)["text"]


class VideoToTextFile:
    """Class to extract text from video."""
    def __init__(self):
        """Constructor of VideoToTextFile class."""
        self.stt = SpeechRecognition()

    def video_to_text_file(self,
                           video_file: str,
                           text_saving_path: str = None,
                           delete_after_process: bool = delete_files):
        """Get text file from video's text.

        :param video_file: Path to a video file.
        :param text_saving_path: Path to a saving file.
        :param delete_after_process: 'True' if you don't need to store video and audio files.
        """
        video_file_name = video_file.split(".")[0]

        if text_saving_path is None:
            text_saving_path = f"{video_file_name}.txt"
        audio_saving_path = f"{video_file_name}.mp3"

        video_to_audio(video_file, audio_saving_path)
        extracted_text = self.stt(audio_saving_path)

        write_file(extracted_text, text_saving_path)

        if delete_after_process:
            remove(video_file)
            remove(audio_saving_path)

    def __call__(self,
                 video_file: str,
                 text_saving_path: str = None,
                 delete_after_process: bool = delete_files,
                 *args, **kwargs):
        """Get text file from video's text.

        :param video_file: Path to a video file.
        :param text_saving_path: Path to a saving file.
        """
        self.video_to_text_file(video_file, text_saving_path)
