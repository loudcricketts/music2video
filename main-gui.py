#!/usr/bin/env python
import PySimpleGUI as sg
from pathlib import Path
from src.music2video.musicvideo import MusicVideo
from src.music2video.generator import VideoGenerator

sg.theme("Dark Amber")
layout = [
    [sg.Text("WIP Gui for music2video", size=100, justification="center")],
    [
        sg.Text("Container Format"),
        sg.Combo(
            ["mkv", "webp", "mp4"],
            key="-CONTAINER-",
            readonly=True,
            default_value="mkv",
            size=8,
        ),
        sg.Text("FPS"),
        sg.Combo(
            [0.5, 1, 2, 6, 12, 24, 30, 60],
            key="-FPS-",
            readonly=False,
            default_value="1",
            size=8,
        ),
    ],
    [
        sg.Text("Select Song File", size=14),
        sg.FileBrowse(target="-MUSIC_STRING-"),
        sg.Input(
            size=64,
            key="-MUSIC_STRING-",
            default_text="Enter File Path",
        ),
    ],
    [
        sg.Text("Select Image File", size=14),
        sg.FileBrowse(target="-IMAGE_STRING-"),
        sg.Input(
            size=64,
            key="-IMAGE_STRING-",
            default_text="Enter File Path",
        ),
    ],
    [
        sg.Text("Display Text"),
        sg.Input(
            size=32,
            key="-DISPLAY_TEXT-",
            default_text="TITLE",
        ),
    ],
    [sg.Button("Create", key="-CREATE-")],
]

window = sg.Window("music2video GUI", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "-CREATE-":
        print(values)
        vidinfo = MusicVideo(
            music_file=Path(values["-MUSIC_STRING-"]).expanduser(),
            cover_file=Path(values["-IMAGE_STRING-"]).expanduser(),
        )
        vidgen = VideoGenerator(
            vidinfo=vidinfo,
            display_text=values["-DISPLAY_TEXT-"],
            video_fps=values["-FPS-"],
            video_file_container=values["-CONTAINER-"],
        )
        print(vidgen.make_video().stderr.decode())
        print("hello")
