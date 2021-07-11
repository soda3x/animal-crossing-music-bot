import discord
from discord.errors import HTTPException
import Playback
from discord.ext import commands
import os
import platform
from Utils import Globals

client = commands.Bot(command_prefix='!')

if (Globals.validate_globals()):
    print(Globals.validate_globals())

print("Chriscord is currently running on:", os.name,
      platform.system(), platform.release())


@client.event
async def on_ready():
    print('Logged in as {0.user} and ready for commands'.format(client))


@client.command(name='acmusic', aliases=['ac'], pass_context=True, help="Play hourly Animal Crossing music, Select which game with the argument: gc, ww / cf, nl or nh")
async def _acmusic(ctx, *, game: str = None):
    destination = ctx.author.voice.channel

    if ctx.voice_client:
        await ctx.voice_state.voice.move_to(destination)

    voice_client = await destination.connect()
    voice_region = voice_client.channel.rtc_region

    await Playback.handle_playback(voice_client, voice_region, True, game)


@client.command(name='leave', pass_context=True, aliases=['recall', 'dismiss'], help="Tell me to leave a Voice Channel")
async def _leave(ctx):
    voice_client = ctx.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandInvokeError):
        print(error)

try:
    client.run(Globals.TOKEN)
except:
    print("Failed to start bot")
