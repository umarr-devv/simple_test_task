from aiogram import types, Router
from aiogram.filters import CommandStart, CommandObject

router = Router()


class Username(StatesGroup):
    get_username = State()


@router.message(CommandStart())
async def on_start(message: types.Message, command: CommandObject):
    text = f'Добро пожаловать, {message.from_user.full_name}'
    await message.answer(text=text)
