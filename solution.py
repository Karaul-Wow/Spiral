from typing import List

from fetcher import fetch_matrix
from parser import parse_matrix
from spiral import get_spiral


async def get_matrix(url: str) -> List[int]:
    """
    Загружает матрицу по URL, парсит её и возвращает элементы в порядке
    обхода по спирали против часовой стрелки.

    :param url: URL для загрузки матрицы (HTTP/HTTPS).
    :return: Список целых чисел — результат спирального обхода.
    :raises RuntimeError: Если произошла ошибка сети или сервера.
    """
    # Шаг 1: асинхронная загрузка
    raw_text = await fetch_matrix(url)

    # Шаг 2: парсинг текста в матрицу (список списков)
    matrix = parse_matrix(raw_text)

    # Шаг 3: обход по спирали и возврат плоского списка
    return get_spiral(matrix)

if __name__ == "__main__":
    import asyncio

    SOURCE_URL = "https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt"
    TRAVERSAL = [
        10, 50, 90, 130,
        140, 150, 160, 120,
        80, 40, 30, 20,
        60, 100, 110, 70,
    ]

