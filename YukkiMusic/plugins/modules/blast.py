from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from YukkiMusic import app

def blast_markup():
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=("Blast!"),
                    callback_data=f"blast",
                ),

            ]
        ]
    )
    return upl

def open_me_markup():
    dei = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text=("🌻 • ⃤•  ᴏᴘᴇɴ ᴍᴇ ! • ⃤• 🌞"),callback_data=f"open_me")],
            [InlineKeyboardButton(text=("🥱 • ⃤•  Sυɾ-Pɾιȥҽ ! • ⃤• 🥴"),callback_data=f"surprise")],
            [InlineKeyboardButton(text=("☕️ •̴ ⃤̴•̴  C̴l̴i̴c̴k̴-̴M̴e̴ ! •̴ ⃤̴•̴  🍔"),callback_data=f"click_me")],
            [InlineKeyboardButton(text=("🌜• ⃤•  ｃĻ𝕠รє-Μ𝐞 ! • ⃤• 🌝"),callback_data=f"close_me")],
            
        ]
    )
    return dei

def effect_markup():
    oii = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Flowers", callback_data="flowers")],
            [InlineKeyboardButton("Rockets", callback_data="rockets")],
            [InlineKeyboardButton("Rain", callback_data="rain")],
            [InlineKeyboardButton("Leaves", callback_data="leaves")],
            [InlineKeyboardButton("Snow", callback_data="snow")],
            [InlineKeyboardButton("Bombs", callback_data="bombs")],
        ]
    )
    return oii
