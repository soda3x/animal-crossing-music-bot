import Playback

_kk_prepared: bool = False

def is_kk_playing(converted_datetime, queue: list):
    """KK Slider, in Animal Crossing New Leaf, plays on Saturdays between 8:00pm and 12:00am, This function determines whether he is currently playing or not in the current Timezone"""
    if (converted_datetime.strftime('%A') == 'Saturday' and converted_datetime.hour >= 20) and not _kk_prepared:
        print('Preparing KK Slider performance')
        queue[:] = prepare_kk()
    return (converted_datetime.strftime('%A') == 'Saturday' and converted_datetime.hour >= 20) and queue

def prepare_kk():
    """Initialise KK Slider playlist"""
    global _kk_prepared
    _kk_prepared = True
    return Playback.create_playlist('./music/kk', True)

def is_kk_prepared():
    return _kk_prepared

def set_kk_prepared(prepared: bool):
    global _kk_prepared
    _kk_prepared = prepared