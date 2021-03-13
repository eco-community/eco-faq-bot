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


@bot.command('pinned')
@resolve_language
async def points(ctx, _):
    widget = Embed(color=0x03d692)
    widget.set_author(
        name=_("ECO Pinned Messages"), icon_url="https://eco-bots.s3.eu-north-1.amazonaws.com/eco_large.png")
    widget.set_image(
        url="https://user-images.githubusercontent.com/61438668/111036517-a535df80-8430-11eb-9c58-413d8aa08c83.png")
    await ctx.send(embed=widget)


@bot.command('navigation')
@resolve_language
async def points(ctx, _):
    widget = Embed(
        title=_("NAVIGATION_TITLE"),
        color=0x03d692,
        description=_("NAVIGATION_TITLE_DESCRIPTION")
    )
    widget.set_thumbnail(
        url="https://eco-bots.s3.eu-north-1.amazonaws.com/eco_large.png"
    )
    widget.add_field(
        name=_("NAVIGATION_TITLE_FIELD1_NAME"),
        value=_("NAVIGATION_TITLE_FIELD1_VALUE"),
        inline=False
    )
    widget.add_field(
        name=_("NAVIGATION_TITLE_FIELD2_NAME"),
        value=_("NAVIGATION_TITLE_FIELD2_VALUE"),
        inline=False
    )
    widget.add_field(
        name=_("NAVIGATION_TITLE_FIELD3_NAME"),
        value=_("NAVIGATION_TITLE_FIELD3_VALUE"),
        inline=False
    )
    await ctx.send(embed=widget)


@bot.command('help')
@resolve_language
async def help(ctx, _):
    widget = Embed(description=_("Available commands for Eco-FAQ-bot"), color=0x03d692,
                   title=_("Help"))
    widget.set_thumbnail(
        url="https://eco-bots.s3.eu-north-1.amazonaws.com/eco_large.png")
    widget.add_field(
        name="faq.eco",
        value=_("FAQ_ECO_CMD"), inline=False)
    widget.add_field(
        name="faq.points",
        value=_("FAQ_POINTS_CMD"), inline=False
    )
    widget.add_field(
        name="faq.navigation",
        value=_("FAQ_NAVIGATION_CMD"), inline=False
    )
    widget.add_field(
        name="faq.pinned",
        value=_("FAQ_PINNED_CMD"), inline=False
    )
    await ctx.send(embed=widget)

if __name__ == "__main__":
    bot.run(TOKEN)
