import datetime
from variables import *
from loguru import logger
from discord import option, Embed

from variables import *

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
async def addrole(ctx, user: discord.Member, role: discord.Role):
    await ctx.defer()
    try:
        await user.add_roles(role)
        await ctx.respond(f"Hey, {user.mention}, you have been given the role: `{role.name}`")
    except Exception as error:
        logger.error(error)
        await ctx.respond(f":x:{error}")