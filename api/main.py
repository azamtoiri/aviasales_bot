import asyncio
from typing import Optional

import requests

from constants import Settings
from api.utils import headers, URL


async def get_flight_prices(
        origin: str,
        destination: str,
        depart_date: str,
        direct: Optional[bool] = True,
        return_date: Optional[str] = "",
        currency: Optional[str] = "rub",
        sorting: Optional[str] = "price"
) -> list:
    """
    Get flight prices
    :param origin: пункт отправления. IATA-код города или аэропорта. Длина не менее двух и не более трёх символов.
     Необходимо указать, если нет destination
    :param destination: пункт назначения. IATA-код города или аэропорта. Длина не менее двух и не более трёх.
     Необходимо указать, если нет origin
    :param depart_date: дата вылета из пункта отправления (в формате YYYY-MM или YYYY-MM-DD).
    :param return_date:(необязательно) — дата возвращения. Чтобы получить билеты в один конец, оставьте это поле пустым.
    :param direct: Получить рейсы без пересадок. Принимает значения true или false. По умолчанию false.
    :param currency: Валюта цен на билеты. Значение по умолчанию — rub.
    :param sorting: Sorting with price or route
    sorting — сортировка цен:
        price — по цене (значение по умолчанию),
        route — по популярности маршрута.
    :return: List with flights tuples
    """
    token = Settings.API_TOKEN

    params = {
        "origin": origin,
        "destination": destination,
        "depart_date": depart_date,
        "return_date": return_date,
        "currency": currency,
        "sorting": sorting,
        "direct": direct,
        "token": token,
    }

    try:
        response = requests.get(URL, headers=headers, params=params)
        response.raise_for_status()  # Проверка наличия ошибок в запросе
        values = response.json().get('data', [])
        flights_data = []

        for price in values:
            flight_info = (
                price['origin_airport'],
                price['destination_airport'],
                price['departure_at'],
                price['price'],
                price['link']
            )
            flights_data.append(flight_info)

        print("Запрос выполнен успешно.")
        return flights_data
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return []


def get_flight_prices_generator(
        origin: str,
        destination: str,
        depart_date: str,
        direct: Optional[bool] = True,
        return_date: Optional[str] = "",
        currency: Optional[str] = "rub",
        sorting: Optional[str] = "price"
) -> list:
    """
    Generator for getting prices,
    :return one flight with type of tuple
    """
    global response
    token = Settings.API_TOKEN

    params = {
        "origin": origin,
        "destination": destination,
        "depart_date": depart_date,
        "return_date": return_date,
        "direct": direct,
        "currency": currency,
        "sorting": sorting,
        "token": token,
    }

    try:
        response = requests.get(URL, headers=headers, params=params)
        response.raise_for_status()  # Проверка наличия ошибок в запросе
        values = response.json().get('data', [])

        for price in values:
            flight_info = (
                price['origin_airport'],
                price['destination_airport'],
                price['departure_at'],
                price['price'],
                price['link']
            )
            yield flight_info
        print("Запрос выполнен успешно.")
    except requests.exceptions.RequestException as e:
        print(response.status_code)
        print(f"Ошибка при выполнении запроса: {e}")


# Пример использования функции
async def main():
    flights_data = await get_flight_prices("MOW", "LED", "2024-01-10")
    print(flights_data)



if __name__ == '__main__':
    # asyncio.run(main())

    # Пример использования генератора
    flight_generator = get_flight_prices_generator("MOW", "LED", "2024-01-10")
    for flight in flight_generator:
        print(flight['origin_airport'], flight['destination_airport'], flight['departure_at'], flight['price'],
              f"\n{flight['link']}")
        print('-' * 20)