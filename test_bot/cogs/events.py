from disnake.ext import commands
import discord
import itertools
import datetime

def iter_all_mentions(message):
    return itertools.chain(message.mentions, message.channel_mentions, message.role_mentions)

class AntiPing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(message):
        for i, mentioned in enumerate(iter_all_mentions(message)):
            allowed_roles = {1089165585214087270, 1010144986806878290, 1000701304110338170, 1032993373470085160, 1070260250709590057}
            if mentioned.id == 746966989347618858 and not any(role.id in allowed_roles for role in message.author.roles):
                DateTime = datetime.datetime.now()
                embed = discord.Embed(
                    title="Please refrain from pinging the Founder",
                    description="""
                    We do not allow you to ping our Founder at this time. For support, please send a Direct Message to @Pleasant Support. Multiple pings to the Founder may result in further moderation action taken.

If you are replying to a message sent by the Founder, please follow the instructions provided in the video below on how to disable pinging the original author.
                    """,
                    color=0xffe1b4
                )
                embed.set_footer(text=f"Pleasant Support • Pleasant Corporation • Today at {DateTime.strftime('%x %H:%M')}")
                embed.set_image(url="https://media.tenor.com/ddg6ge2H_T0AAAAd/discord-reply.gif")
                await message.channel.send(embed=embed)

async def setup(bot):
    bot.add_cog(AntiPing(bot))
