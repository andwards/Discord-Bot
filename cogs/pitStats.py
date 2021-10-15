import discord
from discord.ext import commands
import requests
import string


class pitStats(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(pass_conext=True)
    async def pit(self, ctx, username: str = None):
        embed_footer = "© Andrew Edwards | All Rights Reserved"
        separation = "{:,}".format
        if username is None:
            requested_info = ctx.author.nick
            if username == None:
                requested_info = str(ctx.author)
                split_name = requested_info.split("#", 1)
                username = split_name[0]
            
        username_icon = "https://minotar.net/avatar/" + str(username)

        global API_KEY
        API_KEY = ""

        try:
            mojang_data = requests.get("https://api.mojang.com/users/profiles/minecraft/" + username).json()
            uuid = mojang_data["id"]
            hypixel_data = requests.get("https://api.hypixel.net/player?key=" + API_KEY + "&uuid=" + uuid).json()
            pit_data = hypixel_data["player"]["stats"]["Pit"]
            display_name = hypixel_data["player"]["displayname"]
        except:
            embed=discord.Embed(title = "Invalid Request", color=0xFF0000)
            embed.add_field(name = "Error", value = "`This player cannot be found on the API`")
            embed.add_field(name = "Correct Useage", value = "`-pit <IGN>`")
            embed.set_footer(text= embed_footer)
            await ctx.channel.send(embed=embed)
            return
        
        try:
            pit_support = pit_data["packages"]
            pit_support = "**Pit Supporter**"
        except:
            pit_support = ""

        try:
            pit_prestige = hypixel_data["player"]["achievements"]["pit_prestiges"]
        except:
            pit_prestige = 0
        
        try:
            pit_kills = hypixel_data["player"]["achievements"]["pit_kills"]
        except:
            pit_kills = 0
        
        try:
            pit_current_renown = pit_data["profile"]["renown"]
        except:
            pit_current_renown = 0
        
        try:
            pit_perk_1 = pit_data["profile"]["selected_perk_0"]
        except:
            pit_perk_1 = "N/A"
        
        try:
            pit_perk_2 = pit_data["profile"]["selected_perk_1"]
        except:
            pit_perk_2 = "N/A"
        
        try:
            pit_perk_3 = pit_data["profile"]["selected_perk_2"]
        except:
            pit_perk_3 = "N/A"
        
        try:
            pit_perk_4 = pit_data["profile"]["selected_perk_3"]
        except:
            pit_perk_4 = "N/A"
        
        
        embed=discord.Embed(title = "Pit Statistics", description = str(pit_support), color=0x0097FF)
        embed.add_field(name = "Prestige", value = "`" + str(separation(pit_prestige)) + "`", inline = True)
        embed.add_field(name = "Kills", value = "`" + str(separation(pit_kills)) + "`", inline = True)
        embed.add_field(name = "Renown", value = "`" + str(separation(pit_current_renown)) + "`", inline = True)
        embed.add_field(name = "Perks", value = "1: `" + str(pit_perk_1) + "`\n" + "2: `" + str(pit_perk_2) + "`\n" + "3: `" + str(pit_perk_3) + "`\n" + 
        "4: `" + str(pit_perk_4) + "`\n", inline = True)

        embed.set_author(name = display_name, icon_url = username_icon)
        embed.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/Pit-64.png")
        embed.set_footer(text= embed_footer)

        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(pitStats(client))
