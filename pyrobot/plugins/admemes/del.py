import asyncio
from pyrogram import Client, filters
from pyrobot import COMMAND_HAND_LER
from pyrobot.helper_functions.cust_p_filters import (
    admin_fliter
)


@Client.on_message(
    filters.command(["del"], COMMAND_HAND_LER) &
    admin_fliter
)
async def delmsg(client, message):
    if message.reply_to_message:
         await message.reply_to_message.delete()
         await message.delete()
