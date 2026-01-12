import os

# Configuration
# Old Colors
OLD_PRIMARY = '#4B2E18'
OLD_SECONDARY = '#4B2E18' # Same as primary in root
OLD_GOLD = '#d4a017'
OLD_GOLD_2 = '#c9a24b' # Found in style.css
OLD_GOLD_3 = '#C89F6C' # Found in rating/underline
OLD_DARK_BROWN = '#3A2413' # Hover state

# New Colors
NEW_GREEN = '#78B438'
NEW_DARK_GREEN = '#5A8F24' # Approx 20% darker

TARGET_DIR = 'd:\\website template\\kilimora'

def update_colors(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Replace Primary/Secondary/Gold with NEW_GREEN
        content = content.replace(OLD_PRIMARY, NEW_GREEN)
        content = content.replace(OLD_SECONDARY, NEW_GREEN)
        content = content.replace(OLD_GOLD, NEW_GREEN)
        content = content.replace(OLD_GOLD_2, NEW_GREEN)
        content = content.replace(OLD_GOLD_3, NEW_GREEN)
        
        # Replace Dark Brown (Hover) with NEW_DARK_GREEN
        content = content.replace(OLD_DARK_BROWN, NEW_DARK_GREEN)
        
        # Also handle lowercase variants just in case
        content = content.replace(OLD_PRIMARY.lower(), NEW_GREEN)
        content = content.replace(OLD_GOLD.lower(), NEW_GREEN)
        content = content.replace(OLD_GOLD_2.lower(), NEW_GREEN)
        content = content.replace(OLD_GOLD_3.lower(), NEW_GREEN)
        content = content.replace(OLD_DARK_BROWN.lower(), NEW_DARK_GREEN)

        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[UPDATED] {os.path.basename(filepath)}")
        else:
            # print(f"[SKIP] {os.path.basename(filepath)}")
            pass

    except Exception as e:
        print(f"[ERROR] processing {filepath}: {e}")

def main():
    print("Starting Color Theme Update...")
    for root, dirs, files in os.walk(TARGET_DIR):
        for file in files:
            if file.endswith('.html') or file.endswith('.css'):
                filepath = os.path.join(root, file)
                update_colors(filepath)
    print("Theme Update Complete.")

if __name__ == "__main__":
    main()
