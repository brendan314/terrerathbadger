from flask import Flask, render_template

app = Flask(__name__)

# Dummy video data - in a real application, this would come from a database
videos = [
    {
        'id': 'video1',
        'title': 'Badger Foraging at Night',
        'description': 'A lone badger caught on camera foraging for food during the late hours.',
        'embed_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ' # Placeholder for a real video
    },
    {
        'id': 'video2',
        'title': 'Badger Family Playtime',
        'description': 'A heartwarming video of a badger sow and her cubs playing near the sett entrance.',
        'embed_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ' # Placeholder for a real video
    }
]

@app.route('/')
def index():
    return render_template('index.html', videos=videos)

