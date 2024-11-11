import os

from gtts import gTTS

from rage.config import is_slow, delete_files


class ToMachineSpeech:
    """Class made for text-to-speech task.

    This class translates text into a simple robot speech
    (the same as in a Google Translater)
    """
    def __init__(self):
        """Init func of text-to-speech model."""
        self.model = gTTS

    def get_file(
        self,
        text: str,
        language: str = "ru",
        slow: bool = is_slow,
        saving_path: str = "speech.mp3",
    ):
        """Get file of a machine speech.

        :param text: Text to translate.
        :param language: Language of text.
        :param slow: 'True' if you need slow speech.
        :param saving_path: Path for output file.
        """
        speech = self.model(text=text, lang=language, slow=slow)
        speech.save(saving_path)

    def get_bytes(
        self,
        text: str,
        language: str = "ru",
        slow: bool = is_slow,
        saving_path: str = "speech.mp3",
        delete_saved_file: bool = delete_files,
    ) -> bytes:
        """Get bytes of machine speech.

        :param text: Text to translate.
        :param language: Language of text.
        :param slow: 'True' if you need slow speech.
        :param saving_path: Path for output file.
        :param delete_saved_file: 'True' if you don't need audio file.
        :return: Bytes of audio file with machine speech.
        """
        self.get_file(text=text, language=language, slow=slow, saving_path=saving_path)
        with open(saving_path, "rb") as audio_file:
            audio_bytes = audio_file.read()

        if delete_saved_file:
            os.remove(saving_path)

        return audio_bytes

    def __call__(
        self,
        text: str,
        language: str = "ru",
        slow: bool = False,
        saving_path: str = "speech.mp3",
        delete_saved_file: bool = delete_files,
        *args,
        **kwargs
    ) -> bytes:
        """Get bytes of machine speech.

        :param text: Text to translate.
        :param language: Language of text.
        :param slow: 'True' if you need slow speech.
        :param saving_path: Path for output file.
        :param delete_saved_file: 'True' if you don't need audio file.
        :return: Bytes of audio file with machine speech.
        """
        return self.get_bytes(text, language, slow, saving_path, delete_saved_file)
