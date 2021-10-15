import discord
from discord.ext import commands
import requests
import string


class wallsStats(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(pass_conext=True)
    async def walls(self, ctx, username: str = None):
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
            walls_data = hypixel_data["player"]["stats"]["Walls"]
            display_name = hypixel_data["player"]["displayname"]
        except:
            embed=discord.Embed(title = "Invalid Request", color=0xFF0000)
            embed.add_field(name = "Error", value = "`This player cannot be found on the API`")
            embed.add_field(name = "Correct Useage", value = "`-walls <IGN>`")
            embed.set_footer(text= embed_footer)
            await ctx.channel.send(embed=embed)
            return
        
        try:
            walls_kills = walls_data["kills"]
        except:
            walls_kills = 0
        
        try:
            walls_deaths = walls_data["deaths"]
        except:
            walls_deaths = 0
        
        try:
            walls_kill_death_ratio = walls_kills / walls_deaths
            walls_kill_death_ratio = round(walls_kill_death_ratio, 2)
        except:
            walls_kill_death_ratio = 0
        
        try:
            walls_wins = walls_data["wins"]
        except:
            walls_wins = 0
        
        try:
            walls_losses = walls_data["losses"]
        except:
            walls_losses = 0
        
        try:
            walls_win_loss_ratio = walls_wins / walls_losses
            walls_win_loss_ratio = round(walls_win_loss_ratio, 2)
        except:
            walls_win_loss_ratio = 0
        
        try:
            walls_coins = walls_data["coins"]
        except:
            walls_coins = 0
        
        try:
            walls_diamonds_mined = hypixel_data["player"]["achievements"]["walls_diamond_miner"]
        except:
            walls_diamonds_mined = 0
        
        embed=discord.Embed(title = "The Walls Statistics", color=0x0097FF)
        embed.add_field(name = "Kills", value = "`" + str(separation(walls_kills) + "`"), inline = True)
        embed.add_field(name = "Deaths", value = "`" + str(separation(walls_deaths) + "`"), inline = True)
        embed.add_field(name = "K/D", value = "`" + str(walls_kill_death_ratio) + "`", inline = True)
        embed.add_field(name = "Wins", value = "`" + str(separation(walls_wins) + "`"), inline = True)
        embed.add_field(name = "Losses", value = "`" + str(separation(walls_losses)) + "`", inline = True)
        embed.add_field(name = "W/L", value = "`" + str(walls_win_loss_ratio) + "`", inline = True)
        #embed.add_field(name = "Diamonds Mined", value = "`" + str(separation(walls_diamonds_mined)) + "`", inline = True)
        embed.add_field(name = "Coins", value = "`" + str(separation(walls_coins) + "`"), inline = True)

        embed.set_author(name = display_name, icon_url = username_icon)
        embed.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/Walls-64.png")
        embed.set_footer(text= embed_footer)

        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(wallsStats(client))
