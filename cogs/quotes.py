import discord
from discord.ext import commands
import requests
import string

class quotes(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(pass_conext=True)
    async def quote(self, ctx):
        embed_footer = "© Andrew Edwards | All Rights Reserved"

        try:
            quote_data = requests.get("https://zenquotes.io/api/random").json()
        except:
            embed=discord.Embed(title = "Invalid Request", color=0xFF0000)
            embed.add_field(name = "Error", value = "`Quote API is down`")
            embed.set_footer(text= embed_footer)
            await ctx.channel.send(embed=embed)
            return
        try:
            quote = quote_data[0]["q"]
        except:
            quote = "N/A"
        try:    
            author = quote_data[0]["a"]
        except:
            author = "N/A"

        embed=discord.Embed(title = "Random Quote", description = quote, color=0x0097FF)
        embed.set_author(name = author)
        embed.set_footer(text = embed_footer)

        await ctx.channel.send(embed=embed)
        

def setup(client):
    client.add_cog(quotes(client))
