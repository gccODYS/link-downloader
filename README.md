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

## Setup (First-time Installation)

**New to this? No problem!** Follow these steps to get everything working on your Mac:

### Step 1: Install uv (Python Package Manager)
This tool manages Python packages automatically:

1. **Open Terminal** (Cmd+Space, type "Terminal", press Enter)
2. **Copy and paste this command:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
3. **Press Enter** and wait for installation
4. **Restart Terminal** (close and open again)

### Step 2: Download This Tool
You have two options:

**Option A: Download from GitHub (Easier)**
1. Go to: https://github.com/gccODYS/link-downloader
2. Click the green **"Code"** button
3. Click **"Download ZIP"**
4. **Unzip the file** to your Desktop or Documents folder

**Option B: Use Git (If you know how)**
```bash
git clone https://github.com/gccODYS/link-downloader.git
```

### Step 3: Make the Script Executable
1. **Open Terminal**
2. **Navigate to where you downloaded the tool:**
```bash
cd ~/Desktop/link-downloader-main
```
**Common path examples:**
- If in Documents folder: `cd ~/Documents/link-downloader-main`
- If in Downloads folder: `cd ~/Downloads/link-downloader-main`
- If in a subfolder: `cd ~/Documents/MyProjects/link-downloader-main`

3. **Make the script runnable:**
```bash
chmod +x downloader_hybrid.py
```

### Step 4: Test It!
Try downloading a YouTube video to make sure everything works:
```bash
./downloader_hybrid.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

If you see a video downloading, you're all set! 🎉

---

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