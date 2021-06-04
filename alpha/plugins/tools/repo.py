# alfareza

from alpha import Config, Message, alpha, versions


@alpha.on_cmd("repo",about={
        "header": "Repo Alpha Userbot",
        "description": "Kirim Link Repo Dengan Detail\n\n"
        "© [TheAlphaSupport](https://t.me/thealphasupport)"}

async def see_repo(message: Message):
    """see repo"""
    output = f"""
__Repo Userbot__ 😈 **Alpha** 😈
    __Tahan lama sebagai seorang Serge__
    __The Userbot Plugins__
• **Version** : `0.3.2`
• **License** : {versions.__license__}
• **Copyright** : {versions.__copyright__}
• **Repo** : [Alpha]({Config.UPSTREAM_REPO})
"""
    await message.edit(output)
