from telebot.async_telebot import AsyncTeleBot
from telebot import types
import random
from dotenv import load_dotenv
import os
import asyncio
import aiomysql


load_dotenv()


bot = AsyncTeleBot(os.getenv("TOK"))

@bot.message_handler(content_types=['text'])
async def get_text_messages(massage):
    if massage.text == "/start":
        await bot.send_message(massage.from_user.id, "Для начала напиши Привет")

    if massage.text == "Привет":
        keyboard = types.InlineKeyboardMarkup()
        key_schastie = types.InlineKeyboardButton(text='О счастье ✨', callback_data='schastie')
        keyboard.add(key_schastie)
        key_study = types.InlineKeyboardButton(text='Для учебы и работы 📚', callback_data='study')
        keyboard.add(key_study)
        key_life = types.InlineKeyboardButton(text='О жизни 🕛', callback_data='life')
        keyboard.add(key_life)
        key_love = types.InlineKeyboardButton(text='О любви ❤', callback_data='love')
        keyboard.add(key_love)
        key_loveyourself = types.InlineKeyboardButton(text='О любви к себе 🥰', callback_data='loveyourself')
        keyboard.add(key_loveyourself)
        key_foraday = types.InlineKeyboardButton(text='На каждый день 🏙', callback_data='foraday')
        keyboard.add(key_foraday)
        await bot.send_message(massage.from_user.id, text='Выбери мотивашку на сегодня', reply_markup=keyboard)

    elif massage.text == "/help":
        await bot.send_message(massage.from_user.id, "Напиши Привет")
    else:
        await bot.send_message(massage.from_user.id, "Я тебя не понимаю. Напиши /help.")


'''Функция для обработки нажатий на клавиши'''
@bot.callback_query_handler(func=lambda call: True)
async def callback_worker(call):
    conn = await aiomysql.connect(host='127.0.0.1', port=3306,
                                  user=os.getenv("USER_NAME"), password=os.getenv("USER_PASS"), db='db')
    cur = await conn.cursor()
    msg = ''
    if call.data == "schastie":
        await cur.execute("SELECT quote FROM quotes WHERE id='5' ORDER BY rand() LIMIT 1")
        msg = await cur.fetchall()
    elif call.data == "study":
        await cur.execute("SELECT quote FROM quotes WHERE id='6' ORDER BY rand() LIMIT 1")
        msg = await cur.fetchall()
    elif call.data == "life":
        await cur.execute("SELECT quote FROM quotes WHERE id='2' ORDER BY rand() LIMIT 1")
        msg = await cur.fetchall()
    elif call.data == "love":
        await cur.execute("SELECT quote FROM quotes WHERE id='3' ORDER BY rand() LIMIT 1")
        msg = await cur.fetchall()
    elif call.data == "loveyourself":
        await cur.execute("SELECT quote FROM quotes WHERE id='4' ORDER BY rand() LIMIT 1")
        msg = await cur.fetchall()
    elif call.data == "foraday":
        await cur.execute("SELECT quote FROM quotes WHERE id='1' ORDER BY rand() LIMIT 1")
        msg = await cur.fetchall()
    await cur.close()
    conn.close()
    await bot.send_message(call.message.chat.id, msg[0][0])


asyncio.run(bot.polling())
