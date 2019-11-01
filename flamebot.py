import discord
from discord.ext import commands

TOKEN = 'NjE3ODQ2MTkyMDYzMzgxNTQ2.XWxESw.VBm5-xbJwwWd3haj6hhmxb9aG9I'
client = commands.Bot(command_prefix = '&')
client.remove_command('help')




@client.event
async def on_ready():
    print("general Bot is ready.")
    print('Logged on as {0}!'.format(client.user))



@client.command()
@commands.has_role('Staff')
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount+1)


@client.command()
@commands.has_role('Staff')
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.channel.purge(limit=1)

@client.command()
@commands.has_role('Staff')
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.channel.purge(limit=1)

@client.command()
@commands.has_role('Staff')
async def unban(ctx, *, member):
    banned_users=await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user=ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.channel.purge(limit=1)
            return
        await ctx.channel.purge(limit=1)

@client.command()
@commands.has_role('Staff')
async def mute(ctx, member: discord.Member=None):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not member:
        await ctx.send("Please specify and member")
        return
    await member.add_roles(role)
    await ctx.channel.purge(limit=1)
@client.command()
@commands.has_role('Staff')
async def unmute(ctx, member: discord.Member=None):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not member:
        await ctx.send("Please specify and member")
        return
    await member.remove_roles(role)
    await ctx.channel.purge(limit=1)

@client.command()
@commands.has_role('Staff')
async def messagemanager(ctx):
    await ctx.send('You can manage messages.')

@client.command()
async def echo(ctx, *args):
    output = ""
    for word in args:
        output +=word
        output += ' '
    await ctx.channel.purge(limit=1)
    await ctx.send(output)

@client.command()
@commands.has_role('Staff')
async def count(ctx):
    count = 0
    while True:
        count+=1
        await ctx.send(count)
        
@bot.command()  
async def test(ctx):
    await ctx.send("Test Submitted")

@client.command()
async def help(ctx):
    await ctx.channel.purge(limit=1)
    author = ctx.message.author
    embed = discord.Embed(
        colour = discord.Colour.purple()
        )

    embed.set_author(name="All commands are lowercase")
    embed.add_field(name='Coin', value='Rolls a random change of Heads and Tails', inline=False)
    embed.add_field(name='Echo', value='Echos all works after the command', inline=False)
    await ctx.send(author, embed=embed)
@client.command()
@commands.has_role('Staff')
async def modhelp(ctx):
    await ctx.channel.purge(limit=1)
    author = ctx.message.author
    embed = discord.Embed(
        colour = discord.Colour.purple()
        )

    embed.set_author(name="All commands are lowercase")
    embed.add_field(name='Kick', value='Kicks a member', inline=False)
    embed.add_field(name='Ban', value='Bans a member', inline=False)
    embed.add_field(name='Unban', value='Ubans a member', inline=False)
    embed.add_field(name='Mute', value='Mutes a member', inline=False)
    embed.add_field(name='Unmute', value='Unmutes a member', inline=False)
    embed.add_field(name='Clear', value='Clears a specified amount of messages above', inline=False)
    await ctx.send(author, embed=embed)




client.run(TOKEN)
