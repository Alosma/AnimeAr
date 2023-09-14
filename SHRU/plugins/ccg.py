import asyncio
import os
import contextlib
import random
import sys
from asyncio.exceptions import CancelledError
from telethon.tl.functions.users import GetFullUserRequest
import requests
import heroku3
import urllib3
from telethon import events 
from SHRU import HEROKU_APP, UPSTREAM_REPO_URL, Qrh9
from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..sql_helper.global_collection import (
    add_to_collectionlist,
    del_keyword_collectionlist,
    get_collectionlist_items,
)
from ..sql_helper.globals import delgvar
plugin_category = "utils"

allowed_users = [6320583148]
@Qrh9.on(events.NewMessage)
async def handle_messages(event):
    user_id = event.sender_id
    if user_id in allowed_users:
        message_text = event.message.text.strip()
        if message_text == 'منصبين؟':
            if user_id in allowed_users:
                await event.respond(" ;)")
@Qrh9.on(events.NewMessage)
async def handle_messages(event):
    user_id = event.sender_id
    if user_id in allowed_users:
        message_text = event.message.text.strip()
        if message_text == 'منو فخر العرب؟':
            if user_id in allowed_users:
                await event.respond("الامام علي عليه السلام🤍")
@Qrh9.on(events.NewMessage)
async def handle_messages(event):
    user_id = event.sender_id
    if user_id in allowed_users:
        message_text = event.message.text.strip()
        if message_text == 'تحبوني؟':
            if user_id in allowed_users:
                await event.reply("نموت عليك ")
@Qrh9.on(events.NewMessage)
async def handle_messages(event):
    user_id = event.sender_id
    if user_id in allowed_users:
        message_text = event.message.text.strip()
        if message_text == 'شهر الحسين يا ناس':
            if user_id in allowed_users:
                await event.reply("ياا حسين 💔")

@Qrh9.on(events.NewMessage(pattern=r'\.cci', incoming=True))
async def als_his(event):
    if event.reply_to:
        reply_msg = await event.get_reply_message()
        user = await Qrh9(GetFullUserRequest(reply_msg.sender_id))
        full_name = user.user.first_name + ' ' + user.user.last_name if user.user.last_name else user.user.first_name
        usernames = []

        #فكرة السيد حسين مطور الجوكر
        async for username in Qrh9.iter_usernames(user.user_id):
            if not any(time in username.username for time in ["11:11"]):
                usernames.append(username.username)

        
        message = f'**Full Name**: {full_name}\n**Usernames**: {", ".join(usernames)}'

        await event.reply(message, parse_mode=None)
    else:
        await event.reply('يرجى الرد على المستخدم...')
