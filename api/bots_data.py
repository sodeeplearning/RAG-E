import os
import json

from api.config import users_bots_path, bot_owns_to_path


bots = dict()
users_bots = dict()
bot_owns_to = dict()

# Loading users_bots database
if os.path.isfile(users_bots_path):
    with open(users_bots_path, "r") as json_file:
        users_bots = json.loads(json_file.read())
else:
    json_file = open(users_bots_path, "w")
    json_file.close()

# Loading bot_owns_to database
if os.path.isfile(bot_owns_to_path):
    with open(bot_owns_to_path, "r") as json_file:
        bot_owns_to = json.loads(json_file.read())
else:
    json_file = open(bot_owns_to_path, "w")
    json_file.close()
