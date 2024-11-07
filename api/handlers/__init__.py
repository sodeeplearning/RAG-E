from fastapi import APIRouter
import os

from . import prompting
from . import creating

from api.config import bots_data_path
from api.utils.path import *
from api.bots_data import bots

from rage.rag import RAG


router = APIRouter()

router.include_router(prompting.router)
router.include_router(creating.router)

data_path = bots_data_path


@router.on_event("startup")
async def startup_event():
    if os.path.isdir(data_path):
        user_ids = os.listdir(bots_data_path)
        for current_user_id in user_ids:
            user_data_paths = getting_files(os.path.join(data_path, current_user_id))
            bots[current_user_id] = RAG(user_data_paths)
    else:
        os.mkdir(data_path)


@router.get("/")
async def start():
    return {"available_users": list(bots.keys())}
