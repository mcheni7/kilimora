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
        
        # Update Facebook links - look for href="" followed by fa-facebook icon
        content = re.sub(
            r'(href=")[^"]*("\s*>\s*<i[^>]*class="[^"]*fab fa-facebook)',
            r'\1' + FACEBOOK_URL + r'\2',
            content
        )
        
        # Update Instagram links
        content = re.sub(
            r'(href=")[^"]*("\s*>\s*<i[^>]*class="[^"]*fab fa-instagram)',
            r'\1' + INSTAGRAM_URL + r'\2',
            content
        )
        
        # Update TikTok links
        content = re.sub(
            r'(href=")[^"]*("\s*>\s*<i[^>]*class="[^"]*fab fa-tiktok)',
            r'\1' + TIKTOK_URL + r'\2',
            content
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
