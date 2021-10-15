import discord
from discord.ext import commands
import requests
import string


class skywarsStats(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(pass_conext=True, aliases = ["skywars"])
    async def sw(self, ctx, username: str = None):
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
            slothpixel_data = requests.get("https://api.slothpixel.me/api/players/" + username + "?key=" + API_KEY).json()
            sw_data = hypixel_data["player"]["stats"]["SkyWars"]
            display_name = hypixel_data["player"]["displayname"]
        except:
            embed=discord.Embed(title = "Invalid Request", color=0xFF0000)
            embed.add_field(name = "Error", value = "`This player cannot be found on the API`")
            embed.add_field(name = "Correct Useage", value = "`-sw <IGN>`")
            embed.set_footer(text= embed_footer)
            await ctx.channel.send(embed=embed)
            return
        
        try:
            sw_kills = sw_data["kills"]
        except:
            sw_kills = 0
        
        try:
            sw_deaths = sw_data["deaths"]
        except:
            sw_deaths = 0
        
        try:
            sw_kill_death_ratio = sw_kills / sw_deaths
            sw_kill_death_ratio = round(sw_kill_death_ratio, 2)
        except:
            sw_kill_death_ratio = 0
        
        try:
            sw_wins = sw_data["wins"]
        except:
            sw_wins = 0
        
        try:
            sw_souls = sw_data["souls"]
        except:
            sw_souls = 0
        
        try:
            sw_heads = sw_data["heads"]
        except:
            sw_heads = 0
        
        try:
            sw_level = slothpixel_data["stats"]["SkyWars"]["level"]
            sw_level = round(sw_level, 2)
        except:
            sw_level = 0
        
        try:
            sw_opals = hypixel_data["player"]["achievements"]["skywars_opal_obsession"]
        except:
            sw_opals = 0
        
        try:
            sw_shards = sw_data["shard"]
        except:
            sw_shards = 0
        
        try:
            sw_coins = sw_data["coins"]
        except:
            sw_coins = 0
        

        embed=discord.Embed(title = "Skywars Statistics", description = "**Level:** `" + str(sw_level) + "`", color=0x0097FF)
        embed.add_field(name = "Kills", value = "`" + str(separation(sw_kills)) + "`", inline = True)
        embed.add_field(name = "Deaths", value = "`" + str(separation(sw_deaths)) + "`", inline = True)
        embed.add_field(name = "K/D", value = "`" + str(sw_kill_death_ratio) + "`", inline = True)
        embed.add_field(name = "Wins", value = "`" + str(separation(sw_wins)) + "`", inline = True)
        embed.add_field(name = "Souls", value = "`" + str(separation(sw_souls)) + "`", inline = True)
        embed.add_field(name = "Heads", value = "`" + str(separation(sw_heads)) + "`", inline = True)
        embed.add_field(name = "Opals", value = "`" + str(separation(sw_opals)) + "`", inline = True)
        embed.add_field(name = "Shards", value = "`" + str(separation(sw_shards)) + "`", inline = True)
        embed.add_field(name = "Coins", value = "`" + str(separation(sw_coins)) + "`", inline = False)

        embed.set_author(name = display_name, icon_url = username_icon)
        embed.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/Skywars-64.png")
        embed.set_footer(text= embed_footer)

        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(skywarsStats(client))

        
