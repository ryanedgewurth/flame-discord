#!/usr/bin/env python3
#encoding: UTF-8
import discord
from discord.ext import commands, tasks
import random
import asyncio
import botToken
# Permit imports from modules directory
import sys
sys.path.append("./modules/")
from eightBall import eightBall


description = "FlameBot"






class FlameClient(discord.Client):
    def __init__(self, * args, ** kwargs):
        super().__init__(*args, ** kwargs)
    
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author == client.user:
            return
        # This will be further re-factored
        if message.content.startswith("^24ball"):
            msg = eightBall.runCmd() + eightBall.runCmd() + eightBall.runCmd()
            # Note new syntax for message
            await message.channel.send(msg)

   
    
        @tasks.loop(seconds=30.0, count=2)
        async def slow_count():
            # This may seem trivial for now but is critical for the countdown timer.......
            if slow_count.current_loop == 1:
                await message.channel.send("BOO!...........................did I get ya?")

        

   
        if message.content.startswith("^boo"):
            msg="That was scary"
            slow_count.start()
            await message.channel.send(msg)

        

        


        bot = commands.Bot(command_prefix='?', description=description)
        
            

    # Cheap and easy functionality
    async def on_message_edit(self, before, after):
        fmt = '**{0.author}** edited their message:\n{0.content} -> {1.content}'
        await before.channel.send(fmt.format(before, after))
    
client = FlameClient()
client.run(botToken.token)
