import discord

from loguru import logger

from main import *

async def handle_command_error(interaction: discord.Interaction, error):
    logger.error(error)
    await interaction.respond(content=f":x: {error}", ephemeral=True)

for command in bot.commands:
    @command.error
    async def command_error(ctx, error):
        await handle_command_error(ctx, error)