from os import listdir

from config import bots_data_path, admin_ids
from bots_data import bot_owns_to, clients_database


def is_bot(bot_id: str) -> bool:
    users_bots_ids = set(listdir(bots_data_path))
    return bot_id in users_bots_ids


# TODO:
def is_customer(user_id: str) -> bool:
    return user_id in clients_database


def is_user_bots_owner(user_id, bot_id) -> bool:
    return bot_id in bot_owns_to and user_id in bot_owns_to[bot_id]


def is_admin(user_id: str) -> bool:
    return user_id in admin_ids
