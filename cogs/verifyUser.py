import discord
from discord.ext import commands
import requests
import string
import asyncio

class verifyUser(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(pass_conext=True, aliases = ["link"])
    async def verify(self, ctx, username: str = None):
        if username is None:
            await ctx.channel.send("Please provide a username, for example: `-verify DetectiveAndrew`")
            return
        embed_footer = "© Andrew Edwards | All Rights Reserved"
        username_icon = "https://minotar.net/avatar/" + str(username)

        requested_info = str(ctx.author)
        requested_info_id = str(ctx.author.id)
        verification = "links"
        discord_server = str(ctx.message.guild.id)

        global API_KEY
        API_KEY = ""

        if discord_server == "503432726461022208":
            channel = str(ctx.channel)
            if channel == "verification" or channel == "verify" or channel == "link":
                try:
                    mojang_data = requests.get("https://api.mojang.com/users/profiles/minecraft/" + username).json()
                    uuid = mojang_data["id"]
                    hypixel_data = requests.get("https://api.hypixel.net/player?key=" + API_KEY + "&uuid=" + uuid).json()
                    display_name = hypixel_data["player"]["displayname"]
                except:
                    embed=discord.Embed(title = "Linking Account...", color=0xFF0000)
                    embed.add_field(name = "Status", value = "<:offline:862441939530285086>" + "`Failed`", inline = True)
                    embed.add_field(name = "Error", value = "`Player doesn't exist on the Hypixel API`", inline = False)
                    embed.add_field(name = "How do I fix this?", value = "`You have entered a name that cannot be found on the Hypixel API, make sure you have typed the username correctly.`", incline = False)
                    embed.add_field(name = "I still cannot link my account?", value = "`Check the API status, if up contact DetectiveAndrew`", inline = False)
                    embed.set_footer(text= embed_footer)
                    
                    if discord_server == "503432726461022208":
                        channel = self.client.get_channel(863191414001893376)

                        user = ctx.message.author
                        guild = ctx.message.guild
                        guild_owner = guild.owner
                        avi = user.avatar_url

                        try:
                            member_number = sorted(guild.members, key=lambda m: m.join_at).index(user) + 1
                        except:
                            member_number = "Failed to retrieve"
                        
                        em=discord.Embed(title = "Verification System", color=0xFF0000)
                        em.add_field(name = "Status", value = "<:offline:862441939530285086>" + "`Failed`", inline = True)
                        em.add_field(name = "Discord Name", value = "`" + str(user) + "`")
                        em.add_field(name = "Error", value = "Player doesn't exist on the Hypixel API", inline = False)
                        em.add_field(name = "User ID", value = "`" + requested_info_id + "`", inline = False)
                        em.add_field(name = "Account Created", value = "`" + user.created_at.__format__("%A, %B, %d, %Y") + "`"),
                        em.add_field(name = "Join Date", value = "`" + user.joined_at.__format__("%A, %B, %d, %Y") + "`"),
                        em.set_footer(text = embed_footer)
                        em.set_thumbnail(url = avi)

                    print(">> " + requested_info + " / " + requested_info_id + " has attempted to verify their account with " + username + ", verification failed because the username cannot be found on the Hypixel API.")
                    return_message = await ctx.channel.send(embed=embed)

                    await channel.send(embed=em)
                    await asyncio.sleep(60)
                    await ctx.message.delete()
                    await return_message.delete()
                    return
            
                if "socialMedia" not in hypixel_data["player"] or "links" not in hypixel_data["player"]["socialMedia"] or "DISCORD" not in hypixel_data["player"]["socialMedia"]["links"]:
                    embed = discord.Embed(title = "Linking Account...", color=0xFF0000)
                    embed.add_field(name = "Status", value = "<:offline:862441939530285086>" + "`Failed`", inline = True)
                    embed.add_field(name = "Error", value = "`Discord value is missing in Hypixel player data.`", inline = False)
                    embed.add_field(name = "How do I fix this?", value = "`Please make sure that this is your account and that you have correctly linked your discord account to your Hypixel account.`", inline = False)
                    embed.add_field(name = "I still cannot link my account?", value = "`Check the API status, if up contact DetectiveAndrew`")
                    embed.add_field(name = "Format", value = "`Example: DetectiveAndrew#3645`")
                    embed.set_author(name = display_name, icon_url = username_icon)
                    embed.set_footer(text = embed_footer)
            
                    if discord_server == "503432726461022208":
                        channel = self.client.get_channel(863191414001893376)

                        user = ctx.message.author
                        guild = ctx.message.guild
                        guild_owner = guild.owner
                        avi = user.avatar_url

                        try:
                            member_number = sorted(guild.members, key=lambda m: m.join_at).index(user) + 1
                        except:
                            member_number = "Failed to retrieve"
                        
                        em=discord.Embed(title = "Verification System", color=0xFF0000)
                        em.add_field(name = "Status", value = "<:offline:862441939530285086>" + "`Failed`", inline = True)
                        em.add_field(name = "Discord Name", value = "`" + str(user) + "`")
                        em.add_field(name = "Error", value = "Player doesn't exist on the Hypixel API", inline = False)

                        em.add_field(name = "Minecraft Name", value = "`" + str(display_name) + "`", inline = True)
                        em.add_field(name = "User ID", value = "`" + requested_info_id + "`", inline = False)
                        em.add_field(name = "Account Created", value = "`" + user.created_at.__format__("%A, %B, %d, %Y") + "`"),
                        em.add_field(name = "Join Date", value = "`" + user.joined_at.__format__("%A, %B, %d, %Y") + "`"),
                        em.set_footer(text= embed_footer)
                        em.set_thumbnail(url= avi)

                    print(">> " + requested_info + " / " + requested_info_id + " has attempted to verify their account with " + username + ", verification failed because the username cannot be found on the Hypixel API.")
                    return_message = await ctx.channel.send(embed=embed)

                    await channel.send(embed=em)
                    await asyncio.sleep(60)
                    await ctx.message.delete()
                    await return_message.delete()
                    return


                for key in hypixel_data["player"]["socialMedia"]:
                    try:
                        value = hypixel_data["player"]["socialMedia"][key]
                        display_name = hypixel_data["player"]["displayname"]
                    except:
                        await ctx.channel.send("An error has occured.")
                    if key == verification:
                        try:
                            discordlink = value["DISCORD"]
                        except:
                            return
                        if requested_info == discordlink:
                            nick_before = ctx.author.nick
                        else:
                            embed = discord.Embed(title = "Linking Account...", color=0xFF0000)
                            embed.add_field(name = "Status", value = "<:offline:862441939530285086>" + "`Failed`", inline = True)
                            embed.add_field(name = "Error", value = "`Discord value is missing in Hypixel player data.`", inline = False)
                            embed.add_field(name = "How do I fix this?", value = "`Please make sure that this is your account and that you have correctly linked your discord account to your Hypixel account.`", inline = False)
                            embed.add_field(name = "I still cannot link my account?", value = "`Check the API status, if up contact DetectiveAndrew`")
                            embed.add_field(name = "Format", value = "`Example: DetectiveAndrew#3645`")
                            embed.set_author(name = display_name, icon_url = username_icon)
                            embed.set_footer(text = embed_footer)

                            if discord_server == "503432726461022208":
                                channel = self.client.get_channel(863191414001893376)

                                user = ctx.message.author
                                guild = ctx.message.guild
                                guild_owner = guild.owner
                                avi = user.avatar_url

                                try:
                                    member_number = sorted(guild.members, key=lambda m: m.join_at).index(user) + 1
                                except:
                                    member_number = "Failed to retrieve"
                                
                                em=discord.Embed(title = "Verification System", color=0xFF0000)
                                em.add_field(name = "Status", value = "<:offline:862441939530285086>" + "`Failed`", inline = True)
                                em.add_field(name = "Discord Name", value = "`" + str(user) + "`")
                                em.add_field(name = "Error", value = "Player doesn't exist on the Hypixel API", inline = False)
                                em.add_field(name = "Minecraft Name", value = "`" + str(display_name) + "`", inline = True)
                                em.add_field(name = "User ID", value = "`" + requested_info_id + "`", inline = False)
                                em.add_field(name = "Account Created", value = "`" + user.created_at.__format__("%A, %B, %d, %Y") + "`"),
                                em.add_field(name = "Join Date", value = "`" + user.joined_at.__format__("%A, %B, %d, %Y") + "`"),
                                em.set_footer(text= embed_footer)
                                em.set_thumbnail(url = avi)

                            print(">> " + requested_info + " / " + requested_info_id + " has attempted to verify their account with " + username + ", verification failed because the username cannot be found on the Hypixel API.")
                            return_message = await ctx.channel.send(embed=embed)

                            await channel.send(embed=em)
                            await asyncio.sleep(60)
                            await ctx.message.delete()
                            await return_message.delete()
                            return

                        if nick_before is None:
                            nick_before = "N/A"

                        embed=discord.Embed(title = "Linking Account...", color=0x00ff00)
                        embed.add_field(name = "Status", value = "<:online:862441962484138015>" + "`Successful`", inline = True)
                        embed.add_field(name = "Nickname", value = "`" + str(nick_before) + "`" + "**→**`" + str(display_name) + "`", inline = True)
                        embed.add_field(name = "Roles Assigned", value = "`Tester` \n `Verified Account`", inline = False)
                        embed.add_field(name = "User ID", value = "`" + requested_info_id + "`", inline = False)
                        embed.set_author(name = display_name, icon_url = username_icon)
                        embed.set_footer(text = embed_footer)

                        if discord_server == "503432726461022208":
                            channel = self.client.get_channel(863191414001893376) 

                            user = ctx.message.author
                            guild = ctx.message.guild
                            guild_owner = guild.owner
                            avi = user.avatar_url

                            try:
                                member_number = sorted(guild.members, key=lambda m: m.join_at).index(user) + 1
                            except:
                                member_number = "Failed to retrieve"
                            
                            em=discord.Embed(title = "Verification System", color=0x00ff00)
                            em.add_field(name = "Status", value = "<:online:862441962484138015>" + "`Successful`", inline = True)
                            em.add_field(name = "Discord Name", value = "`" + str(user) + "`", inline = True)
                            em.add_field(name = "Minecraft Name", value = "`" + str(display_name) + "`", inline = True)
                            em.add_field(name = "Roles Assigned", value = "`Tester` \n `Verified Account`", inline = False)
                            em.add_field(name = "User ID", value = "`" + requested_info_id + "`", inline = False)
                            em.add_field(name = "Account Created", value = "`" + user.created_at.__format__("%A, %B, %d, %Y") + "`"),
                            em.add_field(name = "Join Date", value = "`" + user.joined_at.__format__("%A, %B, %d, %Y") + "`"),
                            em.set_author(name = display_name, icon_url = username_icon)
                            em.add_field(name = "Statistics", value = "https://plancke.io/hypixel/player/stats/" + str(display_name), inline = False)
                            em.set_footer(text = embed_footer)   
                            em.set_thumbnail(url= avi)
                            

                        try:
                            await ctx.author.edit(nick = display_name, reason = "Updating nickname to match in-game name.")
                        except:
                            print(">> User has administrator perms, cannot update nickname")
                        
                        print(">> " + requested_info + " / " + requested_info_id + " has attempted to verify their account with " + username + ", verification successful!")
                        return_message = await ctx.channel.send(embed=embed)

                        playerrank = discord.utils.get(ctx.guild.roles, name = "Tester")
                        verified = discord.utils.get(ctx.guild.roles, name = "Verified Account")

                        await ctx.author.add_roles(playerrank, reason = "Linking discord account with Hypixel account.")
                        await ctx.author.add_roles(verified, reason = "Linking discord account with Hypixel account.")
                        print(">> Tester Role assigned")
                        print(">> Verified Account role assigned")
                        roles = sorted(user.roles, key=lambda r: r.position)
                        rolenames = ", ".join([r.name for r in roles if r != "@everyone"]) or "None"

                        await channel.send(embed=em)
                        await asyncio.sleep(60)
                        await ctx.message.delete()
                        await return_message.delete()
                        
            else:
                await ctx.channel.send("This cannot be used in this channel!")
        else:
            await ctx.channel.send("This discord server has not been approved for verification functionality!\nPlease message: `DetectiveAndrew#3645`")

def setup(client):
    client.add_cog(verifyUser(client))




                

