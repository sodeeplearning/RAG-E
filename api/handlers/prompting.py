from fastapi import APIRouter

from api.models import PromptModel, TextModel
from api.bots_data import bots

router = APIRouter()


@router.post("/prompt")
async def prompt(body: PromptModel) -> TextModel:
    model_answer = await bots[body.bot_id](body.prompt)
    return TextModel(text=model_answer)
