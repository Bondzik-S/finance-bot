from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from finance_bot.states import FinanceState


router = Router()

@router.message(Command("add_income"))
async def add_income(message: Message, state: FSMContext):
    await message.answer("💰 Enter the amount of income:")
    await state.set_state(FinanceState.waiting_for_income)

@router.message(FinanceState.waiting_for_income)
async def process_income(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("⚠️ Please enter a number!")
        return

    amount = int(message.text)
    await message.answer(f"✅ Income in the amount of {amount} UAH added!")
    await state.clear()
