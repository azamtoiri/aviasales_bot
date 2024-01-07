from typing import Optional

from aiogram.filters.state import StatesGroup, State


class FlightForm(StatesGroup):
    origin: str = State()
    destination: str = State()
    depart_date: str = State()
    direct: Optional[bool] = State()
    return_date: Optional[str] = State()
    currency: Optional[str] = State()
    sorting: Optional[str] = State()


