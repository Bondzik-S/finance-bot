import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import API_TOKEN
from handlers import start, finance


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

dp.include_router(start.router)
dp.include_router(finance.router)

async def main():
    print("Bot is running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
