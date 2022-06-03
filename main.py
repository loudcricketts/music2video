#!/usr/bin/env python
import argparse, configparser, sys
from ast import parse
from pathlib import Path

from click import argument
from src.music2video.megaprint import Printer
from src.music2video.musicvideo import MusicVideo
from src.music2video.generator import VideoGenerator


def parseArguments() -> argparse.Namespace:
    parse = argparse.ArgumentParser(
        description="Quickly create still image music videos"
    )
    parse.add_argument(
        "-m",
        "--music-file",
        metavar="FILE",
        help="Path to the song to use",
        default="song.mp3",
    )
    parse.add_argument(
        "-i",
        "--image-file",
        metavar="FILE",
        help="Path to the image to use",
        default="image.webp",
    )
    parse.add_argument(
        "--title",
        metavar="TRACK_TITLE",
        help="Optional title override",
        default=None,
    )
    parse.add_argument(
        "--artist",
        metavar="TRACK_ARTIST",
        help="Optional artist override",
        default=None,
    )
    parse.add_argument(
        "--album",
        metavar="TRACK_ALBUM",
        help="Optional album override",
        default=None,
    )
    parse.add_argument(
        "--format",
        metavar="CUSTOM_FORMAT_STRING",
        help="Create a custom output format (Use TITLE, ARTIST, ALBUM as placeholders.)",
        default="[ARTIST] TITLE",
    )
    parse.add_argument(
        "--ffprobe",
        metavar="CUSTOM_FFPROBE_PATH",
        help="Use a custom path for ffprobe.",
        default="ffprobe",
    )
    parse.add_argument(
        "--ffmpeg",
        metavar="CUSTOM_FFMPEG_PATH",
        help="Use a custom path for ffmpeg.",
        default="ffmpeg",
    )
    parse.add_argument(
        "--outdir",
        metavar="OUTPUT_DIRECTORY",
        help="Output directory for videos",
        default="~/Videos",
    )
    parse.add_argument(
        "--fps",
        metavar="FPS_FLOAT",
        help="FPS for output video (Can be below 1!)",
        default=0.5,
    )
    parse.add_argument(
        "--vres",
        metavar="VERTICAL_RESOLUTION_INT",
        help="Vertical Resolution for video (e.g. 480, 720, 1080)",
        default=1080,
    )
    parse.add_argument(
        "--display-text",
        metavar="TEXT",
        help="Create a custom embeded text field on video (Use TITLE, ARTIST, ALBUM as placeholders.)",
        default="TITLE",
    )
    parse.add_argument(
        "--font",
        metavar="FONT_NAME",
        help="Use a particular font for display text",
        default="Noto Sans",
    )
    parse.add_argument(
        "--pos",
        metavar="TEXT_POSITION",
        help='Where to display the text ("top" or "bottom")',
        default="top",
    )
    parse.add_argument(
        "--video-codec",
        metavar="VIDEO_CODEC_PARAMS",
        help='Use the specified encoder with parameters (e.g. "libx264 -qp 20")',
        default="libx264 -qp 20",
    )
    parse.add_argument(
        "--audio-codec",
        metavar="AUDIO_CODEC_PARAMS",
        help='Use the specified encoder with parameters (e.g. "flac")',
        default="flac",
    )
    parse.add_argument(
        "--container",
        metavar="FILE_CONTAINER",
        help="Use the specified container format (mkv is a good choice)",
        default="mkv",
    )
    parse.add_argument(
        "--end-padding",
        metavar="PADDING_IN_SECONDS",
        help="Add extra time to the end of the video",
        default=0,
    )
    parse.add_argument(
        "--verbosity",
        metavar="VERBOSITY_LEVEL",
        help="How verbose to print (between 0 and 3)",
        default=3,
    )
    parse.add_argument(
        "--timestamps",
        metavar="BOOL",
        help="Show timestamps on output (default True)",
        default=True,
    )
    return parse.parse_args()


# Basic driver for project
if __name__ == "__main__":
    args = parseArguments()
    # Pretty printing!
    p = Printer(logging_level=args.verbosity, show_timestamp=True)
    # Gather and calculate the data needed to create the video
    vidinfo = MusicVideo(
        music_file=Path(args.music_file).expanduser(),
        cover_file=Path(args.image_file).expanduser(),
        output_basename_format=args.format,
        song_title=args.title,
        song_artist=args.artist,
        song_album=args.album,
        ffprobe_path=Path(args.ffprobe).expanduser(),
    )
    # Prepare for video creation
    vidgen = VideoGenerator(
        vidinfo,
        display_text=args.display_text,
        ffmpeg_path=Path(args.ffmpeg).expanduser(),
        output_directory=Path(args.outdir).expanduser(),
        video_fps=float(args.fps),
        vertical_resolution=int(args.vres),
        video_codec_parameters=args.video_codec,
        audio_codec_parameters=args.audio_codec,
        video_file_container=args.container,
        added_video_end_length=args.end_padding,
        display_text_font=args.font,
        display_text_position=args.pos,
    )
    p.p(3, f"Music File: {Path(args.music_file).expanduser()}")
    p.p(3, f"Image File: {Path(args.image_file).expanduser()}")
    p.p(3, f"ffprobe: {vidinfo.ffprobe_path}")
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
    results = vidgen.make_video()
    err_results = results.stderr.decode().splitlines()
    normal_results = results.stdout.decode().splitlines()
    for line in err_results:
        p.p(2, line)
    for line in normal_results:
        p.p(3, line)
    p.p(3, f"Done!")
    exit(0)
