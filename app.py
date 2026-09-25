from flask import Flask, request, jsonify, render_template
import yt_dlp
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    link = request.json.get('url')
    ydl_opts = {'format': 'best', 'quiet': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(link, download=False)
        return jsonify({"title": info.get('title'), "url": info.get('url')})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
