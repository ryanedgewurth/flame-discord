#
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
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.
#----------------------------------------------------------------------------
# Importation of Dependencies
import discord
# Below is the list of commands, and thier descriptions
class cmdList:
    
    def getName(cmd):
        if cmd == "help":
            return "Help"
        elif cmd == "about":
            return "Bot Information"
        elif cmd == "ping":
            return "Bot Ping"
        elif cmd == "add":
            return "Addition Calculator"
        elif cmd == "clear":
            return "Message Purger"
        elif cmd == "8ball":
            return "Magic 8-Ball"
        elif cmd == "rng":
            return "Random Number Generator"
        elif cmd == "clock":
            return "Clock"
        elif cmd == "avatar":
            return "Avatar"
        elif cmd == "reminder":
            return "Reminder Test"
        elif cmd == "kill":
            return "!BOT STAFF ONLY! Shutdown Bot"
        else:
            return "Dummy Title Message"
    
    def getDesc(cmd):
        if cmd == "help":
            return "Shows this Command List"
        elif cmd == "about":
            return "Returns the Bot's Version, Team and Discord Link."
        elif cmd == "ping":
            return "Returns with the response of the API of this bot."
        elif cmd == "add":
            return "Adds two numbers together."
        elif cmd == "clear":
            return "Clears a set amount of messages"
        elif cmd == "8ball":
            return "Gives random '8 ball' answer."
        elif cmd == "rng":
            return "Gives a random number between input range."
        elif cmd == "clock":
            return "Gives the current time."
        elif cmd == "avatar":
            return "Sends an User's Avatar"
        elif cmd == "kill":
            return "Shutdown bot."
        elif cmd == "reminder":
            return "Sends the occassional reminder message"
        else:
            return "Dummy Descriptor Message"
    
    def getSyntax(cmd):
        if cmd == "help":
            return "help [command]"
        elif cmd == "about":
            return "about"
        elif cmd == "ping":
            return "ping"
        elif cmd == "add":
            return "add <left> <right>"
        elif cmd == "clear":
            return "clear <amount>"
        elif cmd == "8ball":
            return "eightball <question>"
        elif cmd == "rng":
            return "rng <low> <high>"
        elif cmd == "clock":
            return "clock"
        elif cmd == "avatar":
            return "avatar <member>"
        else:
            return cmd

class cmdHelp():
    def cmdMenu(cmdprefix):
        embed = discord.Embed(
            title = 'Flame Command List',
            description = 'Command Prefix: ``' + cmdprefix + '``',
            color = discord.Color.red()
        )
        embed.set_footer(text='Support Server: https://discord.gg/zRFpys7 \nWebsite: http://flamebot.rf.gd/ ')
        embed.add_field(name=':alarm_clock: Time :alarm_clock:',value='``clock``, ``reminder``',inline=False)
        embed.add_field(name=':game_die: Fun :game_die:',value='``8ball``',inline=False)
        embed.add_field(name=':1234: Maths :1234:',value='``add``, ``rng``',inline=False)
        embed.add_field(name=':information_source: Information :information_source:',value='``about``, ``help``, ``ping``, ``avatar``',inline=False)
        embed.add_field(name=':hammer: Moderation :hammer:',value='``clear``',inline=False)
        return embed
