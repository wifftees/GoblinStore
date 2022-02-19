import asyncio
from aiohttp import ClientSession
from app import token


async def make_request(url, session):
    return await session.post(url)


async def send_messages(chat_ids, message):
    urls = [
        f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}" for chat_id in chat_ids
    ]
    async with ClientSession() as session:
        await asyncio.gather(*[make_request(url, session) for url in urls])
