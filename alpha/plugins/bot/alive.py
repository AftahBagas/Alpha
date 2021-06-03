"""Fun plugin"""

import re
import os
import asyncio
from typing import Tuple, Optional

import wget
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ChatSendMediaForbidden, Forbidden, SlowmodeWait, PeerIdInvalid,
    FileIdInvalid, FileReferenceEmpty, BadRequest, ChannelInvalid, MediaEmpty
)

from alphaz.core.ext import pool
from alphaz.utils import get_file_id_of_media
from alphaz import alphaz, Message, Config, versions, get_version, logging

_LOG = logging.getLogger(__name__)

_IS_TELEGRAPH = False
_IS_STICKER = False

_DEFAULT = "https://t.me/AlphaZPlugins/4"
_CHAT, _MSG_ID = None, None
_LOGO_ID = None


@alphaz.on_cmd("logo", about={
    'header': "This command is just for fun"}, allow_channels=False)
async def alive(message: Message):
    if not (_CHAT and _MSG_ID):
        try:
            _set_data()
        except Exception as set_err:
            _LOG.exception("There was some problem while setting Media Data. "
                           f"trying again... ERROR:: {set_err} ::")
            _set_data(True)

    alive_text, markup = _get_alive_text_and_markup(message)
    if _MSG_ID == "text_format":
        return await message.edit(alive_text, disable_web_page_preview=True, reply_markup=markup)
    await message.delete()
    try:
        await _send_alive(message, alive_text, markup)
    except (FileIdInvalid, FileReferenceEmpty, BadRequest):
        await _refresh_id(message)
        await _send_alive(message, alive_text, markup)


def _get_mode() -> str:
    if alphaz.dual_mode:
        return "Dual"
    if Config.BOT_TOKEN:
        return "Bot"
    return "User"

    def _get_alive_text_and_markup(message: Message) -> Tuple[str, Optional[InlineKeyboardMarkup]]:
    markup = None
    output = f"""**Alpha Z Plugins Is Running 🔥!..**\n
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
