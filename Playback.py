"""This module contains all playback logic such as playing the audio, creating playlists etc."""
from os import listdir
from os.path import isfile, join
from discord.voice_client import VoiceClient
from discord import VoiceRegion
import discord
import asyncio
import random
from Utils import Mappings
from Utils import Globals
from Utils import TimeUtils
import KKSlider

kk_slider_queue = []
aircheck_queue = []
aircheck_playlist_created: bool = False


def create_playlist(path: str, shuffle: bool):
    """Generate a Player Queue from music files in 'path' and whether or not the queue should be shuffled"""
    files = [f for f in listdir(path) if isfile(join(path, f))]
    songs = []

    for f in files:
        songs.append(path + '/' + f)
    if shuffle:
        random.shuffle(songs)
    return songs


def select_next_song(queue: list):
    """Pop Song from Queue and play it"""
    if queue:
        next_song = queue.pop()
        print("Now playing:", next_song)
        return next_song
    else:
        print("Playlist is empty")


def get_next_hourly_song(converted_datetime, game):
    """Return the next hourly song based on the timezone and game"""
    if game == 'cf' or game == 'ww':
        print("Selected Wild World / City Folk audio:",
              Mappings.accf_path[str(converted_datetime.hour)])
        return Mappings.accf_path[str(converted_datetime.hour)]
    elif game == 'gc':
        print("Selected Gamecube audio:",
              Mappings.acgc_path[str(converted_datetime.hour)])
        return Mappings.acgc_path[str(converted_datetime.hour)]
    elif game == 'nh':
        print("Selected New Horizons audio:",
              Mappings.acnh_path[str(converted_datetime.hour)])
        return Mappings.acnh_path[str(converted_datetime.hour)]
    else:
        print("Selected New Leaf audio:",
              Mappings.acnl_path[str(converted_datetime.hour)])
        return Mappings.acnl_path[str(converted_datetime.hour)]


async def handle_playback(voice_client: VoiceClient, voice_region: VoiceRegion, is_playing: bool, selected_game: str = 'nl'):
    """Main audio playback loop"""
    while is_playing:
        if not voice_client.is_playing():
            song = discord.FFmpegPCMAudio(
                executable=Globals.FFMPEG_EXECUTABLE, source=determine_song_to_play(voice_region, selected_game))
            await asyncio.sleep(0.5)
            voice_client.play(song)
        else:
            await asyncio.sleep(1)


def determine_song_to_play(voice_region: VoiceRegion, selected_game: str = 'nl'):
    """Logic to decide which song to play next"""
    global kk_slider_queue
    global aircheck_queue
    song_to_play = ""

    if KKSlider.is_kk_playing(TimeUtils.get_local_time(TimeUtils.get_timezone_from_voice_region(voice_region)), kk_slider_queue):
        song_to_play = select_next_song(kk_slider_queue)

    elif selected_game == 'aircheck':
        if not aircheck_playlist_created:
            aircheck_queue = prepare_aircheck()
        if aircheck_queue:
            song_to_play = select_next_song(aircheck_queue)
        else:
            clear_playlists()

    else:
        clear_playlists()  # We don't want any old playlists here
        # If KK Slider isn't performing, make sure he is not prepared
        KKSlider.set_kk_prepared(False)
        song_to_play = get_next_hourly_song(TimeUtils.get_local_time(
            TimeUtils.get_timezone_from_voice_region(voice_region)), selected_game)

    return song_to_play


def clear_playlists():
    """Reset KK Slider and Aircheck Playlists"""
    global kk_slider_queue
    global aircheck_queue
    global aircheck_playlist_created
    kk_slider_queue = []
    aircheck_queue = []
    aircheck_playlist_created = False


def prepare_aircheck():
    """Initialise Aircheck playlist"""
    global aircheck_playlist_created
    aircheck_playlist_created = True
    return create_playlist('./music/aircheck', True)
