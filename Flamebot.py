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
from cmdHelp import cmdList, cmdHelp
# For debug only
import logging # Levels are DEBUG, INFO, WARNING, ERROR, and CRITICAL
logging.basicConfig(filename='app.log', level=logging.INFO)
if Config.environment == "Dev":
    logging.basicConfig(filename='app.log', level=logging.DEBUG)

bot = commands.Bot(command_prefix=Config.prefix, description=Config.description)

timerRunning = 0

# Log to console that bot is logged in
@bot.event
async def on_ready():
    logging.info('Logged in as')
    logging.info(bot.user.name)
    logging.info(bot.user.id)

# This function acts as the 'tick' for countdown module and will need to poll
# countDown.flamebotTimers.poll() to alert any actions
@tasks.loop(minutes=1)
async def called_once_a_minute(ctx):
    timerRunning = 1


@called_once_a_minute.before_loop
async def before():
    await bot.wait_until_ready()
    logging.debug('Bot in ready state')


try:
    # About command - prints what is stored in description variable
    @bot.command()
    async def about(ctx):
        print (timerRunning)
        #@Todo: Following code is 'dev' code and needs tidying
        logging.debug(ctx.author) # ctx.author holds user id, name etc.
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
    # @Todo: Refactor into module
    # Clear Command [No Refactor Needed Here due to rewrite requiring different syntax]
    @bot.command()
    async def clear(ctx, amount=5):
        """Clears a set amount of messages"""
        await ctx.channel.purge(limit=amount)
        await ctx.send("Cleared " + amount + " messages.")

    @bot.command()
    async def stringsend(ctx, form, cmd):
        """!DEBUG! Sends Descriptor String"""
        if form == "name":
            await ctx.send(cmdList.getName(cmd))
        elif form == "desc":
            await ctx.send(cmdList.getDesc(cmd))
        elif form == "syntax":
            await ctx.send(cmdList.getSyntax(cmd))

    # Infamous 8ball - note renamed to fit with Python's naming rules
    @bot.command()
    async def eightball(ctx):
        """Gives random '8 ball' answer."""
        await ctx.send(eightBall.runCmd())

    @bot.command()
    async def rng(ctx, lowval: int, bigval: int): # Should be renamed to command we want i.e. rng not eightball
        """Gives a random number between input range."""
        await ctx.send(cmdRNG.runCmd(lowval, bigval))

    # @Todo: Refactor into module?
    @bot.command()
    async def clock(ctx): # Clock Command
        """Gives the current time."""
        await ctx.send(datetime.datetime.now())

    bot.remove_command("help")
    @bot.command()
    async def help(ctx, *, cmd=None): # v4.0's Help Command - Todo: MUST REFACTOR -> MODULE
        if cmd == None:
            help_embed = discord.Embed(
                                       title='Flame Command List',
                                       description='Command Prefix: ``' + Config.prefix + '``',
                                       color=discord.Color.red()
                                       )
            footertext = 'Support Server: ' + Config.supportURL + '\nWebsite: ' + Config.Website
            help_embed.set_footer(text=footertext)
            help_embed.add_field(name=':alarm_clock: Time :alarm_clock:', value='``clock``, ``reminder``', inline=False)
            help_embed.add_field(name=':game_die: Fun :game_die:', value='``8ball``', inline=False)
            help_embed.add_field(name=':1234: Maths :1234:', value='``add``, ``rng``', inline=False)
            help_embed.add_field(name=':information_source: Information :information_source:', value='``about``, ``help``, ``ping``, ``avatar``', inline=False)
            help_embed.add_field(name=':hammer: Moderation :hammer:', value='``clear``, ``warn``, ``kick``, ``ban``', inline=False)
        else:
            help_embed = discord.Embed(
                                       title=cmdList.getName(cmd),
                                       description=cmdList.getDesc(cmd),
                                       color=discord.Color.red()
                                       )
            footerText = 'Support Server: ' + Config.supportURL + '\nWebsite: ' + Config.Website
            help_embed.set_footer(text=footerText)
            help_embed.add_field(name='Usage', value='``' + cmdList.getSyntax(cmd) + '``', inline=False)

        await ctx.send(embed=help_embed)

    # @Todo: Refactor into module
    @bot.command()
    async def avatar(ctx, member: discord.Member): # Avatar Command
        """Sends an User's Avatar"""
        show_avatar = discord.Embed() # We need to instantiate this object
        show_avatar.set_image(url='{}'.format(member.avatar_url)) # This returns the image url formatted for display.
        await ctx.send(embed=show_avatar)
    

    @bot.command()
    @commands.has_permissions(kick_members=True)
    async def kick(ctx, member: discord.Member, *, reason=None): # Kick Command (Commented till release-ready)
        """Sends an User's Avatar"""
        await ctx.send("Kicked " + member.display_name + " for " + reason)
        await member.send("You have been kicked from " + member.guild.name + " for " + reason)
        await member.kick(reason=reason)
    
    @bot.command()
    @commands.has_permissions(kick_members=True)
    async def warn(ctx, member: discord.Member, *, reason=None): # Warn Command (Commented till release-ready)
        """Sends an User's Avatar"""
        await ctx.send("Warned " + member.display_name + " for " + reason)
        await member.send("You have been warned in " + member.guild.name + " for " + reason)
        
    @bot.command()
    @commands.has_permissions(ban_members=True)
    async def ban(ctx, member: discord.Member, *, reason=None): # ban Command (Commented till release-ready)
        """Sends an User's Avatar"""
        await ctx.send("Banned " + member.display_name + " for " + reason)
        await member.send("You have been banned from " + member.guild.name + " for " + reason)
        await member.ban(reason=reason)
        
    # @Todo: Refactor into module
    @bot.command()
    async def kill(ctx):
        """Shutdown bot."""
        await ctx.send("Shutting Down bot")
        if timerRunning == 1:
            logging.info("Shutting down bot")
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
    logging.info('Unknown Command')

# # Cheap and easy functionality to flag up edited messages - could be used to 'hook' other event
# @bot.event
# async def on_message_edit(before, after):
    # fmt = '**{0.author}** edited their message:\n{0.content} -> {1.content}'
    # await before.channel.send(fmt.format(before, after))

try:
    bot.run(Config.token)
    logging.info('[Flame] Bot has connected as a client to Discord')

except:
    logging.critical('[Flame] Could not connect client to Discord - Incorrect token?')
