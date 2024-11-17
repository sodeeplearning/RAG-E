import os

import torchaudio
import torch
from transformers import AutoTokenizer, AutoModel

from rage.config import use_gpu, delete_files, audio_speed, torch_dtype


class ToSpeech:
    """Class made for text-to-speech task via AI."""

    def __init__(self, language: str = "rus", use_cuda: bool = use_gpu):
        """Init func of ToSpeech class.

        :param language: Language of text.
        :param use_cuda: 'True' if you will use gpu.
        """
        self.supported_languages = ("rus", "eng")
        assert (
            language in self.supported_languages
        ), f"Supported languages: {self.supported_languages}"

        self.device = "cuda" if use_cuda else "cpu"
        self.usage_case = f"facebook/mms-tts-{language}"
        self.model = AutoModel.from_pretrained(
            self.usage_case,
        ).to(self.device)

        self.tokenizer = AutoTokenizer.from_pretrained(self.usage_case)
        self.default_sample_rate = 16000

    def predict(self, text: str):
        """Get prediction from text in chosen language.

        :param text: Text to get speech.
        :return: Model's output.
        """
        inputs = self.tokenizer(text, return_tensors="pt").to(self.device)
        with torch.no_grad():
            output = self.model(**inputs)
        return output

    def get_file(self, text: str, path: str = "speech.wav", speed: float = audio_speed) -> None:
        """Get file of speech in audio format.

        :param text: Text to get speech.
        :param path: Path for output file.
        :param speed: Speed of speech (Default = 1.0, from 0.1 to 2.0).
        """
        output = self.predict(text=text).waveform.cpu()
        torchaudio.save(
            uri=path, src=output, sample_rate=int(self.default_sample_rate * speed)
        )

    def get_bytes(
        self,
        text: str,
        path: str = "speech.wav",
        speed: float = audio_speed,
        delete_saved_file: bool = delete_files,
    ) -> bytes:
        """Get bytes of audio file with speech.

        :param text: Text to get speech.
        :param path: Path for output file.
        :param speed: Speed of speech (Default = 1.0, from 0.1 to 2.0).
        :param delete_saved_file: 'True' if you don't need audio file.
        :return: Bytes of audio file with speech.
        """
        self.get_file(text=text, path=path, speed=speed)
        with open(path, "rb") as audio_file:
            audio_bytes = audio_file.read()

        if delete_saved_file:
            os.remove(path)

        return audio_bytes

    def __call__(
        self,
        text: str,
        path: str = "speech.wav",
        speed: float = audio_speed,
        delete_saved_file: bool = delete_files,
        *args, **kwargs
    ) -> bytes:
        """Get bytes of audio file with speech.

        :param text: Text to get speech.
        :param path: Path for output file.
        :param speed: Speed of speech (Default = 1.0, from 0.1 to 2.0).
        :param delete_saved_file: 'True' if you don't need audio file.
        :return: Bytes of audio file with speech.
        """
        return self.get_bytes(text=text, path=path, speed=speed, delete_saved_file=delete_saved_file)
