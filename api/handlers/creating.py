import os
from os.path import join

from fastapi import APIRouter, UploadFile
from typing import List
from hashlib import sha256
from datetime import datetime


from api.utils.checking import is_bot, is_customer
from api.utils.files import getting_files
from api.config import bots_data_path
from api.models import BotIdModel, StatusModel, WishesModel, CreatingBotResponseModel

from api.status_messages import not_customer, bot_not_found, bot_launched_before
from api.bots_data import bots

from rage.rag import RAG


router = APIRouter()


@router.post("/create_bot")
async def create_bot(user_id: str, files: List[UploadFile]) -> CreatingBotResponseModel:
    if is_customer(user_id):
        bot_id = sha256(str(datetime.now()).encode("utf-8")).hexdigest()
        bot_dir = join(bots_data_path, bot_id)
        os.mkdir(bot_dir)

        for current_file in files:
            content = await current_file.read()
            saving_path = join(bot_dir, current_file.filename)
            with open(saving_path, "wb") as saving_file:
                saving_file.write(content)

        return CreatingBotResponseModel(bot_id=bot_id)

    return CreatingBotResponseModel(bot_id=None, status=not_customer)


@router.post("/launch_bot")
async def launch_bot(body: BotIdModel) -> StatusModel:
    bot_id = body.bot_id
    status = "success"

    if bot_id in bots:
        status = bot_launched_before
    else:
        if not is_bot(bot_id):
            status = bot_not_found
        else:
            users_path = join(bots_data_path, bot_id)
            users_files = getting_files(users_path)
            bots[bot_id] = RAG(users_files)

    return StatusModel(status=status)


@router.post("/add_wishes")
async def add_wishes(body: WishesModel) -> StatusModel:
    status = "success"

    if is_bot(body.bot_id):
        await bots[body.bot_id].update_wishes(body.wishes)
    else:
        status = bot_not_found

    return StatusModel(status=status)
