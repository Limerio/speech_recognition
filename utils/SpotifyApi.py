from dotenv import load_dotenv
from spotipy import Spotify, SpotifyOAuth

load_dotenv()


class SpotifyApi():
    def __init__(self) -> None:
        self.spotify = Spotify(auth_manager=SpotifyOAuth(
            scope=('user-modify-playback-state')))

    def next_track(self):
        self.spotify.next_track()

    def pause_track(self):
        self.spotify.pause_playback()

    def resume_track(self):
        self.spotify.start_playback()

    def previous_track(self):
        self.spotify.previous_track()
