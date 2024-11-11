from fastapi import APIRouter, UploadFile
from typing import List
from os.path import join

from models import StatusModel
from config import bots_data_path
from status_messages import bot_not_found
from utils.files import zipfiles, getting_files
from utils.checking import is_bot

from bots_data import bots

from rage.rag import RAG
from rage.vtt import VideoToTextFile


router = APIRouter()

vtt_model = VideoToTextFile()


@router.post("/upload_videos")
async def upload_video(bot_id: str, files: List[UploadFile]) -> StatusModel:
    bot_dir = join(bots_data_path, bot_id)
    status = "success"

    if is_bot(bot_id):
        for current_file in files:
            file_name = current_file.filename
            saving_path = join(bot_dir, file_name)

            text_file_name = file_name.split(".")[0] + ".txt"
            text_saving_path = join(bot_dir, text_file_name)

            with open(saving_path, "wb") as saving_file:
                file_content = await current_file.read()
                saving_file.write(file_content)

            vtt_model(video_file=saving_path, text_saving_path=text_saving_path)

        bots[bot_id] = RAG(getting_files(bot_dir))
    else:
        status = bot_not_found

    return StatusModel(status=status)


@router.post("/add_data")
async def add_data(bot_id: str, files: List[UploadFile]) -> StatusModel:
    bot_dir = join(bots_data_path, bot_id)
    status = "success"

    if is_bot(bot_id):
        for current_file in files:
            file_name = current_file.filename
            saving_path = join(bot_dir, file_name)

            with open(saving_path, "wb") as saving_file:
                file_content = await current_file.read()
                saving_file.write(file_content)

        bots[bot_id] = RAG(getting_files(bot_dir))
    else:
        status = bot_not_found

    return StatusModel(status=status)


@router.get("/get_bot_data")
async def get_bot_data(bot_id: str):
    if is_bot(bot_id):
        bot_dir = join(bots_data_path, bot_id)
        user_files = getting_files(bot_dir)
        return zipfiles(user_files)

    return bot_not_found
