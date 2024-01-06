from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.types import ReplyKeyboardRemove

from bot.keyboards.reply.airports_buttons import airports
from bot.states.flight import FlightState

router = Router()


@router.message(F.text == 'Посмотреть цены')
async def fill_search_ticket(msg: Message, state: FSMContext):
    await state.set_state(FlightState.origin)
    await msg.answer('Выберите страну отравления', reply_markup=airports)


@router.message(FlightState.origin)
async def airport_origin(msg: Message, state: FSMContext):
    await state.update_data(origin=msg.text)
    await state.set_state(FlightState.destination)
    await msg.answer('Выберите страну прибытия')


@router.message(FlightState.destination)
async def airport_destination(msg: Message, state: FSMContext):
    await state.update_data(destination=msg.text)
    await state.set_state(FlightState.depart_date)
    await msg.answer('Выберите дату вылета', reply_markup=ReplyKeyboardRemove())


@router.message(FlightState.depart_date)
async def show_tickets(msg: Message, state: FSMContext):
    from api.main import get_flight_prices

    await state.update_data(depart_date=msg.text)
    data = await state.get_data()
    await state.clear()
    prices = await get_flight_prices(data.get('origin'), data.get('destination'), data.get('depart_date'))
    print(prices)

    formatted_text = []
    [
        formatted_text.append(f"{key}: {value}")
        for key, value in data.items()
    ]
    await msg.answer("\n".join(formatted_text))
