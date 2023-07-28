from pytube import Playlist

from downloader import download

if __name__ == "__main__":
    url = input("📝 Input youtube URL: ")
    mode = input("📝 Convert to MP3? [y/n] ")
    convert_mp3 = mode.lower() == "y"

    if "playlist" in url.lower():
        playlist = Playlist(url)
        print(f"📚 Playlist: {playlist.title}")
        print("=====================================================")

        for url in playlist.video_urls:
            download(url, convert_mp3)
    else:
        download(url, convert_mp3)
