from pydantic import BaseModel


class StatusModel(BaseModel):
    status: str = "success"


class BotIdModel(BaseModel):
    bot_id: str


class WishesModel(BotIdModel):
    wishes: str


class PromptTextModel(BotIdModel):
    prompt: str


class TextModel(StatusModel):
    text: str


class CreatingBotResponseModel(BotIdModel):
    status: str = "success"
