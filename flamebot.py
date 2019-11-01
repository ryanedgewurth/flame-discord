# Imports
import discord
from discord.ext import commands
import time
# Bot Setup
TOKEN = 'NjE3ODQ2MTkyMDYzMzgxNTQ2.XWxESw.VBm5-xbJwwWd3haj6hhmxb9aG9I'
client = discord.Client()
bot = commands.Bot(command_prefix='&')

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
    # Join VC Command
#    if message.content.startswith('&join'):
#        msg = ':musical_note: Joined the Voice Channel you are currently in!'
#        await client.send_message(message.channel, msg)
#        await client.join_voice_channel(message.author.voice.voice_channel)
#    # Leave VC Command
#    if message.content.startswith('&leave'):
#        msg = ':door: Disconnected from the Voice Channel'
#        voice = get(client.voice_clients, guild=context.guild)
#        
#        if voice and voice.is_connected():
#            await voice.disconnect()
#            await client.send_message(message.channel, msg)     

@bot.command(name='timer')
async def _timer(context, arg):
    await client.send_message(message.channel, arg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.run(TOKEN)
