import os
import discord
from loguru import logger
from time import time
from discord.ext import commands
import datetime
import re
import pytz
import json
from discord import Embed, option

import matplotlib.pyplot as plt
import numpy as np
import io
from modules.dice.dice import Dice
from modules.graph.graph import Graph
# Variables
channel_name = os.getenv('CHANNEL_NAME', "recursos")
token_discord = os.getenv('DISCORD_TOKEN', "")
brazil = pytz.timezone("America/Sao_Paulo")
rule_id = os.getenv('RULE_ID')
guild_id = os.getenv('GUILD_ID', "1233550515569295401")

intents = discord.Intents.all()
intents.message_content = True

# bot prefix
bot = commands.Bot(command_prefix='/', help_command=None, intents=intents)

# Variables messages
denied_msg = "You dont have permission to do that!"
wrong_msg = ":warning: Something wrong, try use `/help`"
timeout_msg = "Timeout, please try again!"

##############################
###### CONFIG FUNCTIONS ######
##############################

@bot.event
async def on_ready():
    logger.info(f"{bot.user.name} has connected to Discord!")

async def exit(ctx):
    await ctx.respond("tchau")

def is_in_channel():
    def predicate(ctx):
        if ctx.channel.name != channel_name:
            raise commands.CheckFailure(f"You must be in the '{channel_name}' channel to use this command.")
        else:
            return True
    return commands.check(predicate)

# Verify if the user is adm or has the role
def is_adm_or_has_role(role=None):
    async def predicate(ctx):
        try:
            is_adm = await commands.has_permissions(administrator=True).predicate(ctx)
            if is_adm:
                return True
        except commands.CheckFailure:
            pass

        if role is None:
            raise commands.CheckFailure("Only administrators can use this command.")
        else:
            try:
                has_role = await commands.has_any_role(role).predicate(ctx)
                if has_role:
                    return True
            except commands.CheckFailure:
                raise commands.CheckFailure(f"You need the '{role}' role to use this command.")

    return commands.check(predicate)



# Função para enviar a imagem para o canal Discord
async def send_graph(ctx, file):
    with open(file, 'rb') as f:
        file = discord.File(f)
        await ctx.send(file=file)


##############################
###### DISCORD COMMANDS ######
##############################

@bot.slash_command(name="help", description="Show help information", pass_context=True, guild_ids=[guild_id])
@is_in_channel()
async def help(ctx):
    await ctx.defer()
    bot_message = {'message' : f"{help_msg}"'', 'color': 0xFFFF00}#yellow\
    bot_message_formatted = Embed(title=f':bookmark_tabs: Allowed commands:', #TODO mudar url
                        description=bot_message['message'], color=bot_message['color'], timestamp=datetime.datetime.now(brazil))
    await ctx.respond(embed=bot_message_formatted)

# Function addrole
@bot.slash_command(name="addrole", description="Add role to user", pass_context=True, guild_ids=[guild_id])
@option("user", discord.Member, description="User who will receive the role.")
@option("role", discord.Role, description="Role that will be applied to the user.")
@is_adm_or_has_role()
@is_in_channel()
async def _addrole(ctx, user: discord.Member, role: discord.Role):
    await ctx.defer()
    try:
        await user.add_roles(role)
        await ctx.respond(f"Hey, {user.mention}, you have been given the role: `{role.name}`")
    except Exception as error:
        logger.error(error)
        await ctx.respond(f":x:{error}")

##############################
######### COMMANDS ###########
##############################

# Function get-pods
@bot.slash_command(name="somar", description="Show all production instances state", pass_context=True, guild_ids=[guild_id])
@option("number1", int, description="Number.",choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
@option("number2", int, description="Number.",choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
@is_in_channel()
async def _somar(ctx, number1: int, number2: int):
    await ctx.defer()
    
    await ctx.respond(number1+number2)

@bot.slash_command(name="graph", description="Get a image for y=ax²+b+c", pass_context=True, guild_ids=[guild_id])
@option("a", int, description="Number.")
@option("b", int, description="Number.")
@option("c", int, description="Number.")
@is_in_channel()
async def graph(ctx, a: int, b: int, c: int):
    await ctx.defer()
    graph = Graph(a=a, b=b, c=c)  # Instancia a classe Graph
    legend, degree = graph.generate_graph()  # Gera o gráfico
    await send_graph(ctx, f'grafico_funcao_{degree}_grau.png')  # Envia a imagem para o canal Discord
    os.remove(f'grafico_funcao_{degree}_grau.png')  # Apaga a imagem
    await ctx.respond(f"Grafico de {degree} grau gerado com sucesso! funcao {legend}")


@bot.slash_command(name="dice", description="Get a image for y=2x+7", pass_context=True, guild_ids=[guild_id])
@is_in_channel()
async def graph(ctx):
    await ctx.defer()
    dice = Dice()
    result = dice.dice_gen()
    await ctx.respond(f'Seu dado foi {result}')


##############################
####### ERROR HANDLING #######
##############################

async def handle_command_error(interaction: discord.Interaction, error):
    logger.error(error)
    await interaction.respond(content=f":x: {error}", ephemeral=True)


@_addrole.error
async def _addrole_error(interaction: discord.Interaction, error):
    await handle_command_error(interaction, error)

@_somar.error
async def _somar_error(interaction: discord.Interaction, error):
    await handle_command_error(interaction, error)

@graph.error
async def graph_error(interaction: discord.Interaction, error):
    await handle_command_error(interaction, error)

bot.run(token_discord)