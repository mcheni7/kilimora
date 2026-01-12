import os

# Configuration
# Current Colors (To be replaced)
CURRENT_GREEN = '#78B438'
CURRENT_DARK_GREEN = '#5A8F24'

# Target Colors (Restoring)
TARGET_BROWN = '#4B2E18'
TARGET_DARK_BROWN = '#3A2413'

TARGET_DIR = 'd:\\website template\\kilimora'

def update_colors(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Replace Green with Brown
        content = content.replace(CURRENT_GREEN, TARGET_BROWN)
        content = content.replace(CURRENT_GREEN.lower(), TARGET_BROWN)
        
        # Replace Dark Green with Dark Brown
        content = content.replace(CURRENT_DARK_GREEN, TARGET_DARK_BROWN)
        content = content.replace(CURRENT_DARK_GREEN.lower(), TARGET_DARK_BROWN)

        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[REVERTED] {os.path.basename(filepath)}")
        else:
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
