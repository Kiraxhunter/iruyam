# Taken From https://github.com/AASFCYBERKING/SerenaRobot/blob/Aasf/SerenaRobot/modules/alive.py
import asyncio
import os
import requests
import datetime
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, Button, custom, version
from Yuriko.events import register
from Yuriko import telethn as aasf
from Yuriko import StartTime, dispatcher
from telethon.tl.types import ChannelParticipantsAdmins

edit_time = 5
""" =======================YURIKO====================== """
file1 = "https://telegra.ph/file/6d690f3f2679e95a50a83.mp4"
file2 = "https://telegra.ph/file/6d690f3f2679e95a50a83.mp4"
file3 = "https://telegra.ph/file/6d690f3f2679e95a50a83.mp4"
file4 = "https://telegra.ph/file/6d690f3f2679e95a50a83.mp4"
file5 = "https://telegra.ph/file/6d690f3f2679e95a50a83.mp4"
""" =======================YURIKO====================== """

BUTTON = [[Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/CFC_BOT_SUPPORT"), Button.url("ᴜᴘᴅᴀᴛᴇs", "https://t.me/PHOENIX_EMPIRE")]]


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)

@register(pattern=("/alive"))
async def hmm(yes):
    chat = await yes.get_chat()
    await yes.delete()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    pm_caption = "** ♡ I,m Iruyambot **\n\n"
    pm_caption += f"**♡ My Uptime :** `{uptime}`\n\n"
    pm_caption += f"**♡ Telethon Version :** `{version.__version__}`\n\n"
    pm_caption += "**♡ My Team :** [CFC BOTS](https://t.me/CFC_BOT_SUPPORT)\n"
    BUTTON = [[Button.url("Support", "https://t.me/CFC_BOT_SUPPORT"), Button.url("Updates", "https://t.me/PHOENIX_EMPIRE")]]
    on = await aasf.send_file(yes.chat_id, file=file1,caption=pm_caption, buttons=BUTTON)
    

    await asyncio.sleep(edit_time)
    ok = await aasf.edit_message(yes.chat_id, on, file=file2, buttons=BUTTON) 

    await asyncio.sleep(edit_time)
    ok2 = await aasf.edit_message(yes.chat_id, ok, file=file3, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok3 = await aasf.edit_message(yes.chat_id, ok2, file=file4, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok4 = await aasf.edit_message(yes.chat_id, ok3, file=file5, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok5 = await aasf.edit_message(yes.chat_id, ok4, file=file1, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok6 = await aasf.edit_message(yes.chat_id, ok5, file=file2, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok7 = await aasf.edit_message(yes.chat_id, ok6, file=file3, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok8 = await aasf.edit_message(yes.chat_id, ok7, file=file4, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok9 = await aasf.edit_message(yes.chat_id, ok8, file=file5, buttons=BUTTON)
