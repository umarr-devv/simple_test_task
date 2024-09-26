import aiohttp

URL = 'https://www.cbr-xml-daily.ru/daily_json.js'


async def get_rub_currency_price(url: str = URL) -> dict:
    async with aiohttp.client.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json(content_type=None)


async def get_rub_to(to_currency: str) -> int:
    rub_currency_price = await get_rub_currency_price()
    return rub_currency_price['Valute'][to_currency]['Value']
