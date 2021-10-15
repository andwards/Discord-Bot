import discord
from discord.ext import commands
from discord.ext.commands.errors import ExpectedClosingQuoteError
import requests
import string


class buildbattleStats(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(pass_conext=True, aliases = ["buildbattle"])
    async def bb(self, ctx, username: str = None):
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
            bb_data = hypixel_data["player"]["stats"]["BuildBattle"]
            display_name = hypixel_data["player"]["displayname"]
        except:
            embed=discord.Embed(title = "Invalid Request", color=0xFF0000)
            embed.add_field(name = "Error", value = "`This player cannot be found on the API`")
            embed.add_field(name = "Correct Useage", value = "`-bb <IGN>`\n `-buildbattle <IGN>`")
            embed.set_footer(text= embed_footer)
            await ctx.channel.send(embed=embed)
            return
        
        try:
            bb_score = bb_data["score"]
        except:
            bb_score = 0
        
        try:
            bb_solo_wins = bb_data["wins_solo_normal"]
        except:
            bb_solo_wins = 0
        
        try:
            bb_teams_wins = bb_data["wins_teams_normal"]
        except:
            bb_teams_wins = 0
        
        try:
            bb_pro_wins = bb_data["wins_solo_pro"]
        except:
            bb_pro_wins = 0
        
        try:
            bb_gtb_wins = bb_data["wins_guess_the_build"]
        except:
            bb_gtb_wins = 0
        
        try:
            bb_wins_total = bb_data["wins"]
        except:
            bb_wins_total = 0
        
        try:
            bb_games_played = bb_data["games_played"]
        except:
            bb_games_played = 0
        
        try:
            bb_selected_hat = bb_data["new_selected_hat"]
        except:
            bb_selected_hat = "N/A"
        
        try:
            bb_coins = bb_data["coins"]
        except:
            bb_coins = 0
        
        embed=discord.Embed(title = "Build Battle Statistics", description = "**Score:** `" + str(separation(bb_score)) + "`", color=0x0097FF)
        embed.add_field(name = "Wins", value = "`Solo` → `" + str(separation(bb_solo_wins)) + "`\n" + "`Teams` → `" + str(separation(bb_teams_wins)) + "`\n" + 
        "`Pro` → `" + str(separation(bb_solo_wins)) + "`\n" + "`GTB` → `" + str(separation(bb_gtb_wins)) + "`\n" + "`Total` → `" + str(separation(bb_wins_total)) + "`\n", inline = True)
        embed.add_field(name = "Games Played", value = "`" + str(separation(bb_games_played)) + "`", inline = True)
        embed.add_field(name = "Hat Selected", value = "`" + str(bb_selected_hat) + "`", inline = False)
        embed.add_field(name = "Coins", value = "`" + str(separation(bb_coins)) + "`", inline = False)

        embed.set_author(name = display_name, icon_url = username_icon)
        embed.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/BuildBattle-64.png")
        embed.set_footer(text= embed_footer)

        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(buildbattleStats(client))
