from TTS.api import TTS

from tts.config import *


class ToSpeech:
    def __init__(self):
        self.model = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=use_gpu)

    def say(self, text: str):
        pass