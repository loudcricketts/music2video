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
        ffprobe_path: Path = Path("ffprobe").expanduser(),
    ):
        self.ffprobe_path: str = str(ffprobe_path)
        self.music_file: str = str(music_file)
        self.cover_file: str = str(cover_file)
        # Get the length of the song
        self.song_length: float = (
            run(
                [
                    self.ffprobe_path,
                    "-i",
                    self.music_file,
                    "-show_entries",
                    "format=duration",
                    "-v",
                    "quiet",
                    "-of",
                    "csv=p=0",
                ],
                capture_output=True,
            )
            .stdout.decode()
            .replace("\n", "")
            .replace("\r", "")
        )
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
                        "default=noprint_wrappers=1:nokey=1",
                        self.music_file,
                    ],
                    capture_output=True,
                )
                .stdout.decode()
                .replace("\n", "")
                .replace("\r", "")
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
                .replace("\r", "")
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
                .replace("\r", "")
            )
        # Album Artist doesn't exist, so using Artist
        if not song_artist:
            self.song_artist: str = str(
                run(
                    [
                        self.ffprobe_path,
                        "-v",
                        "error",
                        "-show_entries",
                        "format_tags=artist",
                        "-of",
                        "default=nw=1:nk=1",
                        self.music_file,
                    ],
                    capture_output=True,
                )
                .stdout.decode()
                .replace("\n", "")
                .replace("\r", "")
            )

        # Format the basename according to the input provided
        self.output_basename: str = (
            output_basename_format.replace("ARTIST", self.song_artist)
            .replace("TITLE", self.song_title)
            .replace("ALBUM", self.song_album)
        )
