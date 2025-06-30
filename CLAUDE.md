# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A self-contained hybrid video downloader targeting non-technical users. Downloads from YouTube, Instagram, TikTok, and Twitter/X. Uses yt-dlp for YouTube and gallery-dl for social media platforms.

## Target Audience

Non-technical users who want to download videos but have no coding experience. Documentation is optimized for beginners - avoids Git, uses simple ZIP downloads, minimal terminal usage.

## Setup for Development

Requires uv package manager (install via `curl -LsSf https://astral.sh/uv/install.sh | sh`).

```bash
chmod +x downloader_hybrid.py
```

Instagram downloads require session cookie in `~/.config/gallery-dl/config.json`:
```json
{
    "extractor": {
        "instagram": {
            "cookies": {
                "sessionid": "USER_SESSION_ID_HERE"
            }
        }
    }
}
```

## Key Features

- **Self-updating**: `--refresh` flag in shebang ensures latest scraper versions
- **PEP 723 compliant**: Dependencies defined in script metadata
- **Cross-platform support**: YouTube (always), Instagram (with cookies), TikTok, Twitter/X
- **Beginner-friendly**: README optimized for non-technical users

## Usage

Main tool:
```bash
./downloader_hybrid.py urls.txt
./downloader_hybrid.py "https://youtube.com/watch?v=example"
```

## Repository State

- Git repository with clean history
- Hosted at: https://github.com/gccODYS/link-downloader
- README.md optimized for ZIP downloads (no Git instructions)
- User documentation focuses on `/Users/your_username/Documents/link-downloader-main` path structure

## Important Notes

- **Never mention Homebrew** in user docs (removed for simplicity)
- **ZIP downloads only** for end users (creates `link-downloader-main` folder)
- **Instagram cookies expire** every few weeks - users need to refresh
- **Downloads folder** created automatically in script directory