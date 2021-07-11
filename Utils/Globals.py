from logging import error

TOKEN = ''
FFMPEG_EXECUTABLE = ''


def validate_globals():
    """Confirm that all required global constants have been set on start-up"""
    error_vector = []
    if TOKEN == '':
        error_vector.append(
            "Be sure to set the TOKEN value in file Globals.py")
    if FFMPEG_EXECUTABLE == '':
        error_vector.append(
            "Be sure to set the FFMPEG_EXECUTABLE value in file Globals.py")
    return error_vector
