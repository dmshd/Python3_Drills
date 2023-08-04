"""
Get the title of a YouTube video using the YouTube API.
"""
import json
import logging
import re
import urllib.request

# Initiate logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

video_id = "nPDk5qPbf08"
API_KEY = "API_KEY"

url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={API_KEY}"


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


if __name__ == "__main__":
    title = get_yt_video_title(video_id)
    logger.info(f"Title: {title}")
    filename = to_filename(title)
    logger.info(f"Filename: {filename}")
