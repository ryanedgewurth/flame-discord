#!/usr/bin/env python3
#encoding: UTF-8
import discord
import asyncio


class FlameClient(discord.Client):
    async def on_ready(self):
        print('Connected!')
        print('Username: {0.name}\nID: {0.id}'.format(self.user))

    async def on_message(self, message):
        print(message)

    async def on_message_edit(self, before, after):
        fmt = '**{0.author}** edited their message:\n{0.content} -> {1.content}'
        await before.channel.send(fmt.format(before, after))

client = FlameClient()
client.run('token')