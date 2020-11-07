from googletrans import Translator
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrobot import (
    COMMAND_HAND_LER
)


trl = Translator()


@Client.on_message(filters.command("tr", COMMAND_HAND_LER))
async def translate(_client, message):
    if message.reply_to_message and (message.reply_to_message.text or message.reply_to_message.caption):
        if len(message.text.split()) == 1:
            await message.delete()
            return
        target = message.text.split()[1]
        if message.reply_to_message.text:
            text = message.reply_to_message.text
        else:
            text = message.reply_to_message.caption
        detectlang = trl.detect(text)
        try:
            tekstr = trl.translate(text, dest=target)
        except ValueError as err:
            await message.reply_text(f"Error: `{str(err)}`")
            return
    else:
        if len(message.text.split()) <= 2:
            await message.delete()
            return
        target = message.text.split(None, 2)[1]
        text = message.text.split(None, 2)[2]
        detectlang = trl.detect(text)
        try:
            tekstr = trl.translate(text, dest=target)
        except ValueError as err:
            await message.reply_text("Error: `{}`".format(str(err)))
            return

    await message.reply_text(f"**Translated from** `{detectlang.lang}` **to** `{target}`:\n```{tekstr.text}```")