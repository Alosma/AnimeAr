import asyncio
import os
import contextlib
import random
import sys
from asyncio.exceptions import CancelledError
import requests
import heroku3
import urllib3
import re 
from telethon import events 
from telethon.tl import types
from SHRU import HEROKU_APP, UPSTREAM_REPO_URL, Qrh9
from telethon.tl.functions.channels import CreateChannelRequest
from telethon.tl.functions.channels import InviteToChannelRequest
from ..Config import Config
import json
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..sql_helper.global_collection import (
    add_to_collectionlist,
    del_keyword_collectionlist,
    get_collectionlist_items,
)
from ..sql_helper.globals import delgvar
from telethon.tl.functions.channels import JoinChannelRequest

#تعبي هذا اذا اخذته انيجمك
import logging

async def check_username_availability(username):
 
    url = f'https://fragment.com/?query={username}'
    response = requests.get(url)
    if response.status_code == 200:

        return True
    else:

        return False

@Qrh9.on(events.NewMessage(pattern=r"^\.ثلاثي (\d+)$"))
async def generate_random_usernames(event):

    count = int(event.pattern_match.group(1))  # Get the number from the command
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    abc1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    generated_usernames = []
    while count > 0:
        v1 = ''.join((random.choice(abc1) for _ in range(1)))
        v2 = ''.join((random.choice(abc) for _ in range(1)))
        v3 = ''.join((random.choice(abc) for _ in range(1)))
        v4 = ''.join((random.choice(abc) for _ in range(1)))
        username = f"{v1}_{v2}_{v3}"
        if not await Username_exists_by_Qrh9(username):
            generated_usernames.append(username)
            count -= 1

    if generated_usernames:
        usernames_text = "\n".join([f"@{username}" for username in generated_usernames])
        await event.edit(f"**᯽︙ تم انشاء {len(generated_usernames)} يوزر جديد**\n\n{usernames_text}")
@Qrh9.on(events.NewMessage(pattern=r"^\.رباعي (\d+)$"))
async def generate_random_usernames(event):

    count = int(event.pattern_match.group(1))  # Get the number from the command
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    abc1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    generated_usernames = []
    while count > 0:
        v1 = ''.join((random.choice(abc1) for _ in range(1)))
        v2 = ''.join((random.choice(abc) for _ in range(1)))
        v3 = ''.join((random.choice(abc) for _ in range(1)))
        v4 = ''.join((random.choice(abc) for _ in range(1)))
        username = f"{v1}{v2}_{v1}{v3}"
        if not await Username_exists_by_Qrh9(username):
            generated_usernames.append(username)
            count -= 1

    if generated_usernames:
        usernames_text = "\n".join([f"@{username}" for username in generated_usernames])
        await event.edit(f"**᯽︙ تم انشاء {len(generated_usernames)} يوزر جديد**\n\n{usernames_text}")
@Qrh9.on(events.NewMessage(pattern=r"^\.يوزربوت (\d+)$"))
async def generate_random_usernames(event):
    count = int(event.pattern_match.group(1))  # اذا تخمط انت فرخ😆
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    abc1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    generated_usernames = []
    while count > 0:
        v1 = ''.join((random.choice(abc1) for _ in range(1)))
        v2 = ''.join((random.choice(abc) for _ in range(1)))
        v3 = ''.join((random.choice(abc) for _ in range(1)))
        username = f"{v1}_{v2}_bot"
        if not await Username_exists_by_Qrh9(username):
            generated_usernames.append(username)
            count -= 1

    if generated_usernames:
        usernames_text = "\n".join([f"@{username}" for username in generated_usernames])
        await event.edit(f"**᯽︙ تم انشاء {len(generated_usernames)} يوزر جديد**\n\n{usernames_text}")
    

@Qrh9.on(events.NewMessage(pattern=r"^\.خماسي (\d+)$"))
async def generate_random_usernames(event):

    count = int(event.pattern_match.group(1))  # Get the number from the command
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    abc1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    generated_usernames = []
    while count > 0:
        v1 = ''.join((random.choice(abc1) for _ in range(1)))
        v2 = ''.join((random.choice(abc) for _ in range(1)))
        v3 = ''.join((random.choice(abc) for _ in range(1)))
        v4 = ''.join((random.choice(abc) for _ in range(1)))
        username = f"{v1}{v1}{v1}{v2}{v1}"
        if not await Username_exists_by_Qrh9(username):
            generated_usernames.append(username)
            count -= 1

    if generated_usernames:
        usernames_text = "\n".join([f"@{username}" for username in generated_usernames])
        await event.edit(f"**᯽︙ تم انشاء {len(generated_usernames)} يوزر جديد**\n\n{usernames_text}")
@Qrh9.on(events.NewMessage(pattern=r"^\.سداسي (\d+)$"))
async def generate_random_usernames(event):

    count = int(event.pattern_match.group(1))  # Get the number from the command
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    abc1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

    generated_usernames = []
    while count > 0:
        v1 = ''.join((random.choice(abc) for _ in range(1)))
        v2 = ''.join((random.choice(abc) for _ in range(1)))
        v3 = ''.join((random.choice(abc1) for _ in range(1)))
        v4 = ''.join((random.choice(abc) for _ in range(1)))
        username = f"{v1}{v1}{v3}{v1}{v1}{v1}"
        if not await Username_exists_by_Qrh9(username):
            generated_usernames.append(username)
            count -= 1

    if generated_usernames:
        usernames_text = "\n".join([f"@{username}" for username in generated_usernames])
        await event.edit(f"**᯽︙ تم انشاء {len(generated_usernames)} يوزر جديد**\n\n{usernames_text}")

@Qrh9.on(events.NewMessage(pattern=r'\.cci', incoming=True))
async def Qrhis9(event):
    user = event.sender
    if isinstance(user, types.UserFull):
        full_name = user.user.first_name + ' ' + user.user.last_name if user.user.last_name else user.user.first_name
    else:
        full_name = user.first_name + ' ' + user.last_name if user.last_name else user.first_name
        usernames = []

        
        probable_user_mention_entity = event.message.entities
        if probable_user_mention_entity and isinstance(probable_user_mention_entity[0], types.MessageEntityMentionName):
            usernames.append(user.username)

        # فكرة السيد حسين مطور الجوكر
        async for username in Qrh9.iter_usernames(user.user_id):
            if not any(time in username.username for time in ["11:11"]):
                usernames.append(username.username)

        if not usernames:
            message = f'**Full Name**: {full_name}\n**Usernames**: No valid usernames found'
        else:
            message = f'**Full Name**: {full_name}\n**Usernames**: {", ".join(usernames)}'

        await event.reply(message, parse_mode=None)