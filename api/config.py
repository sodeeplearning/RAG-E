import os

# API config
project_bots_data_path = "botdata"
project_users_bots_path = "usersbots.json"
project_bot_owns_to_path = "botownsto.json"

# Setting up config
ex_dir = os.getcwd()
bots_data_path = os.path.join(ex_dir, project_bots_data_path)
users_bots_path = os.path.join(ex_dir, project_users_bots_path)
bot_owns_to_path = os.path.join(ex_dir, project_bot_owns_to_path)
