import discord
from discord.ext import commands
import requests
import string


class paintballStats(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(pass_conext=True, aliases = ["paintball"])
    async def pb(self, ctx, username: str = None):
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
            paintball_data = hypixel_data["player"]["stats"]["Paintball"]
            display_name = hypixel_data["player"]["displayname"]
        except:
            embed=discord.Embed(title = "Invalid Request", color=0xFF0000)
            embed.add_field(name = "Error", value = "`This player cannot be found on the API`")
            embed.add_field(name = "Correct Useage", value = "`-pb <IGN>`\n `-paintball <IGN>`")
            embed.set_footer(text= embed_footer)
            await ctx.channel.send(embed=embed)
            return
        
        try:
            paintball_kills = paintball_data["kills"]
        except:
            paintball_kills = 0
        
        try:
            paintball_deaths = paintball_data["deaths"]
        except:
            paintball_deaths = 0
        
        try:
            paintball_kill_death_ratio = paintball_kills / paintball_deaths
            paintball_kill_death_ratio = round(paintball_kill_death_ratio, 2)
        except:
            paintball_kill_death_ratio = 0
        
        try:
            paintball_killstreaks = paintball_data["killstreaks"]
        except:
            paintball_killstreaks = 0
        
        try:
            paintball_shots_fired = paintball_data["shots_fired"]
        except:
            paintball_shots_fired = 0
        
        try:
            paintball_wins = paintball_data["wins"]
        except:
            paintball_wins = 0
        
        try:
            paintball_hat_selected = paintball_data["hat"]
        except:
            paintball_hat_selected = "N/A"
        
        try:
            paintball_godfather_perk = paintball_data["godfather"]
        except:
            paintball_godfather_perk = 0
        
        try:
            paintball_endurance_perk = paintball_data["endurance"]
        except:
            paintball_endurance_perk = 0
        
        try:
            paintball_superluck_perk = paintball_data["superluck"]
        except:
            paintball_superluck_perk = 0
        
        try:
            paintball_fortune_perk = paintball_data["fortune"]
        except:
            paintball_fortune_perk = 0
        
        try:
            paintball_adrenaline_perk = paintball_data["adrenaline"]
        except:
            paintball_adrenaline_perk = 0
        
        try:
            paintball_transfusion_perk = paintball_data["transfusion"]
        except:
            paintball_transfusion_perk = 0
        
        try:
            paintball_headstart_perk = paintball_data["headstart"]
        except:
            paintball_headstart_perk = 0
        
        try:
            paintball_forcefieldtime = paintball_data["forcefieldTime"]
        except:
            paintball_forcefieldtime = 0
        
        try:
            paintball_kill_prefix = paintball_data["selectedKillPrefix"]
        except:
            paintball_kill_prefix = "N/A"
        
        try:
            paintball_coins = paintball_data["coins"]
        except:
            paintball_coins = 0
        

        embed=discord.Embed(title = "Paintball Statistics", color=0x0097FF)
        embed.add_field(name = "Kills", value = "`" + str(separation(paintball_kills) + "`"), inline = True)
        embed.add_field(name = "Deaths", value = "`" + str(separation(paintball_deaths) + "`"), inline = True)
        embed.add_field(name = "K/D Ratio", value = "`" + str(paintball_kill_death_ratio) + "`", inline = True)
        embed.add_field(name = "Wins", value = "`" + str(separation(paintball_wins) + "`"), inline = True)
        embed.add_field(name = "Killstreaks", value = "`" + str(separation(paintball_killstreaks) + "`"), inline = True)
        embed.add_field(name = "Shots Fired", value = "`" + str(separation(paintball_shots_fired) + "`"), inline = True)
        embed.add_field(name = "Perks", value = "Godfather: `" + str(paintball_godfather_perk) + "/50`\n" + "Endurance: `" + str(paintball_endurance_perk) + "/50`\n" + 
        "Superluck: `" + str(paintball_superluck_perk) + "/20`\n" + "Fortune: `" + str(paintball_fortune_perk) + "/20`\n" + 
        "Adrenaline: `" + str(paintball_adrenaline_perk) + "/10`\n" + "Transfusion: `" + str(paintball_transfusion_perk) + "/10`\n" + 
        "Headstart: `" + str(paintball_headstart_perk) + "/5`", inline = True)
        #embed.add_field(name = "Hat Selected", value = "`" + str(paintball_hat_selected) + "`", inline = True)
        embed.add_field(name = "Forcefield Time", value = "`" + str(separation(paintball_forcefieldtime) + " seconds`"), inline = True)
        embed.add_field(name = "Kill Prefix", value = "`" + str(paintball_kill_prefix) + "`", inline = True)
        embed.add_field(name = "Coins", value = "`" + str(separation(paintball_coins) + "`"), inline = True)
        
        embed.set_author(name = display_name, icon_url = username_icon)
        embed.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/Paintball-64.png")
        embed.set_footer(text= embed_footer)

        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(paintballStats(client))
        
