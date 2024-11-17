from os import remove

from fastapi import APIRouter, UploadFile
from starlette.responses import Response

from models import PromptTextModel, TextModel
from status_messages import bot_not_found
from utils.checking import is_bot

from .transfering import vatt_model

from bots_data import bots

from rage.tts.neural import ToSpeech as Speaker


router = APIRouter()

tts_model = Speaker()


@router.post("/prompt/text")
async def prompt_text(body: PromptTextModel) -> TextModel:
    if is_bot(body.bot_id):
        model_answer = await bots[body.bot_id](body.prompt)
        return TextModel(text=model_answer)

    return TextModel(text=bot_not_found, status=bot_not_found)


@router.post("/prompt/voice")
async def prompt_voice(body: PromptTextModel):
    if is_bot(body.bot_id):
        model_answer = await bots[body.bot_id](body.prompt)
        return Response(
            content=tts_model(model_answer),
            media_type="audio/wav"
        )
    return bot_not_found


@router.post("/prompt/from_voice/text")
async def prompt_text_from_voice(bot_id: str, audio_file: UploadFile) -> TextModel:
    if is_bot(bot_id=bot_id):
        audio_file_name = audio_file.filename
        saving_path = "audio" + audio_file_name

        with open(saving_path, "wb") as saving_file:
            content = await audio_file.read()
            saving_file.write(content)

        text = vatt_model.stt(audio_file=saving_path)
        remove(saving_path)

        model_answer = await bots[bot_id](text)
        return TextModel(text=model_answer)

    return TextModel(text=bot_not_found)


@router.post("/prompt/from_voice/voice")
async def prompt_voice_from_voice(bot_id: str, audio_file: UploadFile):
    if is_bot(bot_id=bot_id):
        audio_file_name = audio_file.filename
        saving_path = "audio" + audio_file_name

        with open(saving_path, "wb") as saving_file:
            content = await audio_file.read()
            saving_file.write(content)

        text = vatt_model.stt(audio_file=saving_path)
        remove(saving_path)

        model_answer = await bots[bot_id](text)

        return Response(
            content=tts_model(model_answer),
            media_type="audio/wav"
        )

    return bot_not_found
