from src.music2video.musicvideo import MusicVideo
from pathlib import Path
import math
from subprocess import run


class VideoGenerator:
    def __init__(
        self,
        vidinfo: MusicVideo,
        ffmpeg_path: Path = Path("ffmpeg").expanduser(),
        output_directory: Path = Path("~/Videos/").expanduser(),
        display_text: str = None,
        display_text_position: str = "top",
        display_text_font: str = "Noto Sans",
        vertical_resolution: int = 1080,
        video_fps: float = 0.5,
        video_codec_parameters: str = "libx264 -qp 20",
        audio_codec_parameters: str = "flac",
        video_file_container: str = "mkv",
        added_video_end_length: int = 0,
    ):
        self.vidinfo: MusicVideo = vidinfo
        self.ffmpeg_path: str = str(ffmpeg_path)
        self.video_fps: float = video_fps
        self.vertical_resolution: int = vertical_resolution
        self.display_text: str = display_text
        self.end_padding: int = int(added_video_end_length)
        self.font_pos: str
        # Create the ffmpeg command, to be used by run()
        self.beginning_command_fragment: list() = [
            self.ffmpeg_path,
            "-y",
            "-hide_banner",
            "-loglevel",
            "error",
        ]
        self.file_command_fragment: list() = [
            "-loop",
            "1",
            "-framerate",
            str(self.video_fps),
            "-i",
            f"file:{str(self.vidinfo.cover_file)}",
            "-t",
            str(math.ceil(float(vidinfo.song_length) + self.end_padding)),
            "-i",
            f"file:{str(self.vidinfo.music_file)}",
            "-t",
            str(math.ceil(float(vidinfo.song_length) + self.end_padding)),
        ]
        self.filter_command_fragment: list() = [
            "-filter_complex",
        ]
        self.filter_list: str = (
            f"[0:v]scale=-2:{str(self.vertical_resolution)},setsar=1:1[video]"
        )
        if self.display_text != None:
            self.display_text = (
                self.display_text.replace("ARTIST", vidinfo.song_artist)
                .replace("TITLE", vidinfo.song_title)
                .replace("ALBUM", vidinfo.song_album)
            )
            match display_text_position:
                case "top":
                    self.font_pos = "x=(w-text_w)/2:y=(text_h/2)"
                case "bottom":
                    self.font_pos = "x=(w-text_w)/2:y=(h-text_h)-text_h/2"
                case _:
                    print("incorrect display text position")
                    exit(1)

            self.filter_list += f";[video]drawtext=text={self.display_text}:font={display_text_font}:fontsize=h/42:fontcolor=white:{self.font_pos}:expansion=none[video]"
        self.filter_command_fragment.append(self.filter_list)
        self.encoder_command_fragment: list() = [
            "-map",
            "[video]",
            "-map",
            "1:a",
            "-c:v",
        ]
        self.encoder_command_fragment.extend(video_codec_parameters.split())
        self.encoder_command_fragment.append("-c:a")
        self.encoder_command_fragment.extend(audio_codec_parameters.split())
        self.final_command_fragment: list() = [
            # "-shortest",
            # "-fflags",
            # "shortest",
            "-max_interleave_delta",
            "200M",
            f"{str(Path.joinpath(output_directory, str(vidinfo.output_basename + '.' + video_file_container)))}",
        ]

    def make_video(self):
        return run(
            args=[
                *(
                    self.beginning_command_fragment
                    + self.file_command_fragment
                    + self.filter_command_fragment
                    + self.encoder_command_fragment
                    + self.final_command_fragment
                )
            ],
            capture_output=True,
        )
