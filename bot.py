from discord.ext import commands
import discord
from discord import Member, Embed
from config import TOKEN
import logging
import gettext

_ = gettext.gettext
ru = gettext.translation('base', localedir='locales', languages=['ru'])
en = gettext.translation('base', localedir='locales', languages=['en'])
fr = gettext.translation('base', localedir='locales', languages=['fr'])
kr = gettext.translation('base', localedir='locales', languages=['kr'])
en.install()

locales = {
    # RU
    820034895341420596: ru,

    # FR
    820034927394422844: fr,

    # KR
    817629795247980544: kr
}


# initialize bot params
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="faq.",
                   help_command=None, intents=intents)

# setup logger
logging.basicConfig(filename="eco-faq.log", level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s:%(message)s")
bot.remove_command(help)


# async wrapper for changing language on the fly
def resolve_language(function):
    async def wrapper(ctx):
        if ctx.channel.id in locales.keys():
            locale = locales[ctx.channel.id]
        else:
            locale = en
        locale.install()
        _ = locale.gettext
        return await function(ctx, _)
    return wrapper


@bot.command('eco')
@resolve_language
async def eco(ctx, _):
    widget = Embed(
        title=_("ECO_TITLE"),
        color=0x03d692,
        description=_("ECO_DESCRIPTION")
    )
    widget.set_thumbnail(
        url="https://eco-bots.s3.eu-north-1.amazonaws.com/eco_large.png"
    )
    widget.add_field(
        name=_("ECO_FIELD1_NAME"),
        value=_("ECO_FIELD1_VALUE")
    )
    await ctx.send(embed=widget)


@bot.command('points')
@resolve_language
async def points(ctx, _):
    widget = Embed(
        title=_("POINTS_TITLE"),
        color=0x03d692,
        description=_("POINTS_DESCRIPTION")
    )
    widget.set_thumbnail(
        url="https://eco-bots.s3.eu-north-1.amazonaws.com/eco_large.png"
    )
    widget.add_field(
        name=_("POINTS_FIELD1_NAME"),
        value=_("POINTS_FIELD1_VALUE")
    )
    await ctx.send(embed=widget)


@bot.command('help')
async def help(ctx):
    widget = Embed(description=_("Available commands for Eco-FAQ-bot"), color=0x03d692,
                   title=_("Help"))
    widget.set_thumbnail(
        url="https://pbs.twimg.com/profile_images/1366064859574661124/Ocl4oSnU_400x400.jpg")
    widget.add_field(
        name="$invites.stats_all",
        value=f"`Displays a list of all invitation links`\n", inline=False)
    widget.add_field(
        name="$invites.stats_uses",
        value="`Displays a list of all invitation links with uses > 0`", inline=False
    )
    await ctx.send(embed=widget)

if __name__ == "__main__":
    bot.run(TOKEN)
