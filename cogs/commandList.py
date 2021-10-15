import discord
from discord.ext import commands
import string

class commandList(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(pass_conext=True)
    async def help(self, ctx):
        
        embed_footer = "© Andrew Edwards | All Rights Reserved"
    
        embed=discord.Embed(title = "Dev Bot", description = "Here are the available commands for Dev Bot.\nPlease use `-` as the command prefix.", color=0x0097FF)
        embed.add_field(name = "General", value = "`verify`, `quote`", inline = False)
        embed.add_field(name = "Hypixel", value = "`stats`, `sb`, `mw`, `classpoints`, `bsg`, `wl`, `uhc`, `suhc`, `tnt`, `cvc`, `sw`, `sh`, `bw`, `mm`, `duels`, `pit`, `arcade`, `walls`, `quake`, `vz`, `pb`, `ab`, `tkr`, `cw`, `sc`", inline = False)
        embed.add_field(name = "Utility", value = "`uptime`", inline = False)
        embed.add_field(name = "Developer", value = "`modules`, `load`, `reload`, `unload`, `say`", inline = False)
     
        embed.set_thumbnail(url = "https://pbs.twimg.com/profile_images/1346968969849171970/DdNypQdN_400x400.png")
        embed.set_footer(text= embed_footer)

        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(commandList(client))
