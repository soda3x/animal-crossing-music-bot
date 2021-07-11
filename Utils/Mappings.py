from discord import VoiceRegion

#
# Convenient way of select ACNL hourly song based on the current hour returned from datetime.hour
#
#
acnl_path = {
    "0": "./music/nl/0000.mp3",
    "1": "./music/nl/0100.mp3",
    "2": "./music/nl/0200.mp3",
    "3": "./music/nl/0300.mp3",
    "4": "./music/nl/0400.mp3",
    "5": "./music/nl/0500.mp3",
    "6": "./music/nl/0600.mp3",
    "7": "./music/nl/0700.mp3",
    "8": "./music/nl/0800.mp3",
    "9": "./music/nl/0900.mp3",
    "10": "./music/nl/1000.mp3",
    "11": "./music/nl/1100.mp3",
    "12": "./music/nl/1200.mp3",
    "13": "./music/nl/1300.mp3",
    "14": "./music/nl/1400.mp3",
    "15": "./music/nl/1500.mp3",
    "16": "./music/nl/1600.mp3",
    "17": "./music/nl/1700.mp3",
    "18": "./music/nl/1800.mp3",
    "19": "./music/nl/1900.mp3",
    "20": "./music/nl/2000.mp3",
    "21": "./music/nl/2100.mp3",
    "22": "./music/nl/2200.mp3",
    "23": "./music/nl/2300.mp3"
}

#
# Convenient way of select AC hourly song based on the current hour returned from datetime.hour
#
#
acgc_path = {
    "0": "./music/gc/0000.mp3",
    "1": "./music/gc/0100.mp3",
    "2": "./music/gc/0200.mp3",
    "3": "./music/gc/0300.mp3",
    "4": "./music/gc/0400.mp3",
    "5": "./music/gc/0500.mp3",
    "6": "./music/gc/0600.mp3",
    "7": "./music/gc/0700.mp3",
    "8": "./music/gc/0800.mp3",
    "9": "./music/gc/0900.mp3",
    "10": "./music/gc/1000.mp3",
    "11": "./music/gc/1100.mp3",
    "12": "./music/gc/1200.mp3",
    "13": "./music/gc/1300.mp3",
    "14": "./music/gc/1400.mp3",
    "15": "./music/gc/1500.mp3",
    "16": "./music/gc/1600.mp3",
    "17": "./music/gc/1700.mp3",
    "18": "./music/gc/1800.mp3",
    "19": "./music/gc/1900.mp3",
    "20": "./music/gc/2000.mp3",
    "21": "./music/gc/2100.mp3",
    "22": "./music/gc/2200.mp3",
    "23": "./music/gc/2300.mp3"
}

#
# Convenient way of select ACCF hourly song based on the current hour returned from datetime.hour
#
#
accf_path = {
    "0": "./music/cf/0000.mp3",
    "1": "./music/cf/0100.mp3",
    "2": "./music/cf/0200.mp3",
    "3": "./music/cf/0300.mp3",
    "4": "./music/cf/0400.mp3",
    "5": "./music/cf/0500.mp3",
    "6": "./music/cf/0600.mp3",
    "7": "./music/cf/0700.mp3",
    "8": "./music/cf/0800.mp3",
    "9": "./music/cf/0900.mp3",
    "10": "./music/cf/1000.mp3",
    "11": "./music/cf/1100.mp3",
    "12": "./music/cf/1200.mp3",
    "13": "./music/cf/1300.mp3",
    "14": "./music/cf/1400.mp3",
    "15": "./music/cf/1500.mp3",
    "16": "./music/cf/1600.mp3",
    "17": "./music/cf/1700.mp3",
    "18": "./music/cf/1800.mp3",
    "19": "./music/cf/1900.mp3",
    "20": "./music/cf/2000.mp3",
    "21": "./music/cf/2100.mp3",
    "22": "./music/cf/2200.mp3",
    "23": "./music/cf/2300.mp3"
}

#
# Convenient way of select ACNH hourly song based on the current hour returned from datetime.hour
#
#
acnh_path = {
    "0": "./music/nh/0000.mp3",
    "1": "./music/nh/0100.mp3",
    "2": "./music/nh/0200.mp3",
    "3": "./music/nh/0300.mp3",
    "4": "./music/nh/0400.mp3",
    "5": "./music/nh/0500.mp3",
    "6": "./music/nh/0600.mp3",
    "7": "./music/nh/0700.mp3",
    "8": "./music/nh/0800.mp3",
    "9": "./music/nh/0900.mp3",
    "10": "./music/nh/1000.mp3",
    "11": "./music/nh/1100.mp3",
    "12": "./music/nh/1200.mp3",
    "13": "./music/nh/1300.mp3",
    "14": "./music/nh/1400.mp3",
    "15": "./music/nh/1500.mp3",
    "16": "./music/nh/1600.mp3",
    "17": "./music/nh/1700.mp3",
    "18": "./music/nh/1800.mp3",
    "19": "./music/nh/1900.mp3",
    "20": "./music/nh/2000.mp3",
    "21": "./music/nh/2100.mp3",
    "22": "./music/nh/2200.mp3",
    "23": "./music/nh/2300.mp3"
}

#
# region_tz maps Discord's VoiceRegion to a TZ Timezone as best as possible
# this is used when the bot needs to select a timezone
#
region_tz = {
    VoiceRegion.amsterdam: "Europe/Amsterdam",
    VoiceRegion.brazil: "America/Sao_Paulo",
    VoiceRegion.dubai: "Asia/Dubai",
    VoiceRegion.eu_central: "Europe/Prague",
    VoiceRegion.eu_west: "Europe/London",
    VoiceRegion.europe: "Europe/Prague",
    VoiceRegion.frankfurt: "Europe/Zurich",
    VoiceRegion.hongkong: "Asia/Hong_Kong",
    VoiceRegion.india: "Asia/Kolkata",
    VoiceRegion.japan: "Asia/Tokyo",
    VoiceRegion.london: "Europe/London",
    VoiceRegion.russia: "Europe/Moscow",
    VoiceRegion.singapore: "Asia/Singapore",
    VoiceRegion.southafrica: "Africa/Johannesburg",
    VoiceRegion.south_korea: "Asia/Seoul",
    VoiceRegion.sydney: "Australia/Sydney",
    VoiceRegion.us_central: "America/Toronto",
    VoiceRegion.us_east: "America/New_York",
    VoiceRegion.us_south: "America/Toronto",
    VoiceRegion.us_west: "America/Los_Angeles",
    VoiceRegion.vip_amsterdam: "Europe/Amsterdam",
    VoiceRegion.vip_us_east: "America/New_York",
    VoiceRegion.vip_us_west: "America/Los_Angeles"
}
