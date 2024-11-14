from os.path import join

from fastapi import APIRouter

from config import bots_data_path
from utils.checking import is_bot, is_user_bots_owner
from status_messages import bot_launched_before, bot_not_found, bots_not_users
from models import WishesModel, StatusModel, BotManageModel, UsersBotsModel, AddRemoveOwnerModel
from utils.files import getting_files
from bots_data import bots, users_bots, bot_owns_to

from rage import RAG


router = APIRouter()


@router.post("/launch_bot")
async def launch_bot(body: BotManageModel) -> StatusModel:
    bot_id = body.bot_id
    status = "success"

    if bot_id in bots:
        status = bot_launched_before
    else:
        if not is_bot(bot_id):
            status = bot_not_found
        else:
            if is_user_bots_owner(user_id=body.user_id, bot_id=bot_id):
                users_path = join(bots_data_path, bot_id)
                users_files = getting_files(users_path)
                bots[bot_id] = RAG(users_files)
            else:
                status = bots_not_users

    return StatusModel(status=status)


@router.post("/stop_bot")
async def stop_bot(body: BotManageModel) -> StatusModel:
    status = "success"

    if is_bot(body.bot_id):
        if is_user_bots_owner(body.user_id, body.bot_id):
            del bots[body.bot_id]
        else:
            status = bots_not_users
    else:
        status = bot_not_found

    return StatusModel(status=status)


@router.post("/add_wishes")
async def add_wishes(body: WishesModel) -> StatusModel:
    status = "success"

    if is_bot(body.bot_id):
        if is_user_bots_owner(bot_id=body.bot_id, user_id=body.user_id):
            await bots[body.bot_id].update_wishes(body.wishes)
        else:
            status = bots_not_users
    else:
        status = bot_not_found

    return StatusModel(status=status)


@router.get("/get_users_bots")
async def get_users_bots(user_id: str) -> UsersBotsModel:
    bots_ids = []
    if user_id in users_bots:
        bots_ids = users_bots[user_id]

    return UsersBotsModel(bots_ids=bots_ids)


@router.post("/add_owner")
async def add_owner_to_bot(body: AddRemoveOwnerModel) -> StatusModel:
    status = "success"
    if is_bot(bot_id=body.bot_id):
        if is_user_bots_owner(user_id=body.bot_owner_user_id, bot_id=body.bot_id):
            bot_owns_to[body.bot_id].append(body.new_owner_user_id)
        else:
            status = bots_not_users
    else:
        status = bot_not_found
    return StatusModel(status=status)


@router.delete("/remove_owner")
async def remove_bots_owner(body: AddRemoveOwnerModel) -> StatusModel:
    status = "success"
    if is_bot(bot_id=body.bot_id):
        if is_user_bots_owner(user_id=body.bot_owner_user_id, bot_id=body.bot_id):
            bot_owns_to[body.bot_id].remove(body.new_owner_user_id)
        else:
            status = bots_not_users
    else:
        status = bot_not_found
    return StatusModel(status=status)
