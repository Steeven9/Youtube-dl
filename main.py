from argparse import ArgumentParser

from pytube import Playlist

from downloader import download

# folder where to put the files in
# (playlists create subfolders with the playlist title)
OUTPUT_PATH = "files"


def youtube_dl(url: str, convert_mp3: bool) -> int:
    success_count = 0

    if "playlist" in url.lower():
        playlist = Playlist(url)
        print(f"📚 Playlist: {playlist.title}")
        urls = playlist.video_urls
        output_path = f"{OUTPUT_PATH}/{playlist.title}"
    else:
        urls = [url]
        output_path = OUTPUT_PATH

    print("=====================================================")

    for url in urls:
        success = download(url, convert_mp3, output_path)
        if success:
            success_count += 1

    print("=====================================================")
    print(f"✅ Done! {success_count} \
{'element' if success_count == 1 else 'elements'} processed, \
{len(urls) - success_count} ignored")

    return success_count


if __name__ == "__main__":
    parser = ArgumentParser(
        description=
        'Quickly and easily download audio or video files from YouTube')
    parser.add_argument('url', help='URL of the video or playlist')
    parser.add_argument('-c',
                        '--convert',
                        action='store_true',
                        help='convert video(s) to MP3 format')
    arguments = parser.parse_args()

    print(f"📝 Input URL: {arguments.url}")
    print(f"📝 Convert to MP3: {arguments.convert}")

    youtube_dl(arguments.url, arguments.convert)
