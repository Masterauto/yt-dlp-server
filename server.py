from flask import Flask, request, send_file
import yt_dlp
import os

app = Flask(__name__)

@app.route('/download', methods=['GET'])
def download():
    video_id = request.args.get('video_id')
    url = f"https://www.youtube.com/watch?v={video_id}"
    output_file = f"{video_id}.mp4"

    ydl_opts = {
        'outtmpl': output_file,
        'format': 'mp4/bestaudio/best',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return send_file(output_file, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
