import discord
from discord.ext import commands
import requests
import string


class turbokartracersStats(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(pass_conext=True, aliases = ["turbokartracers"])
    async def tkr(self, ctx, username: str = None):
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
            tkr_data = hypixel_data["player"]["stats"]["GingerBread"]
            display_name = hypixel_data["player"]["displayname"]
        except:
            embed=discord.Embed(title = "Invalid Request", color=0xFF0000)
            embed.add_field(name = "Error", value = "`This player cannot be found on the API`")
            embed.add_field(name = "Correct Useage", value = "`-tkr <IGN>`\n `-turbokartracers <IGN>`")
            embed.set_footer(text= embed_footer)
            await ctx.channel.send(embed=embed)
            return
        
        try:
            tkr_gold = tkr_data["gold_trophy"]
        except:
            tkr_gold = 0
        
        try:
            tkr_silver = tkr_data["silver_trophy"]
        except:
            tkr_silver = 0
        
        try:
            tkr_bronze = tkr_data["bronze_trophy"]
        except:
            tkr_bronze = 0
        
        try:
            tkr_wins = tkr_data["wins"]
        except:
            tkr_wins = 0
        
        try:
            tkr_box_pickup = tkr_data["box_pickups"]
        except:
            tkr_box_pickup = 0
        
        try:
            tkr_laps = tkr_data["laps_completed"]
        except:
            tkr_laps = 0
        
        try:
            tkr_coins = tkr_data["coins"]
        except:
            tkr_coins = 0
        
        embed=discord.Embed(title = "Turbo Kart Racers Statistics", color=0x0097FF)
        embed.add_field(name = "Trophies", value = "Gold: `" + str(separation(tkr_gold)) + "`\n" + "Silver: `"  + str(separation(tkr_silver)) + "`\n" + 
        "Bronze: `" + str(tkr_bronze) + "`\n" + "Total: `" + str(separation(tkr_wins)) + "`\n", inline = True)
        embed.add_field(name = "Laps", value = "`" + str(separation(tkr_laps) + "`"), inline = True)
        embed.add_field(name = "Boxes", value = "`" + str(separation(tkr_box_pickup) + "`"), inline = True)
        embed.add_field(name = "Coins", value = "`" + str(separation(tkr_coins) + "`"), inline = True)

        embed.set_author(name = display_name, icon_url = username_icon)
        embed.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/TurboKartRacers-64.png")
        embed.set_footer(text= embed_footer)

        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(turbokartracersStats(client))
