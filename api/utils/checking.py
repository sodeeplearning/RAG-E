from os import listdir

from api.config import bots_data_path


def is_bot(bot_id: str) -> bool:
    users_bots_ids = set(listdir(bots_data_path))
    return bot_id in users_bots_ids


# TODO:
def is_customer(user_id: str) -> bool:
    return True


# TODO:
def is_user_bots_owner(user_id, bot_id) -> bool:
    return True
