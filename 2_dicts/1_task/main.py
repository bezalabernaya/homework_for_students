import os

from decimal import Decimal

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SPLIT_SYMBOL = '\n'


def read_file(path: str) -> str:
    with open(path, 'r') as file:
        file_article = file.read()
    return file_article


def get_employees_info() -> list[str]:
    """Внешнее апи, которое возвращает вам список строк с данными по сотрудникам."""
    return read_file(os.path.join(
        BASE_DIR, '1_task', 'input_data.txt',
    )).split(SPLIT_SYMBOL)


def get_parsed_employees_info() -> list[dict[str, int | str]]:
    """Функция парсит данные, полученные из внешнего API и приводит их к стандартизированному виду."""
    _ = get_employees_info()
    parsed_employees_info = []
    d = {}
    # Ваш код ниже
    for m in _:
        i = m.split()
        for j in range(0, len(i), 2):
            if i[j] == 'age' or i[j] == 'id':
                d[i[j]] = int(i[j+1])
            elif i[j] == 'salary':
                d[i[j]] = Decimal(i[j+1])
            elif i[j] == 'name' or i[j] == 'last_name' or i[j] == 'position':
                d[i[j]] = i[j + 1]
        parsed_employees_info += [d]
        d = {}
    return parsed_employees_info
