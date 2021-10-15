import discord
from discord.ext import commands
import requests
import string
import random


class megawallsStats(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(pass_conext=True, aliases = ["walls3", "megawalls"])
    async def mw(self, ctx, username: str = None):
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
            mw_data = hypixel_data["player"]["stats"]["Walls3"]
            display_name = hypixel_data["player"]["displayname"]
        except:
            embed=discord.Embed(title = "Invalid Request", color=0xFF0000)
            embed.add_field(name = "Error", value = "`This player cannot be found on the API`")
            embed.add_field(name = "Correct Useage", value = "`-mw <IGN>`")
            embed.set_footer(text= embed_footer)
            await ctx.channel.send(embed=embed)
            return


        try:
            mw_prestiges = hypixel_data["player"]["achievements"]["walls3_moctezuma"]
        except:
            mw_prestiges = 0
        
        try:
            mw_wins = mw_data["wins"]
        except:
            mw_wins = 0
        
        try:
            mw_losses = mw_data["losses"]
        except:
            mw_losses = 0
        
        try:
            mw_win_lose_ratio = mw_wins / mw_losses
            mw_win_lose_ratio = round(mw_win_lose_ratio, 2)
        except:
            mw_win_lose_ratio = 0
        
        try:
            mw_kills = mw_data["kills"]
        except:
            mw_kills = 0
        
        try:
            mw_deaths = mw_data["deaths"]
        except:
            mw_deaths = 0

        try:
            mw_kill_death_ratio = mw_kills / mw_deaths
            mw_kill_death_ratio = round(mw_kill_death_ratio, 2)
        except:
            mw_kill_death_ratio = 0
        
        try:
            mw_final_kills = mw_data["final_kills"]
        except:
            mw_final_kills = 0
        
        try:
            mw_final_deaths = mw_data["final_deaths"]
        except:
            mw_final_deaths = 0
        
        try:
            mw_final_deaths_pre = mw_data["finalDeaths"]
        except:
            mw_final_deaths_pre = 0
        
        try: 
            mw_wither_damage = mw_data["wither_damage"]
        except:
            mw_wither_damage = 0

        try:
            mw_coins = mw_data["coins"]
        except:
            mw_coins = 0
        
        try:
            mw_selected_class = mw_data["chosen_class"]
        except:
            mw_selected_class = "N/A"

        try:
            mw_final_deaths_fixed = (mw_final_deaths_pre + mw_final_deaths)
        except:
            mw_final_deaths_fixed = 0

        try:
            mw_final_kill_death_ratio = mw_final_kills / mw_final_deaths_fixed
            mw_final_kill_death_ratio = round(mw_final_kill_death_ratio, 2)
        except:
            mw_final_kill_death_ratio = 0

        try: 
            mw_mythic_favor = mw_data["mythic_favor"]
        except:
            mw_mythic_favor = 0
        
        try:
            mw_hours_wins = mw_wins * 45
            mw_hours_wins = mw_hours_wins / 60
        except:
            mw_hours_wins = 0

        try:
            mw_hours_losses = mw_losses * 45
            mw_hours_losses = mw_hours_losses / 60
        except:
            mw_hours_losses = 0
        
        try:
            mw_playtime = mw_hours_wins + mw_hours_losses
            mw_playtime = round(mw_playtime, 2)
        except:
            mw_playtime = "Error"

        
        embed=discord.Embed(title = "Mega Walls Statistics", color=0x0097FF)
        embed.add_field(name = "Kills", value = "`" + str(separation(mw_kills) + "`"), inline = True)
        embed.add_field(name = "Deaths", value = "`" + str(separation(mw_deaths) + "`"), inline = True)
        embed.add_field(name = "K/D Ratio", value = "`" + str(mw_kill_death_ratio) + "`", inline = True)
        embed.add_field(name = "Final Kills", value = "`" + str(separation(mw_final_kills) + "`"), inline = True)
        embed.add_field(name = "Final Deaths", value = "`" + str(separation(mw_final_deaths_fixed) + "`"), inline = True)
        embed.add_field(name = "FK/D Ratio", value = "`" + str(mw_final_kill_death_ratio) + "`", inline = True)
        embed.add_field(name = "Wins", value = "`" + str(separation(mw_wins) + "`"), inline = True)
        embed.add_field(name = "Losses", value = "`" + str(separation(mw_losses) + "`"), inline = True)
        embed.add_field(name = "W/L Ratio", value = "`" + str(mw_win_lose_ratio) + "`", inline = True)
        embed.add_field(name = "Wither Damage", value = "`" + str(separation(mw_wither_damage) + "`"), inline = True)
        embed.add_field(name = "Coins", value = "`" + str(separation(mw_coins) + "`"), inline = True)

        embed.add_field(name = "Mythic Favor", value = "`" + str(separation(mw_mythic_favor)) + "`")
        embed.add_field(name = "Selected Class", value = "`" + mw_selected_class + "`")
        embed.add_field(name = "Prestiges", value = "`" + str(separation(mw_prestiges)) + "`", inline = True)
        embed.add_field(name = "Estimated Playtime", value = "`" + str(mw_playtime) + " hours`", inline = True)

        embed.set_image(url = "https://gen.plancke.io/mw/" + username + "/2.png" + "?random=" + randomString(10))
        embed.set_author(name = display_name, icon_url = username_icon)
        embed.set_thumbnail(url = "https://hypixel.net/styles/hypixel-uix/hypixel/game-icons/MegaWalls-64.png")
        embed.set_footer(text= embed_footer)

        await ctx.channel.send(embed=embed)

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def setup(client):
    client.add_cog(megawallsStats(client))
