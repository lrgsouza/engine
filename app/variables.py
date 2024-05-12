import os
import pytz

from discord.ext import commands

import discord

# Variables
channel_name = os.getenv('CHANNEL_NAME', "recursos")
token_discord = os.getenv('DISCORD_TOKEN', "")
brazil = pytz.timezone("America/Sao_Paulo")
rule_id = os.getenv('RULE_ID')
guild_id = os.getenv('GUILD_ID', "1233550515569295401")

# Variables messages
denied_msg = "You dont have permission to do that!"
wrong_msg = ":warning: Something wrong, try use `/help`"
timeout_msg = "Timeout, please try again!"

help_msg = """
/help - Show help information
/dice - Roll a dice
/graph - Generate a graph
/currency - Get currency value
/exit - Exit the bot
"""

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='/', help_command=None, intents=intents)