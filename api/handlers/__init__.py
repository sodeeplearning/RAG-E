import json

from fastapi import APIRouter

from . import prompting
from . import creating
from . import transfering
from . import botmanage

from config import bots_data_path, users_bots_path, bot_owns_to_path
from utils.files import *
from bots_data import bots, users_bots, bot_owns_to

from rage import RAG


if not os.path.isdir(bots_data_path):
    os.mkdir(bots_data_path)

router = APIRouter()

router.include_router(prompting.router)
router.include_router(creating.router)
router.include_router(transfering.router)
router.include_router(botmanage.router)


@router.on_event("startup")
async def startup_event():
    # Starting bots
    user_ids = os.listdir(bots_data_path)
    for current_user_id in user_ids:
        user_data_paths = getting_files(os.path.join(bots_data_path, current_user_id))
        bots[current_user_id] = RAG(user_data_paths)


@router.on_event("shutdown")
async def shutdown_event():
    # Updating users bots database
    with open(users_bots_path, "w") as json_file:
        json.dump(users_bots, json_file)

    # Updating bot_owns_to database
    with open(bot_owns_to_path, "w") as json_file:
        json.dump(bot_owns_to, json_file)


@router.get("/")
async def start():
    return {"available_users": list(bots.keys())}
