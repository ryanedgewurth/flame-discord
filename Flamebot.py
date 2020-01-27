#!/usr/bin/env python3
#encoding: UTF-8
#      FLAMEBOT
#      Copyright (C) 2019-2020  Edgewurth/RPCS

#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.

#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#
import discord
from discord.ext import commands, tasks
import random
import asyncio
import Config
# Permit imports from modules directory
import sys
sys.path.append("./modules/")
from eightBall import eightBall
from cmdRNG import cmdRNG

from pingCmd import pingCmd

description = "FlameBot - the new speedy version"

bot = commands.Bot(command_prefix='^', description=description)

# Log to console that bot is logged in
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    ####################################################################################
    # Trigger loop to run in background. May need some form of semaphore to indicate
    # client is running to prevent multiple 'ticks' being flagged
    ####################################################################################
    @tasks.loop(seconds=5, minutes=0, hours=0, count=None, reconnect=True, loop=None)
    async def loop(ctx):
        # Do something    print('------')
        print ("Loop 'tick'")

# About command - prints what is stored in description variable
@bot.command()
async def about(ctx):
    await ctx.send(description)

# Ping
@bot.command()
async def ping(ctx):
    startTime = pingCmd.startPing(ctx)
    await ctx.send("Pinging")
    endTime = pingCmd.endPing(ctx)
    latency = endTime - startTime
    msg = 'Pong! The latency is ' + str(round(latency, 3)) + 'ms'
    await ctx.send(msg)

# Simple addition of two numbers showing type-checking on input
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
    
# Infamous 8ball - note renamed to fit with Python's naming rules    
@bot.command()
async def eightball(ctx):
    await ctx.send(eightBall.runCmd())

@bot.command()
async def rnd(ctx, lowval: int, bigval: int): # Should be renamed to command we want i.e. rnd not eightball
    await ctx.send(cmdRNG.runCmd(lowval, bigval))


    
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

try:
    bot.run(Config.token)
except:
    print("Could not connect client to Discord - Incorrect token?")