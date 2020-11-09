import discord, os, json, typing, sys, traceback, asyncio, logging
from discord.ext import commands
import cogs
import config


cfg = config.load_config()


def get_prefix(client, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    with open("./src/prefixes.json", "r") as f:
        prefixes=json.load(f)
    return prefixes[str(message.guild.id)]


client=commands.Bot(command_prefix=get_prefix)


#Event
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f"Type !help for more information"))
    print(f"Logged in as {client.user.name}")
    print(client.user.id)
    print("----------------------")

@client.event
async def on_guild_join(guild):
    with open("./src/prefixes.json", "r") as f:
        prefixes=json.load(f)
    prefixes[str(guild.id)]="!"
    with open("./src/prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open("./src/prefixes.json", "r") as f:
        prefixes=json.load(f)
    prefixes.pop(str(guild.id))
    with open("./src/prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_member_join(member):
    print(f"{member} has joined the server !")

@client.event
async def on_member_remove(member):
    print(f"{member} has left the server !")

@client.event
async def on_command_error(ctx, error):
    if hasattr(ctx.command, "on_error"):
        return  # Don't interfere with custom error handlers

    error = getattr(error, "original", error)  # get original error

    if isinstance(error, commands.CommandNotFound):
        return await ctx.send(
            f"That command does not exist. Please use `!help` for a list of commands."
        )

    if isinstance(error, commands.CommandError):
        return await ctx.send(
            f"Error executing command `{ctx.command.name}`: {str(error)}")

    await ctx.send(
        "An unexpected error occurred while running that command.")
    logging.warn("Ignoring exception in command {}:".format(ctx.command))
    logging.warn("\n" + "".join(
        traceback.format_exception(
            type(error), error, error.__traceback__)))


for filename in os.listdir("./src/cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


def run_client(client=client):
    loop = asyncio.get_event_loop()
    while True:
        try:
            loop.run_until_complete(client.start(os.environ["DISCORD_ACCESS_TOKEN"]))
        except Exception as e:
            print("Error", e)  # or use proper logging
        print("Waiting until restart")
        time.sleep(600)
