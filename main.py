#!/usr/bin/env python
import argparse, configparser, sys
from pathlib import Path
from src.music2video.megaprint import Printer
from src.music2video.musicvideo import MusicVideo
from src.music2video.generator import VideoGenerator

# Basic driver for project
if __name__ == "__main__":
    # Pretty printing!
    p = Printer(logging_level=3, show_timestamp=True)
    # Gather and calculate the data needed to create the video
    vidinfo = MusicVideo(
        music_file=Path("song.mp3").expanduser(),
        cover_file=Path("image.webp").expanduser(),
        output_basename_format="⟦ARTIST⟧ ❰TITLE❱",
        # song_title="TestTitle",
        # song_artist="TestArtist",
        # song_album="TestAlbum",
    )
    # Prepare for video creation
    vidgen = VideoGenerator(vidinfo, display_text="TITLE")
    p.p(3, f"Song: {vidinfo.song_title}")
    p.p(3, f"Album: {vidinfo.song_album}")
    p.p(3, f"Artist: {vidinfo.song_artist}")
    p.p(3, f"Output Basename: {vidinfo.output_basename}")
    p.p(3, f"Song Length: {vidinfo.song_length} seconds")
    p.p(
        3,
        f"FFMPEG Command: {' '.join(vidgen.beginning_command_fragment + vidgen.file_command_fragment + vidgen.filter_command_fragment + vidgen.encoder_command_fragment + vidgen.final_command_fragment)}",
    )
    p.p(3, f"Generating Video")
    p.p(3, vidgen.make_video().stdout.decode())
    # p.p(1, "A sample error message!")
    # p.p(2, "A sample warning message!")
    # p.p(3, "A sample info message!")
    p.p(3, f"Done!")
    exit(0)
