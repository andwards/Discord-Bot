import discord
from discord.ext import commands
from discord.ext.commands.errors import ExpectedClosingQuoteError
import requests
import string


class speeduhcStats(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(pass_conext=True, aliases = ["speeduhc"])
    async def suhc(self, ctx, username: str = None):
        embed_footer = "© Andrew Edawrds | All Rights Reserved"
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
            suhc_data = hypixel_data["player"]["stats"]["SpeedUHC"]
            display_name = hypixel_data["player"]["displayname"]
        except:
            embed=discord.Embed(title = "Invalid Request", color=0xFF0000)
            embed.add_field(name = "Error", value = "`This player cannot be found on the API`")
            embed.add_field(name = "Correct Useage", value = "`-suhc <IGN>`\n `-speeduhc <IGN>`")
            embed.set_footer(text= embed_footer)
            await ctx.channel.send(embed=embed)
            return
        
        try:
            suhc_score = suhc_data["score"]
        except:
            suhc_score = 0
        
        try:
            suhc_kills = suhc_data["kills"]
        except:
            suhc_kills = 0
        
        try:
            suhc_deaths = suhc_data["deaths"]
        except:
            suhc_deaths = 0
        
        try:
            suhc_kill_death_ratio = suhc_kills / suhc_deaths
            suhc_kill_death_ratio = round(suhc_kill_death_ratio, 2)
        except:
            suhc_kill_death_ratio = 0
        
        try:
            suhc_wins = suhc_data["wins"]
        except:
            suhc_wins = 0
        
        try:
            suhc_losses = suhc_data["losses"]
        except:
            suhc_losses = 0
        
        try:
            suhc_win_lose_ratio = suhc_wins / suhc_losses
            suhc_win_lose_ratio = round(suhc_win_lose_ratio, 2)
        except:
            suhc_win_lose_ratio = 0
        

        embed=discord.Embed(title = "Speed UHC Statistics", description = "**Score:** `" + str(separation(suhc_score)) + "`", color=0x0097FF)
        embed.add_field(name = "Kills", value = "`" + str(separation(suhc_kills)) + "`", inline = True)
        embed.add_field(name = "Deaths", value = "`" + str(separation(suhc_deaths)) + "`", inline = True)
        embed.add_field(name = "K/D", value = "`" + str(suhc_kill_death_ratio) + "`", inline = True)
        embed.add_field(name = "Wins", value = "`" + str(separation(suhc_wins) + "`"), inline = True)
        embed.add_field(name = "Losses", value = "`" + str(separation(suhc_losses) + "`"), inline = True)
        embed.add_field(name = "W/L", value = "`" + str(suhc_win_lose_ratio) + "`", inline = True)

        embed.set_author(name = display_name, icon_url = username_icon)
        embed.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/SpeedUHC-64.png")
        embed.set_footer(text= embed_footer)

        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(speeduhcStats(client))
