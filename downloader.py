from os import remove
from urllib.error import URLError

from moviepy.editor import VideoFileClip
from pytube import YouTube
from pytube.exceptions import AgeRestrictedError, RegexMatchError

OUTPUT_PATH = "files"


def convert_to_mp3(filename: str) -> None:
    clip = VideoFileClip(filename)
    clip.audio.write_audiofile(f"{filename[:-4]}.mp3")
    clip.close()


def download(url: str, convert_mp3: bool) -> None:
    try:
        video = YouTube(url)
    except RegexMatchError:
        print(f"❌ Skipping invalid URL: {url}")
        return
    except URLError:
        print(f"⛔ Skipping unreachable URL: {url}")
        return

    print(f"⏬ Downloading {video.title}")
    try:
        stream = video.streams.get_highest_resolution()
    except AgeRestrictedError:
        print(f"🔞 Skipping age-restricted URL: {url}")
        return
    filepath = stream.download(output_path=OUTPUT_PATH, max_retries=1)

    if convert_mp3:
        print(f"♻️  Converting {video.title}")
        convert_to_mp3(filepath)
        remove(filepath)
