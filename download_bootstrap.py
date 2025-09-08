import os
import requests

def download_file(url, path):
    response = requests.get(url)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'wb') as f:
        f.write(response.content)

# Download Bootstrap CSS
bootstrap_css_url = 'https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css'
download_file(bootstrap_css_url, 'static/css/bootstrap.min.css')

# Download Bootstrap JS Bundle
bootstrap_js_url = 'https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js'
download_file(bootstrap_js_url, 'static/js/bootstrap.bundle.min.js')

print("Bootstrap files downloaded successfully!")
