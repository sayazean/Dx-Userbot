import os
from datetime import datetime

from PIL import Image
from telegraph import Telegraph, exceptions, upload_file

from userbot import CMD_HELP, TEMP_DOWNLOAD_DIRECTORY, bot, CMD_HANDLER as cmd
from userbot.utils import edit_or_reply, zean_cmd

telegraph = Telegraph()
r = telegraph.create_account(short_name="telegraph")
auth_url = r["auth_url"]


@zean_cmd(pattern="tg (m|t)$")
async def telegraphs(graph):
    xnxx = await edit_or_reply(graph, "`Sedang Memproses...`")
    if not graph.text[0].isalpha() and graph.text[0] not in (
            "/", "#", "@", "!"):
        if graph.fwd_from:
            return
        if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
            os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
        if graph.reply_to_msg_id:
            start = datetime.now()
            r_message = await graph.get_reply_message()
            input_str = graph.pattern_match.group(1)
            if input_str == "m":
                downloaded_file_name = await bot.download_media(
                    r_message, TEMP_DOWNLOAD_DIRECTORY
                )
                end = datetime.now()
                ms = (end - start).seconds
                await xnxx.edit(
                    "Di Download Ke {} Dalam {} Detik.".format(downloaded_file_name, ms)
                )
                try:
                    if downloaded_file_name.endswith((".webp")):
                        resize_image(downloaded_file_name)
                except AttributeError:
                    return await graph.edit("`Tidak Ada Media Yang Disediakan`")
                try:
                    start = datetime.now()
                    media_urls = upload_file(downloaded_file_name)
                except exceptions.TelegraphException as exc:
                    await xnxx.edit("ERROR: " + str(exc))
                    os.remove(downloaded_file_name)
                else:
                    end = datetime.now()
                    ms_two = (end - start).seconds
                    os.remove(downloaded_file_name)
                    await xnxx.edit(
                        "Berhasil Mengunggah Ke [Telegraph](https://telegra.ph{}).".format(
                            media_urls[0], (ms + ms_two)
                        ),
                        link_preview=True,
                    )
            elif input_str == "t":
                user_object = await bot.get_entity(r_message.from_id)
                title_of_page = user_object.first_name  # + " " + user_object.last_name
                # apparently, all Users do not have last_name field
                page_content = r_message.message
                if r_message.media:
                    if page_content != "":
                        title_of_page = page_content
                    downloaded_file_name = await bot.download_media(
                        r_message, TEMP_DOWNLOAD_DIRECTORY
                    )
                    m_list = None
                    with open(downloaded_file_name, "rb") as fd:
                        m_list = fd.readlines()
                    for m in m_list:
                        page_content += m.decode("UTF-8") + "\n"
                    os.remove(downloaded_file_name)
                page_content = page_content.replace("\n", "<br>")
                response = telegraph.create_page(
                    title_of_page, html_content=page_content
                )
                end = datetime.now()
                ms = (end - start).seconds
                await xnxx.edit(
                    "Berhasil Mengunggah Ke [Telegraph](https://telegra.ph/{}).".format(
                        response["path"], ms
                    ),
                    link_preview=True,
                )
        else:
            await xnxx.edit("`Mohon Balas Ke Pesan, Untuk Mendapatkan Link Telegraph Permanen.`")


def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")


CMD_HELP.update({"telegraph": f">`{cmd}tg` <m|t>"
                 "\nUsage: Mengunggah t(Teks) Atau m(Media) Ke Telegraph."})
