from telethon import Button

from userbot import BOTLOG, BOTLOG_CHATID, LOGS, tgbot


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/a7915ed28a022aa9125a6.jpg",
                caption="⚡ **AbingxUserbot Berhasil Diaktifkan**!!\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - 8.0@AbingxUserbot\n━━━━━━━━━━━━━━━\n➠ **Powered By:** @AbingProject ",
                buttons=[(Button.url("ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/AbingSupport"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
