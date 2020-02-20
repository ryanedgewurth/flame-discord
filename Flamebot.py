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
import datetime
import Config
# Permit imports from modules directory
import sys
sys.path.append("./modules/")
from eightBall import eightBall
from cmdRNG import cmdRNG
from pingCmd import pingCmd
from countDown import countDown, flameBotTimers
# For debug only
from inspect import getmembers
from pprint import pprint

bot = commands.Bot(command_prefix='^', description=Config.description)

timerRunning = 0

# Log to console that bot is logged in
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)




@tasks.loop(minutes=1)
async def called_once_a_minute(ctx):
    timerRunning = 1
    msg = "Tick Tock"
#    await ctx.send(msg)

#    await message_channel.send("Your message")

@called_once_a_minute.before_loop
async def before():
    await bot.wait_until_ready()
    msg = "Ready"
    print(msg)




try:
    # About command - prints what is stored in description variable
    @bot.command()
    async def about(ctx):
        print (timerRunning)
        pprint(ctx.author) # ctx.author holds user id, name etc.
        #<Member id=642074894762508312 name='musicmaestro360' discriminator='1575' bot=False nick=None guild=<Guild id=668830816952123395 name='RPDevServer' shard_id=None chunked=True member_count=3>>
        if timerRunning == 0:
            called_once_a_minute.start(ctx)
        await ctx.send(Config.description)

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
    
    # Clear Command [No Refactor Needed Here due to rewrite requiring different syntax]
    @bot.command()
    async def clear(ctx, amount=5):
        """Clears a set amount of messages"""
        await ctx.channel.purge(limit=amount)
        await ctx.send("Cleared " + amount + " messages.")
        
    # Infamous 8ball - note renamed to fit with Python's naming rules
    @bot.command()
    async def eightball(ctx):
        """Gives random '8 ball' answer."""
        await ctx.send(eightBall.runCmd())

    @bot.command()
    async def rng(ctx, lowval: int, bigval: int): # Should be renamed to command we want i.e. rng not eightball
        """Gives a random number between input range."""
        await ctx.send(cmdRNG.runCmd(lowval, bigval))
    
    @bot.command()
    async def clock(ctx): # Clock Command
        """Gives the current time."""
        await ctx.send(datetime.datetime.now())
    
    @bot.command()
    async def avatar(ctx, member : discord.Member = ctx.message.author): # Avatar Command
        """Sends an User's Avatar"""
        embedavtar = discord.Embed()
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed)

    @bot.command()
    async def kill(ctx):
        """Shutdown bot."""
        await ctx.send("Shutting Down bot")
        if timerRunning == 1:
            print("Shutting down ticker")
            called_once_a_minute.stop(ctx)
        #timer.stop()
        exit(0)


    @tasks.loop(seconds=3.0, count=2)
    async def slow_count(ctx):
    # This may seem trivial for now but is critical for the countdown timer.......
        if slow_count.current_loop == 1:

            await ctx.send("Reminder Alert Message")

    # The bot command 'Reminder' to trigger reminder message for now
    @bot.command()
    async def reminder(ctx):
        slow_count.start(ctx)
except:
    print("Unknown command")
# Cheap and easy functionality to flag up edited messages - could be used to 'hook' other event
@bot.event
async def on_message_edit(before, after):
    fmt = '**{0.author}** edited their message:\n{0.content} -> {1.content}'
    await before.channel.send(fmt.format(before, after))

try:
    bot.run(Config.token)
    print("[Flame] Bot has connected client to Discord")
except:
    print("[Flame] Could not connect client to Discord - Incorrect token?")
