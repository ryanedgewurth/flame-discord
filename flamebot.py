import discord
from discord.ext import commands

TOKEN = 'NjE3ODQ2MTkyMDYzMzgxNTQ2.XWxESw.VBm5-xbJwwWd3haj6hhmxb9aG9I'
client = commands.Bot(command_prefix = '&')
client.remove_command('help')
@client.command()  
async def test(ctx, arg1):
    await ctx.send(arg1)

client.run(TOKEN)
