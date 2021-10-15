import discord
from discord.ext import commands
import requests
import string


class skyclashStats(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(pass_conext=True)
    async def sc(self, ctx, username: str = None):
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
            sc_data = hypixel_data["player"]["stats"]["SkyClash"]
            display_name = hypixel_data["player"]["displayname"]
        except:
            embed=discord.Embed(title = "Invalid Request", color=0xFF0000)
            embed.add_field(name = "Error", value = "`This player cannot be found on the API`")
            embed.add_field(name = "Correct Useage", value = "`-sc <IGN>`")
            embed.set_footer(text= embed_footer)
            await ctx.channel.send(embed=embed)
            return
        
        try:
            sc_kills = sc_data["kills"]
        except:
            sc_kills = 0
        
        try:
            sc_deaths = sc_data["deaths"]
        except:
            sc_deaths = 0
        
        try:
            sc_kill_death_ratio = sc_kills / sc_deaths
            sc_kill_death_ratio = round(sc_kill_death_ratio, 2)
        except:
            sc_kill_death_ratio = 0
        
        try:
            sc_wins = sc_data["wins"]
        except:
            sc_wins = 0
        
        try:
            sc_losses = sc_data["losses"]
        except:
            sc_losses = 0
        
        try:
            sc_win_loss_ratio = sc_wins / sc_losses
            sc_win_loss_ratio = round(sc_win_loss_ratio, 2)
        except:
            sc_win_loss_ratio = 0
        
        try:
            sc_assists = sc_data["assists"]
        except:
            sc_assists = 0
        
        try:
            sc_mobs_killed = sc_data["mobs_killed"]
        except:
            sc_mobs_killed = 0
        
        try:
            sc_games_played = sc_data["games_played"]
        except:
            sc_games_played = 0
        

        embed=discord.Embed(title = "SkyClash Statistics", color=0x0097FF)
        embed.add_field(name = "Kills", value = "`" + str(separation(sc_kills)) + "`", inline = True)
        embed.add_field(name = "Deaths", value = "`" + str(separation(sc_deaths)) + "`", inline = True)
        embed.add_field(name = "K/D", value = "`" + str(sc_kill_death_ratio) + "`", inline = True)
        embed.add_field(name = "Wins", value = "`" + str(separation(sc_wins)) + "`", inline = True)
        embed.add_field(name = "Losses", value = "`" + str(separation(sc_losses)) + "`", inline = True)
        embed.add_field(name = "W/L", value = "`" + str(sc_win_loss_ratio) + "`", inline = True)
        embed.add_field(name = "Assists", value = "`" + str(separation(sc_assists)) + "`", inline = True)
        embed.add_field(name = "Mobs Killed", value = "`" + str(separation(sc_mobs_killed)) + "`", inline = True)
        embed.add_field(name = "Games Played", value = "`" + str(separation(sc_games_played)) + "`", inline = True)

        embed.set_author(name = display_name, icon_url = username_icon)
        embed.set_thumbnail(url = "https://hypixel.net/styles/hypixel-uix/hypixel/game-icons/SkyClash-64.png")
        embed.set_footer(text= embed_footer)

        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(skyclashStats(client))
