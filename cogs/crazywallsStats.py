import discord
from discord.ext import commands
import requests
import string


class crazywallsStats(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(pass_conext=True)
    async def cw(self, ctx, username: str = None):
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
            cw_data = hypixel_data["player"]["stats"]["TrueCombat"]
            display_name = hypixel_data["player"]["displayname"]
        except:
            embed=discord.Embed(title = "Invalid Request", color=0xFF0000)
            embed.add_field(name = "Error", value = "`This player cannot be found on the API`")
            embed.add_field(name = "Correct Useage", value = "`-cw <IGN>`")
            embed.set_footer(text= embed_footer)
            await ctx.channel.send(embed=embed)
            return
        
        try:
            cw_kills = cw_data["kills"]
        except:
            cw_kills = 0
        
        try:
            cw_deaths = cw_data["deaths"]
        except:
            cw_deaths = 0
        
        try:
            cw_kill_death_ratio = cw_kills / cw_deaths
            cw_kill_death_ratio = round(cw_kill_death_ratio, 2)
        except:
            cw_kill_death_ratio = 0
        
        try:
            cw_wins = cw_data["wins"]
        except:
            cw_wins = 0
        
        try:
            cw_losses = cw_data["losses"]
        except:
            cw_losses = 0
        
        try:
            cw_win_loss_ratio = cw_wins / cw_losses
            cw_win_loss_ratio = round(cw_win_loss_ratio, 2)
        except:
            cw_win_loss_ratio = 0
        
        try:
            cw_dust = cw_data["gold_dust"]
        except:
            cw_dust = 0
        
        try:
            cw_skulls = cw_data["golden_skulls"]
        except:
            cw_skulls = 0
        
        try:
            cw_giant_zombie = cw_data["giant_zombie"]
        except:
            cw_giant_zombie = 0
        
        try:
            cw_coins = cw_data["coins"]
        except:
            cw_coins = 0
        

        embed=discord.Embed(title = "Crazy Walls Statistics", color=0x0097FF)
        embed.add_field(name = "Kills", value = "`" + str(separation(cw_kills)) + "`", inline = True)
        embed.add_field(name = "Deaths", value = "`" + str(separation(cw_deaths)) + "`", inline = True)
        embed.add_field(name = "K/D", value = "`" + str(cw_kill_death_ratio) + "`", inline = True)
        embed.add_field(name = "Wins", value = "`" + str(separation(cw_wins)) + "`", inline = True)
        embed.add_field(name = "Losses", value = "`" + str(separation(cw_losses)) + "`", inline = True)
        embed.add_field(name = "W/L", value = "`" + str(cw_win_loss_ratio) + "`", inline = True)
        embed.add_field(name = "Gold Dust", value = "`" + str(separation(cw_dust)) + "`", inline = True)
        embed.add_field(name = "Gold Skulls", value = "`" + str(separation(cw_skulls)) + "`", inline = True)
        embed.add_field(name = "Giant Zombie", value = "`" + str(separation(cw_giant_zombie)) + "`", inline = True)
        embed.add_field(name = "Coins", value = "`" + str(separation(cw_coins)) + "`", inline = True)

        embed.set_author(name = display_name, icon_url = username_icon)
        embed.set_thumbnail(url = "https://hypixel.net/styles/hypixel-uix/hypixel/game-icons/CrazyWalls-64.png")
        embed.set_footer(text= embed_footer)

        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(crazywallsStats(client))

