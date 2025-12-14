import discord
from discord.ext.commands  import BucketType
from discord.ext import commands
import logging
import os
import webserver
from flask import ctx
import random
import uvicorn
from fastapi import FastAPI
from discord.ext.commands import cooldown
import threading
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.environ['discordkey']

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='ET?', intents=intents)

app = FastAPI()
@app.get("/ping")
def ping():
    return {"status": "Alive"}
def run_discord_bot():
    @bot.event
    async def on_ready():
        print(f"We have logged in as {bot.user.name}")

    @bot.command()
    async def wish(ctx):
        wishs = ["The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **PURPLE LIGHT**. PING A HOST NOW!", "The train pulls in and is revealed to have **PURPLE LIGHT**. PING A HOST NOW!", "The train pulls in and is revealed to have **GOLD LIGHT**. PING A HOST NOW!", ]
        random_wish = random.choice(wishs)
        await ctx.send(random_wish)

    @bot.command()
    @cooldown(1, 86400, BucketType.user)
    async def text(ctx):
        reply = await ctx.send("test")

    @bot.command()
    async def pull(ctx):
        reply = await ctx.send("https://tenor.com/view/star-rail-pull-animation-honkai-star-rail-star-rail-pull-animation-gacha-animation-gif-16877364308822784938")

    @bot.command()
    async def Aidan(ctx):
        reply = await ctx.send("<@581913987076194305>")

    @bot.command()
    async def Idol(ctx):
        reply = await ctx.send("**YOU ARE GOING TO DIE NOW!**")

    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            msg = 'You are on cooldown, please try again in **{:.2f}**s.'.format(error.retry_after)
            await ctx.send(msg)
    if __name__ == '__main__':
        bot.run(DISCORD_TOKEN)
bot_thread = threading.Thread(target=run_discord_bot)
bot_thread.start()

uvicorn.run(app, host="0.0.0.0", port=10000)




webserver.keep_alive()
bot.run(DISCORD_TOKEN,log_handler=handler, log_level=logging.DEBUG)






















