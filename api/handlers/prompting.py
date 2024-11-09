from fastapi import APIRouter
from starlette.responses import Response

from api.models import PromptTextModel, TextModel
from api.status_messages import bot_not_found
from api.utils.checking import is_bot

from api.bots_data import bots

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
