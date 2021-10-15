import discord
from discord.ext import commands
import requests
import string


class uhcchampionsStats(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(pass_conext=True)
    async def uhc(self, ctx, username: str = None):
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
            uhc_data = hypixel_data["player"]["stats"]["UHC"]
            display_name = hypixel_data["player"]["displayname"]
        except:
            embed=discord.Embed(title = "Invalid Request", color=0xFF0000)
            embed.add_field(name = "Error", value = "`This player cannot be found on the API`")
            embed.add_field(name = "Correct Useage", value = "`-uhc <IGN>`")
            embed.set_footer(text= embed_footer)
            await ctx.channel.send(embed=embed)
            return
        
        try:
            uhc_score = uhc_data["score"]
        except:
            uhc_score = 0
        
        try:
            uhc_kills = uhc_data["kills"]
        except:
            uhc_kills = 0
        
        try:
            uhc_deaths = uhc_data["deaths"]
        except:
            uhc_deaths = 0
        
        try:
            uhc_kill_death_ratio = uhc_kills / uhc_deaths
            uhc_kill_death_ratio = round(uhc_kill_death_ratio, 2)
        except:
            uhc_kill_death_ratio = 0
        
        try:
            uhc_wins = uhc_data["wins"]
        except:
            uhc_wins = 0
        
        try:
            uhc_heads_eaten = uhc_data["heads_eaten"]
        except:
            uhc_heads_eaten = 0
        
        try:
            uhc_ultimates_crafted = uhc_data["ultimates_crafted"]
        except:
            uhc_ultimates_crafted = 0
        
        try:
            uhc_selected_kit = uhc_data["equippedKit"]
        except:
            uhc_selected_kit = "N/A"
        
        try:
            uhc_coins = uhc_data["coins"]
        except:
            uhc_coins = 0
        

        embed=discord.Embed(title = "UHC Champions Statistics", description = "**Score:** `" + str(separation(uhc_score)) + "`", color=0x0097FF)
        embed.add_field(name = "Kills", value = "`" + str(separation(uhc_kills)) + "`", inline = True)
        embed.add_field(name = "Deaths", value = "`" + str(separation(uhc_deaths)) + "`", inline = True)
        embed.add_field(name = "K/D", value = "`" + str(uhc_kill_death_ratio) + "`", inline = True)
        embed.add_field(name = "Heads\nEaten", value = "`" + str(separation(uhc_heads_eaten)) + "`", inline = True)
        embed.add_field(name = "Ultimates\nCrafted", value = "`" + str(separation(uhc_ultimates_crafted)) + "`", inline = True)
        embed.add_field(name = "Selected Kit", value = "`" + str(uhc_selected_kit) + "`", inline = False)
        embed.add_field(name = "Coins", value = "`" + str(separation(uhc_coins)) + "`", inline = False)

        embed.set_author(name = display_name, icon_url = username_icon)
        embed.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/UHC-64.png")
        embed.set_footer(text= embed_footer)

        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(uhcchampionsStats(client))
