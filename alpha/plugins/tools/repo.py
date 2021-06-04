# alfareza

from alpha import Config, Message, alpha, versions


@alpha.on_cmd("repo", about={"header": "Menunjukkan repo dengan detail/n/n"
              "© [TheAlphaSupport](https://t.me/TheAlphaSupport)"}, 
)

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
