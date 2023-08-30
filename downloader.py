from os import remove
from urllib.error import URLError

from moviepy.editor import VideoFileClip
from pytube import YouTube
from pytube.exceptions import AgeRestrictedError, RegexMatchError


def convert_to_mp3(filename: str) -> None:
    clip = VideoFileClip(filename)
    clip.audio.write_audiofile(f"{filename[:-4]}.mp3", logger=None)
    clip.close()


def download(url: str, convert_mp3: bool, output_path: str) -> bool:
    try:
        video = YouTube(url)
    except RegexMatchError:
        print(f"❌ Skipping invalid URL: {url}")
        return False
    except URLError:
        print(f"⛔ Skipping unreachable URL: {url}")
        return False

    try:
        stream = video.streams.get_highest_resolution()
    except AgeRestrictedError:
        print(f"🔞 Skipping age-restricted video: {video.title}")
        return False
    except RegexMatchError:
        print(f"❌ Cannot download video: {video.title}")
        return False

    print(f"⏬ Downloading {video.title}")
    filepath = stream.download(output_path=output_path, max_retries=1)

    if convert_mp3:
        print(f"♻️  Converting {video.title}")
        convert_to_mp3(filepath)
        remove(filepath)

    return True
