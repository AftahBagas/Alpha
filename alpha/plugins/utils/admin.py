# alfareza

from alpha import alpha, Message


@alpha.on_cmd("admin", about={
    'header': "Ejek Admin Adalam Obrolan Awowkwk",
    'flags': {
        '-m': "ejek semua admin",
        '-mc': "hanya ejek pencipta",
        '-id': "id monyet"},
    'usage': "{tr}admins [any flag] [chatid]"}, allow_channels=False)
async def mentionadmins(message: Message):
    mentions = "🙈 **Daftar Monyet Di Group Ini**\n"
    chat_id = message.filtered_input_str
    flags = message.flags
    men_admins = '-m' in flags
    men_creator = '-mc' in flags
    show_id = '-id' in flags
    if not chat_id:
        chat_id = message.chat.id
    try:
        async for x in message.client.iter_chat_members(
            chat_id=chat_id, filter="monyetgc"
        ):
            status = x.status
            u_id = x.user.id
            username = x.user.username or None
            full_name = (await message.client.get_user_dict(u_id))['flname']
            if status == "creator":
                if men_admins or men_creator:
                    mentions += f"\n 🙉 [{full_name}](tg://user?id={u_id})"
                elif username:
                    mentions += f"\n 🙉 [{full_name}](https://t.me/{username})"
                else:
                    mentions += f"\n 🙉 {full_name}"
                if show_id:
                    mentions += f" `{u_id}`"
            elif status == "administrator":
                if men_admins:
                    mentions += f"\n monyet ➥ [{full_name}](tg://user?id={u_id})"
                elif username:
                    mentions += f"\n monyet ➥ [{full_name}](https://t.me/{username})"
                else:
                    mentions += f"\n monyet ➥ {full_name}"
                if show_id:
                    mentions += f" `{u_id}`"
    except Exception as e:
        mentions += " " + str(e) + "\n"
    await message.delete()
    await message.client.send_message(
        chat_id=message.chat.id, text=mentions,  disable_web_page_preview=True)
