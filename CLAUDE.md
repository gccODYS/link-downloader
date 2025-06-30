# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A hybrid video downloader that uses yt-dlp for YouTube and gallery-dl for Instagram/TikTok. Supports bulk downloads from URL lists.

## Setup

Requires uv package manager. Script is self-contained with PEP 723 metadata.

```bash
chmod +x downloader_hybrid.py
```

Instagram requires session cookie in `~/.config/gallery-dl/config.json`

## Usage

Main self-updating hybrid downloader:
```bash
./downloader_hybrid.py urls.txt
```

Legacy YouTube-only version:
```bash
python3 downloader.py urls.txt
```

## Architecture

- `downloader_hybrid.py` - Self-contained PEP 723 script with uv --refresh for latest scrapers
- `downloader.py` - Legacy YouTube-only using yt-dlp
- Instagram authentication via gallery-dl config
- Downloads saved to `downloads/` directory
- Handles 40+ URLs efficiently with detailed success/failure reporting
- Always uses latest scraper versions to stay ahead of anti-scraping measures