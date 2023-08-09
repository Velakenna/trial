import datetime
import pytz
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

TAGMES = ["good morning", "good evening", "good night", "good afternoon"]
EMOJI = ["😊", "👋", "🌞", "🌙"]

def get_random_news():    
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=8b7f36dbfcdc4d43bf0a9df50243072a"    
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'ok' and data['totalResults'] > 0:
        articles = data['articles']
        random_article = articles[random.randint(0, len(articles) - 1)]
        title = random_article['title']
        description = random_article['description']
        source = random_article['source']['name']
        url = random_article['url']
        
        news_info = f"Title: {title}\n\n\nSource: {source}\n\nURL: {url}"
        return news_info
    else:
        return "Unable to fetch random news article.Better luck next time"

def get_random_quote():
    url = "https://quotes.toscrape.com/random"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    quote = soup.find("span", class_="text").text.strip()    
    return f"{quote}"

def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    data = response.json()
    return f"{data['setup']}\n{data['punchline']}"

@app.on_message(filters.command(["tagu"], prefixes=["/", "#", "@"]))
async def tagme_handler(client, message: Message):
    # Set the desired time zone
    tz = pytz.timezone('Asia/Kolkata')
    # Get the current time
    current_time = datetime.datetime.now(tz).time()
    # Determine the appropriate tag message based on the time of day
    if current_time >= datetime.time(4, 0) and current_time < datetime.time(8, 20):
        #msg = random.choice(TAGMES) + " " + EMOJI[2]  # Good morning
        msg = f"Good morning 🌞"
    elif current_time >= datetime.time(8, 20) and current_time < datetime.time(10, 45):
        #msg = random.choice(TAGMES) + " " + EMOJI[3]  # Good afternoon
        msg = f"Good afternoon 😊"
    elif current_time >= datetime.time(10, 45) and current_time < datetime.time(10, 48):
        #msg = random.choice(TAGMES) + " " + EMOJI[0]  # Good evening
        msg = f"Good evening 👋"
    else:
        #msg = random.choice(TAGMES) + " " + EMOJI[1]  # Good night
        msg = f"Good night 🌙"
    
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
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id})"
        #usrtxt += f"{usr.user.mention}"

        if usrnum == 1:
            markup = open_me_markup()
            tag_message = f"[{usr.user.first_name}](tg://user?id={usr.user.id}) {msg}"
            await message.reply_text(tag_message, reply_markup=markup)
            
            
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
    print("Callback query received:", etho.message.text)
    chat_id = etho.message.chat.id
    user_name = etho.from_user.first_name
    message_text = etho.message.text    
    
    if user_name in etho.message.text:
        if "good morning" in etho.message.text.lower():
            print("Morning button clicked!")
            await etho.edit_message_text(text="Getting your quote...")
            await asyncio.sleep(2)
            quote = get_random_quote()
            await etho.edit_message_text(            
                text=f"Good morning {etho.from_user.mention}! Here's a random quote:\n\n{quote}"
            )

        elif "good afternoon" in etho.message.text.lower():
            print("Afternoon button clicked!")
            await etho.edit_message_text(text="Getting your afternoon joke...")
            await asyncio.sleep(2)
            ta_joke = get_random_tamil_joke()
            await etho.edit_message_text(
                text=f"Good afternoon {etho.from_user.mention}! Here's a random Tamil joke:\n\n{ta_joke}")

        elif "good night" in etho.message.text.lower():
            print("Night button clicked!")
            await etho.edit_message_text(text="Getting your night message...")
            await asyncio.sleep(2)
            #ta_quote = get_random_tamil_quote()
            random_news = get_random_news()
            await etho.edit_message_text(
                text=f"Good night {etho.from_user.mention}! Here's a random news\n\n{random_news}")
            
        else:
            print("Evening button clicked!")
            await etho.edit_message_text(text="Getting your joke...")
            await asyncio.sleep(2)
            joke = get_random_joke()
            await etho.edit_message_text(
                text=f"Good evening {etho.from_user.mention}! Here's a random joke:\n\n{joke}"
            )

        await etho.answer()

    else:
        await etho.answer("Sorry this button is not for you")    
    
