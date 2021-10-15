import discord
from discord.ext import commands
import requests
import string
import nbt
import io
import base64

def xptoLevel(arr, xp):
    i = 0
    maxLvl = len(arr) - 1

    if (xp >= arr[maxLvl]):
        return maxLvl

    if (xp <= arr[0]):
        return 0

    while arr[i] < xp:
           i += 1
    
    return i - 1

def decode_inventory_data(raw):
   data = nbt.nbt.NBTFile(fileobj = io.BytesIO(base64.b64decode(raw)))
   print(data.pretty_tree())

# Unfinished - WIP
class skyblockStats(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_conext=True, aliases = ["skyblock"])
    async def sb(self, ctx, username: str = None):
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
            skyblock_data = requests.get("https://api.hypixel.net/skyblock/profiles?key=" + API_KEY + "&uuid=" + uuid).json()
            display_name = hypixel_data["player"]["displayname"]
        except:
            embed=discord.Embed(title = "Invalid Request", color=0xFF0000)
            embed.add_field(name = "Error", value = "`This player cannot be found on the API`")
            embed.add_field(name = "Correct Useage", value = "`-sb <IGN>`\n `-skyblock <IGN>`")
            embed.set_footer(text= embed_footer)
            await ctx.channel.send(embed=embed)
            return
        
        i = 0

        while i < 5:
            try:
                sb_profile_id = skyblock_data["profiles"][i]["profile_id"]
            except:
                sb_profile_id = 0
                break
            
            try:
                sb_last_save = skyblock_data["profiles"][i]["members"][uuid]["last_save"]
            except:
                sb_last_save = 0

            if i == 0:
                sb_current = sb_last_save
                sb_id = sb_profile_id
                sb_id_place = i

            if sb_last_save > sb_current:
                sb_current = sb_last_save
                sb_id = sb_profile_id
                sb_id_place = i

            i += 1
        
        sb_data = skyblock_data["profiles"][sb_id_place]["members"][uuid]

        try:
           sb_cute_name = skyblock_data["profiles"][sb_id_place]["cute_name"]
        except:
           sb_cute_name = "N/A"
        
        try:
            sb_mining_skill_xp = sb_data["experience_skill_mining"]
            sb_mining_skill_xp = round(sb_mining_skill_xp)
        except:
            sb_mining_skill_xp = 0
        
        try:
            sb_foraging_skill_xp = sb_data["experience_skill_foraging"]
            sb_foraging_skill_xp = round(sb_foraging_skill_xp)
        except:
            sb_foraging_skill_xp = 0
        
        try:
            sb_enchanting_skill_xp = sb_data["experience_skill_enchanting"]
            sb_enchanting_skill_xp = round(sb_enchanting_skill_xp)
        except:
            sb_enchanting_skill_xp = 0
        
        try:
            sb_farming_skill_xp = sb_data["experience_skill_farming"]
            sb_farming_skill_xp = round(sb_farming_skill_xp)
        except:
            sb_farming_skill_xp = 0
        
        try:
            sb_combat_skill_xp = sb_data["experience_skill_combat"]
            sb_combat_skill_xp = round(sb_combat_skill_xp)
        except:
            sb_combat_skill_xp = 0
        
        try:
            sb_fishing_skill_xp = sb_data["experience_skill_fishing"]
            sb_fishing_skill_xp = round(sb_fishing_skill_xp)
        except:
            sb_fishing_skill_xp = 0
        
        try:
            sb_alchemy_skill_xp = sb_data["experience_skill_alchemy"]
            sb_alchemy_skill_xp = round(sb_alchemy_skill_xp)
        except:
            sb_alchemy_skill_xp = 0
        
        try:
            sb_taming_skill_xp = sb_data["experience_skill_taming"]
            sb_taming_skill_xp = round(sb_taming_skill_xp)
        except:
            sb_taming_skill_xp = 0
        
        skill_lvl = [0, 50, 175, 375, 675, 1175, 1925, 2925, 4425, 6425,
         9925, 14925, 22425, 32425, 47425, 67425, 97425, 147425, 222425, 322425, 
         522425, 822425, 1222425, 1722425, 2322425, 3022425, 3822425, 4722425, 5722425, 
         6822425, 8022425, 9322425, 10722425, 12222425, 13822425, 15522425, 17322425, 19222425, 21222425, 
         23322425, 25522425, 27822425, 30222425, 32722425, 35322425, 38072425, 40972425, 44072425, 47472425,
         51172425, 55172425, 59472425, 64072425, 68972425, 74172425, 79672425, 85472425, 91572425, 97972425,
         104672425, 111672425]

        sb_mining_skill_lvl = xptoLevel(skill_lvl, sb_mining_skill_xp)
        sb_foraging_skill_lvl = xptoLevel(skill_lvl, sb_foraging_skill_xp)
        sb_enchanting_skill_lvl = xptoLevel(skill_lvl, sb_enchanting_skill_xp)
        sb_farming_skill_lvl = xptoLevel(skill_lvl, sb_farming_skill_xp)
        sb_combat_skill_lvl = xptoLevel(skill_lvl, sb_combat_skill_xp)
        sb_fishing_skill_lvl = xptoLevel(skill_lvl, sb_fishing_skill_xp)
        sb_alchemy_skill_lvl = xptoLevel(skill_lvl, sb_alchemy_skill_xp)
        sb_taming_skill_lvl = xptoLevel(skill_lvl, sb_taming_skill_xp)

        # Set skills with max cap of 50 to 50 if it is higher
        if sb_taming_skill_lvl > 50:
            sb_taming_skill_lvl = 50
        if sb_alchemy_skill_lvl > 50:
            sb_alchemy_skill_lvl = 50
        if sb_fishing_skill_lvl > 50:
            sb_fishing_skill_lvl = 50
        if sb_foraging_skill_lvl > 50:
            sb_foraging_skill_lvl = 50
        
        sb_skill_average = ((sb_mining_skill_lvl + sb_foraging_skill_lvl + sb_enchanting_skill_lvl + sb_farming_skill_lvl + sb_combat_skill_lvl + sb_fishing_skill_lvl + sb_alchemy_skill_lvl + sb_taming_skill_lvl) / 8)
        sb_skill_average = round(sb_skill_average, 2)

        try:
            slayer_zombie_xp = sb_data["slayer_bosses"]["zombie"]["xp"]
        except:
            slayer_zombie_xp = 0
        
        try:
            slayer_spider_xp = sb_data["slayer_bosses"]["spider"]["xp"]
        except:
            slayer_spider_xp = 0
        
        try:
            slayer_wolf_xp = sb_data["slayer_bosses"]["wolf"]["xp"]
        except:
            slayer_wolf_xp = 0
        
        try:
            slayer_enderman_xp = sb_data["slayer_bosses"]["enderman"]["xp"]
        except:
            slayer_enderman_xp = 0
        
        dungeon_skill_lvl = [0, 50, 125, 235, 395, 625, 955, 1425, 2095, 3045,
        4385, 6275, 8940, 12700, 17960, 25340, 35640, 50040, 70040, 97640,
        135640, 188140, 259640, 356640, 488640, 668640, 911640, 1239640, 1684640, 2284640,
        3084640, 4149640, 5559640, 7459640, 9959640, 13259640, 17559640, 23159640, 30359640, 39559640,
        51559640, 66559640, 85559640, 109559640, 139559640, 177559640, 225559640, 285559640, 360559640, 453559640,
        569809640]

        try:
            sb_catacombs_xp = sb_data["dungeons"]["dungeon_types"]["catacombs"]["experience"]
        except:
            sb_catacombs_xp = 0

        try:    
            sb_healer_xp = sb_data["dungeons"]["player_classes"]["healer"]["experience"]
        except:
            sb_healer_xp = 0

        try:
            sb_mage_xp = sb_data["dungeons"]["player_classes"]["mage"]["experience"]
        except:
            sb_mage_xp = 0

        try:
            sb_berserk_xp = sb_data["dungeons"]["player_classes"]["berserk"]["experience"]
        except:
            sb_berserk_xp = 0

        try:
            sb_archer_xp = sb_data["dungeons"]["player_classes"]["archer"]["experience"]
        except:
            sb_archer_xp = 0

        try:
            sb_tank_xp = sb_data["dungeons"]["player_classes"]["tank"]["experience"]
        except:
            sb_tank_xp = 0

        sb_catacombs_lvl = xptoLevel(dungeon_skill_lvl, sb_catacombs_xp)
        sb_healer_lvl = xptoLevel(dungeon_skill_lvl, sb_healer_xp)
        sb_mage_lvl = xptoLevel(dungeon_skill_lvl, sb_mage_xp)
        sb_berserk_lvl = xptoLevel(dungeon_skill_lvl, sb_berserk_xp)
        sb_archer_lvl = xptoLevel(dungeon_skill_lvl, sb_archer_xp)
        sb_tank_lvl = xptoLevel(dungeon_skill_lvl, sb_tank_xp)

        try:
            sb_test = sb_data["talisman_bag"]["data"]
            sb_test = decode_inventory_data(sb_test)
        except:
            sb_test = "N/A"
        
        embed=discord.Embed(title = "Skyblock Statistics » " + str(sb_cute_name), description = "**BETA**", color=0x0097FF)
        embed.add_field(name = "Skills", value = "```ml\n" + 
        "Mining     > Lvl: " + str(sb_mining_skill_lvl) + "\n" +
        "Foraging   > Lvl: " + str(sb_foraging_skill_lvl) + "\n" +
        "Enchanting > Lvl: " + str(sb_enchanting_skill_lvl) + "\n" +
        "Farming    > Lvl: " + str(sb_farming_skill_lvl) + "\n" +
        "Combat     > Lvl: " + str(sb_combat_skill_lvl) + "\n" +
        "Fishing    > Lvl: " + str(sb_fishing_skill_lvl) + "\n" +
        "Alchemy    > Lvl: " + str(sb_alchemy_skill_lvl) + "\n" +
        "Taming     > Lvl: " + str(sb_taming_skill_lvl) + "\n\n" +
        "Average    > Lvl: " + str(sb_skill_average) + "\n```", inline = False)
        embed.add_field(name = "Slayer", value = "```ml\n" +
        "Revenant   > XP: " + str(separation(slayer_zombie_xp)) + "\n" +
        "Tarantula  > XP: " + str(separation(slayer_spider_xp)) + "\n" +
        "Sven       > XP: " + str(separation(slayer_wolf_xp)) + "\n" +
        "Voidgloom  > XP: " + str(separation(slayer_enderman_xp)) + "\n```", inline = False)
        embed.add_field(name = "Dungeons", value = "```ml\n" +
        "Catacombs  > Lvl: " + str(sb_catacombs_lvl) + "\n" +
        "Healer     > Lvl: " + str(sb_healer_lvl) + "\n" +
        "Mage       > Lvl: " + str(sb_mage_lvl) + "\n" +
        "Berserk    > Lvl: " + str(sb_berserk_lvl) + "\n" +
        "Archer     > Lvl: " + str(sb_archer_lvl) + "\n" + 
        "Tank       > Lvl: " + str(sb_tank_lvl) + "\n```", inline = False)
        embed.add_field(name = "Testing", value = sb_test, inline = False)
        

        embed.set_author(name = display_name, icon_url = username_icon)
        embed.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/SkyBlock-64.png")
        embed.set_footer(text= embed_footer)

        await ctx.channel.send(embed=embed)



def setup(client):
    client.add_cog(skyblockStats(client))
