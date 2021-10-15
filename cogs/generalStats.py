import discord
from discord.ext import commands
import requests
import string
import math
import time

class generalStats(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(pass_conext=True, aliases = ["generalstats"])
    async def stats(self, ctx, username: str = None):

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

        # These are just values used to calculate the level
        BASE = 10_000
        GROWTH = 2_500
        REVERSE_PQ_PREFIX = -(BASE - 0.5 * GROWTH) / GROWTH
        REVERSE_CONST = REVERSE_PQ_PREFIX
        GROWTH_DIVIDES_2 = 2 / GROWTH


        try:
            mojang_data = requests.get("https://api.mojang.com/users/profiles/minecraft/" + username).json()
            uuid = mojang_data["id"]
            hypixel_data = requests.get("https://api.hypixel.net/player?key=" + API_KEY + "&uuid=" + uuid).json()
            hypixel_guild = requests.get("https://api.hypixel.net/guild?key=" + API_KEY +  "&player=" + uuid).json()
            slothpixel_data = requests.get("https://api.slothpixel.me/api/players/" + username + "?key=" + API_KEY).json()
            general_data = hypixel_data["player"]["achievements"]
            display_name = hypixel_data["player"]["displayname"]
        except:
            embed=discord.Embed(title = "Invalid Request", color=0xFF0000)
            embed.add_field(name = "Error", value = "`This player cannot be found on the API`")
            embed.add_field(name = "Correct Useage", value = "`-stats <IGN>`")
            embed.set_footer(text= embed_footer)
            await ctx.channel.send(embed=embed)
            return
        
        try:
            general_quests = general_data["general_quest_master"]
        except:
            general_quests = 0
        
        try:
            general_challenges: general_data["general_challenger"]
        except:
            general_challenges = 0
        
        
        try:
            arcade_wins = hypixel_data["player"]["achievements"]["arcade_arcade_winner"]
        except:
            arcade_wins = 0
        try:
            arena_wins = hypixel_data["player"]["stats"]["Arena"]["wins"]
        except:
            arena_wins = 0
        try:
            bw_wins = hypixel_data["player"]["stats"]["Bedwars"]["wins_bedwars"]
        except:
            bw_wins = 0
        try:
            bsg_wins_solo = hypixel_data["player"]["stats"]["HungerGames"]["wins"]
        except:
            bsg_wins_solo = 0
        try:
            bsg_wins_teams = hypixel_data["player"]["stats"]["HungerGames"]["wins_teams"]
        except:
            bsg_wins_teams = 0
        try:
            bb_wins = hypixel_data["player"]["stats"]["BuildBattle"]["wins"]
        except:
            bb_wins = 0
        try:
            cvc_wins_defusal = hypixel_data["player"]["stats"]["MCGO"]["game_wins"]
        except:
            cvc_wins_defusal = 0
        try:
            cvc_wins_tdm = hypixel_data["player"]["stats"]["MCGO"]["game_wins_deathmatch"]
        except:
            cvc_wins_tdm = 0
        try:
            cw_wins = hypixel_data["player"]["stats"]["TrueCombat"]["wins"]
        except:
            cw_wins = 0
        try:
            duel_wins = hypixel_data["player"]["stats"]["Duels"]["wins"]
        except:
            duel_wins = 0
        try:
            mw_wins = hypixel_data["player"]["stats"]["Walls3"]["wins"]
        except:
            mw_wins = 0
        try:
            mm_wins = hypixel_data["player"]["stats"]["MurderMystery"]["wins"]
        except:
            mm_wins = 0
        try:
            pb_wins = hypixel_data["player"]["stats"]["Paintball"]["wins"]
        except:
            pb_wins = 0
        try:
            quake_wins_solo = hypixel_data["player"]["stats"]["Quake"]["wins"]
        except:
            quake_wins_solo = 0
        try:
            quake_wins_teams = hypixel_data["player"]["stats"]["Quake"]["wins_teams"]
        except:
            quake_wins_teams = 0
        try:
            sc_wins = hypixel_data["player"]["stats"]["SkyClash"]["wins"]
        except:
            sc_wins = 0
        try:
            sw_wins = hypixel_data["player"]["stats"]["SkyWars"]["wins"]
        except:
            sw_wins = 0
        try:
            sh_wins = hypixel_data["player"]["stats"]["SuperSmash"]["wins"]
        except:
            sh_wins = 0
        try:
            suhc_wins = hypixel_data["player"]["stats"]["SpeedUHC"]["wins"]
        except:
            suhc_wins = 0
        try:
            tnt_wins_bow = hypixel_data["player"]["stats"]["TNTGames"]["wins_bowspleef"]
        except:
            tnt_wins_bow = 0
        try:
            tnt_wins_wizard = hypixel_data["player"]["stats"]["TNTGames"]["wins_capture"]
        except:
            tnt_wins_wizard = 0
        try:
            tnt_wins_run = hypixel_data["player"]["stats"]["TNTGames"]["wins_tntrun"]
        except:
            tnt_wins_run = 0
        try:
            tnt_wins_pvp = hypixel_data["player"]["stats"]["TNTGames"]["wins_pvprun"]
        except:
            tnt_wins_pvp = 0
        try:
            tnt_wins_tag = hypixel_data["player"]["stats"]["TNTGames"]["wins_tntag"]
        except:
            tnt_wins_tag = 0
        try:
            tkr_wins = hypixel_data["player"]["stats"]["GingerBread"]["gold_trophy"]
        except:
            tkr_wins = 0
        try:
            uhc_wins_solo = hypixel_data["player"]["stats"]["UHC"]["wins_solo"]
        except:
            uhc_wins_solo = 0
        try:
            uhc_wins_teams = hypixel_data["player"]["stats"]["UHC"]["wins"]
        except:
            uhc_wins_teams = 0
        try:
            uhc_wins_redvsblue = hypixel_data["player"]["stats"]["UHC"]["wins_red vs blue"]
        except:
            uhc_wins_redvsblue = 0
        try:
            uhc_wins_nodiamonds = hypixel_data["player"]["stats"]["UHC"]["wins_no diamonds"]
        except:
            uhc_wins_nodiamonds = 0
        try:
            uhc_wins_vanilla_doubles = hypixel_data["player"]["stats"]["UHC"]["wins_vanilla doubles"]
        except:
            uhc_wins_vanilla_doubles = 0
        try:
            uhc_wins_brawl = hypixel_data["player"]["stats"]["UHC"]["wins_brawl"]
        except:
            uhc_wins_brawl = 0
        try:
            uhc_wins_brawl_solo = hypixel_data["player"]["stats"]["UHC"]["wins_solo brawl"]
        except:
            uhc_wins_brawl_solo = 0
        try:
            uhc_wins_brawl_duo = hypixel_data["player"]["stats"]["UHC"]["wins_duo brawl"]
        except:
            uhc_wins_brawl_duo = 0
        try:
            vz_wins_human = hypixel_data["player"]["stats"]["VampireZ"]["human_wins"]
        except:
            vz_wins_human = 0
        try:
            vz_wins_vamp = hypixel_data["player"]["stats"]["VampireZ"]["vampire_wins"]
        except:
            vz_wins_vamp = 0
        try:
            walls_wins = hypixel_data["player"]["stats"]["Walls"]["wins"]
        except:
            walls_wins = 0
        try:
            wl_wins = hypixel_data["player"]["stats"]["Battleground"]["wins"]
        except:
            wl_wins = 0
        
        try:
            tourney_bw_1_wins = hypixel_data["player"]["stats"]["Bedwars"]["tourney_bedwars4s_0_wins_bedwars"]
        except:
            tourney_bw_1_wins = 0
        try:
            tourney_bw_2_wins = hypixel_data["player"]["stats"]["Bedwars"]["tourney_bedwars4s_1_wins_bedwars"]
        except:
            tourney_bw_2_wins = 0
        try:
            tourney_bsg_1_wins = hypixel_data["player"]["stats"]["HungerGames"]["tourney_blitz_duo_0_wins_teams"]
        except:
            tourney_bsg_1_wins = 0
        try:
            tourney_bsg_2_wins = hypixel_data["player"]["stats"]["HungerGames"]["tourney_blitz_duo_1_wins_teams"]
        except:
            tourney_bsg_2_wins = 0
        try:
            tourney_sw_1_wins = hypixel_data["player"]["stats"]["SkyWars"]["tourney_sw_crazy_solo_0_wins"]
        except:
            tourney_sw_1_wins = 0
        try:
            tourney_sw_2_wins = hypixel_data["player"]["stats"]["SkyWars"]["tourney_sw_insane_doubles_0_wins"]
        except:
            tourney_sw_2_wins = 0
        try:
            tourney_cvc_1_wins = hypixel_data["player"]["stats"]["MCGO"]["game_wins_tourney_mcgo_defusal_0"]
        except:
            tourney_cvc_1_wins = 0
        try:
            tourney_cvc_2_wins = hypixel_data["player"]["stats"]["MCGO"]["game_wins_tourney_mcgo_defusal_1"]
        except:
            tourney_cvc_2_wins = 0
        try:
            tourney_quake_1_wins = hypixel_data["player"]["stats"]["Quake"]["wins_solo_tourney"]
        except:
            tourney_quake_1_wins = 0
        try:
            tourney_tkr_1_wins = hypixel_data["player"]["stats"]["GingerBread"]["tourney_gingerbread_solo_0_wins"]
        except:
            tourney_tkr_1_wins = 0
        try:
            tourney_arcade_1_wins = hypixel_data["player"]["stats"]["Arcade"]["wins_grinch_simulator_v2_tourney"]
        except:
            tourney_arcade_1_wins = 0

        bsg_wins = bsg_wins_solo + bsg_wins_teams
        cvc_wins = cvc_wins_tdm + cvc_wins_defusal
        vz_wins = vz_wins_vamp + vz_wins_human
        quake_wins = quake_wins_solo + quake_wins_teams
        tnt_wins = tnt_wins_bow + tnt_wins_run + tnt_wins_pvp + tnt_wins_tag + tnt_wins_wizard
        uhc_wins = uhc_wins_solo + uhc_wins_teams + uhc_wins_nodiamonds + uhc_wins_redvsblue + uhc_wins_vanilla_doubles + uhc_wins_brawl + uhc_wins_brawl_solo + uhc_wins_brawl_duo
        tourney_wins = tourney_bw_1_wins + tourney_bw_2_wins + tourney_bsg_1_wins + tourney_bsg_2_wins + tourney_sw_1_wins + tourney_sw_2_wins + tourney_cvc_1_wins + tourney_cvc_2_wins + tourney_quake_1_wins + tourney_tkr_1_wins + tourney_arcade_1_wins
    
        total_wins = arcade_wins + arena_wins + bw_wins + bsg_wins + bb_wins + cvc_wins + cw_wins + duel_wins + mw_wins + mm_wins + pb_wins + quake_wins + sc_wins + sw_wins + sh_wins + suhc_wins + tnt_wins + tkr_wins + uhc_wins + vz_wins + walls_wins + wl_wins + tourney_wins
        
        try:
            arcade_quiver_kills = hypixel_data["player"]["achievements"]["arcade_bounty_hunter"]
        except:
            arcade_quiver_kills = 0
        try:
            arcade_dragon_kills = hypixel_data["player"]["stats"]["Arcade"]["kills_dragonwars2"]
        except:
            arcade_dragon_kills = 0
        try:
            arcade_throwout_kills = hypixel_data["player"]["stats"]["Arcade"]["kills_throw_out"]
        except:
            arcade_throwout_kills = 0
        try:
            arcade_sw_kills = hypixel_data["player"]["stats"]["Arcade"]["sw_kills"]
        except:
            arcade_sw_kills = 0
        try:
            arcade_miniwalls_kills = hypixel_data["player"]["stats"]["Arcade"]["kills_mini_walls"]
        except:
            arcade_miniwalls_kills = 0
        try:
            arcade_miniwalls_fkills = hypixel_data["player"]["stats"]["Arcade"]["final_kills_mini_walls"]
        except:
            arcade_miniwalls_fkills = 0
        try:
            arcade_hide_and_seek_kills = hypixel_data["player"]["achievements"]["arcade_hide_and_seek_hider_kills"]
        except:
            arcade_hide_and_seek_kills = 0
        try:
            arcade_ctw_kills = hypixel_data["player"]["achievements"]["arcade_ctw_slayer"]
        except:
            arcade_ctw_kills = 0
        try:
            arena_kills = hypixel_data["player"]["achievements"]["arena_bossed"]
        except:
            arena_kills = 0
        try:
            bw_kills_normal = hypixel_data["player"]["stats"]["Bedwars"]["kills_bedwars"]
        except:
            bw_kills_normal = 0
        try:
            bw_kills_final = hypixel_data["player"]["stats"]["Bedwars"]["final_kills_bedwars"]
        except:
            bw_kills_final = 0
        try:
            bsg_kills = hypixel_data["player"]["stats"]["HungerGames"]["kills"]
        except:
            bsg_kills = 0
        try:
            cvc_kills = hypixel_data["player"]["achievements"]["copsandcrims_serial_killer"]
        except:
            cvc_kills = 0
        try:
            cw_kills = hypixel_data["player"]["stats"]["TrueCombat"]["kills"]
        except:
            cw_kills = 0
        try:
            duel_kills = hypixel_data["player"]["stats"]["Duels"]["kills"]
        except:
            duel_kills = 0
        try:
            mw_kills_normal = hypixel_data["player"]["stats"]["Walls3"]["kills"]
        except:
            mw_kills_normal = 0
        try:
            mw_kills_final = hypixel_data["player"]["stats"]["Walls3"]["final_kills"]
        except:
            mw_kills_final = 0
        try:
            mm_kills = hypixel_data["player"]["stats"]["MurderMystery"]["kills"]
        except:
            mm_kills = 0
        try:
            pb_kills = hypixel_data["player"]["stats"]["Paintball"]["kills"]
        except:
            pb_kills = 0
        try:
            quake_kills = hypixel_data["player"]["stats"]["Quake"]["kills"]
        except:
            quake_kills = 0
        try:
            sc_kills = hypixel_data["player"]["stats"]["SkyClash"]["kills"]
        except:
            sc_kills = 0
        try:
            sw_kills = hypixel_data["player"]["stats"]["SkyWars"]["kills"]
        except:
            sw_kills = 0
        try:
            sh_kills = hypixel_data["player"]["stats"]["SuperSmash"]["kills"]
        except:
            sh_kills = 0
        try:
            suhc_kills = hypixel_data["player"]["stats"]["SpeedUHC"]["kills"]
        except:
            suhc_kills = 0
        try:
            tnt_kills_capture = hypixel_data["player"]["stats"]["TNTGames"]["kills_capture"]
        except:
            tnt_kills_capture = 0
        try:
            tnt_kills_pvp = hypixel_data["player"]["stats"]["TNTGames"]["kills_pvprun"]
        except:
            tnt_kills_pvp = 0
        try:
            uhc_kills_normal = hypixel_data["player"]["stats"]["UHC"]["kills"]
        except:
            uhc_kills_normal = 0
        try:
            uhc_kills_redvsblue = hypixel_data["player"]["stats"]["UHC"]["kills_red vs blue"]
        except:
            uhc_kills_redvsblue = 0
        try:
            uhc_kills_nodiamonds = hypixel_data["player"]["stats"]["UHC"]["kills_no diamonds"]
        except:
            uhc_kills_nodiamonds = 0
        try:
            uhc_kills_vanilla_doubles = hypixel_data["player"]["stats"]["UHC"]["kills_vanilla doubles"]
        except:
            uhc_kills_vanilla_doubles = 0
        try:
            uhc_kills_brawl = hypixel_data["player"]["stats"]["UHC"]["kills_brawl"]
        except:
            uhc_kills_brawl = 0
        try:
            uhc_kills_brawl_solo = hypixel_data["player"]["stats"]["UHC"]["kills_solo brawl"]
        except:
            uhc_kills_brawl_solo = 0
        try:
            uhc_kills_brawl_duo = hypixel_data["player"]["stats"]["UHC"]["kills_duo_brawl"]
        except:
            uhc_kills_brawl_duo = 0
        try:
            vz_kills = hypixel_data["player"]["stats"]["VampireZ"]["human_kills"]
        except:
            vz_kills = 0
        try:
            walls_kills = hypixel_data["player"]["stats"]["Walls"]["kills"]
        except:
            walls_kills = 0
        try:
            wl_kills = hypixel_data["player"]["stats"]["Battleground"]["kills"]
        except:
            wl_kills = 0
        try:
            pit_kills = hypixel_data["player"]["achievements"]["pit_kills"]
        except:
            pit_kills = 0
        try:
            tourney_bw_1_kills = hypixel_data["player"]["stats"]["Bedwars"]["tourney_bedwars4s_0_kills_bedwars"]
        except:
            tourney_bw_1_kills = 0
        try:
            tourney_bw_1_fkills = hypixel_data["player"]["stats"]["Bedwars"]["tourney_bedwars4s_0_final_kills_bedwars"]
        except:
            tourney_bw_1_fkills = 0
        try:
            tourney_bw_2_kills = hypixel_data["player"]["stats"]["Bedwars"]["tourney_bedwars4s_1_kills_bedwars"]
        except:
            tourney_bw_2_kills = 0
        try:
            tourney_bw_2_fkills = hypixel_data["player"]["stats"]["Bedwars"]["tourney_bedwars4s_1_final_kills_bedwars"]
        except:
            tourney_bw_2_fkills = 0
        try:
            tourney_bsg_1_kills = hypixel_data["player"]["stats"]["HungerGames"]["tourney_blitz_duo_0_kills"]
        except:
            tourney_bsg_1_kills = 0
        try:
            tourney_bsg_2_kills = hypixel_data["player"]["stats"]["HungerGames"]["tourney_blitz_duo_1_kills"]
        except:
            tourney_bsg_2_kills = 0
        try:
            tourney_sw_1_kills = hypixel_data["player"]["stats"]["SkyWars"]["tourney_sw_crazy_solo_0_kills"]
        except:
            tourney_sw_1_kills = 0
        try:
            tourney_sw_2_kills = hypixel_data["player"]["stats"]["SkyWars"]["tourney_sw_insane_doubles_0_kills"]
        except:
            tourney_sw_2_kills = 0
        try:
            tourney_cvc_1_kills = hypixel_data["player"]["stats"]["MCGO"]["kills_tourney_mcgo_defusal_0"]
        except:
            tourney_cvc_1_kills = 0
        try:
            tourney_cvc_2_kills = hypixel_data["player"]["stats"]["MCGO"]["kills_tourney_mcgo_defusal_1"]
        except:
            tourney_cvc_2_kills = 0
        try:
            tourney_quake_1_kills = hypixel_data["player"]["stats"]["Quake"]["kills_solo_tourney"]
        except:
            tourney_quake_1_kills = 0
            
            
        arcade_kills = arcade_ctw_kills + arcade_dragon_kills + arcade_miniwalls_fkills + arcade_miniwalls_kills + arcade_hide_and_seek_kills + arcade_quiver_kills + arcade_sw_kills + arcade_throwout_kills
        bw_kills = bw_kills_normal + bw_kills_final
        tnt_kills = tnt_kills_capture + tnt_kills_pvp
        uhc_kills = uhc_kills_normal + uhc_kills_nodiamonds + uhc_kills_redvsblue + uhc_kills_brawl + uhc_kills_brawl_solo + uhc_kills_brawl_duo + uhc_kills_vanilla_doubles
        mw_kills = mw_kills_normal + mw_kills_final
        tourney_kills = tourney_bw_1_kills + tourney_bw_1_fkills + tourney_bw_2_kills + tourney_bw_2_fkills + tourney_bsg_1_kills + tourney_bsg_2_kills + tourney_sw_1_kills + tourney_sw_2_kills + tourney_cvc_1_kills + tourney_cvc_2_kills + tourney_quake_1_kills

        total_kills = pit_kills + arcade_kills + arena_kills + bw_kills + bsg_kills + cvc_kills + cw_kills + duel_kills + mw_kills + mm_kills + pb_kills + quake_kills + sc_kills + sw_kills + sh_kills + suhc_kills + tnt_kills + uhc_kills + vz_kills + walls_kills + wl_kills + tourney_kills
        
        try:
            arcade_coins = hypixel_data["player"]["stats"]["Arcade"]["coins"]
        except:
            arcade_coins = 0
        try:
            arena_coins = hypixel_data["player"]["stats"]["Arena"]["coins"]
        except:
            arena_coins = 0
        try:
            bw_coins = hypixel_data["player"]["stats"]["Bedwars"]["coins"]
        except:
            bw_coins = 0
        try:
            bsg_coins = hypixel_data["player"]["stats"]["HungerGames"]["coins"]
        except:
            bsg_coins = 0
        try:
            bb_coins = hypixel_data["player"]["stats"]["BuildBattle"]["coins"]
        except:
            bb_coins = 0
        try:
            cvc_coins = hypixel_data["player"]["stats"]["MCGO"]["coins"]
        except:
            cvc_coins = 0
        try:
            cw_coins = hypixel_data["player"]["stats"]["TrueCombat"]["coins"]
        except:
            cw_coins = 0
        try:
            duel_coins = hypixel_data["player"]["stats"]["Duels"]["coins"]
        except:
            duel_coins = 0
        try:
            mw_coins = hypixel_data["player"]["stats"]["Walls3"]["coins"]
        except:
            mw_coins = 0
        try:
            mm_coins = hypixel_data["player"]["stats"]["MurderMystery"]["coins"]
        except:
            mm_coins = 0
        try:
            pb_coins = hypixel_data["player"]["stats"]["Paintball"]["coins"]
        except:
            pb_coins = 0
        try:
            quake_coins = hypixel_data["player"]["stats"]["Quake"]["coins"]
        except:
            quake_coins = 0
        try:
            sc_coins = hypixel_data["player"]["stats"]["SkyClash"]["coins"]
        except:
            sc_coins = 0
        try:
            sw_coins = hypixel_data["player"]["stats"]["SkyWars"]["coins"]
        except:
            sw_coins = 0
        try:
            sh_coins = hypixel_data["player"]["stats"]["SuperSmash"]["coins"]
        except:
            sh_coins = 0
        try:
            suhc_coins = hypixel_data["player"]["stats"]["SpeedUHC"]["coins"]
        except:
            suhc_coins = 0
        try:
            tnt_coins = hypixel_data["player"]["stats"]["TNTGames"]["coins"]
        except:
            tnt_coins = 0
        try:
            tkr_coins = hypixel_data["player"]["stats"]["GingerBread"]["coins"]
        except:
            tkr_coins = 0
        try:
            uhc_coins = hypixel_data["player"]["stats"]["UHC"]["coins"]
        except:
            uhc_coins = 0
        try:
            vz_coins = hypixel_data["player"]["stats"]["VampireZ"]["coins"]
        except:
            vz_coins = 0
        try:
            walls_coins = hypixel_data["player"]["stats"]["Walls"]["coins"]
        except:
            walls_coins = 0
        try:
            wl_coins = hypixel_data["player"]["stats"]["Battleground"]["coins"]
        except:
            wl_coins = 0
            
        
        total_coins = arcade_coins + arena_coins + bw_coins + bsg_coins + bb_coins + cvc_coins + cw_coins + duel_coins + mw_coins + mm_coins + pb_coins + quake_coins + sc_coins + sw_coins + sh_coins + suhc_coins + tnt_coins + tkr_coins + uhc_coins + vz_coins + walls_coins + wl_coins
        total_coins = round(total_coins)
        
        try:
            general_achievement_points = hypixel_data["player"]["achievementPoints"]
        except:
            general_achievement_points = 0
        
        try:
            general_rank =  slothpixel_data["rank"]
            if general_rank == "MVP_PLUS_PLUS":
                general_rank = "MVP++"
            if general_rank == "MVP_PLUS":
                general_rank = "MVP+"
            if general_rank == "VIP_PLUS":
                general_rank = "VIP+"
            if general_rank == "GAME_MASTER":
                general_rank = "Game Master"
        except:
            general_rank = "None"
        
        try:
            general_guild = hypixel_guild["guild"]["name"]
        except:
            general_guild = "N/A"
        
        try:
            general_karma = hypixel_data["player"]["karma"]
        except:
            general_karma = 0
        
        try:
            general_level = hypixel_data["player"]["networkExp"]
            general_level = math.floor(1 + REVERSE_PQ_PREFIX + math.sqrt(REVERSE_CONST + GROWTH_DIVIDES_2 * general_level))
        except:
            general_level = 0
        
        try:
            general_firstlogin = slothpixel_data["first_login"]
            general_firstlogin = round(general_firstlogin / 1000)
        except:
            general_firstlogin = "NULL"
    

        embed=discord.Embed(title = "General Statistics", color=0x0097FF)
        embed.add_field(name = "Rank", value = "`" + str(general_rank) + "`", inline = True)
        embed.add_field(name = "Level", value = "`" + str(separation(general_level) + "`"), inline = True)
        embed.add_field(name = "Guild", value = "`" + general_guild + "`", inline = True)
        embed.add_field(name = "Karma", value = "`" + str(separation(general_karma) + "`"), inline = True)
        embed.add_field(name = "Achievement Points", value = "`" + str(separation(general_achievement_points) + "`"), inline = True)
        embed.add_field(name = "Quests", value = "`" + str(separation(general_quests) + "`"), inline = True)
        embed.add_field(name = "Total Wins", value = "`" + str(separation(total_wins) + "`"), inline = True)
        embed.add_field(name = "Total Kills", value = "`" + str(separation(total_kills) + "`"), inline = True)
        embed.add_field(name = "Total Current Coins", value = "`" + str(separation(total_coins) + "`"), inline = True)

        embed.add_field(name = "First Login", value = "<t:" + str(general_firstlogin) + ">", inline = True)

        embed.set_author(name = display_name, icon_url = username_icon)
        embed.set_thumbnail(url = "https://minotar.net/body/" + str(username) + "/100.png")
        embed.set_footer(text= embed_footer)

        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(generalStats(client))


