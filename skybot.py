import discord
import asyncio
import os
import time
import random
import openpyxl
from json import loads
from discord.utils import get
from discord import Message

client = discord.Client()
access_token = os.environ["BOT_TOKEN"]
token = "access_token"

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
