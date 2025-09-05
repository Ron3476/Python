import os
import requests
from urllib.parse import urlparse
import hashlib

# Directory to store downloaded images
SAVE_DIR = "Fetched_Images"

# Create the directory if it doesn't exist
os.makedirs(SAVE_DIR, exist_ok=True)

def get_filename_from_url(url: str) -> str:
    """
    Extracts filename from URL or generates a unique one if not available.
    """
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    
    # If no filename is found, generate one using hash
    if not filename:
        filename = hashlib.md5(url.encode()).hexdigest() + ".jpg"
    return filename

def download_image(url: str) -> None:
    """
    Downloads an image from the given URL and saves it in the SAVE_DIR folder.
    Includes error handling and duplicate prevention.
    """
    try:
        print(f"Fetching: {url}")
        response = requests.get(url, stream=True, timeout=10)

        # Raise exception for HTTP errors
        response.raise_for_status()

        # Check headers for content type
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"❌ Skipped: {url} (Not an image)")
            return

        # Generate filename
        filename = get_filename_from_url(url)
        filepath = os.path.join(SAVE_DIR, filename)

        # Prevent duplicates
        if os.path.exists(filepath):
            print(f"⚠️ Skipped: {filename} (Already downloaded)")
            return

        # Save file in binary mode
        with open(filepath, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"✅ Saved: {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to fetch {url}: {e}")

def main():
    """
    Main function to handle user input for single or multiple URLs.
    """
    print("=== Image Fetcher ===")
    print("Enter one or more image URLs (separated by spaces):")
    urls = input(">> ").split()

    for url in urls:
        download_image(url)

if __name__ == "__main__":
    main()
