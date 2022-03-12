""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.lhelp$")
async def usit(e):
    await e.edit(
        f"**Halo {DEFAULTUSER} Jika Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke @sayaabing atau tag admin di @AbingSupport:\n"
        "\n[Telegram](t.me/sayaabing)"
        "\n[Repo](https://github.com/SayaAbing/AbingxUserbot/)"
        "\n[Instagram](instagram.com/aabinggg/)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/Yansaii/Bdrl-userbot/Bdrl-userbot/varshelper.txt)")


CMD_HELP.update({
    "helper":
    "`.lhelp`\
\nUsage: Bantuan Untuk AbingxUserbot.\
\n`.vars`\
\nUsage: Melihat Daftar Vars."
})
