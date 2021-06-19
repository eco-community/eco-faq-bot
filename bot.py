import gettext
import logging

import discord
from discord import Embed
from discord.ext import commands

import config
from utils import use_sentry
from constants import SENTRY_ENV_NAME


_ = gettext.gettext
ru = gettext.translation("base", localedir="locales", languages=["ru"])
en = gettext.translation("base", localedir="locales", languages=["en"])
fr = gettext.translation("base", localedir="locales", languages=["fr"])
kr = gettext.translation("base", localedir="locales", languages=["kr"])
jp = gettext.translation("base", localedir="locales", languages=["jp"])
en.install()

locales = {
    # RU
    config.RU_CHANNEL_ID: ru,
    # RU-flood
    config.RU_FLOOD_CHANNEL_ID: ru,
    # FR
    config.FR_CHANNEL_ID: fr,
    # KR
    config.KR_CHANNEL_ID: kr,
    # JP
    config.JP_CHANNEL_ID: jp
}


# initialize bot params
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="faq.", help_command=None, intents=intents)

# init sentry SDK
use_sentry(
    bot,
    dsn=config.SENTRY_API_KEY,
    environment=SENTRY_ENV_NAME,
)

# setup logger
logging.basicConfig(filename="eco-faq.log", level=logging.INFO, format="%(asctime)s %(levelname)s:%(message)s")
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


@bot.command("eco")
@resolve_language
async def eco(ctx, _):
    widget = Embed(title=_("ECO_TITLE"), color=0x03D692, description=_("ECO_DESCRIPTION"))
    widget.set_thumbnail(url="https://eco-bots.s3.eu-north-1.amazonaws.com/eco_large.png")
    widget.add_field(name=_("ECO_FIELD1_NAME"), value=_("ECO_FIELD1_VALUE"))
    await ctx.send(embed=widget)


@bot.command("points")
@resolve_language
async def points(ctx, _):
    widget = Embed(title=_("POINTS_TITLE"), color=0x03D692, description=_("POINTS_DESCRIPTION"))
    widget.set_thumbnail(url="https://eco-bots.s3.eu-north-1.amazonaws.com/eco_large.png")
    widget.add_field(name=_("POINTS_FIELD1_NAME"), value=_("POINTS_FIELD1_VALUE"))
    await ctx.send(embed=widget)


@bot.command("pinned")
@resolve_language
async def pinned(ctx, _):
    widget = Embed(color=0x03D692)
    widget.set_author(
        name=_("ECO Pinned Messages"), icon_url="https://eco-bots.s3.eu-north-1.amazonaws.com/eco_large.png"
    )
    widget.set_image(
        url="https://user-images.githubusercontent.com/61438668/111036517-a535df80-8430-11eb-9c58-413d8aa08c83.png"
    )
    await ctx.send(embed=widget)


@bot.command("navigation")
@resolve_language
async def navigation(ctx, _):
    widget = Embed(title=_("NAVIGATION_TITLE"), color=0x03D692, description=_("NAVIGATION_TITLE_DESCRIPTION"))
    widget.set_thumbnail(url="https://eco-bots.s3.eu-north-1.amazonaws.com/eco_large.png")
    widget.add_field(name=_("NAVIGATION_FIELD1_NAME"), value=_("NAVIGATION_FIELD1_VALUE"), inline=False)
    widget.add_field(name=_("NAVIGATION_FIELD2_NAME"), value=_("NAVIGATION_FIELD2_VALUE"), inline=False)
    widget.add_field(name=_("NAVIGATION_FIELD3_NAME"), value=_("NAVIGATION_FIELD3_VALUE"), inline=False)
    widget.add_field(name=_("NAVIGATION_FIELD4_NAME"), value=_("NAVIGATION_FIELD4_VALUE"), inline=False)
    widget.add_field(name=_("NAVIGATION_FIELD5_NAME"), value=_("NAVIGATION_FIELD5_VALUE"), inline=False)
    widget.add_field(name=_("NAVIGATION_FIELD6_NAME"), value=_("NAVIGATION_FIELD6_VALUE"), inline=False)
    widget.add_field(name=_("NAVIGATION_FIELD7_NAME"), value=_("NAVIGATION_FIELD7_VALUE"), inline=False)
    widget.add_field(name=_("NAVIGATION_FIELD8_NAME"), value=_("NAVIGATION_FIELD8_VALUE"), inline=False)
    await ctx.send(embed=widget)


@bot.command("help")
@resolve_language
async def help(ctx, _):
    widget = Embed(description=_("Available commands for Eco-FAQ-bot"), color=0x03D692, title=_("Help"))
    widget.set_thumbnail(url="https://eco-bots.s3.eu-north-1.amazonaws.com/eco_large.png")
    widget.add_field(name="faq.eco", value=_("FAQ_ECO_CMD"), inline=False)
    widget.add_field(name="faq.points", value=_("FAQ_POINTS_CMD"), inline=False)
    widget.add_field(name="faq.navigation", value=_("FAQ_NAVIGATION_CMD"), inline=False)
    widget.add_field(name="faq.pinned", value=_("FAQ_PINNED_CMD"), inline=False)
    widget.add_field(name="faq.artrules", value=_("FAQ_FANCYRULES_CMD"), inline=False)
    widget.add_field(name="faq.memerules", value=_("FAQ_MEMERULES_CMD"), inline=False)
    widget.add_field(name="faq.marketingrules", value=_("FAQ_MARKETINGRULES_CMD"), inline=False)
    await ctx.send(embed=widget)


@bot.command("artrules")
@resolve_language
async def fancy_rules(ctx, _):
    widget = Embed(title=_("FANCYRULES_TITLE"), color=0x03D692)
    widget.set_thumbnail(url="https://eco-bots.s3.eu-north-1.amazonaws.com/eco_large.png")
    widget.add_field(name=_("FANCYRULES_FIELD1_NAME"), value=_("FANCYRULES_FIELD1_VALUE"), inline=False)
    await ctx.send(embed=widget)


@bot.command("memerules")
@resolve_language
async def meme_rules(ctx, _):
    widget = Embed(title=_("MEMERULES_TITLE"), color=0x03D692)
    widget.set_thumbnail(url="https://eco-bots.s3.eu-north-1.amazonaws.com/eco_large.png")
    widget.add_field(name=_("MEMERULES_FIELD1_NAME"), value=_("MEMERULES_FIELD1_VALUE"), inline=False)
    await ctx.send(embed=widget)


@bot.command("marketingrules")
@resolve_language
async def marketing_rules(ctx, _):
    widget = Embed(title=_("MARKETINGRULES_TITLE"), color=0x03D692)
    widget.set_thumbnail(url="https://eco-bots.s3.eu-north-1.amazonaws.com/eco_large.png")
    widget.add_field(name=_("MARKETINGRULES_FIELD1_NAME"), value=_("MARKETINGRULES_FIELD1_VALUE"), inline=False)
    await ctx.send(embed=widget)

if __name__ == "__main__":
    bot.run(config.TOKEN)
