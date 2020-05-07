import discord
import asyncio
import time
import random
import openpyxl
from json import loads
from discord.utils import get
from discord import Message

client = discord.Client()
token = "NzA3NTA2NTMxMDI0NzY0OTg4.XrJy2A.Z8bPbUl5tHXzDm_H5UKlcRhQW_g"

@client.event
async def on_ready():
    print("=========================")
    print("다음으로 로그인 합니다 : ")
    print(client.user.name)
    print("connection was successful")
    game = discord.Game("도움말:하늘아 안녕")
    print("=========================")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "하늘아 안녕?":
        await message.channel.send("네 안녕하세요")

client.run(token)