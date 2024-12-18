
import discord
import random
from discord.ext import commands
import os


client = commands.Bot(command_prefix = '-')
BOTTOKEN = '' #Insert Bot Tokene here

players = {}
@client.event
async def on_ready():
    print('Bot is ready')

@client.command(aliases= ['5man'])
async def _5man(ctx, p1: discord.Member, p2: discord.Member, p3: discord.Member, p4: discord.Member, p5: discord.Member):
    roles = ['King',
                 'Knight',
                 'Assassin',
                 'Barbarian',
                 'Barbarian']
    random.shuffle(roles)
    await p1.send(f'Your role is: {roles[0]}')
    await p2.send(f'Your role is: {roles[1]}')
    await p3.send(f'Your role is: {roles[2]}')
    await p4.send(f'Your role is: {roles[3]}')
    await p5.send(f'Your role is: {roles[4]}')

    await ctx.send(f'Roles Assigned. Check PMs')

@_5man.error
async def _5manError(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Could not find 1 or more members.')


@client.command(aliases= ['WhatAmI?', 'whatami?', 'WhatAmI','whatAmI'])
async def whatami(ctx):
    selector = random.randint(0,1)
    if selector == 0:
        await ctx.send( ctx.message.author.mention + " You are King")
    else:
        await ctx.send( ctx.message.author.mention + " You are Pomu and so am I. " + 'https://impomu.com/')

@client.command(aliases=['RoomCode', 'Room', 'roomcode', 'room', 'rc', 'RC'])
async def roomCode(ctx, code):
    channel = client.get_channel(533158745870696448)
    await channel.send('https://nhentai.net/g/' + str(int(code)))

@client.command(aliases = ['Beg', 'beg' ])
async def plead(ctx, p1: discord.Member, game):
    await ctx.send(" hey {} {} is begging you on their knees here pleading please play {} with them tonight they are seriously begging here they are going to pass away please help {} is the only cure please {}".format(p1.mention, ctx.message.author.mention ,game,game,p1.mention))

client.run(BOTTOKEN)
