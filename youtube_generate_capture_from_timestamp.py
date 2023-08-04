"""
Generate a capture from a timestamp in a video
"""
import logging
import os
import re
import sys

# Initiate logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


# Check that there is a timestamp and a video file
if len(sys.argv) != 2:
    logger.error("Usage: python youtube_generate_capture_from_timestamp.py <video_file>")
    sys.exit(1)
# If it is a folder, list the files
if os.path.isdir(sys.argv[1]):
    logger.error("Folder given, listing files")
    for file in os.listdir(sys.argv[1]):
        print(file)
    sys.exit(1)
else:
    # Retrieve the video file from the arguments
    video_file = sys.argv[1]
    # Check that it is a valid file
    if not os.path.isfile(video_file):
        logger.error(f'"{video_file}" is not a file')
        sys.exit(1)
    if not os.path.exists(video_file):
        logger.error(f'Video file "{video_file}" does not exist')
        sys.exit(1)

# Retrieve the timestamp from a terminal prompt instead of args till a valid one is given
timestamp = None
while not timestamp:
    timestamp = input("Timestamp (HH:MM:SS) or (MM:SS): ")
    if not re.match(r"^\d{2}:\d{2}:\d{2}$", timestamp) and not re.match(r"^\d{2}:\d{2}$", timestamp):
        logger.error("Invalid timestamp, must be HH:MM:SS or MM:SS")
        timestamp = None
    else:
        logger.info(f"Timestamp: {timestamp}")

# Generate a part of a filename with the timestamp
timestamp_filename = timestamp.replace(":", "-")
base_filename = video_file.split("/")
base_filename = base_filename[-1]
base_filename, extension = base_filename.split(".")
base_filename = re.sub(r"[^\w]", "_", base_filename)

# Generate a filename for the capture
capture_filename = f"{base_filename}_{timestamp_filename}.webp"

# Extract the capture
import subprocess

logger.info(f"Generating capture {capture_filename} from {video_file} at {timestamp}...")

subprocess.run(
    [
        "ffmpeg",
        "-y",
        "-loglevel",
        "quiet",
        "-ss",
        timestamp,
        "-vframes",
        "1",
        capture_filename,
        "-i",
        video_file,
    ]
)

# Check that the capture was generated
if os.path.isfile(capture_filename):
    logger.info(f"Capture {capture_filename} generated")
    sys.exit(1)
else:
    logger.error(f"Capture {capture_filename} not generated")
    sys.exit(1)
