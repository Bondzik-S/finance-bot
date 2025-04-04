from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def on_start(message: Message):
    await message.answer("Hello! I'm your finance bot. \nUse /help for details.")

@router.message(Command("help"))
async def on_help(message: Message):
    help_text = (
        "📌 <b>List of commands:</b>\n\n"
        "/help - Show all commands\n"
        "/add_income - Add income\n"
        "/add_expense - Add expense\n"
        "/balance - View the balance\n"
        "/history - View transaction history\n"
    )
    await message.answer(help_text, parse_mode="HTML")