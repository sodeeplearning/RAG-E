import os
from os.path import join
from shutil import rmtree

from fastapi import APIRouter, UploadFile
from typing import List
from hashlib import sha256
from datetime import datetime


from utils.checking import is_bot, is_customer, is_user_bots_owner
from config import bots_data_path
from models import StatusModel, CreatingBotResponseModel, DeleteStopBotModel

from status_messages import not_customer, bot_not_found, bots_not_users
from bots_data import bots, users_bots, bot_owns_to


router = APIRouter()


@router.post("/create_bot")
async def create_bot(user_id: str, files: List[UploadFile]) -> CreatingBotResponseModel:
    if is_customer(user_id):
        bot_id = sha256(str(datetime.now()).encode("utf-8")).hexdigest()

        # Adding bot id to users' bots database
        if user_id in users_bots:
            users_bots[user_id].append(bot_id)
        else:
            users_bots[user_id] = [bot_id]

        # Updating bot_owns_to database
        bot_owns_to[bot_id] = [user_id]

        bot_dir = join(bots_data_path, bot_id)
        os.mkdir(bot_dir)

        for current_file in files:
            content = await current_file.read()
            saving_path = join(bot_dir, current_file.filename)
            with open(saving_path, "wb") as saving_file:
                saving_file.write(content)

        return CreatingBotResponseModel(bot_id=bot_id)

    return CreatingBotResponseModel(bot_id=None, status=not_customer)


@router.delete("/delete_bot")
async def delete_bot(body: DeleteStopBotModel) -> StatusModel:
    status = "success"

    if is_bot(body.bot_id):
        if is_user_bots_owner(body.user_id, body.bot_id):
            # Updating databases
            users_bots[body.user_id].remove(body.bot_id)
            del bot_owns_to[body.bot_id]

            bot_dir = join(bots_data_path, body.bot_id)
            if body.bot_id in bots:
                del bots[body.bot_id]
            rmtree(bot_dir)
        else:
            status = bots_not_users
    else:
        status = bot_not_found

    return StatusModel(status=status)
