from gpytranslate import Translator
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrobot import COMMAND_HAND_LER



gpytrl = Translator()


@Client.on_message(filters.command("trg", COMMAND_HAND_LER))
async def translate(_, message: Message) -> None:
    reply_msg = message.reply_to_message
    if not reply_msg:
        await message.reply_text("Reply to a message to translate it!")
        return
    if reply_msg.caption:
        to_translate = reply_msg.caption
    elif reply_msg.text:
        to_translate = reply_msg.text
    try:
        args = message.text.split()[1].lower()
        if "//" in args:
            source = args.split("//")[0]
            dest = args.split("//")[1]
        else:
            source = await gpytrl.detect(to_translate)
            dest = args
    except IndexError:
        source = await gpytrl.detect(to_translate)
        dest = "en"
    translation = await gpytrl(to_translate,
                              sourcelang=source, targetlang=dest)
    reply = f"**Translated from** `{source}` **to** `{dest}`:\n```{translation.text}```" 

    await message.reply_text(reply, parse_mode="markdown")

