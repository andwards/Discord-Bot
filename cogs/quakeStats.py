import discord
from discord.ext import commands
import requests
import string


class quakeStats(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(pass_conext=True)
    async def quake(self, ctx, username: str = None):
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
            quake_data = hypixel_data["player"]["stats"]["Quake"]
            display_name = hypixel_data["player"]["displayname"]
        except:
            embed=discord.Embed(title = "Invalid Request", color=0xFF0000)
            embed.add_field(name = "Error", value = "`This player cannot be found on the API`")
            embed.add_field(name = "Correct Useage", value = "`-quake <IGN>`")
            embed.set_footer(text= embed_footer)
            await ctx.channel.send(embed=embed)
            return
        
        try:
            quake_kills_solo = quake_data["kills"]
        except:
            quake_kills_solo = 0
        
        try:
            quake_kills_teams = quake_data["kills_teams"]
        except:
            quake_kills_teams = 0
        
        try:
            quake_kills_total = quake_kills_solo + quake_kills_teams
        except:
            quake_kills_total = 0
        
        try:
            quake_deaths_solo = quake_data["deaths"]
        except:
            quake_deaths_solo = 0
        
        try:
            quake_deaths_teams = quake_data["deaths_teams"]
        except:
            quake_deaths_teams = 0
        
        try:
            quake_deaths_total = quake_deaths_solo + quake_deaths_teams
        except:
            quake_deaths_total = 0
        
        try:
            quake_kill_death_ratio = quake_kills_total / quake_deaths_total
            quake_kill_death_ratio = round(quake_kill_death_ratio, 2)
        except:
            quake_kill_death_ratio = 0

        try:
            quake_wins_solo = quake_data["wins"]
        except:
            quake_win_solo = 0
        
        try:
            quake_wins_teams = quake_data["wins_teams"]
        except:
            quake_win_teams = 0

        try:
            quake_wins_total = quake_wins_solo + quake_wins_teams
        except:
            quake_win_total = 0
        
        try:
            quake_killstreaks_solo = quake_data["killstreaks"]
        except:
            quake_killstreaks_solo = 0
        
        try:
            quake_killstreaks_teams = quake_data["killstreaks_teams"]
        except:
            quake_killstreaks_teams = 0
        
        try:
            quake_killstreaks_total = quake_killstreaks_solo + quake_killstreaks_teams
        except:
            quake_killstreaks_total = 0
        
        try:
            quake_headshots_solo = quake_data["headshots"]
        except:
            quake_headshots_solo = 0
        
        try:
            quake_headshots_teams = quake_data["headshots_teams"]
        except:
            quake_headshots_teams = 0
        
        try:
            quake_headshots_total = quake_headshots_solo + quake_headshots_teams
        except:
            quake_headshots_total = 0
        
        try:
            quake_godlikes = hypixel_data["player"]["achievements"]["quake_godlikes"]
        except:
            quake_godlikes = 0
        
        try:
            quake_coins = quake_data["coins"]
        except:
            quake_coins = 0
        
        
        embed=discord.Embed(title = "Quakecraft Statistics", color=0x0097FF)
        embed.add_field(name = "Kills", value = "Solo: `" + str(separation(quake_kills_solo) + "`\n" + "Teams: `" + str(separation(quake_kills_teams) + "`\n" + 
        "Total: `" + str(separation(quake_kills_total) + "`"))), inline = True)
        embed.add_field(name = "Deaths", value = "Solo: `" + str(separation(quake_deaths_solo) + "`\n" + "Teams: `" + str(separation(quake_deaths_teams) + "`\n" + 
        "Total: `" + str(separation(quake_deaths_total) + "`"))), inline = True)
        embed.add_field(name = "K/D", value = "`" + str(quake_kill_death_ratio) + "`", inline = True)
        embed.add_field(name = "Wins", value = "Solo: `" + str(separation(quake_wins_solo) + "`\n" + "Teams: `" + str(separation(quake_wins_teams) + "`\n" + 
        "Total: `" + str(separation(quake_wins_total) + "`"))), inline = True)
        embed.add_field(name = "Killstreaks", value = "`" + str(separation(quake_killstreaks_total) + "`"), inline = True)
        embed.add_field(name = "Headshots", value = "`" + str(separation(quake_headshots_total) + "`"), inline = True)
        embed.add_field(name = "Godlikes", value = "`" + str(separation(quake_godlikes) + "`"), inline = True)
        embed.add_field(name = "Coins", value = "`" + str(separation(quake_coins) + "`"), inline = True)

        embed.set_author(name = display_name, icon_url = username_icon)
        embed.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/Quakecraft-64.png")
        embed.set_footer(text= embed_footer)

        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(quakeStats(client))
