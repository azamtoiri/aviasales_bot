from datetime import datetime
from difflib import get_close_matches


class NoMatchCountryError(Exception):
    def __init__(self) -> None:
        super().__init__(f"Извините но мы не нашли старну по имени попробуйте еще раз")


class DateError(Exception):
    def __init__(self) -> None:
        super().__init__("Введите дату в этом формате YYYY-MM-DD")


async def validate_country(input_value, country_dict) -> str | None:
    """Validating country"""
    input_value_lower = input_value

    # Используем difflib для нахождения близких совпадений
    matches = get_close_matches(input_value_lower, country_dict.keys(), n=1, cutoff=0.6)

    if matches:
        return country_dict.get(matches[0])
    else:
        raise NoMatchCountryError


def validate_date(input_date):
    try:
        # Пытаемся преобразовать строку в объект datetime
        datetime_object = datetime.strptime(input_date, '%Y-%m-%d')
        return datetime_object
    except ValueError:
        # Если произошла ошибка, значит, введенная строка не соответствует формату
        raise DateError


def readable_datetime(raw_time):
    # Преобразование строки времени в объект datetime
    datetime_obj = datetime.fromisoformat(raw_time[:-6])  # Удаление часового пояса (+03:00)

    # Форматирование времени в более читаемый вид
    readable_time = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')

    return readable_time


def convert_minutes_to_hours_and_minutes(minutes) -> str:
    if minutes < 0:
        raise ValueError("Количество минут должно быть неотрицательным числом.")

    hours = minutes // 60
    remaining_minutes = minutes % 60

    return f"{hours}ч {remaining_minutes} минут"


if __name__ == '__main__':
    print(convert_minutes_to_hours_and_minutes(315))
