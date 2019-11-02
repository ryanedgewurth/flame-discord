# Imports
import discord
from discord.ext import commands
import random
import sys
import string
import time
from time import sleep
# Bot Setup
TOKEN = 'NjE3ODQ2MTkyMDYzMzgxNTQ2.XWxESw.VBm5-xbJwwWd3haj6hhmxb9aG9I'
client = discord.Client()
# bot = commands.Bot(command_prefix='!')

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    
    #------------------------
    #    BOT INFO COMMANDS
    #------------------------
    
    # About Command
    if message.content.startswith('&about'):
        print("[FLAME] About Command Sent")
        msg = 'Hello. My bot name is Flame and I am created by ``Edgewurth#1827``. My support discord is at https://discord.gg/Xb5asjm - join it if you need help.'
        await client.send_message(message.channel, msg)
    # Help Command
    if message.content.startswith('&help'):
        print("[FLAME] Help Command Sent")
        msg = ':incoming_envelope: I have sent an message with the commands to help you.'
        pmsg = 'List of **Flame** commands\n__***:game_die: Fun :game_die:***__\n``&8ball [question]`` - Ask the Magic 8-Ball an Question\n``&rng [minvalue] [maxvalue]`` - Random Number Generator\n__***:question: Bot Information :question:***__\n``&ping`` - Responds with Latency (ALPHA! ONLY RESPONDS WITH PONG!)\n``&about`` - Sends you how to contact the developer, the bot name and an support server invite.\n``&version`` - Get Bot Version\n``&help`` - Show this Command List'
        await client.send_message(message.channel, msg)
        await client.send_message(message.author, pmsg)
    # Ping Command
    if message.content.startswith('&ping'):
        print("[FLAME] Ping Command Sent by ", message.author)
        msg = 'Pong!'
        await client.send_message(message.channel, msg)
    # Version Command
    if message.content.startswith('&version'):
        msg = '__***FLAME***___\nVersion v134 \nRunning Python 3.6.8\nHosted on Heroku'
        await client.send_message(message.channel, msg)
    
    
    #----------------------------
    # DEBUG COMMANDS
    #----------------------------
    
    # Argument Command Test
    if message.content.startswith('&argtest'):
        print("[FLAME] Argtest Command Sent")
        clearcount = message.content.split(" ")
        msg = clearcount
        await client.send_message(message.channel, 'Command Contents:')
        await client.send_message(message.channel, msg)
        msg = clearcount[1]
        await client.send_message(message.channel, 'First Argument (Second Array item)')
        await client.send_message(message.channel, msg)
    
    #------------------
    # TIME COMMANDS
    #------------------
    # Current Time Command
    if message.content.startswith('&clock'):
        print("[FLAME] Clock Command Sent")
        msg = time.asctime()
        await client.send_message(message.channel, msg)
            
    # Countdown Command
    if message.content.startswith('&countdown'):
        print("[FLAME] Countdown Command Sent")
        args = message.content.split(" ")
        times = args[1]
        format = args[2]
        msg = 'Started a Timer of ' + times + format
        await client.send_message(message.channel, msg)
        if format == 'm':
            # Secs = Mins * 60
            times = times * 60
        elif format == 'h':
            # Mins = H * 60
            times = times * 60
            # Secs = Mins * 60
            times = times * 60
        elif format == 'd':
            # Day = H * 24
            times = times * 24
            # Mins = H * 60
            times = times * 60
            # Secs = Mins * 60
            times = times * 60
        elif format == 'mo':
            # Month = D * 28
            times = times * 28
            # Day = H * 24
            times = times * 24
            # Mins = H * 60
            times = times * 60
            # Secs = Mins * 60
            times = times * 60
        times = int(times)
        while times >= 0:
            if times == 7200:
                msg = '2 Hours Left'
                await client.send_message(message.channel, msg)
            elif times == 3600:
                msg = '1 Hour Left'
                await client.send_message(message.channel, msg)
            elif times == 2700:
                msg = '45 Minutes Left'
                await client.send_message(message.channel, msg)
            elif times == 1800:
                msg = '30 Minutes Left'
                await client.send_message(message.channel, msg)
            elif times == 900:
                msg = '15 Minutes Left'
                await client.send_message(message.channel, msg)
            elif times == 600:
                msg = '10 Minutes Left'
                await client.send_message(message.channel, msg)
            elif times == 300:
                msg = '5 Minutes Left'
                await client.send_message(message.channel, msg)
            elif times == 120:
                msg = '2 Minutes Left'
                await client.send_message(message.channel, msg)
            elif times == 60:
                msg = '1 Minute Left'
                await client.send_message(message.channel, msg)
            elif times == 30:
                msg = '30 Seconds Left'
                await client.send_message(message.channel, msg)
            sleep(1)
            time = times - 1
        msg = 'TIME\'S UP {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        
    #------------------
    # ADMIN COMMANDS
    #------------------
    if message.content.startswith('&warn'):
        if message.author.roles("FBMod"):
            args = message.content.split(" ")
            user = args[1]
            reason = args[2]
            if reason == None:
                reason = 'No Reason Specified'
            if user == None:
                msg = 'Please specifiy a User'
                await client.send_message(message.channel, msg)
            else:
                msg = 'Warned ' + user + ' for ' + reason
                pmsg = 'You have been warned in ' + discord.message.guild + '!\n**Reason: ' + reason
                await client.send_message(message.channel, msg)
                await client.send_message(user, pmsg)
    #------------------
    # FUN COMMANDS
    #------------------
    # RND Command
    if message.content.startswith('&rng'):
        print("[FLAME] RNG Command Sent")
        args = message.content.split(" ")
        msg = random.randint(int(args[1]), int(args[2]))
        await client.send_message(message.channel, msg)
    # 8-Ball Command Command
    if message.content.startswith('&8ball'):
        print("[FLAME] 8Ball Command Sent")
        possible_responses = [
        'It is certain.',
        'It is decidedly so.',
        'Without a doubt.',
        'Yes - definitely.',
        'You may rely on it.',
        'As I see it, yes.',
        'Most likely.',
        'Outlook good.',
        'Yes.',
        'Signs point to yes.',
        'Reply Hazy, try again.',
        'Ask again later.',
        'Better not tell you now.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        'Don\'t count on it.',
        'My reply is no.',
        'My sources say no',
        'Outlook not so good.',
        'Very doubtful.',
        'No.',
        ]
        await client.send_message(message.channel, random.choice(possible_responses))
@client.event
async def on_ready():
    print("[FLAME] Bot Signed In and Started!")
client.run(TOKEN)
