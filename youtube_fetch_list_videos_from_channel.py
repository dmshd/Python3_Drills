"""
Retrieve a list of YouTube video titles from a YouTube channel using pytube
"""

import pytube

# Get the channel
channel = pytube.Channel("https://www.youtube.com/c/CryptoCred")

# Access the list of videos
videos = channel.videos

breakpoint()
