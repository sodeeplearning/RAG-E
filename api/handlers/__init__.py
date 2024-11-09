from fastapi import APIRouter
import os

from . import prompting
from . import creating
from . import transfering
from . import botmanage

from api.config import bots_data_path
from api.utils.files import *
from api.bots_data import bots

from rage.rag import RAG


if not os.path.isdir(bots_data_path):
    os.mkdir(bots_data_path)

router = APIRouter()

router.include_router(prompting.router)
router.include_router(creating.router)
router.include_router(transfering.router)
router.include_router(botmanage.router)


@router.on_event("startup")
async def startup_event():
    user_ids = os.listdir(bots_data_path)
    for current_user_id in user_ids:
        user_data_paths = getting_files(os.path.join(bots_data_path, current_user_id))
        bots[current_user_id] = RAG(user_data_paths)


@router.get("/")
async def start():
    return {"available_users": list(bots.keys())}
