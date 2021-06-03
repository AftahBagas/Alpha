"""Fun plugin"""

import asyncio
from re import compile as comp_regex

from pyrogram.errors import BadRequest, Forbidden, MediaEmpty
from pyrogram.file_id import PHOTO_TYPES, FileId
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from alpha import Config, Message, alpha, get_version, versions
from alpha.utils import get_file_id, rand_array

_ALIVE_REGEX = comp_regex(
    r"http[s]?://(i\.imgur\.com|telegra\.ph/file|t\.me)/(\w+)(?:\.|/)(gif|jpg|png|jpeg|[0-9]+)(?:/([0-9]+))?"
)
_USER_CACHED_MEDIA, _BOT_CACHED_MEDIA = None, None

LOGGER = alpha.getLogger(__name__)


async def _init() -> None:
    global _USER_CACHED_MEDIA, _BOT_CACHED_MEDIA
    if Config.ALIVE_MEDIA and Config.ALIVE_MEDIA.lower() != "false":
        am_type, am_link = await Bot_Alive.check_media_link(Config.ALIVE_MEDIA.strip())
        if am_type and am_type == "tg_media":
            try:
                if Config.HU_STRING_SESSION:
                    _USER_CACHED_MEDIA = get_file_id(
                        await alpha.get_messages(am_link[0], am_link[1])
                    )
            except Exception as u_rr:
                LOGGER.debug(u_rr)
            try:
                if alpha.has_bot:
                    _BOT_CACHED_MEDIA = get_file_id(
                        await alpha.bot.get_messages(am_link[0], am_link[1])
                    )
            except Exception as b_rr:
                LOGGER.debug(b_rr)


@alpha.on_cmd("alive", about={"header": "Just For Fun"}, allow_channels=False)
async def alive_inline(message: Message):
    try:
        if message.client.is_bot:
            await send_alive_message(message)
        elif alpha.has_bot:
            try:
                await send_inline_alive(message)
            except BadRequest:
                await send_alive_message(message)
        else:
            await send_alive_message(message)
    except Exception as e_all:
        await message.err(str(e_all), del_in=10, log=__name__)


async def send_inline_alive(message: Message) -> None:
    _bot = await alpha.bot.get_me()
    try:
        i_res = await alpha.get_inline_bot_results(_bot.username, "alive")
        i_res_id = (
            (
                await petercord.send_inline_bot_result(
                    chat_id=message.chat.id,
                    query_id=i_res.query_id,
                    result_id=i_res.results[0].id,
                )
            )
            .updates[0]
            .id
        )
    except (Forbidden, BadRequest) as ex:
        await message.err(str(ex), del_in=5)
        return
    await message.delete()
    await asyncio.sleep(200)
    await alpha.delete_messages(message.chat.id, i_res_id)


async def send_alive_message(message: Message) -> None:
    global _USER_CACHED_MEDIA, _BOT_CACHED_MEDIA
    chat_id = message.chat.id
    client = message.client
    caption = Bot_Alive.alive_info()
    if not Config.ALIVE_MEDIA:
        await client.send_photo(
            chat_id,
            photo=Bot_Alive.alive_default_imgs(),
            caption=caption,
            reply_markup=reply_markup,
        )
        return
    url_ = Config.ALIVE_MEDIA.strip()
    if url_.lower() == "false":
        await client.send_message(
            chat_id,
            caption=caption,
            reply_markup=reply_markup,
            disable_web_page_preview=True,
        )
    else:
        type_, media_ = await Bot_Alive.check_media_link(Config.ALIVE_MEDIA)
        if type_ == "url_gif":
            await client.send_animation(
                chat_id,
                animation=url_,
                caption=caption,
                reply_markup=reply_markup,
            )
        elif type_ == "url_image":
            await client.send_photo(
                chat_id,
                photo=url_,
                caption=caption,
                reply_markup=reply_markup,
            )
        elif type_ == "tg_media":
            try:
                await client.send_cached_media(
                    chat_id,
                    file_id=file_id,
                    caption=caption,
                    reply_markup=reply_markup,
                )
            except MediaEmpty:
                if not message.client.is_bot:
                    try:
                        refeshed_f_id = get_file_id(
                            await alpha.get_messages(media_[0], media_[1])
                        )
                        await alpha.send_cached_media(
                            chat_id,
                            file_id=refeshed_f_id,
                            caption=caption,
                        )
                    except Exception as u_err:
                        LOGGER.error(u_err)
                    else:
                        _USER_CACHED_MEDIA = refeshed_f_id


class Bot_Alive:
    @staticmethod
    async def check_media_link(media_link: str):
        match = _ALIVE_REGEX.search(media_link.strip())
        if not match:
            return None, None
        if match.group(1) == "i.imgur.com":
            link = match.group(0)
            link_type = "url_gif" if match.group(3) == "gif" else "url_image"
        elif match.group(1) == "telegra.ph/file":
            link = match.group(0)
            link_type = "url_image"
        else:
            link_type = "tg_media"
            if match.group(2) == "c":
                chat_id = int("-100" + str(match.group(3)))
                message_id = match.group(4)
            else:
                chat_id = match.group(2)
                message_id = match.group(3)
            link = [chat_id, int(message_id)]
        return link_type, link

    @staticmethod
    def alive_info() -> str:
        alive_info_ = f"""**Alpha Z Plugins Is Running 🔥!..**\n
**╭━─━─━─━─≪✠≫─━─━─━─━╮**\n
**❍ ⏱️ • uptime** : `{alphaz.uptime}`
**❍ 🧪 • version** : `{get_version()}`
**❍ 😈 • mode** : `{_get_mode()}`
**❍ 👥 • Sudo**: `{_parse_arg(Config.SUDO_ENABLED)}`
**❍ ⚙️ • Pm-Guard**: `{_parse_arg(not Config.ALLOW_ALL_PMS)}`
**❍ 🖐️ • Anti-Spam**: `{_parse_arg(Config.ANTISPAM_SENTRY)}`"""

    if Config.HEROKU_APP:
        output += f"\n❍ **🌐 • Dyno-saver**: `{_parse_arg(Config.RUN_DYNO_SAVER)}`"
    output += f"""
**❍ 🚀 • Unofficial**: `{_parse_arg(Config.LOAD_UNOFFICIAL_PLUGINS)}`
  🐍**__Python__**: `{versions.__python_version__}`
  💻**__Pyrogram__**: `{versions.__pyro_version__}`
\n**╰━─━─━─━─━─━─━─━─━─━╯**"""
    if not message.client.is_bot:
        output += f"""\n
🎖 **{versions.__license__}** | 😈 **{versions.__copyright__}** | 🔮 **[Repo]({Config.UPSTREAM_REPO})**
"""
    else:
        copy_ = "https://github.com/AftahBagas/AlphaZ-Plugins/blob/alpha/LICENSE"
        markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="😈 Github", url="https://github.com/AftahBagas"
                    ),
                    InlineKeyboardButton(text="🧪 Repo", url=Config.UPSTREAM_REPO),
                ],
                [InlineKeyboardButton(text="🎖 GNU GPL v3.0", url=copy_)],
            ]

    @staticmethod
        alive_imgs = [
            "https://t.me/AlphaZPlugins/4",
        ]
        return rand_array(alive_imgs)

    @staticmethod
        return _BOT_CACHED_MEDIA

    @staticmethod
        return bool(FileId.decode(file_id).file_type in PHOTO_TYPES)
