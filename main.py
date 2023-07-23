from pytube import Playlist

from downloader import download

if __name__ == "__main__":
    url = input("Input youtube URL: ")
    mode = input("Download [a]udio or [v]ideo? ")

    if "playlist" in url.lower():
        playlist = Playlist(url)
        print(f"Playlist: {playlist.title}")

        for url in playlist.video_urls:
            download(url, mode)
    else:
        download(url, mode)

    print("Done!")
