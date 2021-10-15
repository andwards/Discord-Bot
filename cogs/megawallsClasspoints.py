import discord
from discord.ext import commands
import requests
import string


class megawallsClasspoints(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(pass_conext=True, aliases = ["classpoints"])
    async def cp(self, ctx, username: str = None):
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
            embed.add_field(name = "Correct Useage", value = "`-cp <IGN>` \n `-classpoints <IGN>`")
            embed.set_footer(text= embed_footer)
            await ctx.channel.send(embed=embed)
            return
        
        embed=discord.Embed(title = "Mega Walls Class Points", color=0x0097FF)
        mw_class_points_total = 0

        mwClasses = ["cow", "hunter", "shark", "dreadlord", "golem", "herobrine", "pigman", "zombie", "arcanist", "shaman", "squid", "enderman", "blaze", "skeleton", "spider", "pirate", "creeper", "assassin", "werewolf", "phoenix", "automaton", "moleman", "renegade", "snowman"]
        for x in mwClasses:
            try:
                mw_class_wins_cp = mw_data[x + "_wins_standard"]
            except:
                mw_class_wins_cp = 0
        
            try:
                mw_class_fks_cp = mw_data[x + "_final_kills_standard"]
            except:
                mw_class_fks_cp = 0
        
            try:
                mw_class_assistS_cp = mw_data[x + "_final_assists_standard"]
            except:
                mw_class_assistS_cp = 0
            
            mw_class_wins_cp = mw_class_wins_cp * 10
            mw_class_fksassists_cp = mw_class_fks_cp + mw_class_assistS_cp
            mw_class_points = mw_class_wins_cp + mw_class_fksassists_cp

            mw_class_points_total = mw_class_points_total + mw_class_points
            embed.add_field(name = x.capitalize(), value = "`" + str(separation(mw_class_points) + "`"), inline = True)
        
        embed.add_field(name = "Total Class Points", value = "`" + str(separation(mw_class_points_total) + "`"), inline = False)

        embed.set_author(name = display_name, icon_url = username_icon)
        embed.set_thumbnail(url = "https://hypixel.net/styles/hypixel-uix/hypixel/game-icons/MegaWalls-64.png")
        embed.set_footer(text= embed_footer)

        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(megawallsClasspoints(client))

        
