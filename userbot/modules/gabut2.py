from time import sleep
from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import zean_cmd


@zean_cmd(pattern='Zean(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai Perkenalkan Namaku Zean`")
    sleep(3)
    await typew.edit("`Umur Ku Ga Ada Yang Tau`")
    sleep(1)
    await typew.edit("`Tinggal Di Jakarta, Salam Kenal:)`")
# Create by myself @localheart


@zean_cmd(pattern='sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Aku Sayang Kamu`")
    sleep(1)
    await typew.edit("`I LOVE YOU π`")
# Create by myself @localheart


@zean_cmd(pattern='semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")
# Create by myself @localheart


CMD_HELP.update({
    "oi": f"πΎπ€π’π’ππ£π: `{cmd}Zean`\
    \nβ³ : perkenalan Zean\
    \n\nπΎπ€π’π’ππ£π: `{cmd}sayang`\
    \nβ³ : Gombalan maut`\
    \n\nπΎπ€π’π’ππ£π: `{cmd}semangat`\
    \nβ³ : Jan Lupa Semangat."
})
