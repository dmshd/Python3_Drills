"""
This script fetches a YouTube video from a distant server and saves it locally.
"""
import json
import logging
import os
import re
import subprocess
import sys
import urllib

import pytube

# Initiate logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


def get_yt_video_title(video_id):
    """
    Get and return the title of a YouTube video using the YouTube API.
    """
    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={API_KEY}"
    with urllib.request.urlopen(url) as response:
        data = response.read()
        data = json.loads(data)
        title = data["items"][0]["snippet"]["title"]
        response.close()
        return title


def to_filename(s: str) -> str:
    """
    Convert a string to a valid filename.
    """
    # Replace spaces with underscores
    s = s.replace(" ", "_")
    # Remove all non-alphanumeric characters
    s = re.sub(r"[^a-zA-Z0-9._-]", "", s)
    # Truncate the string to 255 characters max
    s = s[:255]
    return s


# Check that there is an argument
if len(sys.argv) != 2:
    logger.info("Usage: python youtube_fetch_distant_video_locally.py <video_id>")
    VIDEO_ID = None
    while not VIDEO_ID:
        VIDEO_ID = input("Video ID: ")
        logger.info(f"Video ID: {VIDEO_ID}")
else:
    # Retrieve the video ID from the arguments
    VIDEO_ID = sys.argv[1]
    # Check that it is a valid video ID
    logger.info(f"Video ID: {VIDEO_ID}")

# Create the folder to store the video
if not os.path.exists("./youtube_videos"):
    os.mkdir("./youtube_videos")

# Retrieve the video from YouTube
video_url = f"https://www.youtube.com/watch?v={VIDEO_ID}"
yt = pytube.YouTube(video_url)  # <pytube.__main__.YouTube object: videoId=nPDk5qPbf08>

# Select the highest quality video stream
video_streams = yt.streams.filter(mime_type="video/mp4").order_by("resolution")
video_stream = None
for stream in video_streams:
    if stream.resolution == "1080p":
        video_stream = stream
        break
for stream in video_streams:
    if stream.resolution == "720p":
        video_stream = stream
        break
if not video_stream:
    video_stream = video_streams.first()

# # Create a folder to store the video usind the video ID
# if not os.path.exists(f"./youtube_videos/{VIDEO_ID}"):
#     os.mkdir(f"./youtube_videos/{VIDEO_ID}")

# Create a folder to store the video using the video title
API_KEY = "API_KEY"
YOUTUBE_API_URL = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={VIDEO_ID}&key={API_KEY}"
video_title = get_yt_video_title(VIDEO_ID)
video_title = to_filename(video_title)

# Check that the video file is not already present and that the file contains something
if os.path.exists(f"./youtube_videos/{video_title}/{video_stream.default_filename}"):
    if os.path.getsize(f"./youtube_videos/{video_title}/{video_stream.default_filename}") > 0:
        logger.info("Video file already downloaded")
    else:
        logger.info("Video file is empty, downloading again")
        video_stream.download(f"./youtube_videos/{video_title}")
else:
    logger.info("Downloading video file")
    video_stream.download(f"./youtube_videos/{video_title}")


# Check that the audio file is not already present and that the file contains something
audio_stream = yt.streams.filter(only_audio=True).order_by("abr").last()
# breakpoint()
if os.path.exists(f"./youtube_videos/{video_title}/{audio_stream.default_filename}"):
    if os.path.getsize(f"./youtube_videos/{video_title}/{audio_stream.default_filename}") > 0:
        logger.info("Audio file already downloaded")
    else:
        logger.info("Audio file is empty, downloading again")
        audio_stream.download(f"./youtube_videos/{video_title}")
else:
    logger.info("Downloading audio file")
    audio_stream.download(f"./youtube_videos/{video_title}")


# Use ffmpeg to mergethe video and audio streams
logger.info("Merging video and audio streams using ffmpeg...")
subprocess.run(
    [
        "ffmpeg",
        "-y",
        "-loglevel",
        "quiet",
        "-i",
        f"./youtube_videos/{video_title}/{video_stream.default_filename}",
        "-i",
        f"./youtube_videos/{video_title}/{audio_stream.default_filename}",
        "-c",
        "copy",
        f"./youtube_videos/{video_title}/{video_stream.default_filename[:-4]}_merged.mp4",
    ]
)

# Delete the video and audio files
logger.info("Deleting video and audio files...")
os.remove(f"./youtube_videos/{video_title}/{video_stream.default_filename}")
os.remove(f"./youtube_videos/{video_title}/{audio_stream.default_filename}")

# Rename the merged video file
os.rename(
    f"./youtube_videos/{video_title}/{video_stream.default_filename[:-4]}_merged.mp4",
    f"./youtube_videos/{video_title}/{video_stream.default_filename}",
)

# List the files in the folder to check that the video and audio files have been deleted
logger.info("Files in the folder:")
for file in os.listdir(f"./youtube_videos/{video_title}"):
    logger.info(f"└ {file}")

"""
YouTube video object.

Attributes:
    age_restricted (bool): A boolean indicating whether the video is age-restricted.
    author (str): The author of the video.
    bypass_age_gate (bool): A boolean indicating whether the age-restricted status of the video should be bypassed.
    caption_tracks (list): A list of caption tracks for the video.
    captions (list): A list of captions for the video.
    channel_id (str): The ID of the channel that uploaded the video.
    channel_url (str): The URL of the channel that uploaded the video.
    description (str): The description of the video.
    embed_html (str): The HTML code for embedding the video.
    embed_url (str): The URL for embedding the video.
    fmt_streams (list): A list of available streams for the video.
    initial_data (str): The initial data for the video.
    js (str): The JavaScript for the video.
    js_url (str): The URL of the JavaScript for the video.
    keywords (list): A list of keywords for the video.
    length (int): The length of the video in seconds.
    metadata (str): The metadata for the video.
    publish_date (str): The date when the video was published.
    rating (float): The rating for the video.
    stream_monostate (str): The monostate for the video's streams.
    streaming_data (str): The streaming data for the video.
    streams (list): A list of streams for the video.
    thumbnail_url (str): The URL of the thumbnail image for the video.
    title (str): The title of the video.
    use_oauth (bool): A boolean indicating whether OAuth should be used to access the video.
    vid_info (str): The video info for the video.
    video_id (str): The ID of the video.
    views (int): The number of views for the video.
    watch_html (str): The HTML for the video's watch page.
    watch_url (str): The URL of the video's watch page.

Methods:
    check_availability(): Check the availability of the video.
    register_on_complete_callback(callback): Register a callback function to be called when the video has finished loading.
    register_on_progress_callback(callback): Register a callback function to be called when the video's loading progress changes.
"""
