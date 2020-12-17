from gpytranslate import Translator
from pyrobot import COMMAND_HAND_LER
from pyrogram import Client, filters
from pyrobot.gpytrhelper.gpytranslatehelper import edrep


trl = Translator()




@Client.on_message(filters.command("trg", COMMAND_HAND_LER))
async def gtranslate(_, message):
    trl = Translator()
    if message.reply_to_message and (
        message.reply_to_message.text or message.reply_to_message.caption
    ):
        if len(message.text.split()) == 1:
            await message.delete()
            return
        target = message.text.split()[1]
        if message.reply_to_message.text:
            text = message.reply_to_message.text
        else:
            text = message.reply_to_message.caption
        try:
            tekstr = await trl(text, targetlang=target)
        except ValueError as err:
            await edrep(message, text=f"Error: `{str(err)}`", parse_mode="Markdown")
            return
    else:
        if len(message.text.split()) <= 2:
            await message.delete()
            return
        target = message.text.split(None, 2)[1]
        text = message.text.split(None, 2)[2]
        try:
            tekstr = await trl(text, targetlang=target)
        except ValueError as err:
            await edrep(
                message, text="Error: `{}`".format(str(err)), parse_mode="Markdown"
            )
            return

    await edrep(
        message,
        text=f"**Translated from:**```{(await trl.detect(text))}```\n\n**Translated text:**\n\n `{tekstr.text}`",
        parse_mode="Markdown",
    )
