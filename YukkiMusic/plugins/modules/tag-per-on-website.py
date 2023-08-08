from YukkiMusic import app
import random
import asyncio
import requests
from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery
from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from YukkiMusic.plugins.modules.blast import open_me_markup
from typing import Union


spam_chats = []

#TAGMES = ["hi", "hello", "good morning", "good evening", "good night"]
TAGMES = ["good morning", "good evening", "good night"]
EMOJI = ["😊", "👋", "🌞", "🌙"]

def get_random_quote():
    url = "https://quotes.toscrape.com/random"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    quote = soup.find("span", class_="text").text.strip()
    #author = soup.find("span", class_="author").text.strip()
    #return f"{quote}\n- {author}"
    return f"{quote}"

def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    data = response.json()
    return f"{data['setup']}\n{data['punchline']}"

@app.on_message(filters.command(["tagu"], prefixes=["/", "#", "@"]))
async def tagme_handler(client, message: Message):
    chat_id = message.chat.id
    if chat_id in spam_chats:
        await message.reply("The tagme command is already running in this chat.")
        return

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""

    async for usr in client.iter_chat_members(chat_id):
        if not chat_id in spam_chats:
            break

        if usr.user.is_bot:
            continue

        usrnum += 1
        #usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id})"
        usrtxt += f"{usr.user.mention}"

        if usrnum == 1:
            markup = open_me_markup()            
            await message.reply_text(
                f"{usrtxt} {random.choice(TAGMES)}", 
                reply_markup=markup
            )
            # Generate a random sleep time between 10 and 30 seconds
            sleep_time = random.randint(0, 5)
            await asyncio.sleep(sleep_time)

            usrnum = 0
            usrtxt = ""

    try:
        spam_chats.remove(chat_id)
    except:
        pass

@app.on_callback_query(
    filters.regex("open_me")
)
async def on_open_me_button_click(client, etho: Union[types.Message, types.CallbackQuery]):
    print("Callback query received:", message.text)
    chat_id = etho.message.chat.id
    try:
        message_text = callback_query.message.text
        user_name, query_message = message_text.split(": ", 1)  # Split only once
        # Now you can use user_name and query_message in your code        
    except:
        print("could not split")
        return

    time_of_day = query_message.lower()     
        
    if time_of_day == "good morning":
        print("Morning button clicked!")
        await etho.edit_message_text(text="Getting your quote...")
        asyncio.sleep(2)
        quote = get_random_quote()
        await etho.edit_message_text(            
            text=f"Good morning {etho.from_user.mention}! Here's a random quote:\n\n{quote}"
        )
    else:
        print("Evening button clicked!")
        await etho.edit_message_text(text="Getting your joke...")
        joke = get_random_joke()
        await etho.edit_message_text(
            text=f"Good evening {etho.from_user.mention}! Here's a random joke:\n\n{joke}"
        )

    await etho.answer()


