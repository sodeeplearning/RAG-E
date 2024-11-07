import os
from os.path import join

from fastapi import APIRouter, UploadFile
from typing import List
from hashlib import sha256
from datetime import datetime


from api.utils.checking import is_bot
from api.utils.path import getting_files
from api.config import bots_data_path
from api.models import BotIdModel, StatusModel

from api.bots_data import bots

from rage.rag import RAG


router = APIRouter()


@router.post("/createbot")
async def create_bot(files: List[UploadFile]) -> BotIdModel:
    bot_id = sha256(str(datetime.now()).encode("utf-8")).hexdigest()
    bot_dir = join(bots_data_path, bot_id)
    os.mkdir(bot_dir)

    for current_file in files:
        content = await current_file.read()
        saving_path = join(bot_dir, current_file.filename)
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
            status = "Error! Bot id has not found."
        else:
            users_path = join(bots_data_path, bot_id)
            users_files = getting_files(users_path)
            bots[bot_id] = RAG(users_files)

    return StatusModel(status=status)
