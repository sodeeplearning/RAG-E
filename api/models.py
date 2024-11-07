from pydantic import BaseModel


class BotIdModel(BaseModel):
    bot_id: str


class StatusModel(BaseModel):
    status: str = "success"
