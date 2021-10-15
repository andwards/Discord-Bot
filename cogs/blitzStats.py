import discord
from discord.ext import commands
import requests
import string
import random


class blitzStats(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(pass_conext=True, aliases = ["blitz"])
    async def bsg(self, ctx, username: str = None):
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
            blitz_data = hypixel_data["player"]["stats"]["HungerGames"]
            display_name = hypixel_data["player"]["displayname"]
        except:
            embed=discord.Embed(title = "Invalid Request", color=0xFF0000)
            embed.add_field(name = "Error", value = "`This player cannot be found on the API`")
            embed.add_field(name = "Correct Useage", value = "`-bsg <IGN>`\n `-blitz <IGN>`")
            embed.set_footer(text= embed_footer)
            await ctx.channel.send(embed=embed)
            return
        
        
        try:
            blitz_kills = blitz_data["kills"]
        except:
            blitz_kills = 0
        
        try:
            blitz_deaths = blitz_data["deaths"]
        except:
            blitz_deaths = 0
        
        try: 
            blitz_kill_death_ratio = blitz_kills / blitz_deaths
            blitz_kill_death_ratio = round(blitz_kill_death_ratio, 2)
        except:
            blitz_kill_death_ratio = 0
        
        try:
            blitz_solo_wins = blitz_data["wins_solo_normal"]
        except:
            blitz_solo_wins = 0

        try:
            blitz_team_wins = blitz_data["wins_teams"]
        except:
            blitz_team_wins = 0

        try:
            blitz_total_wins = blitz_solo_wins + blitz_team_wins
        except:
            blitz_total_wins = 0
        
        try:
            blitz_default_kit = blitz_data["defaultkit"]
        except:
            blitz_default_kit = "N/A"
        
        try:
            blitz_coins = blitz_data["coins"]
        except:
            blitz_coins = 0
        
        try:
            blitz_chests_opened = blitz_data["chests_opened"]
        except:
            blitz_chests_opened = 0
        
        try:
            blitz_taunt_kills = blitz_data["taunt_kills"]
        except:
            blitz_taunt_kills = 0
        
        embed=discord.Embed(title = "Blitz Statistics", color=0x0097FF)
        embed.add_field(name = "Kills", value = "`" + str(separation(blitz_kills) + "`"), inline = True)
        embed.add_field(name = "Deaths", value = "`" + str(separation(blitz_deaths) + "`"), inline = True)
        embed.add_field(name = "K/D Ratio", value = "`" + str(blitz_kill_death_ratio) + "`", inline = True)
        embed.add_field(name = "Wins", value = "Solo: `" + str(separation(blitz_solo_wins) + "`\n" + "Teams: `" + str(separation(blitz_team_wins) + "`\n" + 
        "Total: `" + str(separation(blitz_total_wins) + "`"))), inline = True)
        embed.add_field(name = "Default Kit", value = "`" + str(blitz_default_kit) + "`", inline = True)
        embed.add_field(name = "Coins", value = "`" + str(separation(blitz_coins) + "`"), inline = True)
        embed.add_field(name = "Chests Opened", value = "`" + str(separation(blitz_chests_opened) + "`"), inline = True)
        embed.add_field(name = "Taunt Kills", value = "`" + str(separation(blitz_taunt_kills) + "`"), inline = True)

        embed.set_image(url = "https://gen.plancke.io/blitz/" + username + "/3.png" + "?random=" + randomString(10))
        embed.set_author(name = display_name, icon_url = username_icon)
        embed.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/SG-64.png")
        embed.set_footer(text= embed_footer)

        await ctx.channel.send(embed=embed)

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def setup(client):
    client.add_cog(blitzStats(client))
