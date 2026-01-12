import re
import os

# Define image mappings for each tour card position (1-4) for each destination
tour_images = {
    'destination-serengeti.html': {
        'img1': 'nyumbu-migrate.jpeg',  # Migration theme
        'img2': 'pro3.jpg',              # Safari vehicle with people
        'img3': 'simba.jpg',             # Lion
        'img4': 'photo1.jpeg'            # Keep existing
    },
    'destination-ngorongoro.html': {
        'img1': 'ngo.jpg',               # Crater view
        'img2': 'pro3.jpg',              # Safari vehicle with people
        'img3': 'tembo10.jpeg',          # Elephants
        'img4': 'photo1.jpeg'            # Keep existing
    },
    'destination-terangile.html': {
        'img1': 'tembo.jpg',             # Elephants (Tarangire theme)
        'img2': 'pro3.jpg',              # Safari vehicle with people
        'img3': 'tarangire.jpg',         # Tarangire landscape
        'img4': 'photo1.jpeg'            # Keep existing
    },
    'destination-kilimanjaro.html': {
        'img1': 'kilimanjaro2.jpg',      # Mountain
        'img2': 'pro3.jpg',              # Safari vehicle with people
        'img3': 'kilimanjaro3.jpg',      # Mountain view
        'img4': 'photo1.jpeg'            # Keep existing
    },
    'destination-manyara.html': {
        'img1': 'treelion.jpg',          # Tree-climbing lions
        'img2': 'pro3.jpg',              # Safari vehicle with people
        'img3': 'ndege6.jpeg',           # Birds/flamingos
        'img4': 'photo1.jpeg'            # Keep existing
    },
    'destination-mikumi.html': {
        'img1': 'mix.jpg',               # Mixed wildlife
        'img2': 'pro3.jpg',              # Safari vehicle with people
        'img3': 'pundamilia.jpeg',       # Zebras
        'img4': 'photo1.jpeg'            # Keep existing
    }
}

def update_tour_images(filename, images):
    filepath = f"d:\\website template\\kilimora\\{filename}"
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all tour image tags in the carousel section
        # Pattern to match: <img class="img-fluid" src="img/XXXXX.jpg" alt="">
        
        # Replace Tour Item 1 image
        content = re.sub(
            r'(<!-- Tour Item 1 -->.*?<div class="overflow-hidden dest-img-container">.*?<img class="img-fluid" src=")img/[^"]+(")',
            f'\\1img/{images["img1"]}\\2',
            content,
            flags=re.DOTALL
        )
        
        # Replace Tour Item 2 image
        content = re.sub(
            r'(<!-- Tour Item 2 -->.*?<div class="overflow-hidden dest-img-container">.*?<img class="img-fluid" src=")img/[^"]+(")',
            f'\\1img/{images["img2"]}\\2',
            content,
            flags=re.DOTALL
        )
        
        # Replace Tour Item 3 image
        content = re.sub(
            r'(<!-- Tour Item 3 -->.*?<div class="overflow-hidden dest-img-container">.*?<img class="img-fluid" src=")img/[^"]+(")',
            f'\\1img/{images["img3"]}\\2',
            content,
            flags=re.DOTALL
        )
        
        # Replace Tour Item 4 image
        content = re.sub(
            r'(<!-- Tour Item 4 -->.*?<div class="overflow-hidden dest-img-container">.*?<img class="img-fluid" src=")img/[^"]+(")',
            f'\\1img/{images["img4"]}\\2',
            content,
            flags=re.DOTALL
        )
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"[OK] Updated tour images in: {filename}")
        print(f"     - Tour 1: {images['img1']}")
        print(f"     - Tour 2: {images['img2']}")
        print(f"     - Tour 3: {images['img3']}")
        print(f"     - Tour 4: {images['img4']}")
        return True
        
    except Exception as e:
        print(f"[ERROR] Error updating {filename}: {str(e)}")
        return False

# Process each file
print("Updating tour card images in destination files...")
print("=" * 70)

for filename, images in tour_images.items():
    update_tour_images(filename, images)
    print()

print("=" * 70)
print("Tour image updates complete!")
