"""
https://www.youtube.com/watch?v=nPDk5qPbf08
"""
import json
import logging
import os

from youtube_fetch_video_title import get_yt_video_title
from youtube_transcript_api import YouTubeTranscriptApi

# Initiate logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

import re


def to_filename(s: str) -> str:
    # Replace spaces with underscores
    s = s.replace(" ", "_")

    # Remove all non-alphanumeric characters
    s = re.sub(r"[^a-zA-Z0-9._-]", "", s)

    # Truncate the string to 255 characters max
    s = s[:255]

    return s


# ID of the video
# video_id = "Yp0k8HD5xro"
video_id = "tmeCWULSTHc"


# Get video title
video_title = get_yt_video_title(video_id)

# Transform video title to a valid filename
video_title = to_filename(video_title)
filename = f"subs_{video_title}.txt"

# Write subtitles to a file if it does not exist and if it is not up to date
if os.path.exists(filename) and os.path.isfile(filename):
    logger.error(f"File {filename} already exists locally")
    with open(filename, "r") as f:
        local_data = f.read()
        local_data = json.dumps(local_data)
        f.close()
else:
    # Get video subtitles
    try:
        logger.info("Trying to get subtitles from YouTube API using youtube_transcript_api python package...")
        video_subtitles = YouTubeTranscriptApi.get_transcript(video_id)
    except:
        logger.error("Failed to get subtitles from YouTube API using youtube_transcript_api python package")
        exit(1)
    logger.info("Successfully got subtitles from YouTube")

    # Write subtitles to a file
    try:
        logger.info(f"Writing subtitles to file {filename}...")
        with open(filename, "w") as f:
            for subtitle in video_subtitles:
                # f.write(f"{subtitle['text']}\n")
                f.write(f"{subtitle}\n")
            f.close()
        logger.info(f"Successfully wrote subtitles to file {filename} !")
    except Exception as e:
        logger.error(f"Failed to write subtitles to file {filename} with error: {e}")
        exit(1)
