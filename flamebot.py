# Imports
import discord
from discord.ext import commands
import random
# Bot Setup
TOKEN = 'NjE3ODQ2MTkyMDYzMzgxNTQ2.XWxESw.VBm5-xbJwwWd3haj6hhmxb9aG9I'
client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    # About Command
    if message.content.startswith('&about'):
        msg = 'Hello. My bot name is Flame and I am created by ``Edgewurth#1827``. My support discord is at https://discord.gg/Xb5asjm - join it if you need help.'
        await client.send_message(message.channel, msg)
    # Help Command
    if message.content.startswith('&help'):
        msg = ':incoming_envelope: I have sent an message with the commands to help you.'
        pmsg = 'List of **Flame** commands\n__***:question: Bot Information :question:***__\n``&about`` - Sends you how to contact the developer, the bot name and an support server invite.\n``&help`` - Show this Command List'
        await client.send_message(message.channel, msg)
        await client.send_message(message.author, pmsg)
    # Ping Command
    if message.content.startswith('&ping'):
        msg = 'Pong! The latency is', {round(bot.latency * 1000)},'ms'
        await client.send_message(message.channel, msg)
    
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.run(TOKEN)
