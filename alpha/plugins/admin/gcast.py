from pyrogram.errors import (
    FloodWait,
)

from alpha import Message, alpha

import asyncio


Gblacklist = [-1001159103924, -1001718757023]



@alpha.on_cmd("gcast", about={
    'header': "gcast chat",
    'alpha': "{tr}gcast text",
    'examples': "{tr}gcast"})
async def gcast(message: Message):
    xx = message.text
    if xx:
        msg = xx
    elif message.reply_to_message:
        msg = await alpha.get_reply_message()
    else:
        return await message.edit("`Berikan Sebuah Pesan atau Reply`")
    alfa = await message.edit("`Globally Broadcasting Msg...`")
    er = 0
    done = 0
    async for x in alpha.iter_dialogs():
                try:
                    await alpha.send_message(chat, msg)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWait as anj:
                    await asyncio.sleep(int(anj.seconds))
                    await alpha.send_message(chat, msg)
                    done += 1
                except BaseException:
                    er += 1
    await alfa.edit(
        f"_Sukses Mengirim Pesan Ke_ `{done}` _Grup, Gagal Mengirim Pesan Ke_ `{er}` _Grup_"
    )
