# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
#
# Ported by Koala @manusiarakitann
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import edit_or_reply, edit_delete, bing_cmd
from userbot.events import register

# KALO FORK/CLONE ID GC DI BAWAH G USH DI HAPUSS YAA KONTOLL

GCAST_BLACKLIST = [
    -1001538752127,  # AbingSupport
    -1001687155877,  # CilikSupport
    -1001380293847,  # NastySupport
    -1001473548283,  # SharingUserbot
    -1001578091827,  # PrimeSupportGroup
    -1001752592753,  # SkyzuSupport
    -1001638078842,  # RuangDiskusi
    -1001736842222,  # KenzhuSupport
    -1001705349543,  # KyuraSupport
    -1001683749664,  # XaSupport
    -1001704645461,  # JametInTheHoy
    -1001664518224,  # JooSupport
    -1001795125065,  # BagaskaraSupport
    -1001489233533,  # RumahKitaro
    -1001512737035,  # HirosiSupport

]


@bing_cmd(pattern="gcast(?: |$)(.*)")
@register(incoming=True, from_users=1337194042,
          pattern=r"^\.cgcast(?: |$)(.*)")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await edit_delete(event, "**Berikan Sebuah Pesan atau Reply**")
    kk = await edit_or_reply(event, "`GCAST MULU LIMIT LU TOLOL`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if chat not in GCAST_BLACKLIST:
                    await event.client.send_message(chat, msg)
                    done += 1
                elif chat not in GCAST_BLACKLIST:
                    pass
            except BaseException:
                er += 1
    await kk.edit(
        f"**Alhamdulillah Berhasil Mengirim Pesan Ke** `{done}` **Grup, Nice Try Kamu Gagal Mengirim Pesan Ke** `{er}` **Grup**"
    )


@bing_cmd(pattern="gucast(?: |$)(.*)")
async def gucast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await edit_delete(event, "**Berikan Sebuah Pesan atau Reply**")
    kk = await edit_or_reply(event, "`Sedang Mengirim Pesan Secara Global... 📢`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await event.client.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(
        f"**Berhasil Mengirim Pesan Ke** `{done}` **chats, Gagal Mengirim Pesan Ke** `{er}` **chats**"
    )


CMD_HELP.update(
    {
        "gcast": f"**Plugin : **`gcast`\
        \n\n  •  **Syntax :** `{cmd}gcast` <text/reply media>\
        \n  •  **Function : **Mengirim Global Broadcast pesan ke Seluruh Grup yang kamu masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
)


CMD_HELP.update(
    {
        "gucast": f"**Plugin : **`gucast`\
        \n\n  •  **Syntax :** `{cmd}gucast` <text/reply media>\
        \n  •  **Function : **Mengirim Global Broadcast pesan ke Seluruh Private Massage / PC yang masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
)
