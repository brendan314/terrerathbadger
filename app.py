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
    # Process videos and group them by month
    grouped_videos = {}
    for video_item in videos_data:
        video_datetime_str = video_item['datetime']
        video_url = video_item['url']

        video_datetime_obj = datetime.strptime(video_datetime_str, "%Y-%m-%d %H:%M")
        
        # Key for grouping: Year-Month (e.g., "2026-03")
        group_key = video_datetime_obj.strftime("%Y-%m")
        display_month_year = video_datetime_obj.strftime("%B %Y") # e.g., "March 2026"

        if group_key not in grouped_videos:
            grouped_videos[group_key] = {
                'display_month_year': display_month_year,
                'videos': []
            }
        
        grouped_videos[group_key]['videos'].append({
            'id': video_datetime_str.replace(' ', '_').replace(':', '-'),
            'datetime_obj': video_datetime_obj,
            'display_datetime': video_datetime_obj.strftime("%b %d, %Y %H:%M"),
            'embed_url': video_url
        })
    
    # Sort videos within each group by datetime, most recent first
    for group_key in grouped_videos:
        grouped_videos[group_key]['videos'].sort(key=lambda x: x['datetime_obj'], reverse=True)

    # Sort the groups by month/year, most recent month first
    sorted_groups = sorted(grouped_videos.items(), key=lambda item: item[0], reverse=True)

    return render_template('index.html', sorted_groups=sorted_groups)

