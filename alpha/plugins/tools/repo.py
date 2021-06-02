# alfareza

from alpha import alpha, Message, Config, versions, get_version


@alpha.on_cmd("repo", about={'header': "get repo link and details"})
async def see_repo(message: Message):
    """see repo"""
    output = f"""
__Repo Userbot__ 😈 **Alpha** 😈
    __Tahan lama sebagai seorang Serge__
    __The Userbot Plugins__
• **Version** : `{get_version()}`
• **License** : {versions.__license__}
• **Copyright** : {versions.__copyright__}
• **Repo** : [Alpha]({Config.UPSTREAM_REPO})
"""
    await message.edit(output)
