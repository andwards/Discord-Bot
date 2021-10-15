import discord
from discord.ext import commands
import requests
import string


class copsandcrimsStats(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(pass_conext=True, aliases = ["copsvscrims"])
    async def cvc(self, ctx, username: str = None):
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
            cvc_data = hypixel_data["player"]["stats"]["MCGO"]
            display_name = hypixel_data["player"]["displayname"]
        except:
            embed=discord.Embed(title = "Invalid Request", color=0xFF0000)
            embed.add_field(name = "Error", value = "`This player cannot be found on the API`")
            embed.add_field(name = "Correct Useage", value = "`-cvc <IGN>`\n")
            embed.set_footer(text= embed_footer)
            await ctx.channel.send(embed=embed)
            return
        
        try:
            cvc_defusal_kills = cvc_data["kills"]
        except:
            cvc_defusal_kills = 0

        try:
            cvc_defusal_deaths = cvc_data["deaths"]
        except:
            cvc_defusal_deaths = 0
        
        try: 
            cvc_defusal_kill_death_ratio = cvc_defusal_kills / cvc_defusal_deaths
            cvc_defusal_kill_death_ratio = round(cvc_defusal_kill_death_ratio, 2)
        except:
            cvc_defusal_kill_death_ratio = 0
        
        try:
            cvc_defusal_wins = cvc_data["game_wins"]
        except:
            cvc_defusal_wins = 0
        
        try:
            cvc_defusal_losses = cvc_data["game_plays"] - cvc_defusal_wins
        except:
            cvc_defusal_losses = 0
        
        try:
            cvc_defusal_win_lose_ratio = cvc_defusal_wins / cvc_defusal_losses
            cvc_defusal_win_lose_ratio = round(cvc_defusal_win_lose_ratio, 2)
        except:
            cvc_defusal_win_lose_ratio = 0
        
        try:
            cvc_tdm_kills = cvc_data["kills_deathmatch"]
        except:
            cvc_tdm_kills = 0
        
        try:
            cvc_tdm_deaths = cvc_data["deaths_deathmatch"]
        except:
            cvc_tdm_deaths = 0
        
        try:
            cvc_tdm_kill_death_ratio = cvc_tdm_kills / cvc_tdm_deaths
            cvc_tdm_kill_death_ratio = round(cvc_tdm_kill_death_ratio, 2)
        except:
            cvc_tdm_kill_death_ratio = 0
        
        try:
            cvc_tdm_wins = cvc_data["game_wins_deathmatch"]
        except:
            cvc_tdm_wins = 0
        
        try:
            cvc_tdm_losses = cvc_data["game_plays_deathmatch"] - cvc_tdm_wins
        except:
            cvc_tdm_losses = 0
        
        try:
            cvc_tdm_win_lose_ratio = cvc_tdm_wins / cvc_tdm_losses
            cvc_tdm_win_lose_ratio = round(cvc_tdm_win_lose_ratio, 2)
        except:
            cvc_tdm_win_lose_ratio = 0
        
        try:
            cvc_total_kills = cvc_defusal_kills + cvc_tdm_kills
        except:
            cvc_total_kills = 0
        
        try:
            cvc_total_deaths = cvc_defusal_deaths + cvc_tdm_deaths
        except:
            cvc_total_deaths = 0
        
        try: 
            cvc_total_kill_death_ratio = cvc_total_kills / cvc_total_deaths
            cvc_total_kill_death_ratio = round(cvc_total_kill_death_ratio, 2)
        except:
            cvc_total_kill_death_ratio = 0
        
        try:
            cvc_total_wins = cvc_defusal_wins + cvc_tdm_wins
        except:
            cvc_total_wins = 0
        
        try:
            cvc_total_losses = cvc_defusal_losses + cvc_tdm_losses
        except:
            cvc_total_losses = 0
        
        try:
            cvc_total_win_lose_ratio = cvc_total_wins / cvc_total_losses
            cvc_total_win_lose_ratio = round(cvc_total_win_lose_ratio, 2)
        except:
            cvc_total_win_lose_ratio = 0
        
        try:
            cvc_bombs_defused = cvc_data["bombs_defused"]
        except:
            cvc_bombs_defused = 0
        
        try:
            cvc_bombs_planted = cvc_data["bombs_planted"]
        except:
            cvc_bombs_planted = 0
        
        try:
            cvc_headshots = cvc_data["headshot_kills"]
        except:
            cvc_headshots = 0
        
        try:
            cvc_grenade_kills = cvc_data["grenade_kills"]
        except:
            cvc_grenade_kills = 0
        
        try:
            cvc_prefix_color = cvc_data["lobbyPrefixColor"]
        except:
            cvc_prefix_color = "Default"
        
        try:
            cvc_coins = cvc_data["coins"]
        except:
            cvc_coins = 0
        
        try:
            cvc_shots_fired = cvc_data["shots_fired"]
        except:
            cvc_shots_fired = 0
        
        try:
            cvc_score = (cvc_total_kills / 2) + ((cvc_bombs_planted + cvc_bombs_defused) / 3) + cvc_total_wins + ((cvc_total_kills / cvc_shots_fired) * 200)
            cvc_score = round(cvc_score)
        except:
            cvc_score = 0
        
        embed=discord.Embed(title = "Cops and Crims Statistics", description = "**Score:** `" + str(separation(cvc_score)) + "`", color=0x0097FF)
        embed.add_field(name = "Defusal", value = "Kills: `" + str(separation(cvc_defusal_kills)) + "`\n" + "Deaths: `" + str(separation(cvc_defusal_deaths)) + "`\n" +
        "Wins: `" + str(separation(cvc_defusal_wins)) + "`\n" + "K/D: `" + str(cvc_defusal_kill_death_ratio) + "`", inline = True)
        embed.add_field(name = "Team Deathmatch", value = "Kills: `" + str(separation(cvc_tdm_kills)) + "`\n" + "Deaths: `" + str(separation(cvc_tdm_deaths)) + "`\n" +
        "Wins: `" + str(separation(cvc_tdm_wins)) + "`\n" + "K/D: `" + str(cvc_tdm_kill_death_ratio) + "`", inline = True)
        embed.add_field(name = "Total", value = "Kills: `" + str(separation(cvc_total_kills)) + "`\n" + "Deaths: `" + str(separation(cvc_total_deaths)) + "`\n" +
        "Wins: `" + str(separation(cvc_total_wins)) + "`\n" + "K/D: `" + str(cvc_total_kill_death_ratio) + "`", inline = True)
        embed.add_field(name = "Bombs", value = "Defused: `" + str(separation(cvc_bombs_defused)) + "`\n" + "Plants: `" + str(separation(cvc_bombs_planted)) + "`", inline = True)
        embed.add_field(name = "Headshots", value = "`" + str(separation(cvc_headshots)) + "`", inline = True)
        embed.add_field(name = "Grenade Kills", value = "`" + str(separation(cvc_grenade_kills)) + "`", inline = True)
        embed.add_field(name = "Prefix Color", value = "`" + str(cvc_prefix_color) + "`", inline = False)
        embed.add_field(name = "Coins", value = "`" + str(separation(cvc_coins)) + "`", inline = False)

        embed.set_author(name = display_name, icon_url = username_icon)
        embed.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/CVC-64.png")
        embed.set_footer(text= embed_footer)

        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(copsandcrimsStats(client))
