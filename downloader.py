#!/usr/bin/env python3

import os
import sys
from pathlib import Path
import yt_dlp

def download_video(url, output_dir="downloads"):
    Path(output_dir).mkdir(exist_ok=True)
    
    ydl_opts = {
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'format': 'best[height<=720]',  # Download best quality up to 720p
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            print(f"Downloaded: {url}")
        except Exception as e:
            print(f"Error downloading {url}: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python downloader.py <url1> [url2] [url3] ...")
        print("  python downloader.py urls.txt")
        sys.exit(1)
    
    # Check if argument is a file
    if len(sys.argv) == 2 and os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as f:
            urls = [line.strip() for line in f if line.strip()]
    else:
        urls = sys.argv[1:]
    
    print(f"Downloading {len(urls)} video(s)...")
    
    for url in urls:
        download_video(url)
    
    print("Done!")

if __name__ == "__main__":
    main()