from aiogram import types, Router
from aiogram.filters import CommandStart, CommandObject

router = Router()


class Username(StatesGroup):
    get_username = State()


@router.message(CommandStart())
async def on_start(message: types.Message, command: CommandObject, state: FSMContext):
    text = f'Добрый день. Как вас зовут?'
    await state.set_state(Username.get_username)
    await message.answer(text=text)
