# alfareza

import requests

from alpha import Message, alpha


@alpha.on_cmd(
    "head",
    about={
        "header": "Lihat header di URL",
        "flags": {
            "-r": "izinkan pengalihan",
            "-s": "izinkan aliran",
            "-t": "meminta waktu tunggu",
        },
        "usage": "{tr}head [flags] [url]",
        "examples": "{tr}head -r -s -t5 https://www.google.com",
    },
)
async def req_head(message: Message):
    await message.edit("Processing ...")
    link = message.filtered_input_str
    flags = message.flags
    red = "-r" in flags
    stm = "-s" in flags
    tout = int(flags.get("-t", 3))
    if not link:
        await message.err(text="Tolong beri saya tautan tautan!")
        return
    try:
        cd = requests.head(url=link, stream=stm, allow_redirects=red, timeout=tout)
    except Exception as i_e:
        await message.err(i_e)
        return
    output = f"**URL**: `{link}`\n\n**STATUS CODE**: __{cd.status_code}__\n\n**HEADERS**:\n\n"
    for k, v in cd.headers.items():
        output += f"   🏷 __{k.lower()}__ : `{v}`\n\n"
    await message.edit_or_send_as_file(
        text=output, caption=link, disable_web_page_preview=True
    )
