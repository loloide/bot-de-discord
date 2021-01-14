import discord
import asyncio
import math
from discord.ext import commands

client = commands.Bot(command_prefix=".")

poll = []

@client.event
async def on_ready():
    print('Bot is ready.')


@client.command()
async def polls(ctx):
    await ctx.send(f"y or n")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and \
               msg.content.lower() in ["y", "n"]

    msg = await client.wait_for("message", check=check)
    if msg.content.lower() == "y":
        await ctx.send("You said yes!")
        poll.append(1)
    else:
        await ctx.send("You said no!")
        poll.append(-1)

    result = math.fsum(poll)

    await ctx.send(result)

    try:
        msg = await client.wait_for("message", check=check, timeout=5)  # 30 seconds to reply
    except asyncio.TimeoutError:
        await ctx.send("time out")


@client.command()
async def clearpoll(ctx):
    poll.clear()


client.run("Nzc4Mzg0NzM4MDkxOTI1NTc1.X7RNRw.gITDEnrucc9LOY4LITeJFId0Foc")