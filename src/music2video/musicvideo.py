# from megaprint import Printer
from subprocess import run
from pathlib import Path


class MusicVideo:
    def __init__(
        self,
        music_file: Path,
        cover_file: Path,
        song_title: str = None,
        song_album: str = None,
        song_artist: str = None,
        output_basename_format: str = "[ARTIST] TITLE",
        ffprobe_path: Path = Path("ffprobe"),
    ):
        self.ffprobe_path: Path = ffprobe_path
        self.music_file: Path = music_file
        self.cover_file: Path = cover_file
        # Get the song title from the music file, unless specified
        if song_title:
            self.song_title: str = song_title
        else:
            self.song_title: str = str(
                run(
                    [
                        self.ffprobe_path,
                        "-v",
                        "error",
                        "-show_entries",
                        "format_tags=title",
                        "-of",
                        "default=nw=1:nk=1",
                        self.music_file,
                    ],
                    capture_output=True,
                )
                .stdout.decode()
                .replace("\n", "")
            )
        # Get the song album from the music file, unless specified
        if song_album:
            self.song_album: str = song_album
        else:
            self.song_album: str = str(
                run(
                    [
                        self.ffprobe_path,
                        "-v",
                        "error",
                        "-show_entries",
                        "format_tags=album",
                        "-of",
                        "default=nw=1:nk=1",
                        self.music_file,
                    ],
                    capture_output=True,
                )
                .stdout.decode()
                .replace("\n", "")
            )
        # Get the song artist from the music file, unless specified
        if song_artist:
            self.song_artist: str = song_artist
        else:
            self.song_artist: str = str(
                run(
                    [
                        self.ffprobe_path,
                        "-v",
                        "error",
                        "-show_entries",
                        "format_tags=album_artist",
                        "-of",
                        "default=nw=1:nk=1",
                        self.music_file,
                    ],
                    capture_output=True,
                )
                .stdout.decode()
                .replace("\n", "")
            )
        self.output_basename: str = output_basename_format
        self.output_basename = (
            self.output_basename.replace("ARTIST", self.song_artist)
            .replace("TITLE", self.song_title)
            .replace("ALBUM", self.song_album)
        )
