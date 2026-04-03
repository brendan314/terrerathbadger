import os
from flask import Flask, render_template
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.utils import cloudinary_url

app = Flask(__name__)

# Configure Cloudinary - REPLACE WITH YOUR OWN CREDENTIALS
cloudinary.config(
    cloud_name = os.environ.get('CLOUDINARY_CLOUD_NAME', 'your_cloud_name'),
    api_key = os.environ.get('CLOUDINARY_API_KEY', 'your_api_key'),
    api_secret = os.environ.get('CLOUDINARY_API_SECRET', 'your_api_secret')
)

# Cloudinary public IDs for your videos
# In a real application, this would come from a database.
videos_public_ids = [
    'vauq4o_xhtmy9', # Replace with your actual Cloudinary video public ID
    'j6wxck_g9ps3t',  # Replace with another actual Cloudinary video public ID
    '9uenlv_ntdjg5',         # Add more public IDs as needed
    'y9by5s_dtvlbj'
]

@app.route('/')
def index():
    processed_videos = []
    for public_id in videos_public_ids:
        # Generate a secure Cloudinary video URL
        video_url, options = cloudinary_url(
            public_id,
            resource_type="video",
            format="mp4", # Or your preferred video format
            controls=True
        )

        # Generate title and description from the public ID
        # Example: "badger_foraging_example_video" -> "Badger Foraging Example Video"
        title = public_id.replace('_', ' ').title()
        description = f"A captivating moment from Terrerath Badger Watch: {title.lower()}."

        processed_videos.append({
            'id': public_id, # Use public_id as a unique ID
            'title': title,
            'description': description,
            'embed_url': video_url
        })
    return render_template('index.html', videos=processed_videos)

