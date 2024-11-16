from transformers import pipeline

from rage.config import use_gpu, stt_model


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
