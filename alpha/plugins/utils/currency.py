# alfareza

import json

import aiohttp

from alpha import Config, Message, alpha

CHANNEL = alpha.getCLogger(__name__)
LOG = alpha.getLogger(__name__)


@alpha.on_cmd(
    "cr",
    about={
        "header": "gunakan ini untuk mengonversi mata uang & mendapatkan nilai tukar",
        "description": "Ubah mata uang & dapatkan nilai tukar.",
        "examples": "{tr}cr 1 BTC USD",
    },
)
async def cur_conv(message: Message):
    """
    fungsi ini bisa mendapatkan hasil nilai tukar
    """
    if Config.CURRENCY_API is None:
        await message.edit(
            "<code>Oops!!dapatkan API dari</code> "
            "<a href='https://free.currencyconverterapi.com'>HERE</a> "
            "<code>& add it to Heroku config vars</code> (<code>CURRENCY_API</code>)",
            disable_web_page_preview=True,
            parse_mode="html",
            del_in=0,
        )
        return

    filterinput = get_emoji_regexp().sub("", message.input_str)
    curcon = filterinput.upper().split()

    if len(curcon) == 3:
        amount, currency_to, currency_from = curcon
    else:
        await message.edit("`ada yang salah!! lakukan .help cr`")
        return

    if amount.isdigit():
        async with aiohttp.ClientSession() as ses:
            async with ses.get(
                "https://free.currconv.com/api/v7/convert?"
                f"apiKey={Config.CURRENCY_API}&q="
                f"{currency_from}_{currency_to}&compact=ultra"
            ) as res:
                data = json.loads(await res.text())
        try:
            result = data[f"{currency_from}_{currency_to}"]
        except KeyError:
            LOG.info(data)
            await message.err("respon tidak valid dari api !")
            return
        result = float(amount) / float(result)
        result = round(result, 5)
        await message.edit(
            "**HASIL NILAI TUKAR MATA UANG:**\n\n"
            f"`{amount}` **{currency_to}** = `{result}` **{currency_from}**"
        )
        await CHANNEL.log("`cr` perintah berhasil dijalankan")

    else:
        await message.edit(
            r"`Ini sepertinya mata uang asing, yang tidak dapat saya konversi sekarang.. (⊙_⊙;)`",
            del_in=0,
        )
