#!/usr/bin/env -S uv run --refresh
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "yt-dlp",
#     "gallery-dl",
# ]
# ///

import os
import sys
import subprocess
from pathlib import Path
import yt_dlp

def is_instagram_url(url):
    return 'instagram.com' in url

def is_tiktok_url(url):
    return 'tiktok.com' in url

def download_with_gallery_dl(url, output_dir="downloads"):
    Path(output_dir).mkdir(exist_ok=True)
    try:
        result = subprocess.run([
            sys.executable, '-m', 'gallery_dl',
            '--dest', output_dir,
            '--filename', '{category}_{id}.{extension}',
            url
        ], check=True, capture_output=True, text=True)
        print(f"Downloaded (gallery-dl): {url}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error downloading {url} with gallery-dl: {e.stderr}")
        return False

def download_with_ytdlp(url, output_dir="downloads"):
    Path(output_dir).mkdir(exist_ok=True)
    
    ydl_opts = {
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'format': 'best[height<=720]',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            print(f"Downloaded (yt-dlp): {url}")
            return True
        except Exception as e:
            print(f"Error downloading {url} with yt-dlp: {e}")
            return False

def download_video(url, output_dir="downloads"):
    if is_instagram_url(url) or is_tiktok_url(url):
        return download_with_gallery_dl(url, output_dir)
    else:
        return download_with_ytdlp(url, output_dir)

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python downloader_hybrid.py <url1> [url2] [url3] ...")
        print("  python downloader_hybrid.py urls.txt")
        sys.exit(1)
    
    if len(sys.argv) == 2 and os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as f:
            urls = [line.strip() for line in f if line.strip()]
    else:
        urls = sys.argv[1:]
    
    print(f"Downloading {len(urls)} video(s)...")
    
    successful = 0
    failed = 0
    
    for url in urls:
        if download_video(url):
            successful += 1
        else:
            failed += 1
    
    print(f"Done! {successful} successful, {failed} failed")

if __name__ == "__main__":
    main()