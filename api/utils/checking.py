from os import listdir

from ..config import bots_data_path


users_bots_ids = set(listdir(bots_data_path))


def is_bot(bot_id):
    return bot_id in users_bots_ids
