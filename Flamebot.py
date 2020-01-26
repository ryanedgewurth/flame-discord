#!/usr/bin/env python3
#encoding: UTF-8
import discord
from discord.ext import commands, tasks
import random
import asyncio
import Config
# Permit imports from modules directory
import sys
sys.path.append("./modules/")
from eightBall import eightBall


description = "FlameBot - the new speedy version"

bot = commands.Bot(command_prefix='^', description=description)

# Log to console that bot is logged in
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

# Simple addition of two numbers showing type-checking on input
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
    
# Infamous 8ball - note renamed to fit with Python's naming rules    
@bot.command()
async def eightball(ctx):
    await ctx.send(eightBall.runCmd())

# Loop that can be triggered outside of events but respond to events
# Will expand on this later for the reminder programming
@tasks.loop(seconds=3.0, count=2)
async def slow_count(ctx):
# This may seem trivial for now but is critical for the countdown timer.......
    if slow_count.current_loop == 1:
        
        await ctx.send("Reminder Alert Message")
        
# The bot command 'Reminder' to trigger reminder message for now
@bot.command()
async def reminder(ctx):
    slow_count.start(ctx)

# Cheap and easy functionality to flag up edited messages - could be used to 'hook' other event
@bot.event
async def on_message_edit(before, after):
    fmt = '**{0.author}** edited their message:\n{0.content} -> {1.content}'
    await before.channel.send(fmt.format(before, after))


bot.run(Config.token)
