import os
import re

# Social media links
FACEBOOK_URL = "https://www.facebook.com/share/1GWydnMmsK/?mibextid=wwXIfr"
INSTAGRAM_URL = "https://www.instagram.com/kilimora.adventure?igsh=cjVjaTV4dTZzZXk2"
TIKTOK_URL = "https://www.tiktok.com/@kilimora_adventure?_r=1&_t=ZS-92vfi2bYN0b"

# Directory containing HTML files
html_dir = r"d:\website template\kilimora"

# Get all HTML files
html_files = [f for f in os.listdir(html_dir) if f.endswith('.html')]

print(f"Found {len(html_files)} HTML files to update\n")

updated_count = 0

for filename in html_files:
    filepath = os.path.join(html_dir, filename)
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 1. Inject TikTok link in Top Bar if missing
        # We look for the Instagram button in the top bar style and append TikTok after it
        # Pattern matches the Instagram button with specific classes used in the top bar
        # We use a negative lookahead to ensure we don't add it if it's already there (checking for fa-tiktok immediately after)
        
        topbar_tiktok_btn = f'<a class="btn btn-sm btn-outline-light btn-sm-square rounded-circle me-2" href="{TIKTOK_URL}"><i class="fab fa-tiktok fw-normal"></i></a>'
        
        # Regex to find Instagram button in Top Bar
        # Expected format: <a class="..." href=""><i class="fab fa-instagram fw-normal"></i></a>
        # We capture the whole Instagram anchor tag
        instagram_btn_pattern = r'(<a\s+class="[^"]*btn-outline-light[^"]*"\s+href="[^"]*"><i\s+class="[^"]*fab fa-instagram[^"]*"></i></a>)'
        
        def inject_tiktok(match):
            full_match = match.group(0)
            # Check context after the match to see if TikTok is already their (heuristically)
            # This check happens on the string during replacement but re.sub processes sequentially.
            # However, simpler to just rely on the fact that we run this once or check content first.
            # But to be safe against re-runs, we can use a callback.
            
            # The callback replaces the match. We want to return match + tiktok if tiktok not present.
            # But the lookahead in regex is cleaner.
            return full_match
        
        # Regex with negative lookahead to prevent duplicate injection
        # Matches Instagram button NOT followed by whitespace* + <a ... fa-tiktok
        injection_pattern = instagram_btn_pattern + r'(?!\s*<a[^>]*><i[^>]*class="[^"]*fab fa-tiktok)'
        
        content = re.sub(
            injection_pattern,
            r'\1\n                    ' + topbar_tiktok_btn,
            content,
            flags=re.IGNORECASE
        )

        # 2. Update existing links (Facebook, Instagram, TikTok) in the whole file (TopBar + Footer)
        
        # Update Facebook links (handling both fa-facebook and fa-facebook-f)
        content = re.sub(
            r'(href=")[^"]*("\s*>\s*<i[^>]*class="[^"]*fab fa-facebook(?:-f)?\b)',
            r'\1' + FACEBOOK_URL + r'\2',
            content,
            flags=re.IGNORECASE
        )
        
        # Update Instagram links
        content = re.sub(
            r'(href=")[^"]*("\s*>\s*<i[^>]*class="[^"]*fab fa-instagram\b)',
            r'\1' + INSTAGRAM_URL + r'\2',
            content,
            flags=re.IGNORECASE
        )
        
        # Update TikTok links (if any existing ones, e.g. in footer)
        content = re.sub(
            r'(href=")[^"]*("\s*>\s*<i[^>]*class="[^"]*fab fa-tiktok\b)',
            r'\1' + TIKTOK_URL + r'\2',
            content,
            flags=re.IGNORECASE
        )
        
        # Write back if changes were made
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] Updated: {filename}")
            updated_count += 1
        else:
            print(f"[ -] No changes: {filename}")
            
    except Exception as e:
        print(f"[ERR] Error processing {filename}: {str(e)}")

print(f"\nDone! Updated {updated_count} files.")
