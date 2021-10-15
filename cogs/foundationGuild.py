import discord
from discord.ext import commands, tasks
import requests
from datetime import date
import time

def numberSystem(arr, pos):
    num = len(arr) + 1
    position = str(num) + ". **"

    return position

# Unfinished - WIP
class foundationGuild(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.gexp_records.start()

    # Go off at 12:10am everyday to give time for api to update correctly   
    @tasks.loop(seconds=15)
    async def gexp_records(self):
        
        # Actually needs to be yesterdays date
        today = date.today()
        current_date = today.strftime("%Y-%m-%d")
    
        embed_footer = current_date
        separation = "{:,}".format
        discord_server = "503432726461022208"
        guild = "The%20Foundation"

        global API_KEY
        API_KEY = "a0f07d36-334d-44f7-b533-6e4e51ccdcdd"

        if discord_server == "503432726461022208":
            channel = self.client.get_channel(875100562071388210)
            try:
                guild_data = requests.get("https://api.hypixel.net/guild?key=" + API_KEY + "&name=" + guild).json()
                
            except:
                embed=discord.Embed(title = "Foundation Daily Stats", color=0xFF0000)
                embed.add_field(name = "Status", value = "<:offline:862441939530285086>" + "`Failed`", inline = True)
                embed.add_field(name = "Error", value = "`Problem retrieving the guild API data`", inline = False)
                embed.add_field(name = "Needs Manual Update", value = "<@461735532494454797>", inline = False)
                embed.set_author(name = "The Foundation", icon_url = "https://pbs.twimg.com/profile_images/722551604860293124/8mVwin0N_400x400.jpg")
                embed.set_footer(text= embed_footer)
                await channel.send(embed=embed)

            

            # Should probably use hashmap in future
            g_members = len(guild_data["guild"]["members"])
            g_members_name = []
            g_members_gexp = []

            for i in range(g_members):
                uuid = guild_data["guild"]["members"][i]["uuid"]
                gexp = guild_data["guild"]["members"][i]["expHistory"]["2021-08-11"]

                if gexp >= 80000:
                    try:
                        hypixel_data = requests.get("https://api.hypixel.net/player?key=" + API_KEY + "&uuid=" + uuid).json()
                        display_name = hypixel_data["player"]["displayname"]
                        g_members_name.append(display_name)
                        g_members_gexp.append(gexp)
                    except:
                        embed=discord.Embed(title = "Foundation Daily Stats", color=0xFF0000)
                        embed.add_field(name = "Status", value = "<:offline:862441939530285086>" + "`Failed`", inline = True)
                        embed.add_field(name = "Error", value = "`Problem retrieving the API data`", inline = False)
                        embed.add_field(name = "Uuid", value = "`" + str(uuid) + "`", inline = False)
                        embed.set_author(name = "The Foundation", icon_url = "https://pbs.twimg.com/profile_images/722551604860293124/8mVwin0N_400x400.jpg")
                        embed.set_footer(text= embed_footer)
                        await channel.send(embed=embed)   
                else:
                    continue
            
            if len(g_members_name) > 1:
                g_members_gexp, g_members_name = zip(*sorted(zip(g_members_gexp,g_members_name), reverse=True))
            
            embed=discord.Embed(title = "Foundation Daily Stats", description = "To earn a star, gain 80k GEXP in a day", color=0x8a2be2)
            embed.add_field(name = "Daily GEXP Records", value = "1. **" + str(g_members_name[0]) + "** - " + str(separation(g_members_gexp[0])) + " GEXP\n", inline = True)
            embed.set_author(name = "The Foundation", icon_url = "https://pbs.twimg.com/profile_images/722551604860293124/8mVwin0N_400x400.jpg")
            embed.set_footer(text= embed_footer)

            await channel.send(embed=embed)  

    
        

    @gexp_records.before_loop
    async def before_gexp_records(self):
        await self.client.wait_until_ready()
        

def setup(client):
    client.add_cog(foundationGuild(client))
