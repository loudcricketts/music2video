#!/usr/bin/env python
import argparse, configparser, sys
from pathlib import Path
from src.music2video.megaprint import Printer
from src.music2video.musicvideo import MusicVideo

if __name__ == "__main__":
    p = Printer(logging_level=3, show_timestamp=True)
    vidinfo = MusicVideo(music_file=Path("song.flac"), cover_file=Path("setup.cfg"))
    p.p(3, "Song: " + vidinfo.song_title)
    p.p(3, "Album: " + vidinfo.song_album)
    p.p(3, "Artist: " + vidinfo.song_artist)
    p.p(3, vidinfo.output_basename)
    p.p(1, "A sample error message!")
    p.p(2, "A sample warning message!")
    p.p(3, "A sample info message!")
    exit(0)
