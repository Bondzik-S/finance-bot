from aiogram.fsm.state import State, StatesGroup

class FinanceState(StatesGroup):
    waiting_for_income = State()
    waiting_for_expense = State()
