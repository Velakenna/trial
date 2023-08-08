from YukkiMusic import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions, Message
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from YukkiMusic.plugins.modules.blast import blast_markup

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ " **Hey inga va veh nee** ",
           " **VE-NN-A thalaiya yena da pandra** ",
           " **Nalavaneee saptiya yenna pandra** ",
           " **deiii nee lam yen irruka poidu appdey heh😋** ",
           " **Nanae kolanthai da nambumga da** ",
           " **moodhugula knife yedhutu yara kuthulam nu partha yenna da nee vanthu nikuraa🙃** ",
           " **Ana solliten ithulam nalathuku illa parthukaa ! avalothan han🤨** ",
           " **Oru flow la poiturukum bothu yevan da athu nadula comedy pannikituu __ odddu** ",
           " **Ama onu vanganum heh yenna vangalam solluu🥲** ",
           " **dei murugesha antha AK47 gun ha konjam kooda bore adikuthu😋** ",
           " **yenna da suda matikuthi ! manichidu talaivarey bullet podala** ",
           " **athu yeppadey da yunna sudanum nu kekum bothu mattum bullet kanum🙄🤔** ",
           " **yunnaku yenna mooku neelama irrukam 🤔! pakathu theru la poster la irrunthuchhiii🏃🏃** ",
           " **Ana yunnaku vai irruke yennaku mela irruku 🙄🙄** ",
           " **sari yedhachum nalla song sollu kepom🫶** ",
           " **paatu poda sonna yena yen da podura ! venna thalaiya** ",
           " **yenna game thala aduva nee😛! oru match polama** ",
           " **Ama yunna pathi onu sonnangley ath uumnai ha🤔** ",
           " **sari yellame vithudu, nan oru 3 kelvi kekuren soluriya nu pakalam** ",
           " **yara nee neelam oru aley illaa venna thalaiya🤗** ",
           " **konjam kooda navura vidamatikuran heh yenna da venum yunnaku** ",
           " **Yevalo vati da sollurathu yunnaku mandai la brain heh illa da yunnaku venna thalaiya** ",
           " **Ana sathiyama sollala nee lam thiruntha mata🥺🥺** ",
           " **ama nan paitiyakaran na nee yaruu😶** ",
           " **yunnaku vekam lam vratha da sena panni marri nikuraa🤔** ",
           " **appadey ha ithu vera theriyaama pocha😜** ",
           " **amaa yenna alaiyee kanum sethutiya** ",
           " **nalla thingura yenna vitutu nalla irrpa** ",
           " **sari satu butu nu sollu yenna venum sapuda apram kasu illanu nu soliduven** ",
           " **Nee nalavana illna ketavanuku mela nalavn ha🙊** ",
           " **ama nee ipo yenna pandra yenna marri vetiya thane irrukaa apram yenga pore😺** ",
           " **sari sari pesunathu pothum poi toongu🥲** ",
           " **yepayum happy ha samthosama irru apo than yunna pakuravanga irruntha ivana marri irrukanum nu ninachi santhosama irrupanga😅** ",
           " **illana irrukura vanagalaiyum auchi irruka vidu da venna ythalaiya🙊🙊** ",
           " **Sooruu inga illaiyam pakathu veedu layum illaiyam agamothathuku sorru ilaiyam🙈🙈** ",
           " **porathum pore irru kuli kulla thali viduren🕳** ",
           " **sari apo nan kilamburen neeyum pesitu nalla urutitu poi toongu, thaniya da🙊** ",
           " **Nan nee avan avar ival iva yellarum ... onum illa..?👀** ",
           " **yelai anga yenna da pandra inga va game adalam** ",
           " **sari bore adicha sollu game adalam** ",
           " **inga oruthan irrupan nalla parru yunnakula irrukpan ana irrukamatan avan yar??😻** ",
           " **ama nee yaru sollu ?🙃** ",
           ]
ALONE = ["😊", "👋", "🌞", "🌛"]

