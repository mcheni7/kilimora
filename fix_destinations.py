import re

# Define corrections for each destination file
corrections = {
    'destination-kilimanjaro.html': {
        'title': 'Mount Kilimanjaro - Kilimora Adventures',
        'keywords': 'Kilimanjaro, Mountain, Climbing, Hiking, Tanzania',
        'description': 'Conquer Africa\'s highest peak, Mount Kilimanjaro, standing at 5,895 meters above sea level.',
        'hero_title': 'MOUNT KILIMANJARO',
        'hero_desc': 'Conquer Africa\'s highest peak, Mount Kilimanjaro, standing majestically at 5,895 meters above sea level.',
        'about_title': 'About Mount Kilimanjaro',
        'about_p1': 'Mount Kilimanjaro is Africa\'s highest mountain, standing at 5,895 meters (19,341 feet) above sea level. Located in northeastern Tanzania, this dormant volcano is one of the world\'s most accessible high summits and attracts thousands of climbers each year.',
        'about_p2': 'The mountain has three volcanic cones: Kibo, Mawenzi, and Shira. Kilimanjaro is a UNESCO World Heritage Site and offers several climbing routes, each providing unique experiences and varying difficulty levels. The climb takes you through five distinct climate zones, from tropical rainforest to arctic summit.',
        'highlight1_title': 'Uhuru Peak',
        'highlight1_desc': 'Reach the highest point in Africa at 5,895 meters.',
        'highlight3_title': 'Five Climate Zones',
        'highlight3_desc': 'Experience diverse ecosystems from rainforest to arctic.',
        'tours_title': 'Experience Kilimanjaro\'s Top Tours'
    },
    'destination-manyara.html': {
        'title': 'Lake Manyara National Park - Kilimora Adventures',
        'keywords': 'Lake Manyara, Tree-climbing Lions, Flamingos, Safari, Tanzania',
        'description': 'Discover Lake Manyara National Park, famous for tree-climbing lions and spectacular birdlife.',
        'hero_title': 'LAKE MANYARA',
        'hero_desc': 'Discover Lake Manyara National Park, famous for its unique tree-climbing lions and vibrant flamingo populations.',
        'about_title': 'About Lake Manyara',
        'about_p1': 'Lake Manyara National Park is a protected area in Tanzania\'s Arusha and Manyara Regions, covering an area of 325 square kilometers. The park is famous for its unique tree-climbing lions and large flocks of flamingos that paint the lake pink.',
        'about_p2': 'The park offers a diverse landscape including groundwater forests, acacia woodlands, and the alkaline soda lake itself. It is home to over 400 bird species and provides excellent opportunities for birdwatching and photography. The park also hosts elephants, hippos, giraffes, and various antelope species.',
        'highlight1_title': 'Tree-Climbing Lions',
        'highlight1_desc': 'Witness the rare sight of lions resting in acacia trees.',
        'highlight3_title': 'Flamingo Spectacle',
        'highlight3_desc': 'Thousands of flamingos create a pink carpet on the lake.',
        'tours_title': 'Experience Lake Manyara\'s Top Tours'
    },
    'destination-mikumi.html': {
        'title': 'Mikumi National Park - Kilimora Adventures',
        'keywords': 'Mikumi, Wildlife, Safari, National Park, Tanzania',
        'description': 'Explore Mikumi National Park, Tanzania\'s fourth-largest national park with abundant wildlife.',
        'hero_title': 'MIKUMI',
        'hero_desc': 'Explore Mikumi National Park, Tanzania\'s fourth-largest park with abundant wildlife and stunning landscapes.',
        'about_title': 'About Mikumi',
        'about_p1': 'Mikumi National Park is Tanzania\'s fourth-largest national park, covering an area of 3,230 square kilometers. Located between the Uluguru Mountains and the Lumango range, the park is part of a much larger ecosystem centered on the Selous Game Reserve.',
        'about_p2': 'The park is characterized by its Mkata Floodplain, which is often compared to the Serengeti plains due to its open horizons and abundant wildlife. Mikumi hosts buffaloes, giraffes, elephants, lions, pythons, zebras, leopards, crocodiles, and various bird species, making it an excellent destination for wildlife viewing.',
        'highlight1_title': 'Mkata Floodplain',
        'highlight1_desc': 'Open savanna plains teeming with diverse wildlife.',
        'highlight3_title': 'Accessible Safari',
        'highlight3_desc': 'Close proximity to Dar es Salaam makes it easily accessible.',
        'tours_title': 'Experience Mikumi\'s Top Tours'
    }
}

