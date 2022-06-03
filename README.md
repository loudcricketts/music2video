# music2video
A python package and program that will generate a customizable still-image music video with your provided files.

```
usage: main.py [-h] [-m FILE] [-i FILE] [--title TRACK_TITLE] [--artist TRACK_ARTIST] [--album TRACK_ALBUM] [--format CUSTOM_FORMAT_STRING]
               [--ffprobe CUSTOM_FFPROBE_PATH] [--ffmpeg CUSTOM_FFMPEG_PATH] [--outdir OUTPUT_DIRECTORY] [--fps FPS_FLOAT]
               [--vres VERTICAL_RESOLUTION_INT] [--display-text TEXT] [--font FONT_NAME] [--pos TEXT_POSITION] [--video-codec VIDEO_CODEC_PARAMS]
               [--audio-codec AUDIO_CODEC_PARAMS] [--container FILE_CONTAINER] [--end-padding PADDING_IN_SECONDS]

Quickly create still image music videos

options:
  -h, --help            show this help message and exit
  -m FILE, --music-file FILE
                        Path to the song to use
  -i FILE, --image-file FILE
                        Path to the image to use
  --title TRACK_TITLE   Optional title override
  --artist TRACK_ARTIST
                        Optional artist override
  --album TRACK_ALBUM   Optional album override
  --format CUSTOM_FORMAT_STRING
                        Create a custom output format (Use TITLE, ARTIST, ALBUM as placeholders.)
  --ffprobe CUSTOM_FFPROBE_PATH
                        Use a custom path for ffprobe.
  --ffmpeg CUSTOM_FFMPEG_PATH
                        Use a custom path for ffmpeg.
  --outdir OUTPUT_DIRECTORY
                        Output directory for videos
  --fps FPS_FLOAT       FPS for output video (Can be below 1!)
  --vres VERTICAL_RESOLUTION_INT
                        Vertical Resolution for video (e.g. 480, 720, 1080)
  --display-text TEXT   Create a custom embeded text field on video (Use TITLE, ARTIST, ALBUM as placeholders.)
  --font FONT_NAME      Use a particular font for display text
  --pos TEXT_POSITION   Where to display the text ("top" or "bottom")
  --video-codec VIDEO_CODEC_PARAMS
                        Use the specified encoder with parameters (e.g. "libx264 -qp 20")
  --audio-codec AUDIO_CODEC_PARAMS
                        Use the specified encoder with parameters (e.g. "flac")
  --container FILE_CONTAINER
                        Use the specified container format (mkv is a good choice)
  --end-padding PADDING_IN_SECONDS
                        Add extra time to the end of the video
```

## Planned Features
- Optional Config
- ~~Arguments~~
- ~~Custom output filenames.~~
- ~~Custom ffmpeg/ffplay executable paths.~~
- ~~Custom video encoding arguments.~~
- ~~Custom text displaying on the video.~~
- ~~A very beautiful and optionally verbose console output.~~
- ... And more than I can currently recall.

## Known Issues
- The current ffprobe-based implementation for grabbing the tags seems to have trouble with certain files.