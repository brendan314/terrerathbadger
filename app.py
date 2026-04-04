from flask import Flask, render_template
import os
from datetime import datetime

app = Flask(__name__)

# List of video data with URL and date/time.
# The 'datetime' strings are used for sorting and display.
videos_data = [
    {"url": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775246414/vauq4o_xhtmy9.mp4",
     "datetime": "2026-03-30 00:30"},
    {"url": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775246413/izjoty_tkg9xn.mp4",
     "datetime": "2026-03-25 02:22"},
    {"url": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775246410/j6wxck_g9ps3t.mp4",
     "datetime": "2026-03-29 01:57"},
    {"url": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775246409/9uenlv_ntdjg5.mp4",
     "datetime": "2026-03-23 22:01"}
]

@app.route('/')
def index():
    processed_videos = []
    for video_item in videos_data:
        video_datetime_str = video_item['datetime']
        video_url = video_item['url']

        # Parse datetime string for sorting and formatting
        video_datetime_obj = datetime.strptime(video_datetime_str, "%Y-%m-%d %H:%M")

        processed_videos.append({
            'id': video_datetime_str.replace(' ', '_').replace(':', '-'), # Create a simple ID from datetime
            'datetime_obj': video_datetime_obj, # Use datetime object for sorting
            'display_datetime': video_datetime_obj.strftime("%b %d, %Y %H:%M"), # Format for display
            'embed_url': video_url
        })

    # Sort videos by datetime, most recent first
    processed_videos.sort(key=lambda x: x['datetime_obj'], reverse=True)

    return render_template('index.html', videos=processed_videos)

