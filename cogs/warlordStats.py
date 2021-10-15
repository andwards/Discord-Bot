import discord
from discord.ext import commands
import requests
import string
import random


class warlordsStats(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(pass_conext=True, aliases = ["warlords"])
    async def wl(self, ctx, username: str = None):
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
            wl_data = hypixel_data["player"]["stats"]["Battleground"]
            display_name = hypixel_data["player"]["displayname"]
        except:
            embed=discord.Embed(title = "Invalid Request", color=0xFF0000)
            embed.add_field(name = "Error", value = "`This player cannot be found on the API`")
            embed.add_field(name = "Correct Useage", value = "`-wl <IGN>`\n `-warlords <IGN>`")
            embed.set_footer(text= embed_footer)
            await ctx.channel.send(embed=embed)
            return
        

        try:
            wl_kills = wl_data["kills"]
        except:
            wl_kills = 0
        
        try:
            wl_deaths = wl_data["deaths"]
        except:
            wl_deaths = 0
        
        try:
            wl_kill_death_ratio = wl_kills / wl_deaths
            wl_kill_death_ratio = round(wl_kill_death_ratio, 2)
        except:
            wl_kill_death_ratio = 0
        
        try:
            wl_wins_CTF = wl_data["wins_capturetheflag"]
        except:
            wl_wins_CTF = 0
        
        try:
            wl_wins_dom = wl_data["wins_domination"]
        except:
            wl_wins_dom = 0
        
        try:
            wl_wins_tdm = wl_data["wins_teamdeathmatch"]
        except:
            wl_wins_tdm = 0
        
        try:
            wl_wins = wl_data["wins"]
        except:
            wl_wins = 0
        
        try:
            wl_assists = wl_data["assists"]
        except:
            wl_assists = 0
        
        try:
            wl_flags_captured = wl_data["flag_conquer_self"]
        except:
            wl_flags_captured = 0
        
        try:
            wl_flags_returned = wl_data["flag_returns"]
        except:
            wl_flags_returned = 0
        
        try:
            wl_magic_dust = wl_data["magic_dust"]
        except:
            wl_magic_dust = 0
        
        try: 
            wl_void_shards = wl_data["void_shards"]
        except:
            wl_void_shards = 0
        
        try:
            wl_coins = wl_data["coins"]
        except:
            wl_coins = 0
        

        embed=discord.Embed(title = "Warlords Statistics", color=0x0097FF)
        embed.add_field(name = "Kills", value = "`" + str(separation(wl_kills) + "`"), inline = True)
        embed.add_field(name = "Deaths", value = "`" + str(separation(wl_deaths) + "`"), inline = True)
        embed.add_field(name = "K/D", value = "`" + str(wl_kill_death_ratio) + "`", inline = True)
        embed.add_field(name = "Wins", value = "CTF: `" + str(separation(wl_wins_CTF)) + "`\n" + "DOM: `" + str(separation(wl_wins_dom)) + "`\n" + 
        "TDM: `" + str(separation(wl_wins_tdm)) + "`\n" + "Total: `" + str(separation(wl_wins)) + "`", inline = True)
        embed.add_field(name = "Flags", value = "Captured: `" + str(separation(wl_flags_captured)) + "`\n" + 
        "Returned: `" + str(separation(wl_flags_returned)) + "`\n", inline = True)
        embed.add_field(name = "Assists", value = "`" + str(separation(wl_assists)) + "`", inline = True)
        
        embed.add_field(name = "Magic Dust", value = "`" + str(separation(wl_magic_dust)) + "`", inline = True)
        embed.add_field(name = "Void Shards", value = "`" + str(separation(wl_void_shards)) + "`", inline = True)
        embed.add_field(name = "Coins", value = "`" + str(separation(wl_coins)) + "`", inline = False)

        embed.set_image(url = "https://gen.plancke.io/warlords/class/" + username + ".png" + "?random=" + randomString(10))
        embed.set_author(name = display_name, icon_url = username_icon)
        embed.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/Warlords-64.png")
        embed.set_footer(text= embed_footer)

        await ctx.channel.send(embed=embed)

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def setup(client):
    client.add_cog(warlordsStats(client))
