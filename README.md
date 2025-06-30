# Video Downloader Tool

Downloads videos from YouTube, Instagram, TikTok, and Twitter/X. Self-updating and self-contained.

## How to Use This Tool

### Step 1: Prepare your URLs
- Put URLs in a text file (one per line), or
- Have URLs ready to paste directly

### Step 2: Open Terminal and navigate to the tool
1. **Open Terminal** (on Mac: press Cmd+Space, type "Terminal", press Enter)
2. **Navigate to this folder** by typing:
```bash
cd "/Users/ogallagher27/Documents/2_Extracurriculars/Link_downloader"
```
3. **Press Enter** - you're now in the right place!

### Step 3: Run the downloader
```bash
./downloader_hybrid.py urls.txt
```
or for single URLs:
```bash
./downloader_hybrid.py "https://youtube.com/watch?v=example"
```

### Step 4: Find your videos
Videos are saved in the `downloads/` folder (in the same directory as the script)

## Instagram Setup (One-time only)

If you want to download Instagram content, you need to get your session cookie:

1. **Log into Instagram** in your browser
2. **Open Developer Tools** (F12 key)
3. **Go to Application tab** → Storage → Cookies → instagram.com
4. **Copy the `sessionid` value** (long string of letters/numbers)
5. **Create config file:**
```bash
mkdir -p ~/.config/gallery-dl
```
6. **Edit `~/.config/gallery-dl/config.json`:**
```json
{
    "extractor": {
        "instagram": {
            "cookies": {
                "sessionid": "PASTE_YOUR_SESSION_ID_HERE"
            }
        }
    }
}
```

**Note:** Instagram cookies expire every few weeks. If Instagram downloads stop working, repeat these steps.

## What Works

- ✅ **YouTube** - Always works
- ✅ **Instagram** - Requires session cookie setup (see above)
- ✅ **TikTok** - Usually works
- ✅ **Twitter/X** - Usually works  
- ❌ **Frame.io** - Doesn't work (needs authentication)

## Troubleshooting

**Instagram suddenly stops working?**
→ Your cookie expired. Redo the Instagram setup steps above.

**Script won't run?**
→ Make sure you have `uv` installed and the script is executable: `chmod +x downloader_hybrid.py`

**Script is slow to start?**
→ Normal! It checks for the latest scraper versions each time to stay ahead of anti-scraping measures.

## Technical Notes

- Self-contained script using PEP 723 metadata
- Automatically downloads latest yt-dlp and gallery-dl versions
- No manual dependency management needed