# Imports
import discord
from discord.ext import commands
import random
# Bot Setup
TOKEN = 'NjE3ODQ2MTkyMDYzMzgxNTQ2.XWxESw.VBm5-xbJwwWd3haj6hhmxb9aG9I'
client = discord.Client()
# bot = commands.Bot(command_prefix='!')

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
        pmsg = 'List of **Flame** commands\n__***:question: Bot Information :question:***__\n``&ping`` - Responds with Latency (ALPHA! ONLY RESPONDS WITH PONG!)\n``&about`` - Sends you how to contact the developer, the bot name and an support server invite.\n``&help`` - Show this Command List'
        await client.send_message(message.channel, msg)
        await client.send_message(message.author, pmsg)
    # Ping Command
    if message.content.startswith('&ping'):
        msg = 'Pong!'
        await client.send_message(message.channel, msg)
    # Clear Command
    if message.content.startswith('&clear'):
        clearcount = message.content.split(" ")
        msg = 'Cleared {clearcount} messages.'
        await client.send_message(message.channel, msg)
        await message.channel.purge(limit=clearcount + 1)
@client.event
async def on_ready():
    print('Session has Begun')
client.run(TOKEN)
