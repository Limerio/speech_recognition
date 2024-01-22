import asyncio
import random

from winrt.windows.media.control import \
    GlobalSystemMediaTransportControlsSessionManager as MediaManager

def run(args, response):
  
  control = args[0].lower()

  if control in response:
    if control == "status":
        current_media_info = asyncio.run(get_media_info())
        return random.choice(response["status"]).replace('[music]', current_media_info["title"]).replace('[artist]', current_media_info["album_artist"])
    elif control == "pause" or control == "resume":
        asyncio.run(toggle_music())
        return random.choice(response[control])

  return "Music task"

TARGET_ID = ""

async def toggle_music():
    sessions = await MediaManager.request_async()
    current_session = sessions.get_current_session()
    if current_session:  # there needs to be a media session running
        # if current_session.source_app_user_model_id == TARGET_ID:
          # if current_session.playback_status == 4:
            await current_session.try_toggle_play_pause_async()

async def get_media_info():
    sessions = await MediaManager.request_async()

    # This source_app_user_model_id check and if statement is optional
    # Use it if you want to only get a certain player/program's media
    # (e.g. only chrome.exe's media not any other program's).

    # To get the ID, use a breakpoint() to run sessions.get_current_session()
    # while the media you want to get is playing.
    # Then set TARGET_ID to the string this call returns.

    current_session = sessions.get_current_session()
    if current_session:  # there needs to be a media session running
        # if current_session.source_app_user_model_id == TARGET_ID:
            info = await current_session.try_get_media_properties_async()

            # song_attr[0] != '_' ignores system attributes
            info_dict = {song_attr: info.__getattribute__(
                song_attr) for song_attr in dir(info) if song_attr[0] != '_'}

            # converts winrt vector to list
            info_dict['genres'] = list(info_dict['genres'])

            return info_dict

    # It could be possible to select a program from a list of current
    # available ones. I just haven't implemented this here for my use case.
    # See references for more information.
    raise Exception('TARGET_PROGRAM is not the current media session')
