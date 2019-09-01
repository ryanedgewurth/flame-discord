# Work with Python 3.6
import discord

TOKEN = 'NjE3ODQ2MTkyMDYzMzgxNTQ2.XWxESw.VBm5-xbJwwWd3haj6hhmxb9aG9I'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('&test'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    
    if message.content.startswith('&info'):
        msg = 'Flame Bot is developed by ``Ryan In The Horizon#1827``. Join the Support Discord at https://discord.gg/HUZEd63!'.format(message)
        await client.send_message(message.channel, msg)
        
#Kick Command
@bot.command(pass_context = True)
@commands.has_permissions(administrator=True)
@commands.bot_has_permissions(administrator=True)
async def kick(ctx, user: discord.User):
    await client.kick(user)
    await client.say(("{} was successfully kicked.").format(user))

#Ban Command
@bot.command(pass_context = True)
@commands.has_permissions(ban_members=True)
@commands.bot_has_permissions(ban_members=True)
async def ban(ctx, user: discord.User):
    await client.ban(user)
    await client.say(("{} was successfully banned.").format(user))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)