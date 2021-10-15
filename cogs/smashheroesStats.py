import discord
from discord.ext import commands
import requests
import string
import random


class smashheroesStats(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(pass_conext=True, aliases = ["smash"])
    async def sh(self, ctx, username: str = None):
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
            sh_data = hypixel_data["player"]["stats"]["SuperSmash"]
            display_name = hypixel_data["player"]["displayname"]
        except:
            embed=discord.Embed(title = "Invalid Request", color=0xFF0000)
            embed.add_field(name = "Error", value = "`This player cannot be found on the API`")
            embed.add_field(name = "Correct Useage", value = "`-sh <IGN>`\n `-smash <IGN>`")
            embed.set_footer(text= embed_footer)
            await ctx.channel.send(embed=embed)
            return
        
        try:
            sh_level = sh_data["smashLevel"]
        except:
            sh_level = 0
        
        try:
            sh_kills_normal = sh_data["kills_normal"]
        except:
            sh_kills_normal = 0
        
        try:
            sh_deaths_normal = sh_data["deaths_normal"]
        except:
            sh_deaths_normal = 0
        
        try:
            sh_kill_death_ratio_normal = sh_kills_normal / sh_deaths_normal
            sh_kill_death_ratio_normal = round(sh_kill_death_ratio_normal, 2)
        except:
            sh_kill_death_ratio_normal = 0
        
        try:
            sh_wins_normal = sh_data["wins_normal"]
        except:
            sh_wins_normal = 0
        
        try:
            sh_losses_normal = sh_data["losses_normal"]
        except:
            sh_losses_normal = 0
        
        try:
            sh_win_loss_ratio_normal = sh_wins_normal / sh_losses_normal
            sh_win_loss_ratio_normal = round(sh_win_loss_ratio_normal, 2)
        except:
            sh_win_loss_ratio_normal = 0
        
        try:
            sh_kills_2v2 = sh_data["kills_2v2"]
        except:
            sh_kills_2v2 = 0
        
        try:
            sh_deaths_2v2 = sh_data["deaths_2v2"]
        except:
            sh_deaths_2v2 = 0
        
        try:
            sh_kill_death_ratio_2v2 = sh_kills_2v2 / sh_deaths_2v2
            sh_kill_death_ratio_2v2= round(sh_kill_death_ratio_2v2, 2)
        except:
            sh_kill_death_ratio_2v2 = 0
        
        try:
            sh_wins_2v2 = sh_data["wins_2v2"]
        except:
            sh_wins_2v2 = 0
        
        try:
            sh_losses_2v2 = sh_data["losses_2v2"]
        except:
            sh_losses_2v2 = 0
        
        try:
            sh_win_loss_ratio_2v2 = sh_wins_2v2 / sh_losses_2v2
            sh_win_loss_ratio_2v2 = round(sh_win_loss_ratio_2v2, 2)
        except:
            sh_win_loss_ratio_2v2 = 0
        
        try:
            sh_kills_teams = sh_data["kills_teams"]
        except:
            sh_kills_teams = 0
        
        try:
            sh_deaths_teams = sh_data["deaths_teams"]
        except:
            sh_deaths_teams = 0
        
        try:
            sh_kill_death_ratio_teams = sh_kills_teams / sh_deaths_teams
            sh_kill_death_ratio_teams= round(sh_kill_death_ratio_teams, 2)
        except:
            sh_kill_death_ratio_teams = 0
        
        try:
            sh_wins_teams = sh_data["wins_teams"]
        except:
            sh_wins_teams = 0
        
        try:
            sh_losses_teams = sh_data["losses_teams"]
        except:
            sh_losses_teams = 0
        
        try:
            sh_win_loss_ratio_teams = sh_wins_teams / sh_losses_teams
            sh_win_loss_ratio_teams = round(sh_win_loss_ratio_teams, 2)
        except:
            sh_win_loss_ratio_teams = 0
        
        try:
            sh_wins_total = sh_data["wins"]
        except:
            sh_wins_total = 0
        
        try:
            sh_kills_total = sh_data["kills"]
        except:
            sh_kills_total = 0
        
        try:
            sh_coins = sh_data["coins"]
        except:
            sh_coins = 0
        
        try:
            sh_current_class = sh_data["active_class"]
        except:
            sh_current_class = "N/A"
        

        embed=discord.Embed(title = "Smash Heroes Statistics", color=0x0097FF)
        embed.add_field(name = "Solo", value = "Kills: `" + str(separation(sh_kills_normal)) + "`\n" + "Deaths: `" + str(separation(sh_deaths_normal)) + "`\n" +
        "Wins: `" + str(separation(sh_wins_normal)) + "`\n" + "Losses: `" + str(separation(sh_losses_normal)) + "`\n" + "K/D: `" + str(sh_kill_death_ratio_normal) + "`\n" +
        "W/L: `" + str(sh_win_loss_ratio_normal) + "`", inline = True)
        embed.add_field(name = "2v2", value = "Kills: `" + str(separation(sh_kills_2v2)) + "`\n" + "Deaths: `" + str(separation(sh_deaths_2v2)) + "`\n" +
        "Wins: `" + str(separation(sh_wins_2v2)) + "`\n" + "Losses: `" + str(separation(sh_losses_2v2)) + "`\n" + "K/D: `" + str(sh_kill_death_ratio_2v2) + "`\n" +
        "W/L: `" + str(sh_win_loss_ratio_2v2) + "`", inline = True)
        embed.add_field(name = "Teams", value = "Kills: `" + str(separation(sh_kills_teams)) + "`\n" + "Deaths: `" + str(separation(sh_deaths_teams)) + "`\n" +
        "Wins: `" + str(separation(sh_wins_teams)) + "`\n" + "Losses: `" + str(separation(sh_losses_teams)) + "`\n" + "K/D: `" + str(sh_kill_death_ratio_teams) + "`\n" +
        "W/L: `" + str(sh_win_loss_ratio_teams) + "`", inline = True)

        embed.add_field(name = "Smash Level", value = "`" + str(separation(sh_level)) + "`", inline = True)
        embed.add_field(name = "Wins", value = "`" + str(separation(sh_wins_total)) + "`", inline = True)
        embed.add_field(name = "Kills", value = "`" + str(separation(sh_kills_total)) + "`", inline = True)
        embed.add_field(name = "Selected Class", value = "`" + str(sh_current_class) + "`", inline = True)
        embed.add_field(name = "Coins", value = "`" + str(separation(sh_coins)) + "`", inline = False)

        embed.set_image(url = "https://gen.plancke.io/supersmash/" + username + "/2.png" + "?random=" + randomString(10))
        embed.set_author(name = display_name, icon_url = username_icon)
        embed.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/SmashHeroes-64.png")
        embed.set_footer(text= embed_footer)

        await ctx.channel.send(embed=embed)

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def setup(client):
    client.add_cog(smashheroesStats(client))
        
