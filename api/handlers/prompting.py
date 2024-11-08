from fastapi import APIRouter

from api.models import PromptTextModel, TextModel
from api.status_messages import bot_not_found
from api.utils.checking import is_bot

from api.bots_data import bots


router = APIRouter()


@router.post("/prompt_text")
async def prompt_text(body: PromptTextModel) -> TextModel:
    if is_bot(body.bot_id):
        model_answer = await bots[body.bot_id](body.prompt)
        return TextModel(text=model_answer)

    return TextModel(text=bot_not_found, status=bot_not_found)
