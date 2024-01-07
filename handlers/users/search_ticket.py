from aiogram import Router, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.types import ReplyKeyboardRemove

from states.flight import FlightForm
from utils.misc.utils import origin_codes
from utils.misc.validate import NoMatchCountryError, DateError, validate_country, validate_date

router = Router()


@router.message(Command('find_ticket'))
async def fill_search_ticket(msg: Message, state: FSMContext):
    await state.clear()
    await state.set_state(FlightForm.origin)
    await msg.answer(
        'Введите страну отправления',
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(F.text == 'Посмотреть цены')
async def fill_search_ticket(msg: Message, state: FSMContext):
    await state.clear()
    await state.set_state(FlightForm.origin)
    await msg.answer(
        'Введите страну отправления',
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(FlightForm.origin)
async def airport_origin(msg: Message, state: FSMContext):
    try:
        origin_country = await validate_country(msg.text.casefold(), origin_codes)
        await state.update_data(origin=origin_country)
        await state.set_state(FlightForm.destination)
        await msg.answer('Выберите страну прибытия')
    except NoMatchCountryError as country_err:
        await msg.answer(f"{str(country_err)}")
    except Exception as e:
        await msg.answer("".join(str(e)))


@router.message(FlightForm.destination)
async def airport_destination(msg: Message, state: FSMContext):
    try:
        destination_codes = origin_codes.copy()
        destination_country = await validate_country(msg.text.casefold(), destination_codes)
        await state.update_data(destination=destination_country)
        await state.set_state(FlightForm.depart_date)
        await msg.answer('Введите дату вылета в формате YYYY-MM-DD')
    except NoMatchCountryError as country_err:
        await msg.answer(f"{str(country_err)}")
    except Exception as e:
        await msg.answer("".join(str(e)))


@router.message(FlightForm.depart_date)
async def show_tickets(msg: Message, state: FSMContext):
    from api.main import get_flight_prices
    from utils.misc.validate import readable_datetime, convert_minutes_to_hours_and_minutes
    from utils.misc.utils import reversed_origin_codes
    try:
        validate_date(msg.text)
        await state.update_data(depart_date=msg.text)
        data = await state.get_data()
        print(data)
        await state.clear()

        prices = await get_flight_prices(data.get('origin'), data.get('destination'), data.get('depart_date'))
        """All tickets prices"""
        print(prices[0])
        message = [
            f"<b>С:</b> {reversed_origin_codes.get(price[0])}\n"
            f"<b>В:</b> {reversed_origin_codes.get(price[1])}\n"
            f"<b>Дата и время:</b> {readable_datetime(price[2])}\n"
            f"<b>Price:</b> {price[3]}₽\n"
            f"<b>Время полета:</b> {convert_minutes_to_hours_and_minutes(price[4])}\n"
            f"<b>Рейс:</b> {price[5]} {price[6]}\n"
            f"<a href='https://aviasales.ru{price[7]}'>Посмотреть на сайте </a>\n"
            for price in prices
        ]

        """One ticket price"""
        cheapest_price = prices[0]
        cheapest_price = [
            f"<b> Самая выгодная цена! 🎲 </b>\n"
            f"<b>С:</b> {reversed_origin_codes.get(cheapest_price[0]).upper()}\n"
            f"<b>В:</b> {reversed_origin_codes.get(cheapest_price[1]).upper()}\n"
            f"<b>Дата и время:</b> {readable_datetime(cheapest_price[2])}\n"
            f"<b>Цена:</b> {cheapest_price[3]}₽\n"
            f"<b>Время полета:</b> {convert_minutes_to_hours_and_minutes(cheapest_price[4])}\n"
            f"<b>Рейс:</b> {cheapest_price[5]} {cheapest_price[6]}\n"
            f"<a href='https://aviasales.ru{cheapest_price[7]}'>Посмотреть на сайте </a>\n"
        ]

        await msg.answer("\n".join(message))
        await msg.answer("\n".join(cheapest_price))

    except DateError as de:
        await msg.answer("".join(str(de)))
