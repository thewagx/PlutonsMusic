from pyrogram import filters
from pyrogram.enums import ChatType, ParseMode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

import config
from FallenMusic import BOT_MENTION, BOT_NAME, app
from FallenMusic.Helpers.database.chatsdb import add_served_chat
from FallenMusic.Helpers.database.usersdb import add_served_user
from FallenMusic.Helpers import gp_buttons, pm_buttons
from FallenMusic.Helpers.dossier import *


@app.on_message(filters.command(["start"]) & ~filters.forwarded)
@app.on_edited_message(filters.command(["start"]) & ~filters.forwarded)
async def fallen_st(_, message: Message):
    if message.chat.type == ChatType.PRIVATE:
        if len(message.text.split()) > 1:
            cmd = message.text.split(None, 1)[1]
            if cmd[0:3] == "inf":
                m = await message.reply_text("🔎")
                query = (str(cmd)).replace("info_", "", 1)
                query = f"https://www.youtube.com/watch?v={query}"
                results = VideosSearch(query, limit=1)
                for result in (await results.next())["result"]:
                    title = result["başlık"]
                    duration = result["süre"]
                    views = result["viewCount"]["short"]
                    thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                    channellink = result["kanal"]["link"]
                    channel = result["kanal adı"]["name"]
                    link = result["link"]
                    published = result["tamamlanma süresi"]
                searched_text = f"""
➻ **Parça Bilgileri** 

📌 **ʙᴀşʟıᴋ :** {title}

⏳ **sᴜ̈ʀᴇ :** {duration} ᴅᴀᴋɪᴋᴀ
👀 **ᴠɪᴇᴡs :** `{views}`
⏰ **ʏᴀʏıɴʟᴀʏᴀɴ :** {published}
🔗 **ʟɪɴᴋ :** [ᴡᴀᴛᴄʜ ᴏɴ ʏᴏᴜᴛᴜʙᴇ]({link})
🎥 **ᴋᴀɴᴀʟ :** [{channel}]({channellink})

💖 ᴀʀᴀᴍᴀʏᴀ ɢᴜ̈ᴄ̧ ᴋᴀᴛᴀɴ {BOT_NAME}"""
                key = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="ʏᴏᴜᴛᴜʙᴇ", url=link),
                            InlineKeyboardButton(
                                text="ᴅᴇsᴛᴇᴋ", url=config.SUPPORT_CHAT
                            ),
                        ],
                    ]
                )
                await m.delete()
                return await app.send_photo(
                    message.chat.id,
                    photo=thumbnail,
                    caption=searched_text,
                    parse_mode=ParseMode.MARKDOWN,
                    reply_markup=key,
                )
        else:
            await add_served_user(message.from_user.id)
            await message.reply_photo(
                photo=config.START_IMG,
                caption=PM_START_TEXT.format(
                    message.from_user.first_name,
                    BOT_MENTION,
                ),
                reply_markup=InlineKeyboardMarkup(pm_buttons),
            )
    else:
        await add_served_chat(message.chat.id)
        await message.reply_photo(
            photo=config.START_IMG,
            caption=START_TEXT.format(
                message.from_user.first_name,
                BOT_MENTION,
                message.chat.title,
                config.SUPPORT_CHAT,
            ),
            reply_markup=InlineKeyboardMarkup(gp_buttons),
        )
