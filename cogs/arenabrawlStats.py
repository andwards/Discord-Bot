import discord
from discord.ext import commands
import requests
import string


class arenabrawlStats(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(pass_conext=True, aliases = ["arena"])
    async def ab(self, ctx, username: str = None):
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
            ab_data = hypixel_data["player"]["stats"]["Arena"]
            display_name = hypixel_data["player"]["displayname"]
        except:
            embed=discord.Embed(title = "Invalid Request", color=0xFF0000)
            embed.add_field(name = "Error", value = "`This player cannot be found on the API`")
            embed.add_field(name = "Correct Useage", value = "`-ab <IGN>`\n `-arena <IGN>`")
            embed.set_footer(text= embed_footer)
            await ctx.channel.send(embed=embed)
            return
        
        try:
            ab_kills_1v1 = ab_data["kills_1v1"]
        except:
            ab_kills_1v1 = 0
        
        try: 
            ab_deaths_1v1 = ab_data["deaths_1v1"]
        except:
            ab_deaths_1v1 = 0
        
        try:
            ab_kill_death_ratio_1v1 = ab_kills_1v1 / ab_deaths_1v1
            ab_kill_death_ratio_1v1 = round(ab_kill_death_ratio_1v1, 2)
        except:
            ab_kill_death_ratio_1v1 = 0
        
        try:
            ab_wins_1v1 = ab_data["wins_1v1"]
        except:
            ab_wins_1v1 = 0
        
        try:
            ab_losses_1v1 = ab_data["losses_1v1"]
        except:
            ab_losses_1v1 = 0
        
        try:
            ab_win_lose_ratio_1v1 = ab_wins_1v1 / ab_losses_1v1
            ab_win_lose_ratio_1v1 = round(ab_win_lose_ratio_1v1, 2)
        except:
            ab_win_lose_ratio_1v1 = 0
        
        try:
            ab_kills_2v2 = ab_data["kills_2v2"]
        except:
            ab_kills_2v2 = 0
        
        try: 
            ab_deaths_2v2 = ab_data["deaths_2v2"]
        except:
            ab_deaths_2v2 = 0
        
        try:
            ab_kill_death_ratio_2v2 = ab_kills_2v2 / ab_deaths_2v2
            ab_kill_death_ratio_2v2 = round(ab_kill_death_ratio_2v2, 2)
        except:
            ab_kill_death_ratio_2v2 = 0
        
        try:
            ab_wins_2v2 = ab_data["wins_2v2"]
        except:
            ab_wins_2v2 = 0
        
        try:
            ab_losses_2v2 = ab_data["losses_2v2"]
        except:
            ab_losses_2v2 = 0
        
        try:
            ab_win_lose_ratio_2v2 = ab_wins_2v2 / ab_losses_2v2
            ab_win_lose_ratio_2v2 = round(ab_win_lose_ratio_2v2, 2)
        except:
            ab_win_lose_ratio_2v2 = 0
        
        try:
            ab_kills_4v4 = ab_data["kills_4v4"]
        except:
            ab_kills_4v4 = 0
        
        try: 
            ab_deaths_4v4 = ab_data["deaths_4v4"]
        except:
            ab_deaths_4v4 = 0
        
        try:
            ab_kill_death_ratio_4v4 = ab_kills_4v4 / ab_deaths_4v4
            ab_kill_death_ratio_4v4 = round(ab_kill_death_ratio_4v4, 2)
        except:
            ab_kill_death_ratio_4v4 = 0
        
        try:
            ab_wins_4v4 = ab_data["wins_4v4"]
        except:
            ab_wins_4v4 = 0
        
        try:
            ab_losses_4v4 = ab_data["losses_4v4"]
        except:
            ab_losses_4v4 = 0
        
        try:
            ab_win_lose_ratio_4v4 = ab_wins_4v4 / ab_losses_4v4
            ab_win_lose_ratio_4v4 = round(ab_win_lose_ratio_4v4, 2)
        except:
            ab_win_lose_ratio_4v4 = 0
        
        try:
            ab_wins_total = ab_wins_1v1 + ab_wins_2v2 + ab_wins_4v4
        except:
            ab_wins_total = 0
        
        try:
            ab_kills_total = ab_kills_1v1 + ab_kills_2v2 + ab_kills_4v4
        except:
            ab_kills_total = 0
        
        try:
            ab_keys = ab_data["keys"]
        except:
            ab_keys = 0
        
        try:
            ab_coins = ab_data["coins"]
        except:
            ab_coins = 0
        

        embed=discord.Embed(title = "Arena Brawl Statistics", color=0x0097FF)
        embed.add_field(name = "1v1", value = "Kills: `" + str(separation(ab_kills_1v1)) + "`\n" + "Deaths: `"  + str(separation(ab_deaths_1v1)) + "`\n" + 
        "K/D: `" + str(ab_kill_death_ratio_1v1) + "`\n" + "Wins: `" + str(separation(ab_wins_1v1)) + "`\n" + "Losses: `" + str(separation(ab_losses_1v1)) + "`\n" + 
        "W/L: `" + str(ab_win_lose_ratio_1v1) + "`", inline = True)
        embed.add_field(name = "2v2", value = "Kills: `" + str(separation(ab_kills_2v2)) + "`\n" + "Deaths: `"  + str(separation(ab_deaths_2v2)) + "`\n" + 
        "K/D: `" + str(ab_kill_death_ratio_2v2) + "`\n" + "Wins: `" + str(separation(ab_wins_2v2)) + "`\n" + "Losses: `" + str(separation(ab_losses_2v2)) + "`\n" + 
        "W/L: `" + str(ab_win_lose_ratio_2v2) + "`", inline = True)
        embed.add_field(name = "4v4", value = "Kills: `" + str(separation(ab_kills_4v4)) + "`\n" + "Deaths: `"  + str(separation(ab_deaths_4v4)) + "`\n" + 
        "K/D: `" + str(ab_kill_death_ratio_4v4) + "`\n" + "Wins: `" + str(separation(ab_wins_4v4)) + "`\n" + "Losses: `" + str(separation(ab_losses_4v4)) + "`\n" + 
        "W/L: `" + str(ab_win_lose_ratio_4v4) + "`", inline = True)
    
        embed.add_field(name = "Wins", value = "`" + str(separation(ab_wins_total) + "`"), inline = True)
        embed.add_field(name = "Kills", value = "`" + str(separation(ab_kills_total) + "`"), inline = True)
        embed.add_field(name = "Keys", value = "`" + str(separation(ab_keys) + "`"), inline = True)
        embed.add_field(name = "Coins", value = "`" + str(separation(ab_coins) + "`"), inline = True)
        
        embed.set_author(name = display_name, icon_url = username_icon)
        embed.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/Arena-64.png")
        embed.set_footer(text= embed_footer)

        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(arenabrawlStats(client))

