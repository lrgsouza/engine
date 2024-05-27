import os
from discord import option

from modules.dice.dice import Dice
from modules.graph.graph import Graph
from modules.currency.currency import Currency
from modules.units.units import Units
from variables import *
from discord_function import *

async def send_graph(ctx, file):
    with open(file, 'rb') as f:
        file = discord.File(f)
        await ctx.send(file=file)

@bot.slash_command(name="somar", description="Show all production instances state", pass_context=True, guild_ids=[guild_id])
@option("number1", int, description="Number.",choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
@option("number2", int, description="Number.",choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
@is_in_channel()
async def somar(ctx, number1: int, number2: int):
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

@bot.slash_command(name="trigonometric-graph", description="Get a image for sin, cos and tan", pass_context=True, guild_ids=[guild_id])
@option("trigonometric", str, description="Number.", choices=["sin", "cos", "tan"], required=True)
@is_in_channel()
async def graph(ctx, trigonometric: str):
    await ctx.defer()
    graph = Graph(trigonometric=trigonometric)  # Instancia a classe Graph
    graph.generate_trigonometric_graph()  # Gera o gráfico
    await send_graph(ctx, f'grafico_funcao_{trigonometric}.png')  # Envia a imagem para o canal Discord
    os.remove(f'grafico_funcao_{trigonometric}.png')  # Apaga a imagem
    await ctx.respond(f"Grafico de {trigonometric} gerado com sucesso!")

@bot.slash_command(name="dice", description="Get a image for y=2x+7", pass_context=True, guild_ids=[guild_id])
@is_in_channel()
async def graph(ctx):
    await ctx.defer()
    dice = Dice()
    result = dice.dice_gen()
    await ctx.respond(f'Seu dado foi {result}')


@bot.slash_command(name="currency", description="Get currency value", pass_context=True, guild_ids=[guild_id])
@option("origin", str, description="Currency code.", choices=Currency.codes())
@option("target", str, description="Currency code.", choices=Currency.codes())
@is_in_channel()
async def currency(ctx, origin: str, target: str):
    await ctx.defer()
    currency = Currency()
    value = currency.currency(origin, target)

    if value is None:
        await ctx.respond(f'An error occurred while trying to get the currency value. Please try again later.')
        return

    if value < 0:
        await ctx.respond(f'An error occurred while trying to get the currency value. Please try again later.')
        return
    
    formatted_value = "{:.8f}".format(value).rstrip('0').rstrip('.')
    await ctx.respond(f'# {Currency.emojis()[origin]} {origin} = **{formatted_value}** {target} {Currency.emojis()[target]}')

@bot.slash_command(name="convert_weight", description="Convert weight units", pass_context=True, guild_ids=[guild_id])
@option("origin", str, description="Origin unit.", choices=Units.weight_units())
@option("dest", str, description="Destination unit.", choices=Units.weight_units())
@option("value", float, description="Value to convert.")
@is_in_channel()
async def weight(ctx, origin: str, dest: str, value: float):
    await ctx.defer()
    units = Units()
    result = units.weight(origin, dest, value)
    await ctx.respond(f'{value} {origin} = {result} {dest}')

@bot.slash_command(name="convert_temperature", description="Convert temperature units", pass_context=True, guild_ids=[guild_id])
@option("origin", str, description="Origin unit.", choices=Units.temperature_units())
@option("dest", str, description="Destination unit.", choices=Units.temperature_units())
@option("value", float, description="Value to convert.")
@is_in_channel()
async def temperature(ctx, origin: str, dest: str, value: float):
    await ctx.defer()
    units = Units()
    result = units.temperature(origin, dest, value)
    await ctx.respond(f'{value} {origin} = {result} {dest}')

@bot.slash_command(name="convert_distance", description="Convert distance units", pass_context=True, guild_ids=[guild_id])
@option("origin", str, description="Origin unit.", choices=Units.distance_units())
@option("dest", str, description="Destination unit.", choices=Units.distance_units())
@option("value", float, description="Value to convert.")
@is_in_channel()
async def distance(ctx, origin: str, dest: str, value: float):
    await ctx.defer()
    units = Units()
    result = units.distance(origin, dest, value)
    await ctx.respond(f'{value} {origin} = {result} {dest}')

bot.run(token_discord)