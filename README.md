![Animal Crossing Discord Bot](https://raw.githubusercontent.com/soda3x/animal-crossing-music-bot/main/header.png)
 # Animal Crossing Music Bot
 
 ## Discord Bot that plays hourly music from the Animal Crossing games
 
 ### Features
 * Support for all currently released Animal Crossing games (Gamecube, Wild World / City Folk, New Leaf, New Horizons)
 * KK Slider perfomance on Saturdays from 8pm - 12am!
 * Aircheck songs
 * Supports your local timezone! (set by Discord voice channel Region)

 ### Prerequisites
 * discord.py
 * asyncio
 * PyNaCl
 * [FFmpeg](https://ffmpeg.org)

 ### Configuration
 To use this as a Discord bot, first create a Discord application and:
 * Clone this repository
 * In the Utils/Globals.py file, set the `TOKEN` value to your Discord application token
 * In the Utils/Globals.py file, set the `FFMPEG_EXECUTABLE` value to your FFmpeg executable

 ### Usage
 
 By default, the bot's command prefix is `!`
 
 `[acmusic | ac] [game]`
 
 `game` acceptable values are:
 * `gc` Gamecube
 * `ww` Wild World
 * `cf` City Folk
 * `nl` New Leaf
 * `nh` New Horizons
 * `aircheck` Aircheck songs

 If no game argument is given, it will default to New Leaf
 For example, `!acmusic nh`, will play hourly music from the New Horizons game
 
 If it happens to be Saturday and between the hours of 8pm and 12am, no matter which `game` argument is used, KK Slider will perform a private concert just for you and your mates!
 
 ### Seems too hard, I just want the bot in my Server!
 
 Head to [this link](https://discord.com/oauth2/authorize?client_id=863728299053940756&permissions=36769024&scope=bot) and invite the bot to your Server
 
 
