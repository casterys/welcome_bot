from aiogram import Bot, Dispatcher, executor, types
from main import *
from filter import *
from words_delete import delete_words

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply("Hello! I'm etrys_bot\nPowered by erys.vee")

@dp.message_handler(commands=['help'])
async def cmd_help(message: types.Message):
    await message.reply('h1 - Information about bot'
                        '\nh2 - Help from development'
                        '\nh3 - /commands')

@dp.message_handler(commands=['commands'])
async def cmd_commands(message: types.Message):
    await message.reply('/start\n/help\n/ban\n/youtube')

@dp.message_handler(is_admin=True, commands=["ban"])
async def cmd_ban(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Это команда должна быть ответом на сообщение!")
        return

    await message.bot.delete_message(config.GROUP_ID, message.message_id)
    await message.bot.kick_chat_member(chat_id=config.GROUP_ID, user_id=message.reply_to_message.from_user.id)

    await message.reply_to_message.reply("Пользова тель забанен!\n Правосудие совершилось :3")

@dp.inline_handler()
async def inline_handlar(query: types.InlineQuery):
    text = query.query or 'echo'
    links = searcher(text)

    articles = [types.InlineQueryResultArticle(
        id = hashlib.md5(f'{link["id"]}'.encode()).hexdigest(),
        title=f'{link["title"]}',
        url=f'https://www.youtube.com/watch?v={link["id"]}',
        thumb_url = f'{link["thumbnails"][0]}',
        input_message_content=types.InputTextMessageContent(message_text=f'https://www.youtube.com/watch?v={link["id"]}')
    ) for link in links]

    await query.answer(articles, cache_time=60, is_personal=True)

@dp.message_handler()
async def filter_message(message: types.Message):
    for i in delete_words:
        if i == message.text:
            await message.delete()
            break
