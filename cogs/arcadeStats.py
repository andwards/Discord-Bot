import discord
from discord.ext import commands
import requests
import string


class arcadeStats(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(pass_conext=True)
    async def arcade(self, ctx, username: str = None):
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
            arcade_data = hypixel_data["player"]["stats"]["Arcade"]
            display_name = hypixel_data["player"]["displayname"]
        except:
            embed=discord.Embed(title = "Invalid Request", color=0xFF0000)
            embed.add_field(name = "Error", value = "`This player cannot be found on the API`")
            embed.add_field(name = "Correct Useage", value = "`-arcade <IGN>`")
            embed.set_footer(text= embed_footer)
            await ctx.channel.send(embed=embed)
            return
        
        try:
            arcade_holeinwall_wins = arcade_data["wins_hole_in_the_wall"]
        except:
            arcade_holeinwall_wins = 0
        
        try:
            arcade_blockingdead_wins = arcade_data["wins_dayone"]
        except:
            arcade_blockingdead_wins = 0

        try:
            arcade_blockingdead_headshots = arcade_data["headshots_dayone"]
        except:
            arcade_blockingdead_headshots = 0
        
        try:
            arcade_bounty_wins = arcade_data["wins_oneinthequiver"]
        except:
            arcade_bounty_wins = 0
        
        try:
            arcade_bounty_kills = arcade_data["kills_oneinthequiver"]
        except:
            arcade_bounty_kills = 0
        
        try:
            arcade_bounty_bountykills = arcade_data["bounty_kills_oneinthequiver"]
        except:
            arcade_bounty_bountykills = 0
        
        try:
            arcade_creeper_bestwave = arcade_data["max_wave"]
        except:
            arcade_creeper_bestwave = 0
        
        try:
            arcade_dragonwars_wins = arcade_data["wins_dragonwars2"]
        except:
            arcade_dragonwars_wins = 0
        
        try:
            arcade_ender_wins = arcade_data["wins_ender"]
        except:
            arcade_ender_wins = 0
        
        try:
            arcade_farmhunt_wins = arcade_data["wins_farm_hunt"]
        except:
            arcade_farmhunt_wins = 0
        
        try:
            arcade_football_wins = arcade_data["wins_soccer"]
        except:
            arcade_football_wins = 0
        
        try:
            arcade_football_goals = arcade_data["goals_soccer"]
        except:
            arcade_football_goals = 0
        
        try:
            arcade_galaxy_wins = arcade_data["sw_game_wins"]
        except:
            arcade_galaxy_wins = 0
        
        try:
            arcade_hide_in_seek_hider_wins = arcade_data["hider_wins_hide_and_seek"]
        except:
            arcade_hide_in_seek_hider_wins = 0
        
        try:
            arcade_hide_in_week_seeker_wins = arcade_data["seeker_wins_hide_and_seek"]
        except:
            arcade_hide_in_week_seeker_wins = 0
        
        try:
            arcade_hypixel_says_wins = arcade_data["wins_simon_says"]
        except:
            arcade_hypixel_says_wins = 0
        
        try:
            arcade_miniwalls_wins = arcade_data["wins_mini_walls"]
        except:
            arcade_miniwalls_wins = 0
        
        try:
            arcade_party_wins = arcade_data["wins_party"]
        except:
            arcade_party_wins = 0
        
        try:
            arcade_party_2_wins = arcade_data["wins_party_2"]
        except:
            arcade_party_2_wins = 0
        
        try:
            arcade_party_3_wins = arcade_data["wins_party_3"]
        except:
            arcade_party_3_wins = 0
        
        try:
            arcade_party_total_wins = arcade_party_wins + arcade_party_2_wins + arcade_party_3_wins
        except:
            arcade_party_total_wins = 0
        
        try:
            arcade_pixel_painters_wins = arcade_data["wins_draw_their_thing"]
        except:
            arcade_pixel_painters_wins = 0
        
        try:
            arcade_throw_out_wins = arcade_data["wins_throw_out"]
        except:
            arcade_throw_out_wins = 0
        
        try:
            arcade_zombies_wins = arcade_data["wins_zombies"]
        except:
            arcade_zombies_wins = 0
        
        try:
            arcade_coins = arcade_data["coins"]
        except:
            arcade_coins = 0

        embed=discord.Embed(title = "Arcade Statistics", description = "Capture the Wool is not in the API", color=0x0097FF)
        embed.add_field(name = "Blocking Dead", value = "Wins: `" + str(separation(arcade_blockingdead_wins)) + "`", inline = True)
        embed.add_field(name = "Bounty Hunters", value = "Wins: `" + str(separation(arcade_bounty_wins)) + "`", inline = True)

        embed.add_field(name = "Creeper Attack", value = "Best Wave: `" + str(separation(arcade_creeper_bestwave)) + "`", inline = True)
        embed.add_field(name = "Dragon Wars", value = "Wins: `" + str(separation(arcade_dragonwars_wins)) + "`", inline = True)
        embed.add_field(name = "Ender Spleef", value = "Wins: `" + str(separation(arcade_ender_wins)) + "`", inline = True)
        embed.add_field(name = "Farm Hunt", value = "Wins: `" + str(separation(arcade_farmhunt_wins)) + "`", inline = True)
        embed.add_field(name = "Football", value = "Wins: `" + str(separation(arcade_football_wins)) + "`", inline = True)
        embed.add_field(name = "Galaxy Wars", value = "Wins: `" + str(separation(arcade_galaxy_wins)) + "`", inline = True)
        embed.add_field(name = "Hole In The Wall", value = "Wins: `" + str(separation(arcade_holeinwall_wins)) + "`", inline = True)
        embed.add_field(name = "Hypixel Says", value = "Wins: `" + str(separation(arcade_hypixel_says_wins)) + "`", inline = True)
        embed.add_field(name = "Mini Walls", value = "Wins: `" + str(separation(arcade_miniwalls_wins)) + "`", inline = True)
        embed.add_field(name = "Party Games", value = "Wins: `" + str(separation(arcade_party_total_wins)) + "`", inline = True)
        embed.add_field(name = "Pixel Painters", value = "Wins: `" + str(separation(arcade_pixel_painters_wins)) + "`", inline = True)
        embed.add_field(name = "Throw Out", value = "Wins: `" + str(separation(arcade_throw_out_wins)) + "`", inline = True)
        embed.add_field(name = "Zombies", value = "Wins: `" + str(separation(arcade_zombies_wins)) + "`", inline = True)
        embed.add_field(name = "Hide and Seek", value = "Hider Wins: `" + str(separation(arcade_hide_in_seek_hider_wins)) + "`\n" +
        "Seeker Wins: `" + str(separation(arcade_hide_in_week_seeker_wins)) + "`", inline = True)
        embed.add_field(name = "Coins", value = "`" + str(separation(arcade_coins)) + "`", inline = False)

        embed.set_author(name = display_name, icon_url = username_icon)
        embed.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/Arcade-64.png")
        embed.set_footer(text= embed_footer)

        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(arcadeStats(client))

        
        
