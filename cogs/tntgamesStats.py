import discord
from discord.ext import commands
import requests
import string


class tntgamesStats(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(pass_conext=True, aliases = ["tntgames"])
    async def tnt(self, ctx, username: str = None):
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
            tnt_data = hypixel_data["player"]["stats"]["TNTGames"]
            display_name = hypixel_data["player"]["displayname"]
        except:
            embed=discord.Embed(title = "Invalid Request", color=0xFF0000)
            embed.add_field(name = "Error", value = "`This player cannot be found on the API`")
            embed.add_field(name = "Correct Useage", value = "`-tnt <IGN>`")
            embed.set_footer(text= embed_footer)
            await ctx.channel.send(embed=embed)
            return
        
        try:
            tnt_run_wins = tnt_data["wins_tntrun"]
        except:
            tnt_run_wins = 0
        
        try:
            tnt_pvp_wins = tnt_data["wins_pvprun"]
        except:
            tnt_pvp_wins = 0
        
        try:
            tnt_pvp_kills = tnt_data["kills_pvprun"]
        except:
            tnt_pvp_kills = 0
        
        try:
            tnt_pvp_deaths = tnt_data["deaths_pvprun"]
        except:
            tnt_pvp_deaths = 0

        try:
            tnt_pvp_kill_death_ratio = tnt_pvp_kills / tnt_pvp_deaths
            tnt_pvp_kill_death_ratio = round(tnt_pvp_kill_death_ratio, 2)
        except:
            tnt_pvp_kill_death_ratio = 0

        try:
            tnt_tag_wins = tnt_data["wins_tntag"]  
        except:
            tnt_tag_wins = 0
        
        try:
            tnt_bow_wins = tnt_data["wins_bowspleef"]
        except:
            tnt_bow_wins = 0
        
        try:
            tnt_wizards_wins = tnt_data["wins_capture"]
        except:
            tnt_wizards_wins = 0
        
        try:
            tnt_wizards_kills = tnt_data["kills_capture"]
        except:
            tnt_wizards_kills = 0
        
        try:
            tnt_wizards_deaths = tnt_data["deaths_capture"]
        except:
            tnt_wizards_deaths = 0
        
        try:
            tnt_wizards_kill_death_ratio = tnt_wizards_kills / tnt_wizards_deaths
            tnt_wizards_kill_death_ratio = round(tnt_wizards_kill_death_ratio, 2)
        except:
            tnt_wizards_kill_death_ratio = 0
        
        try:
            tnt_hat_selected = tnt_data["new_selected_hat"]
        except:
            tnt_hat_selected = "N/A"
        
        try:
            tnt_coins = tnt_data["coins"]
        except:
            tnt_coins = 0
        

        embed=discord.Embed(title = "TNT Games Statistics", color=0x0097FF)
        embed.add_field(name = "TNT Run", value = "Wins: `" + str(separation(tnt_run_wins)) + "`", inline = True)
        embed.add_field(name = "Bowspleef", value = "Wins: `" + str(separation(tnt_bow_wins)) + "`", inline = True)
        embed.add_field(name = "TNT Tag", value = "Wins: `" + str(separation(tnt_tag_wins)) + "`", inline = True)
        embed.add_field(name = "PVP Run", value = "Wins: `" + str(separation(tnt_pvp_wins)) + "`\n" + "Kills: `" + str(separation(tnt_pvp_kills)) + "`\n" +
        "Deaths: `" + str(separation(tnt_pvp_deaths)) + "`\n" + "K/D: `" + str(tnt_pvp_kill_death_ratio) + "`", inline = True)
        embed.add_field(name = "TNT Wizards", value = "Wins: `" + str(separation(tnt_wizards_wins)) + "`\n" + "Kills: `" + str(separation(tnt_wizards_kills)) + "`\n" +
        "Deaths: `" + str(separation(tnt_wizards_deaths)) + "`\n" + "K/D: `" + str(tnt_wizards_kill_death_ratio) + "`", inline = True)
        embed.add_field(name = "Hat Selected", value = "`" + str(tnt_hat_selected) + "`", inline = False)
        embed.add_field(name = "Coins", value = "`" + str(separation(tnt_coins)) + "`", inline = False)

        embed.set_author(name = display_name, icon_url = username_icon)
        embed.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/TNT-64.png")
        embed.set_footer(text= embed_footer)

        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(tntgamesStats(client))
