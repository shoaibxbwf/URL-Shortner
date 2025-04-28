from flask import Flask, request, jsonify, send_from_directory
import string
import random

app = Flask(__name__)

# Store URLs temporarily
url_map = {}

# Function to generate random short codes
def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Serve HTML
@app.route('/')
def home():
    return send_from_directory('home_pages', 'index.html')

# API to shorten URL
@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.json
    original_url = data.get('url')
    if not original_url:
        return jsonify({'error': 'No URL provided'}), 400

    short_code = generate_short_code()
    url_map[short_code] = original_url
    short_url = f"http://localhost:5000/{short_code}"
    return jsonify({'short_url': short_url})

# Redirect logic
@app.route('/<short_code>')
def redirect_to_url(short_code):
    url = url_map.get(short_code)
    if url:
        return f"""
        <h1>Redirecting to {url}...</h1>
        <script>
            setTimeout(function(){{window.location.href='{url}';}}, 1000);
        </script>
        """
    else:
        return "<h1>URL Not Found</h1>", 404

# Clear stored URLs
@app.route('/clear', methods=['POST'])
def clear_urls():
    url_map.clear()
    return jsonify({'message': 'All URLs cleared!'})

if __name__ == '__main__':
    app.run(debug=True)
