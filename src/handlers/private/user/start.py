from aiogram import types, Router, Bot
from aiogram.filters import CommandStart, CommandObject, StateFilter
from aiogram.filters.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.utils.chat_action import ChatActionSender

from src.service.currency import get_rub_to

router = Router()


class Username(StatesGroup):
    get_username = State()


@router.message(CommandStart())
async def on_start(message: types.Message, command: CommandObject, state: FSMContext):
    text = f'Добрый день. Как вас зовут?'
    await state.set_state(Username.get_username)
    await message.answer(text=text)


@router.message(StateFilter(Username.get_username))
async def on_after_getting_username(message: types.Message, state: FSMContext, bot: Bot):
    async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
        username = message.text
        currency_value = await get_rub_to('USD')
        text = f'Рад знакомству, <b>{username}</b>!\n\n' \
               f'Курс доллара сегодня <code>{round(currency_value, 2)}</code> ₽'
        await message.answer(text)
    await state.clear()
