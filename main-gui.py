#!/usr/bin/env python
import PySimpleGUI as sg

sg.theme("Dark Amber")
layout = [
    [sg.Text("WIP Gui for music2video", size=64, justification="center")],
    [
        sg.Text("Container Format"),
        sg.DropDown(
            ["mkv", "webp", "mp4"],
            key="-SELECTION-",
            readonly=True,
            default_value="mkv",
            size=8,
        ),
        sg.Text("FPS"),
        sg.DropDown(
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
]

window = sg.Window("music2video GUI", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    # if event == "-MUSIC_SELECT-":
    # window["-MUSIC_STRING-"].update(values["-MUSIC_SELECT-"])
    #   print(window["-MUSIC_STRING-"])
