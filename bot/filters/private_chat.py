from typing import Optional

from aiogram.enums import ChatType
from aiogram.filters import BaseFilter
from aiogram.types import Message


class ChatPrivateFilter(BaseFilter):
    def __init__(self, chat_type: Optional[str, list]) -> None:
        self.chat_type = chat_type

    def __call__(self, message: Message) -> bool:
        return message.chat.type == ChatType.PRIVATE
