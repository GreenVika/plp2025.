import os
import requests
from urllib.parse import urlparse
import hashlib

def get_file_hash(filepath):
    """Compute MD5 hash of a file."""
    hasher = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def fetch_images(urls):
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    # Store known hashes to avoid duplicate downloads
    known_hashes = {}

    # Preload hashes of already existing files in the folder
    for fname in os.listdir(save_dir):
        fpath = os.path.join(save_dir, fname)
        if os.path.isfile(fpath):
            known_hashes[get_file_hash(fpath)] = fname

    for url in urls:
        print(f"\nFetching: {url}")
        try:
            response = requests.get(url, timeout=10, stream=True)
            response.raise_for_status()  # Raise error for bad responses

            # Check important headers
            content_type = response.headers.get("Content-Type", "")
            if not content_type.startswith("image/"):
                print("⚠️ Skipped: URL is not an image")
                continue

            # Extract filename
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path) or "downloaded_image.jpg"
            filepath = os.path.join(save_dir, filename)

            # Save image temporarily to compute hash
            temp_path = filepath + ".part"
            with open(temp_path, "wb") as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)

            # Compute hash
            file_hash = get_file_hash(temp_path)

            if file_hash in known_hashes:
                print(f"⚠️ Skipped: Duplicate image detected (same as {known_hashes[file_hash]})")
                os.remove(temp_path)  # Delete temp file
                continue

            # Rename temp file to final name
            os.rename(temp_path, filepath)
            known_hashes[file_hash] = filename

            print("✅ Image saved as:", filepath)

        except requests.exceptions.RequestException as e:
            print("❌ Error fetching image:", e)

if __name__ == "__main__":
    # Allow multiple URLs (space-separated)
    urls_input = input("Enter image URLs (separated by space): ").strip()
    urls = urls_input.split()
    fetch_images(urls)
