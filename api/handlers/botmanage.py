from os.path import join

from fastapi import APIRouter

from api.config import bots_data_path
from api.utils.checking import is_bot, is_user_bots_owner
from api.status_messages import bot_launched_before, bot_not_found, bots_not_users
from api.models import BotIdModel, WishesModel, StatusModel, DeleteStopBotModel
from api.utils.files import getting_files
from api.bots_data import bots

from rage.rag import RAG

router = APIRouter()


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


@router.post("/stop_bot")
async def stop_bot(body: DeleteStopBotModel) -> StatusModel:
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
        await bots[body.bot_id].update_wishes(body.wishes)
    else:
        status = bot_not_found

    return StatusModel(status=status)
