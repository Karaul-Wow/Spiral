import asyncio
import aiohttp

async def fetch_matrix(url: str) -> str:
    """Обеспечивает асинхронную загрузку сроки из внешнего ресурса в соответствии с URL

    Raises:
    RuntimeError: Если загрузить данные не удалось.
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                raise RuntimeError(f"Статус ответа - {resp.status}")
            text = await resp.text()
            return text

if __name__ == "__main__":
    """Функция проверки работоспособности модуля"""
    url = "https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt" # + "убрать знак комментария для проверки отработки ошибки загрузки"
    try:
        text = asyncio.run(fetch_matrix(url))
        print("Получено символов:", len(text))
        print('Первые 200 символов загруженной строки: \n', text[:200])
    except RuntimeError as e:
        print(f"Ошибка загрузки. {e}")