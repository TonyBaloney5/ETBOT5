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
        wishs = ["The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **BLUE LIGHT**.", "The train pulls in and is revealed to have **PURPLE LIGHT**. PING A HOST NOW!", "The train pulls in and is revealed to have **PURPLE LIGHT**. PING A HOST NOW!", "The train pulls in and is revealed to have **GOLD LIGHT**. PING A HOST NOW!"]
        random_wish = random.choice(wishs)
        await ctx.send(random_wish)

    @bot.command()
    async def item(ctx): 
        items = ["*You have received a **TURBO BOOST**!*",
"*You have received an **OIL SPILL**!*",
"*You have received a **NITRO BOOST**!*",
"*You have received a **SPIKE TRAP**!*",
"*You have received a **SPONSORSHIP**!*",
"*You have received a **SCANDAL**!*",
"*You have received  **GILDED WHEELS**!*",
"*You have received a **DICE TICKET**!*",
"*You have received an **EVENT TICKET**!*",
"*You have received a **GOLDEN DICE**!*"]
        random_item = random.choice(items)
        await ctx.send(random_item)
        
    @bot.command()
    async def event(ctx):        
        events = ["__***MOVEMENT***__: Move **1 tile** forward.","__***MOVEMENT***__: Move **2 tiles** forward.","__***MOVEMENT***__: Move **3 tiles** forward.","__***MOVEMENT***__: Move **4 tiles** forward.",
"__***MOVEMENT***__: Move **1 tile** backward.",
"__***MOVEMENT***__: Move **2 tiles** backward.",
"__***MOVEMENT***__: Move **3 tiles** backward.",
"__***MOVEMENT***__: Move **4 tiles** backward.",
"__***MOVEMENT***__: Move **1 tile** in any direction.",
"__***MOVEMENT***__: Move **2 tiles** in any direction.",
"__***MOVEMENT***__: Move **3 tiles** in any direction.",
"__***MEDALS***__: Bet anywhere from **1-8 medals** and then pick **heads or tails**. If you pick correctly, you will **double your bet**. If you are wrong, you **lose your bet**.",
"__***MEDALS***__: Gain **6 medals**!",
"__***MEDALS***__: Gain **5 medals**!",
"__***MEDALS***__: Gain **4 medals**!",
"__***MEDALS***__: Gain **3 medals**!",
"__***MEDALS***__: Gain **2 medals**!",
"__***MEDALS***__: Gain **1 medal**!",
"__***MEDALS***__: Lose **4 medals**...",
"__***MEDALS***__: Lose **3 medals**...",
"__***MEDALS***__: Lose **2 medals**...",
"__***MEDALS***__: Lose **1 medal**...",
"__***MEDALS***__: Take **2 medals** from any player on your tribe.",
"__***MEDALS***__: Give **2 medals** to any player on your tribe.",
"__***MOVEMENT***__: Advance to the nearest **PIT STOP**. ",
"__***MOVEMENT***__: Advance to the nearest **PIT STOP**. ",
"__***MOVEMENT***__: Advance to the nearest **BANK**. ",
"__***MOVEMENT***__: Advance to the nearest **BANK**. ",                
"__***ITEM***__: Gain a random item.**. ",                  
"__***MOVEMENT***__: Advance to the nearest **FLAG POST**. ",
"__***MOVEMENT***__: READ CAREFULLY. You have an opportunity to swap to another tribe of your choosing for the price of **5 MEDALS**. If you choose to swap, you will swap at the start of the next immunity challenge. Ping the HOSTS with your decision. ",
"__***MOVEMENT***__: Bonus roll! Use `ET?bonusroll` to roll again.",]
        random_event = random.choice(events)
        await ctx.send(random_event)

    @bot.command()
    @cooldown(1, 86400, BucketType.user)
    async def roll(ctx): 
        rolls = ["*You rolled a **1** and a **1** for a total of __**2**__!*",
"*You rolled a **1** and a **2** for a total of __**3**__!*",
"*You rolled a **1** and a **3** for a total of __**4**__!*",
"*You rolled a **1** and a **4** for a total of __**5**__!*",
"*You rolled a **1** and a **5** for a total of __**6**__!*",
"*You rolled a **1** and a **6** for a total of __**7**__!*",
"*You rolled a **2** and a **1** for a total of __**3**__!*",
"*You rolled a **2** and a **2** for a total of __**4**__!*",
"*You rolled a **2** and a **3** for a total of __**5**__!*",
"*You rolled a **2** and a **4** for a total of __**6**__!*",
"*You rolled a **2** and a **5** for a total of __**7**__!*",
"*You rolled a **2** and a **6** for a total of __**8**__!*",
"*You rolled a **3** and a **1** for a total of __**4**__!*",
"*You rolled a **3** and a **2** for a total of __**5**__!*",
"*You rolled a **3** and a **3** for a total of __**6**__!*",
"*You rolled a **3** and a **4** for a total of __**7**__!*",
"*You rolled a **3** and a **5** for a total of __**8**__!*",
"*You rolled a **3** and a **6** for a total of __**9**__!*",
"*You rolled a **4** and a **1** for a total of __**5**__!*",
"*You rolled a **4** and a **2** for a total of __**6**__!*",
"*You rolled a **4** and a **3** for a total of __**7**__!*",
"*You rolled a **4** and a **4** for a total of __**8**__!*",
"*You rolled a **4** and a **5** for a total of __**9**__!*",
"*You rolled a **4** and a **6** for a total of __**10**__!*",
"*You rolled a **5** and a **1** for a total of __**6**__!*",
"*You rolled a **5** and a **2** for a total of __**7**__!*",
"*You rolled a **5** and a **3** for a total of __**8**__!*",
"*You rolled a **5** and a **4** for a total of __**9**__!*",
"*You rolled a **5** and a **5** for a total of __**10**__!*",
"*You rolled a **5** and a **6** for a total of __**11**__!*",
"*You rolled a **6** and a **1** for a total of __**7**__!*",
"*You rolled a **6** and a **2** for a total of __**8**__!*",
"*You rolled a **6** and a **3** for a total of __**9**__!*",
"*You rolled a **6** and a **4** for a total of __**10**__!*",
"*You rolled a **6** and a **5** for a total of __**11**__!*",
"*You rolled a **6** and a **6** for a total of __**12**__!*"]
        random_roll = random.choice(rolls)
        await ctx.send(random_roll)
        
    @bot.command()
    async def bonusroll(ctx): 
        bonusrolls = ["*You rolled a **1** and a **1** for a total of __**2**__!*",
"*You rolled a **1** and a **2** for a total of __**3**__!*",
"*You rolled a **1** and a **3** for a total of __**4**__!*",
"*You rolled a **1** and a **4** for a total of __**5**__!*",
"*You rolled a **1** and a **5** for a total of __**6**__!*",
"*You rolled a **1** and a **6** for a total of __**7**__!*",
"*You rolled a **2** and a **1** for a total of __**3**__!*",
"*You rolled a **2** and a **2** for a total of __**4**__!*",
"*You rolled a **2** and a **3** for a total of __**5**__!*",
"*You rolled a **2** and a **4** for a total of __**6**__!*",
"*You rolled a **2** and a **5** for a total of __**7**__!*",
"*You rolled a **2** and a **6** for a total of __**8**__!*",
"*You rolled a **3** and a **1** for a total of __**4**__!*",
"*You rolled a **3** and a **2** for a total of __**5**__!*",
"*You rolled a **3** and a **3** for a total of __**6**__!*",
"*You rolled a **3** and a **4** for a total of __**7**__!*",
"*You rolled a **3** and a **5** for a total of __**8**__!*",
"*You rolled a **3** and a **6** for a total of __**9**__!*",
"*You rolled a **4** and a **1** for a total of __**5**__!*",
"*You rolled a **4** and a **2** for a total of __**6**__!*",
"*You rolled a **4** and a **3** for a total of __**7**__!*",
"*You rolled a **4** and a **4** for a total of __**8**__!*",
"*You rolled a **4** and a **5** for a total of __**9**__!*",
"*You rolled a **4** and a **6** for a total of __**10**__!*",
"*You rolled a **5** and a **1** for a total of __**6**__!*",
"*You rolled a **5** and a **2** for a total of __**7**__!*",
"*You rolled a **5** and a **3** for a total of __**8**__!*",
"*You rolled a **5** and a **4** for a total of __**9**__!*",
"*You rolled a **5** and a **5** for a total of __**10**__!*",
"*You rolled a **5** and a **6** for a total of __**11**__!*",
"*You rolled a **6** and a **1** for a total of __**7**__!*",
"*You rolled a **6** and a **2** for a total of __**8**__!*",
"*You rolled a **6** and a **3** for a total of __**9**__!*",
"*You rolled a **6** and a **4** for a total of __**10**__!*",
"*You rolled a **6** and a **5** for a total of __**11**__!*",
"*You rolled a **6** and a **6** for a total of __**12**__!*"]
        random_bonusroll = random.choice(bonusrolls)
        await ctx.send(random_bonusroll)

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

































