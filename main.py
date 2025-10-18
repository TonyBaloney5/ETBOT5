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

from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.environ['discordkey']

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='ET?', intents=intents)

app = fastapi()
@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    # Get the port from the environment variable or use a default for local development
    port = int(os.environ.get("PORT", 8080)) 
    uvicorn.run(app, host="0.0.0.0", port=port)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user.name}")

@bot.command()
async def text(ctx):
    reply = await ctx.send("test")

@bot.command()
@cooldown(1, 5, BucketType.user)
async def forest(ctx):
    forests = ["You have found an **Apple**.", "You have found a piece of **Leather**.", "You have found a **Stick**.", "You have found a **Stick**."]
    random_forest = random.choice(forests)
    await ctx.send(random_forest)

@bot.command()
@cooldown(1, 5, BucketType.user)
async def river(ctx):
    rivers = ["You have found a piece of **Leather**.", "You have found a piece of **Leather**.", "You have found a piece of **Leather**.", "You have found a piece of **string**."]
    random_river = random.choice(rivers)
    await ctx.send(random_river)

@bot.command()
@cooldown(1, 5, BucketType.user)
async def cavern(ctx):
    caverns = ["You have found a **Diamond**!", "You have found a bar of **Iron**.", "You have found a bar of **Iron**."]
    random_cavern = random.choice(caverns)
    await ctx.send(random_cavern)

@bot.command()
@cooldown(1, 5, BucketType.user)
async def mineshaft(ctx):
    mineshafts = ["You have found a bar of **Gold**.", "You have found a bar of **Iron**.", "You have found a bar of **Gold**.",  "You have found a piece of **string**.", "You have found a piece of **string**."]
    random_mineshaft = random.choice(mineshafts)
    await ctx.send(random_mineshaft)


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


webserver.keep_alive()
bot.run(DISCORD_TOKEN,log_handler=handler, log_level=logging.DEBUG)












