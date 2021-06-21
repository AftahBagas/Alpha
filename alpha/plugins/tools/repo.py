# alfareza

from alpha import Config, Message, alpha, versions, get_version


@alpha.on_cmd("repo", about={"header": "get repo link and details"})
async def see_repo(message: Message):
    """see repo"""
    output = f"""
[Alpha](https://t.me/TeamSquadUserbotSupport) repo :
  • **Version** : {get_version()}
  • **License** : {versions.__license__}
  • **Copyright** : {versions.__copyright__}
  • **Repo** : [Alpha]({Config.UPSTREAM_REPO})
"""
    await message.edit(output)
