# Imports
import discord
from discord.ext import commands
import random
import sys
import string
import time
from time import sleep
import datetime
version = '2xx'
# Bot Setup
TOKEN = 'X'
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
        msg = 'Hello. My bot name is **Flame** and I am created by ``Edgewurth#1827``. Development begun on the 1st September 2019.\nMy support discord is at https://discord.gg/Xb5asjm - join it if you need help.'
        await client.send_message(message.channel, msg)
    
    # Perms Command
    if message.content.startswith('&perms'):
        print("[FLAME] About Command Sent")
        msg = ':incoming_envelope: I have sent an message with the commands to help you.'
        pmsg = 'List of **Flame** permissions\n__``&clear``__\nThis Command Requires Manage Messages for the User and Bot.'
        try:
            args = message.content.split(" ")
            await client.send_message(message.author, pmsg)
            await client.send_message(message.channel, msg)
        except:
            msg = ':warning: ERROR: ``Unable to DM you the permissions list.``'
            await client.send_message(message.channel, msg)
        
    # Help Commands
    if message.content.startswith('&help'):
        print("[FLAME] Help Command Sent")
        try:
            args = message.content.split(" ")
            msg = ':incoming_envelope: I have sent an message with the commands to help you.'
            pmsg = 'List of **Flame** commands\n__***:alarm_clock: Time :alarm_clock: ***__\n``&clock`` - Gives you the Current Time\n__***:hammer: Moderation :hammer:***__\n``&clear [value]`` - Clears an specified amount of messages.\n__***:game_die: Fun :game_die:***__\n``&8ball [question]`` - Ask the Magic 8-Ball an Question\n``&rng [minvalue] [maxvalue]`` - Random Number Generator\n__***:question: Bot Information :question:***__\n``&ping`` - Responds with Latency\n``&perms`` - Get Permissions for commands which require permissions.\n``&about`` - Sends you how to contact the developer, the bot name and an support server invite.\n``&version`` - Get Bot Version\n``&help`` - Show this Command List'
            await client.send_message(message.author, pmsg)
            await client.send_message(message.channel, msg)
        except:
            msg = ':warning: ERROR: ``Unable to DM you the command list.``'
            await client.send_message(message.channel, msg)
            
            
    # Credits Commands
    if message.content.startswith('&credits'):
        print("[FLAME] Credits Command Sent")
        try:
            args = message.content.split(" ")
            msg = ':incoming_envelope: I have sent an message with the commands to help you.'
            pmsg = 'This is the list of people who have helped with the development of **Flame** in history or to the present.\n__Lead Developer__\nEdgewurth\n__Developers__\niycchan\nnicochulo2001\nRedDog2904\n__Tools Used__\nPython Language\nDiscord.PY\nHeroku\n__Special Thanks__\nCekko for setting up the discord support server\nAnd You for the Usage of this Bot!'
            await client.send_message(message.author, pmsg)
            await client.send_message(message.channel, msg)
        except:
            msg = ':warning: ERROR: ``Unable to DM you the credits list.``'
            await client.send_message(message.channel, msg)
                
        
    # Ping Command
    if message.content.startswith('&ping'):
        timestampbef = datetime.datetime.now().timestamp()
        print("[FLAME] Ping Command Sent by ", message.author)
        msg = 'Pinging... Please Wait...'
        await client.send_message(message.channel, msg)
        timestampaft = datetime.datetime.now().timestamp()
        latency = timestampaft - timestampbef
        msg = 'Pong! The latency is ' + str(round(latency, 3)) + 'ms'
        await client.send_message(message.channel, msg)
    # Version Command
    if message.content.startswith('&version'):
        msg = '__***FLAME***___\nVersion Siries: ' + version + '\nRunning Python: 3.6.8 with Discord.py as framework\nHosted on Heroku'
        await client.send_message(message.channel, msg)
    
    
    #------------------
    # TIME COMMANDS
    #------------------
    # Current Time Command
    if message.content.startswith('&clock'):
        print("[FLAME] Clock Command Sent")
        msg = datetime.datetime.now()
        await client.send_message(message.channel, msg)
            
    # Countdown Command
    if message.content.startswith('&countdown'):
        print("[FLAME] Countdown Command")
        args = message.content.split(" ")
        times = args[1]
        format = args[2]
        msg = 'Started a Timer of ' + times + format
        await client.send_message(message.channel, msg)
        client.loop.create_task(countdown_command(times, format))
        
    #------------------
    # ADMIN COMMANDS
    #------------------ 
    # Warn
    if message.content.startswith('&warn'):
        if message.author.server_permissions.kick_members:
            args = message.content.split(" ")
            username = args[1]
            reason = args[2]
            msg = 'Warned ' + str(discord.User.name) + ' for ' + str(reason)
            pmsg = 'You have been warned!\n**Reason: ' + reason
            await client.send_message(message.channel, msg)
            await client.send_message(discord.User(username).dm_channel, pmsg)
        else:
            msg = ':warning: ERROR: ``You do not have the permission "Kick Members"``'
            await client.send_message(message.channel, msg)
    # Clear
    if message.content.startswith('&clear'):
        print("[FLAME] Clear Command")
        if message.author.server_permissions.manage_messages:
            msgs = []
            args = message.content.split(" ")
            amount = args[1]
            async for message in client.logs_from(message.channel, limit=int(amount) + 1):
                msgs.append(message)
            await client.delete_messages(msgs)
            await client.send_message(message.channel, 'Deleted ' + amount + ' messages')
        else:
            msg = ':warning: ERROR: ``You do not have the permission "Manage Messages"``'
            await client.send_message(message.channel, msg)
    #EMERGENCY        
    if message.content.startswith('&clearx'):
        if message.author.server_permissions.manage_messages:
            try:
                msgs = []
                args = message.content.split(" ")
                amount = args[1]
                async for message in client.logs_from(message.channel, limit=int(amount) + 1):
                    msgs.append(message)
                    await client.delete_messages(msgs)
                await client.send_message(message.channel, 'Deleted ' + amount + ' messages')
            except IndexError:            
                msg = ':warning: ERROR: ``Value \'amount\' needs to be filled!``'
                await client.send_message(message.channel, msg)
            except:
                msg = ':warning: ERROR: ``Unknown Error``'
                await client.send_message(message.channel, msg) 
        else:
            msg = ':warning: ERROR: ``You do not have the permission "Manage Messages"``'
            await client.send_message(message.channel, msg)
    # Kick
    if message.content.startswith('&kick'):
        if message.author.server_permissions.kick_members:
            args   = message.content.split(" ")
            userId = args[1]
            username = client.get_user_info(userId)
            await client.kick(username)
            msg = 'Kicked ' + args[1]
            await client.send_message(userId, msg)
        else:
            msg = ':warning: ERROR: ``You do not have the permission "Kick Members"``'
            await client.send_message(message.channel, msg)
    #------------------
    # UTILITIES
    #------------------
    # CALC Command
    if message.content.startswith('&calc'):
        args   = message.content.split(" ")
        no1    = int(args[1])
        action = args[2]
        no2    = int(args[3])
        if action == '*':
            awns = no1 * no2
        elif action == '/':
            awns = no1 / no2
        elif action == '+':
            awns = no1 + no2
        elif action == '-':
            awns = no1 - no2
        else:
            msg = ':warning: ERROR: ``Value \'action\' needs to have an valid id from (* / + -)!``'
            await client.send_message(message.channel, msg)
	if message.content.startswith('&ticket'):
        args   = message.content.split(" ")
        action = args[1]
		if action == 'new':
			 await client.create_text_channel('ticket' & message.author.name, *, overwrites=None)
        else:
            msg = ':warning: ERROR: ``Value \'action\' needs to have an valid id from (new, close)!``'
            await client.send_message(message.channel, msg)
        
    
    #------------------
    # FUN COMMANDS
    #------------------
    # RNG Command
    if message.content.startswith('&rng' or '&randomnogenerator' or '&randomnumber' or '&randomnumbergenerator'):
        print("[FLAME] RNG Command Sent")
        args = message.content.split(" ")
        try:
            msg = random.randint(int(args[1]), int(args[2]))
            await client.send_message(message.channel, msg)
        except IndexError:
            msg = ':warning: ERROR: ``Values \'minval\' and \'maxval\' needs to be filled!``'
            await client.send_message(message.channel, msg)
        except:
            msg = ':warning: ERROR: ``Unknown Error``'
            await client.send_message(message.channel, msg)
    # 8-Ball Command Command x
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

    #---------------------
    # HIDDEN DEBUG CMDS
    #---------------------
    # NOTE: Only Ryan can access these
    if message.content.startswith('&debug_token'):
        if message.author.id == "354512960250576896":
            await client.send_message(message.channel, TOKEN)
    if message.content.startswith('&debug_announce'):
        if message.author.id == "354512960250576896":
            args = message.content.split(" ")
            msg  = '@everyone ' + args[1] 
            await client.send_message(discord.Object(id='609681917331243048'), msg)
    if message.content.startswith('&debug_update_changelog'):
        if message.author.id == "354512960250576896":
            args = message.content.split(" ")
            msg  = args[1] 
            await client.send_message(discord.Object(id='609681917331243048'), msg)
    if message.content.startswith('&debug_getuserid'):
        args   = message.content.split(" ")
        userId = args[1]
        username = client.get_user_info(userId)
        msg = 'An name is ' + str(username)
        await client.send_message(message.channel, msg)
@client.event
async def countdown_command(times, format):
    await client.wait_until_ready()
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
        times = times - 1
    msg = '{0.author.mention}\'s Alarm is Rinning!'.format(message)
    await client.send_message(message.channel, msg)
@client.event
async def on_ready():

    client.change_presence(game=discord.Game(name="&help"))
    print("[FLAME] Bot Signed In and Started!")
client.run(TOKEN)
