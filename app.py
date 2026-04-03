from flask import Flask, render_template
import os

app = Flask(__name__)

# List of video data with URL and date/time.
# You will need to manually provide the 'datetime' for each video.
# In a real application, this would typically come from a database.
videos_data = [
    {"url": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775246414/vauq4o_xhtmy9.mp4", "datetime": "YYYY-MM-DD HH:MM"}, # Update this datetime
    {"url": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775246413/izjoty_tkg9xn.mp4", "datetime": "YYYY-MM-DD HH:MM"}, # Update this datetime
    {"url": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775246410/j6wxck_g9ps3t.mp4", "datetime": "YYYY-MM-DD HH:MM"}, # Update this datetime
    {"url": "https://res.cloudinary.com/dkheyxxzk/video/upload/v1775246409/9uenlv_ntdjg5.mp4", "datetime": "YYYY-MM-DD HH:MM"}  # Update this datetime
]

@app.route('/')
def index():
    processed_videos = []
    for video_item in videos_data:
        # Use the provided datetime as an identifier and display text
        video_datetime = video_item['datetime']
        video_url = video_item['url']

        processed_videos.append({
            'id': video_datetime.replace(' ', '_').replace(':', '-'), # Create a simple ID from datetime
            'datetime': video_datetime,
            'embed_url': video_url
        })
    return render_template('index.html', videos=processed_videos)

