# Youtube-dl

Quickly and easily download audio or video files from YouTube.

Features:

- 100% free, no ads, no license needed
- automagical AI-based playlist detection
- fast as hek (compared to other similar softwares)

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Youtube-dl can be run from the command line:

```bash
python main.py https://www.youtube.com/watch?v=QsdxE02o4Zo --convert
```

Or also imported in another script:

```python
from main import youtube_dl 

youtube_dl("https://www.youtube.com/watch?v=QsdxE02o4Zo", True)
```

## Credits

This project uses:

- [moviepy](https://zulko.github.io/moviepy), a Python module for video processing
- [pytube](https://pytube.io), a lightweight library for downloading YouTube videos
