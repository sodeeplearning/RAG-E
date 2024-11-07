from fastapi import APIRouter, UploadFile
from typing import List
from os.path import join
from hashlib import sha256
from datetime import datetime

from . import bots

from ..utils.checking import is_bot
from ..utils.path import getting_files
from ..config import bots_data_path
from ..models import BotIdModel, StatusModel

from ...rage.rag import RAG


router = APIRouter()


@router.post("/createbot")
async def create_bot(files: List[UploadFile]) -> BotIdModel:
    bot_id = sha256(str(datetime.now()).encode("utf-8")).hexdigest()

    for current_file in files:
        content = await current_file.read()
        saving_path = join(bots_data_path, bot_id, current_file.filename)
        with open(saving_path, "wb") as saving_file:
            saving_file.write(content)

    return BotIdModel(bot_id=bot_id)


@router.post("/launchbot")
async def launch_bot(body: BotIdModel) -> StatusModel:
    bot_id = body.bot_id
    status = "success"

    if bot_id in bots:
        status = "Error! Bot has been launched before."
    else:
        if is_bot(bot_id):
            status = "Error! But id has not found!"
        else:
            users_path = join(bots_data_path, bot_id)
            users_files = getting_files(users_path)
            bots[bot_id] = RAG(users_files)

    return StatusModel(status=status)
