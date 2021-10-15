import discord
from discord.ext import commands
import requests
import string


class duelStats(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(pass_conext=True)
    async def duels(self, ctx, username: str = None):
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
            duels_data = hypixel_data["player"]["stats"]["Duels"]
            display_name = hypixel_data["player"]["displayname"]
        except:
            embed=discord.Embed(title = "Invalid Request", color=0xFF0000)
            embed.add_field(name = "Error", value = "`This player cannot be found on the API`")
            embed.add_field(name = "Correct Useage", value = "`-duels <IGN>`")
            embed.set_footer(text= embed_footer)
            await ctx.channel.send(embed=embed)
            return
        
        try:
            duels_kills = duels_data["kills"]
        except:
            duels_kills = 0
        
        try:
            duels_deaths = duels_data["deaths"]
        except:
            duels_deaths = 0
        
        try:
            duels_kill_death_ratio = duels_kills / duels_deaths
            duels_kill_death_ratio = round(duels_kill_death_ratio, 2)
        except:
            duels_kill_death_ratio = 0
        
        try:
            duels_wins = duels_data["wins"]
        except:
            duels_wins = 0
        
        try:
            duels_losses = duels_data["losses"]
        except:
            duels_losses = 0
        
        try:
            duels_win_loss_ratio = duels_wins / duels_losses
            duels_win_loss_ratio = round(duels_win_loss_ratio, 2)
        except:
            duels_win_loss_ratio = 0
        
        try:
            duels_coins = duels_data["coins"]
        except:
            duels_coins = 0
        

        embed=discord.Embed(title = "Duels Statistics", color=0x0097FF)
        embed.add_field(name = "Kills", value = "`" + str(separation(duels_kills)) + "`", inline = True)
        embed.add_field(name = "Deaths", value = "`" + str(separation(duels_deaths)) + "`", inline = True)
        embed.add_field(name = "K/D", value = "`" + str(duels_kill_death_ratio) + "`", inline = True)
        embed.add_field(name = "Wins", value = "`" + str(separation(duels_wins)) + "`", inline = True)
        embed.add_field(name = "Losses", value = "`" + str(separation(duels_losses)) + "`", inline = True)
        embed.add_field(name = "W/L", value = "`" + str(separation(duels_win_loss_ratio)) + "`", inline = True)
        embed.add_field(name = "Coins", value = "`" + str(separation(duels_coins)) + "`", inline = True)

        embed.set_author(name = display_name, icon_url = username_icon)
        embed.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/Duels-64.png")
        embed.set_footer(text= embed_footer)

        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(duelStats(client))
