import requests
import sys
import os

def download_favicon(url):
    try:
        if not url.startswith("http"):
            url = "http://" + url
        favicon_url = url.rstrip('/') + "/favicon.ico"
        response = requests.get(favicon_url, stream=True)
        response.raise_for_status()
        with open("favicon.ico", "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Favicon downloaded successfully from {favicon_url}")
    except Exception as e:
        print(f"Error downloading favicon: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python app.py <url>")
        sys.exit(1)
    url = sys.argv[1]
    download_favicon(url)
