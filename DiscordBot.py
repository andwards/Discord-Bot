import discord
import os
from discord.ext import commands
from os import listdir
from os.path import realpath, split, join, splitext
from pathlib import Path
import time
import sys
import asyncio
import datetime
from discord import embeds
import random

intents = discord.Intents.all()

client = commands.Bot(command_prefix=commands.when_mentioned_or('-'), case_insensitive=True, intents = intents)
client.remove_command("help")

insufficient_permissions = "You don't have permission to do this!"
andrew_tag = "DetectiveAndrew#3645"

global start_time
start_time = time.time()

token = ''

global embeded_footer
embeded_footer = "© Andrew Edwards | All Rights Reserved"

print(">> Beginning startup process...")
print(">> Loading files...\n")

@client.command()
async def uptime(ctx):
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(datetime.timedelta(seconds=difference))
    embed = discord.Embed(color = 0x0097FF)
    embed.add_field(name="Uptime", value=text)

    try:
        await ctx.channel.send(embed=embed)
    except discord.HTTPException:
        await ctx.channel.send("Current uptime: " + text)

@client.command(pass_context=True)
async def say(ctx,*,message):
    requested_info = str(ctx.author)
    split_name = requested_info.split("#", 1)
    
    if requested_info == andrew_tag:
        await ctx.message.delete()
        await ctx.channel.send(message)

    else:
        await ctx.channel.send(insufficient_permissions)

@client.command(pass_context=True, aliases = ["l"])
async def load(ctx, extension):
    requested_info = str(ctx.author)
    split_name = requested_info.split("#", 1)
    fixed_info = split_name[0]

    if requested_info == andrew_tag:
        client.load_extension(f"cogs.{extension}")

        embed=discord.Embed(title = "Dev Modules", color=0x00ff00)
        embed.add_field(name = "Action", value = "`LOAD`", inline = True) 
        embed.add_field(name = "Authorized", value = "`" + fixed_info + "`", inline = True)
        embed.add_field(name = "Module", value = "`" + "".join(extension) + "`", inline = True)
        embed.set_footer(text = embeded_footer)

        await ctx.channel.send(embed=embed)
        print(">> " + fixed_info + " has loaded the " + "".join(extension) + " module.")
    else:
        await ctx.channel.send(insufficient_permissions)

@client.command(pass_context=True, aliases = ["ul"])
async def unload(ctx, extension):
    requested_info = str(ctx.author)
    split_name = requested_info.split("#", 1)
    fixed_info = split_name[0]

    if requested_info == andrew_tag:
        client.unload_extension(f"cogs.{extension}")

        embed=discord.Embed(title = "Dev Modules", color=0xFF0000) 
        embed.add_field(name = "Action", value = "`UNLOAD`", inline = True)
        embed.add_field(name = "Authorized", value = "`" + fixed_info + "`", inline = True)
        embed.add_field(name = "Module", value = "`" + "".join(extension) + "`", inline = True)
        embed.set_footer(text = embeded_footer)

        await ctx.channel.send(embed=embed)
        print(">> " + fixed_info + " has unloaded the " + "".join(extension) + " module.")
    else:
        await ctx.channel.send(insufficient_permissions)

@client.command(pass_context=True, aliases = ["rl"])
async def reload(ctx, extension):
    requested_info = str(ctx.author)
    split_name = requested_info.split("#", 1)
    fixed_info = split_name[0]

    if requested_info == andrew_tag:
        client.reload_extension(f"cogs.{extension}")

        embed=discord.Embed(title = "Dev Modules", color=0xFF7000)
        embed.add_field(name = "Action", value = "`RELOAD`", inline = True)
        embed.add_field(name = "Authorized", value = "`" + fixed_info + "`", inline = True)
        embed.add_field(name = "Module", value = "`" + "".join(extension) + "`", inline = True)
        embed.set_footer(text = embeded_footer)

        await ctx.channel.send(embed=embed)
        print(">> " + fixed_info + " has reloaded the " + "".join(extension) + " module.")
    else:
        await ctx.channel.send(insufficient_permissions)

@client.command()
async def modules(ctx):
    requested_info = str(ctx.author)
    split_name = requested_info.split("#", 1)
    fixed_info = split_name[0]

    filename_list = ""
    filename_count = 0

    if requested_info == andrew_tag:
        for item in listdir(join(split(realpath(__file__))[0], "cogs")):
            filename_list += "\n`" + splitext(item)[0] + "`"
            filename_count += 1

        embed=discord.Embed(title = "Dev Modules", description = filename_list, color=0x00ff00)
        embed.add_field(name = "Count", value = "`" + str(filename_count) + "`", inline = False)
        embed.set_footer(text = embeded_footer)

        print(">> " + fixed_info + " has executed the module list command")
        await ctx.channel.send(embed=embed)
        
for item in listdir(join(split(realpath(__file__))[0], "cogs")):
    try: 
        client.load_extension(f"cogs." + splitext(item)[0])
        print(">> Loaded: " + splitext(item)[0])
    except:
        print(">> Failed: " + splitext(item)[0])

client.run(token)
