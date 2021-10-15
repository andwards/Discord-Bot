import discord
from discord.ext import commands
import requests
import string

class vampirezStats(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(pass_conext=True, aliases = ["vampirez"])
    async def vz(self, ctx, username: str = None):
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
            vz_data = hypixel_data["player"]["stats"]["VampireZ"]
            display_name = hypixel_data["player"]["displayname"]
        except:
            embed=discord.Embed(title = "Invalid Request", color=0xFF0000)
            embed.add_field(name = "Error", value = "`This player cannot be found on the API`")
            embed.add_field(name = "Correct Useage", value = "`-vz <IGN>`")
            embed.set_footer(text= embed_footer)
            await ctx.channel.send(embed=embed)
            return
        
        try:
            vz_human_wins = vz_data["human_wins"]
        except:
            vz_human_wins = 0

        try:
            vz_human_kills = vz_data["human_kills"]
        except:
            vz_human_kills = 0
        
        try:
            vz_human_deaths = vz_data["human_deaths"]
        except:
            vz_human_deaths = 0
        
        try:
            vz_vampire_wins = vz_data["vampire_wins"]
        except:
            vz_vampire_wins = 0

        try:
            vz_vampire_kills = vz_data["vampire_kills"]
        except:
            vz_vampire_kills = 0
        
        try:
            vz_vampire_deaths = vz_data["vampire_deaths"]
        except:
            vz_human_deaths = 0
        
        try:
            vz_zombie_kills = vz_data["zombie_kills"]
        except:
            vz_zombie_kills = 0
        
        try:
            vz_coins = vz_data["coins"]
        except:
            vz_coins = 0
        

        embed=discord.Embed(title = "VampireZ Statistics", color=0x0097FF)
        embed.add_field(name = "Human", value = "Wins: `" + str(separation(vz_human_wins) + "`\n" + "Kills: `" + str(separation(vz_human_kills) + "`\n" + 
        "Deaths: `" + str(separation(vz_human_deaths) + "`"))), inline = True)
        embed.add_field(name = "Vampire", value = "Wins: `" + str(separation(vz_vampire_wins) + "`\n" + "Kills: `" + str(separation(vz_vampire_kills) + "`\n" +
         "Deaths: `" + str(separation(vz_vampire_deaths) + "`"))), inline = True)
        embed.add_field(name = "Zombie Kills", value = "`" + str(separation(vz_zombie_kills) + "`"), inline = False)
        embed.add_field(name = "Coins", value = "`" + str(separation(vz_coins) + "`"), inline = True)

        embed.set_author(name = display_name, icon_url = username_icon)
        embed.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/VampireZ-64.png")
        embed.set_footer(text= embed_footer)

        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(vampirezStats(client))
            