def fix_destination_file(filename, fixes):
    filepath = f"d:\\website template\\kilimora\\{filename}"
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix title
        content = re.sub(
            r'<title>.*?</title>',
            f'<title>{fixes["title"]}</title>',
            content
        )
        
        # Fix meta keywords
        content = re.sub(
            r'<meta content="[^"]*" name="keywords">',
            f'<meta content="{fixes["keywords"]}" name="keywords">',
            content
        )
        
        # Fix meta description
        content = re.sub(
            r'<meta content="[^"]*"\s+name="description">',
            f'<meta content="{fixes["description"]}"\n        name="description">',
            content
        )
        
        # Fix hero title (h6 and h1)
        content = re.sub(
            r'<h6 class="text-white mb-2 animated slideInDown"[^>]*>.*?\s*DESTINATIONS</h6>',
            f'<h6 class="text-white mb-2 animated slideInDown" style="letter-spacing: 2px;">{fixes["hero_title"]}\n                        DESTINATIONS</h6>',
            content,
            flags=re.DOTALL
        )
        
        content = re.sub(
            r'<h1 class="text-white mb-3 animated slideInDown"[^>]*>.*?</h1>',
            f'<h1 class="text-white mb-3 animated slideInDown" style="font-size: 3rem;">{fixes["hero_title"]}</h1>',
            content
        )
        
        # Fix hero description
        content = re.sub(
            r'<p class="fs-6 text-white mb-4 animated slideInDown">.*?</p>',
            f'<p class="fs-6 text-white mb-4 animated slideInDown">\n                        {fixes["hero_desc"]}\n                    </p>',
            content,
            flags=re.DOTALL
        )
        
        # Fix About section title
        content = re.sub(
            r'<h2 class="mb-0">About .*?</h2>',
            f'<h2 class="mb-0">{fixes["about_title"]}</h2>',
            content
        )
        
        # Fix About section paragraphs
        # Find the About section and replace both paragraphs
        about_section_pattern = r'(<h2 class="mb-0">About.*?</h2>\s*</div>\s*)<p class="mb-4">.*?</p>\s*<p class="mb-4">.*?</p>'
        about_replacement = f'\\1<p class="mb-4">{fixes["about_p1"]}</p>\n                        <p class="mb-4">{fixes["about_p2"]}</p>'
        content = re.sub(about_section_pattern, about_replacement, content, flags=re.DOTALL)
        
        # Fix Highlights
        # First highlight
        content = re.sub(
            r'(<div class="col-lg-4 col-md-6 wow fadeInUp" data-wow-delay="0\.1s">.*?<i class="fa fa-paw"></i>\s*)<h5>.*?</h5>\s*<p class="mb-0">.*?</p>',
            f'\\1<h5>{fixes["highlight1_title"]}</h5>\n                        <p class="mb-0">{fixes["highlight1_desc"]}</p>',
            content,
            flags=re.DOTALL
        )
        
        # Third highlight (Endless Plains / Globe icon)
        content = re.sub(
            r'(<div class="col-lg-4 col-md-6 wow fadeInUp" data-wow-delay="0\.5s">.*?<i class="fa fa-globe"></i>\s*)<h5>.*?</h5>\s*<p class="mb-0">.*?</p>',
            f'\\1<h5>{fixes["highlight3_title"]}</h5>\n                        <p class="mb-0">{fixes["highlight3_desc"]}</p>',
            content,
            flags=re.DOTALL
        )
        
        # Fix Top Tours title
        content = re.sub(
            r'<h2 class="mb-0">Experience .*?\'s Top Tours</h2>',
            f'<h2 class="mb-0">{fixes["tours_title"]}</h2>',
            content
        )
        
        # Write back to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"[OK] Fixed: {filename}")
        return True
        
    except Exception as e:
        print(f"[ERROR] Error fixing {filename}: {str(e)}")
        return False

# Process each file
print("Starting destination file corrections...")
print("=" * 60)

for filename, fixes in corrections.items():
    fix_destination_file(filename, fixes)

print("=" * 60)
print("Destination file corrections complete!")