@app.on_message(filters.command(["tagalls", "alls", "tagmembers"], prefixes=["/", "@", "!"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == "private":
        return await message.reply("This command can be used in groups and channels!")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in ("administrator", "creator"):
            is_admin = True
    if not is_admin:
        return await message.reply("**ᴏɴʟʏ ᴀᴅᴍɪɴ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ!**")

    if message.reply_to_message and message.text:
        return await message.reply("/tagme hello 🔫** ᴛʀʏ ᴛʜɪs ɴᴇxᴛ ᴛɪᴍᴇ ғᴏʀ ᴛᴀɢɢɪɴɢ...*")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagme hii 🔫 **ᴛʀʏ ᴛʜɪs ᴏʀ ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ...**")
    else:
        return await message.reply("/tagme hii 🔫 **ᴛʀʏ ᴛʜɪs ᴏʀ ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ...**")

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                print("text on cmd mode")
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            else:
                mode == "text_on_reply"
                print("text on reply mode")
                await msg.reply(f"[{random.choice(ALONE)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(10)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass

@app.on_message(filters.command(["cancel", "stop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("**innum arambikave illa ley 1st start pannu hehe apparam end pannu ! athayum thapa panatha ...**")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in ("administrator", "creator"):
            is_admin = True
    if not is_admin:
        return await message.reply("**ithu than thavarana seyal - niruvagi kitta kelunga (admins)...**")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("**yevan da niruthunathu irrunga da varen**")

# Assuming you have defined the client object and necessary setup for the Telegram bot

spam_chats = []

TAGMES = ["hi", "hello", "good morning", "good evening", "good night", "yellarum yenna pandringa","vetiya iruntha vc ku vanga work la irrunthalum vanga😉"]
EMOJI = ["😊", "👋", "🌞", "🌙","❤️", "💚", "💙", "💜", "🖤"]


#@app.on_message(filters.command(["tagme"], prefixes=["/", "@", "!"]))
@app.on_message(filters.regex(r'^/tagme ?(.*)'))
async def tagme_handler(client, message: Message):
    chat_id = message.chat.id
    if chat_id in spam_chats:
        await message.reply("The tagme command is already running in this chat.")
        return

    #if message.reply_to_message and message.text:
    if message.matches[0].group(1) and message.reply_to_message:
        return await message.reply("/tagme ** ᴛʀʏ ᴛʜɪs ɴᴇxᴛ ᴛɪᴍᴇ uh ғᴏʀ ᴛᴀɢɢɪɴɢ...*")
    #elif message.text:
    elif message.matches[0].group(1):
        mode = "text_on_cmd"
        #msg = message.text
        msg = message.matches[0].group(1)
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        #msg = await app.get_messages(message.chat.id, message.reply_to_message.message_id)
        if msg is None:
            return await message.reply("I cannot mention msgs sent before I was added in group")
    else:
        return await message.reply("Reply to message or give me a message for mentioning")
              
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""

    async for usr in client.iter_chat_members(chat_id):
        if not chat_id in spam_chats:
            break

        if usr.user.is_bot:
            continue

        usrnum += 1
        #usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "
        usrtxt += f"{usr.user.mention}"

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                markup = blast_markup()                    
                await message.reply_text(
                          txt, 
                          reply_markup=markup
                )
            elif mode == "text_on_reply":
                #await message.delete()
                markup = blast_markup()                       
                await msg.reply_text(
                          f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})", 
                          #reply_markup=markup
                )

            # Generate a random sleep time between 10 and 30 seconds(0 and 5 seconds)
            sleep_time = random.randint(0, 5)
            await asyncio.sleep(sleep_time)

            usrnum = 0
            usrtxt = ""

    try:
        spam_chats.remove(chat_id)
    except:
        pass

@app.on_callback_query(filters.regex("^blast$"))
async def on_callback_query(client, events):
    print("Callback query received:", events.data)
    if events.data == "blast":
              print("Blast button clicked!")
              morning_quote = f"Good morning {events.from_user.mention}! Here's a beautiful quote to start your day:\n\n""Life is what happens when you're busy making other plans. - John Lennon"                             
              await events.answer(f"Getting..")
              await events.message.edit_text(morning_quote)              
             
