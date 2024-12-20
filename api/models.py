from pydantic import BaseModel


class StatusModel(BaseModel):
    status: str = "success"


class BotIdModel(BaseModel):
    bot_id: str


class WishesModel(BotIdModel):
    wishes: str
    user_id: str


class PromptTextModel(BotIdModel):
    prompt: str


class TextModel(StatusModel):
    text: str


class CreatingBotResponseModel(BotIdModel):
    status: str = "success"


class BotManageModel(BotIdModel):
    user_id: str


class UsersBotsModel(BaseModel):
    bots_ids: list = []


class AddRemoveOwnerModel(BaseModel):
    bot_id: str
    bot_owner_user_id: str
    new_owner_user_id: str


class UserIdModel(BaseModel):
    user_id: str


class CustomerModel(UserIdModel):
    admin_id: str
