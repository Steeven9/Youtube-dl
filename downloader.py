from pytube import YouTube
from pytube.exceptions import RegexMatchError


def download(url: str, mode: str) -> None:
    try:
        video = YouTube(url)
    except RegexMatchError:
        print(f"Invalid URL: {url}")
        exit(-1)

    print(f"Downloading {video.title}")

    if mode.lower() in ["a", "audio"]:
        stream = video.streams.get_audio_only()
    elif mode.lower() in ["v", "video"]:
        stream = video.streams.get_highest_resolution()
    else:
        print(f"Invalid input: {mode}")
        exit(-1)

    stream.download()
