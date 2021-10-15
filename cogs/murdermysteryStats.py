import discord
from discord.ext import commands
import requests
import string


class murdermysteryStats(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(pass_conext=True)
    async def mm(self, ctx, username: str = None):
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
            mm_data = hypixel_data["player"]["stats"]["MurderMystery"]
            display_name = hypixel_data["player"]["displayname"]
        except:
            embed=discord.Embed(title = "Invalid Request", color=0xFF0000)
            embed.add_field(name = "Error", value = "`This player cannot be found on the API`")
            embed.add_field(name = "Correct Useage", value = "`-mm <IGN>`")
            embed.set_footer(text= embed_footer)
            await ctx.channel.send(embed=embed)
            return
        
        try:
            mm_kills = mm_data["kills"]
        except:
            mm_kills = 0
        
        try:
            mm_knife_kills = mm_data["knife_kills"]
        except:
            mm_knife_kills = 0
        
        try:
            mm_bow_kills = mm_data["bow_kills"]
        except:
            mm_bow_kills = 0
        
        try:
            mm_wins = mm_data["wins"]
        except:
            mm_wins = 0
        
        try:
            mm_murderer_wins = mm_data["murderer_wins"]
        except:
            mm_murderer_wins = 0

        try:
            mm_detective_wins = mm_data["detective_wins"]
        except:
            mm_detective_wins = 0
        
        try:
            mm_coins = mm_data["coins"]
        except:
            mm_coins = 0
        
        embed=discord.Embed(title = "Murder Mystery Statistics", color=0x0097FF)
        embed.add_field(name = "Total\nKills", value = "`" + str(separation(mm_kills)) + "`", inline = True)
        embed.add_field(name = "Knife\nKills", value = "`" + str(separation(mm_knife_kills)) + "`", inline = True)
        embed.add_field(name = "Bow\nKills", value = "`" + str(separation(mm_bow_kills)) + "`", inline = True)
        embed.add_field(name = "Total\nWins", value = "`" + str(separation(mm_wins)) + "`", inline = True)
        embed.add_field(name = "Murderer\nWins", value = "`" + str(separation(mm_murderer_wins)) + "`", inline = True)
        embed.add_field(name = "Detective\nWins", value = "`" + str(separation(mm_detective_wins)) + "`", inline = True)
        embed.add_field(name = "Coins", value = "`" + str(separation(mm_coins)) + "`", inline = True)

        embed.set_author(name = display_name, icon_url = username_icon)
        embed.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/MurderMystery-64.png")
        embed.set_footer(text= embed_footer)

        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(murdermysteryStats(client))
