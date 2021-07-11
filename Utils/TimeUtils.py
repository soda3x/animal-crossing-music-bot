"""This module contains all time and timezone related logic"""
import pytz
import datetime as dt
from Utils import Mappings
from discord import VoiceRegion

def get_timezone_from_voice_region(voice_region: VoiceRegion) -> str:
    """Get Timezone From Voice Region"""
    if voice_region != None:
        return Mappings.region_tz[voice_region]
    else:
        return "Australia/Adelaide"

def get_local_time(timezone: str):
    """Convert UTC time to local time based on input timezone tz string"""
    utc_datetime = dt.datetime.utcnow()
    if timezone != None:
        tz = pytz.timezone(timezone)
        converted_datetime = utc_datetime.replace(
            tzinfo=pytz.utc).astimezone(tz)
        print("UTC Time:", utc_datetime)
        print("Converted Time to", timezone, ":", converted_datetime)
        return converted_datetime
    else:
        print("No timezone given, defaulting to UTC time")
        return utc_datetime
        