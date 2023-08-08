import asyncio
from pyrogram import filters
from pyrogram.types import CallbackQuery, Message

from aiogram import types
from typing import Union

from YukkiMusic import app


@app.on_callback_query(
    filters.regex("^open_me$")
)
async def on_open_me_button_click(_, etho: Union[types.Message, types.CallbackQuery]):
    print("Callback query received:", etho.message.text)
    chat_id = etho.message.chat.id    
    #await etho.answer("Getting your quote...", show_alert=False)
    await etho.edit_message_text(text="Getting your quote...")
    await asyncio.sleep(3)
    quote = get_random_quote()
    await etho.edit_message_text(            
        text=f"Good morning {etho.from_user.mention}! Here's a random quote:\n\n{quote}"
    )
    print("Morning button clicked!")    
    

    await etho.answer()
