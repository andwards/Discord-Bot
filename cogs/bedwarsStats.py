import discord
from discord.ext import commands
import requests
import string


class bedwarsStats(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(pass_conext=True, aliases = ["bedwars"])
    async def bw(self, ctx, username: str = None):
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
            bw_data = hypixel_data["player"]["stats"]["Bedwars"]
            display_name = hypixel_data["player"]["displayname"]
        except:
            embed=discord.Embed(title = "Invalid Request", color=0xFF0000)
            embed.add_field(name = "Error", value = "`This player cannot be found on the API`")
            embed.add_field(name = "Correct Useage", value = "`-bw <IGN>`")
            embed.set_footer(text= embed_footer)
            await ctx.channel.send(embed=embed)
            return
        
        try:
            bw_kills = bw_data["kills_bedwars"]
        except:
            bw_kills = 0
        
        try:
            bw_deaths = bw_data["deaths_bedwars"]
        except:
            bw_deaths = 0
        
        try:
            bw_kill_death_ratio = bw_kills / bw_deaths
            bw_kill_death_ratio = round(bw_kill_death_ratio, 2)
        except:
            bw_kill_death_ratio = 0
        
        try:
            bw_final_kills = bw_data["final_kills_bedwars"]
        except:
            bw_final_kills = 0
        
        try:
            bw_final_deaths = bw_data["final_deaths_bedwars"]
        except:
            bw_final_deaths = 0
        
        try:
            bw_final_kill_death_ratio = bw_final_kills / bw_final_deaths
            bw_final_kill_death_ratio = round(bw_final_kill_death_ratio, 2)
        except:
            bw_final_kill_death_ratio = 0
        
        try:
            bw_wins = bw_data["wins_bedwars"]
        except:
            bw_wins = 0
        
        try:
            bw_beds_broken = bw_data["beds_broken_bedwars"]
        except:
            bw_beds_broken = 0
        
        try:
            bw_beds_lost = bw_data["beds_lost_bedwars"]
        except:
            bw_beds_lost = 0
        
        try:
            bw_coins = bw_data["coins"]
        except:
            bw_coins = 0
        
        try:
            bw_level = hypixel_data["player"]["achievements"]["bedwars_level"]
        except:
            bw_level = 0
        

        embed=discord.Embed(title = "Bed Wars Statistics", description = "**Level:** `" + str(separation(bw_level)) + "`", color=0x0097FF)
        embed.add_field(name = "Kills", value = "`" + str(separation(bw_kills)) + "`", inline = True)
        embed.add_field(name = "Deaths", value = "`" + str(separation(bw_deaths)) + "`", inline = True)
        embed.add_field(name = "K/D", value = "`" + str(bw_kill_death_ratio) + "`", inline = True)
        embed.add_field(name = "Final Kills", value = "`" + str(separation(bw_final_kills)) + "`", inline = True)
        embed.add_field(name = "Final Deaths", value = "`" + str(separation(bw_final_deaths)) + "`", inline = True)
        embed.add_field(name = "FK/D", value = "`" + str(bw_final_kill_death_ratio) + "`", inline = True)
        embed.add_field(name = "Wins", value = "`" + str(separation(bw_wins)) + "`", inline = True)
        embed.add_field(name = "Beds", value = "Broken: `" + str(separation(bw_beds_broken)) + "`\n" + "Lost: `" + str(separation(bw_beds_lost)) + "`", inline = True)
        embed.add_field(name = "Coins", value = "`" + str(separation(bw_coins)) + "`", inline = False)

        embed.set_author(name = display_name, icon_url = username_icon)
        embed.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/BedWars-64.png")
        embed.set_footer(text= embed_footer)

        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(bedwarsStats(client))

        
        
