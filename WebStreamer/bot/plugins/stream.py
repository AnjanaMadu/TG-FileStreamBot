# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters
from WebStreamer.vars import Var
from urllib.parse import quote_plus
from WebStreamer.bot import StreamBot
from pyrogram.types.messages_and_media import message
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

def detect_type(m: Message):
    if m.document:
        return m.document
    elif m.video:
        return m.video
    elif m.audio:
        return m.audio
    else:
        return
    

@StreamBot.on_message(filters.private & (filters.document | filters.video | filters.audio), group=4)
async def media_receive_handler(_, m: Message):
    file = detect_type(m)
    file_name = ''
    if file:
        file_name = file.file_name
    log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
    stream_link = Var.URL + str(log_msg.message_id) + '/' +quote_plus(file_name) if file_name else ''
    text = f"**Download Link Generated!** 🎈\n**File Name:** `{file_name}`\n**Download Link:** `{stream_link}`"
    await m.reply_text(
        text=text,
        quote=True,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Download Now 🔗', url=stream_link)]])
    )
