import re

# 1. Read the Template (Serengeti)
with open('d:\\website template\\kilimora\\destination-serengeti.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Define FAQ HTML Generator
def generate_faq_html(faqs):
    html = '''    <!-- FAQ Section -->
    <div class="container-xxl py-5">
        <div class="container">
            <div class="text-center wow fadeInUp" data-wow-delay="0.1s">
                <h6 class="section-title bg-white text-center text-primary px-3">Travel Guide</h6>
                <h1 class="mb-5">Frequently Asked Questions</h1>
            </div>
            <div class="row justify-content-center">
                <div class="col-lg-10">
                    <div class="accordion" id="accordionExample">'''
    
    for i, (q, a) in enumerate(faqs):
        is_show = 'show' if i == 0 else ''
        is_collapsed = 'collapsed' if i != 0 else ''
        aria_expanded = 'true' if i == 0 else 'false'
        html += f'''
                        <div class="accordion-item">
                            <h2 class="accordion-header" id="heading{i+1}">
                                <button class="accordion-button {is_collapsed}" type="button" data-bs-toggle="collapse"
                                    data-bs-target="#collapse{i+1}" aria-expanded="{aria_expanded}" aria-controls="collapse{i+1}">
                                    {q}
                                </button>
                            </h2>
                            <div id="collapse{i+1}" class="accordion-collapse collapse {is_show}" aria-labelledby="heading{i+1}"
                                data-bs-parent="#accordionExample">
                                <div class="accordion-body">
                                    {a}
                                </div>
                            </div>
                        </div>'''
    
    html += '''
                    </div>
                </div>
            </div>
        </div>
    </div>'''
    return html

def generate_highlights_html(highlights):
    html = '''    <!-- Highlights Section -->
    <div class="container-xxl py-5 bg-light">
        <div class="container">
            <div class="d-flex align-items-center mb-5">
                <span class="section-title-line"></span>
                <h2 class="mb-0">Highlights</h2>
            </div>
            <div class="row g-4">'''
            
    delays = ['0.1s', '0.3s', '0.5s', '0.7s', '0.9s']
    for i, (icon, title, desc) in enumerate(highlights):
        d = delays[i] if i < len(delays) else '0.1s'
        html += f'''
                <div class="col-lg-4 col-md-6 wow fadeInUp" data-wow-delay="{d}">
                    <div class="icon-box text-center">
                        <i class="fa {icon}"></i>
                        <h5>{title}</h5>
                        <p class="mb-0">{desc}</p>
                    </div>
                </div>'''
                
    html += '''
            </div>
        </div>
    </div>'''
    return html

# Content Map for ALL 5 Destinations (excluding Serengeti itself)
content_map = {
    'destination-ngorongoro.html': {
        'title': 'Ngorongoro Conservation Area - Kilimora Adventures',
        'keywords': 'Ngorongoro, Crater, Safari, Tanzania, Wildlife',
        'desc': 'Explore the Ngorongoro Crater, a UNESCO World Heritage Site and natural wonder of Africa.',
        'hero_subtitle': 'NGORONGORO DESTINATIONS',
        'hero_title': 'NGORONGORO',
        'hero_desc': 'Descend into the world\'s largest inactive volcanic caldera, a natural amphitheater teeming with wildlife and stunning geological formations.',
        'hero_bg': 'ngo.jpg',
        'about_img': 'ngoro22.jpeg',
        'about_title': 'About Ngorongoro Crater',
        'about_html': '''<p class="mb-4">The Ngorongoro Conservation Area constitutes a UNESCO World Heritage Site located 180 km (110 mi) west of Arusha in the Crater Highlands area of Tanzania. The conservation area is named after Ngorongoro Crater, a large volcanic caldera within the area.</p>
                        <p class="mb-4">The crater, which formed when a large volcano exploded and collapsed on itself two to three million years ago, is 610 meters (2,000 feet) deep and its floor covers 260 square kilometers (100 square miles). It is home to a dense population of wildlife including the Big 5.</p>''',
        'highlights': [
            ('fa-paw', 'Big 5 Safari', 'One of the best places to see the Big 5 in a single day.'),
            ('fa-camera', 'Black Rhino', 'A sanctuary for the endangered Black Rhino.'),
            ('fa-globe', 'Volcanic Caldera', 'The world\'s largest inactive, intact and unfilled volcanic caldera.'),
            ('fa-cloud', 'Maasai Culture', 'Witness the coexistence of Maasai herdsmen and wildlife.'),
            ('fa-binoculars', 'Bird Watching', 'Flamingos in Lake Magadi and diverse avian life.')
        ],
        'tours_title': 'Experience Ngorongoro\'s Top Tours',
        'tour_images': ['ngo.jpg', 'pro3.jpg', 'tembo10.jpeg', 'photo1.jpeg'],
        'nearby_text': 'Extend your safari adventure by visiting these iconic destinations near Ngorongoro.',
        'nearby_replace_target': 'Ngorongoro Crater',
        'nearby_replace_html': '''
            <!-- Serengeti Block -->
            <div class="row align-items-center mb-5">
                <div class="col-lg-6 position-relative">
                    <img src="img/nyumbu-migrate.jpeg" class="img-fluid rounded main-img" alt="Serengeti Plains">
                    <img src="img/simba.jpg" class="img-fluid rounded small-img shadow-lg" alt="Lion">
                </div>
                <div class="col-lg-6">
                    <h3 class="dest-country">Serengeti National Park</h3>
                    <div class="dest-underline"></div>
                    <p class="dest-text">
                        The endless plains of the Serengeti are the stage for the Great Migration. Witness millions of
                        wildebeest, zebras, and predators in this world-renowned ecosystem.
                    </p>
                    <a href="destination-serengeti.html" class="dest-btn">→ EXPLORE SERENGETI</a>
                </div>
            </div>''',
        'faq': [
            ('When is the best time to visit Ngorongoro?', 'Wildlife viewing inside the crater is excellent <strong>year-round</strong>. However, the dry season (June to October) is often preferred.'),
            ('Do I need a 4x4 vehicle?', '<strong>Yes</strong>, a 4x4 safari vehicle is mandatory for descending into the Ngorongoro Crater due to the steep terrain.'),
            ('Can I see the Big 5 here?', '<strong>Absolutely</strong>. The Ngorongoro Crater is one of the few places in Africa where you have a very high chance of seeing all of the Big 5 in a single day.')
        ]
    },
    'destination-manyara.html': {
        'title': 'Lake Manyara National Park - Kilimora Adventures',
        'keywords': 'Lake Manyara, Tree-climbing Lions, Flamingos, Safari, Tanzania',
        'desc': 'Discover Lake Manyara National Park, famous for tree-climbing lions and spectacular birdlife.',
        'hero_subtitle': 'LAKE MANYARA DESTINATIONS',
        'hero_title': 'LAKE MANYARA',
        'hero_desc': 'Discover Lake Manyara National Park, famous for its unique tree-climbing lions and vibrant flamingo populations painting the lake pink.',
        'hero_bg': 'treelion.jpg',
        'about_img': 'destination-4.jpg',
        'about_title': 'About Lake Manyara',
        'about_html': '''<p class="mb-4">Lake Manyara National Park is a protected area in Tanzania\'s Arusha and Manyara Regions, covering an area of 325 square kilometers. The park is famous for its unique tree-climbing lions and large flocks of flamingos that paint the lake pink.</p>
                        <p class="mb-4">The park offers a diverse landscape including groundwater forests, acacia woodlands, and the alkaline soda lake itself. It is home to over 400 bird species and provides excellent opportunities for birdwatching and photography.</p>''',
        'highlights': [
            ('fa-paw', 'Tree-Climbing Lions', 'Witness the rare behavior of lions resting in trees.'),
            ('fa-camera', 'Flamingos', 'Thousands of pink flamingos covering the alkaline lake.'),
            ('fa-globe', 'Groundwater Forest', 'Lush forests fed by underground springs.'),
            ('fa-cloud', 'Bird Watching', 'Over 400 species including pelicans and storks.'),
            ('fa-binoculars', 'Baboon Troops', 'Large troops of olive baboons in the forests.')
        ],
        'tours_title': 'Experience Lake Manyara\'s Top Tours',
        'tour_images': ['treelion.jpg', 'pro3.jpg', 'ndege6.jpeg', 'photo1.jpeg'],
        'nearby_text': 'Extend your safari adventure by visiting these iconic destinations near Lake Manyara.',
        'nearby_replace_target': 'Lake Manyara',
        'nearby_replace_html': '''
            <!-- Serengeti Block -->
            <div class="row align-items-center mb-5 flex-lg-row-reverse">
                <div class="col-lg-6 position-relative">
                    <img src="img/nyumbu-migrate.jpeg" class="img-fluid rounded main-img" alt="Serengeti Plains">
                    <img src="img/simba.jpg" class="img-fluid rounded small-img shadow-lg" alt="Lion">
                </div>
                <div class="col-lg-6">
                    <h3 class="dest-country">Serengeti National Park</h3>
                    <div class="dest-underline"></div>
                    <p class="dest-text">
                        The endless plains of the Serengeti are the stage for the Great Migration. Witness millions of
                        wildebeest, zebras, and predators in this world-renowned ecosystem.
                    </p>
                    <a href="destination-serengeti.html" class="dest-btn">→ EXPLORE SERENGETI</a>
                </div>
            </div>''',
        'faq': [
            ('What is special about Lake Manyara?', 'Lake Manyara is famous for its <strong>tree-climbing lions</strong>, vast flocks of <strong>flamingos</strong>, and diverse landscape.'),
            ('When is the best time for bird watching?', 'For bird watching, the <strong>wet season (November to May)</strong> is ideal as migratory birds arrive and the lake is full.'),
            ('Can I do a day trip to Lake Manyara?', '<strong>Yes</strong>, due to its proximity to Arusha (approx. 1.5 - 2 hours), Lake Manyara is perfect for a day trip.')
        ]
    },
    'destination-terangile.html': {
        'title': 'Tarangire National Park - Kilimora Adventures',
        'keywords': 'Tarangire, Elephants, Baobab, Safari, Tanzania',
        'desc': 'Discover Tarangire National Park, home to massive elephant herds and iconic baobab trees.',
        'hero_subtitle': 'TARANGIRE DESTINATIONS',
        'hero_title': 'TARANGIRE',
        'hero_desc': 'Known as the "Elephant Playground", Tarangire is famous for its massive herds of elephants and ancient baobab trees dotting the landscape.',
        'hero_bg': 'tembo.jpg',
        'about_img': 'tarangire.jpg',
        'about_title': 'About Tarangire',
        'about_html': '''<p class="mb-4">Tarangire National Park is a protected area in Tanzania\'s Manyara Region. The name of the park originates from the Tarangire River that crosses the park. The river is the primary source of fresh water for wild animals in the Tarangire Ecosystem during the annual dry season.</p>
                        <p class="mb-4">The park is famous for its high density of elephants and baobab trees. Visitors to the park in the June to November dry season can expect to see large herds of thousands of zebra, wildebeest and cape buffalo.</p>''',
        'highlights': [
            ('fa-paw', 'Elephant Herds', 'Largest concentration of elephants in the world.'),
            ('fa-camera', 'Baobab Trees', 'Iconic ancient trees dotting the landscape.'),
            ('fa-globe', 'Tarangire River', 'Lifeline of the park attracting wildlife.'),
            ('fa-cloud', 'Dry Season Safari', 'Incredible game viewing from June to October.'),
            ('fa-binoculars', 'Bird Life', 'A paradise for birders with over 550 species.')
        ],
        'tours_title': 'Experience Tarangire\'s Top Tours',
        'tour_images': ['tembo.jpg', 'pro3.jpg', 'tarangire.jpg', 'photo1.jpeg'],
        'nearby_text': 'Extend your safari adventure by visiting these iconic destinations near Tarangire.',
        'nearby_replace_target': 'Tarangire National Park',
        'nearby_replace_html': '''
            <!-- Serengeti Block -->
            <div class="row align-items-center mb-5">
                <div class="col-lg-6 position-relative">
                    <img src="img/nyumbu-migrate.jpeg" class="img-fluid rounded main-img" alt="Serengeti Plains">
                    <img src="img/simba.jpg" class="img-fluid rounded small-img shadow-lg" alt="Lion">
                </div>
                <div class="col-lg-6">
                    <h3 class="dest-country">Serengeti National Park</h3>
                    <div class="dest-underline"></div>
                    <p class="dest-text">
                        The endless plains of the Serengeti are the stage for the Great Migration. Witness millions of
                        wildebeest, zebras, and predators in this world-renowned ecosystem.
                    </p>
                    <a href="destination-serengeti.html" class="dest-btn">→ EXPLORE SERENGETI</a>
                </div>
            </div>''',
        'faq': [
            ('When is the best time to visit Tarangire?', 'The best time is during the <strong>dry season (June to October)</strong> when animals migrate to the Tarangire River.'),
            ('What is Tarangire famous for?', 'Tarangire is most famous for its <strong>massive elephant herds</strong> and iconic <strong>baobab trees</strong>.'),
            ('How far is Tarangire from Arusha?', 'Tarangire is approximately <strong>120 km (2 hours drive)</strong> from Arusha.')
        ]
    },
    'destination-kilimanjaro.html': {
        'title': 'Mount Kilimanjaro - Kilimora Adventures',
        'keywords': 'Kilimanjaro, Mountain, Climbing, Hiking, Tanzania',
        'desc': 'Conquer Africa\'s highest peak, Mount Kilimanjaro, standing at 5,895 meters above sea level.',
        'hero_subtitle': 'MOUNT KILIMANJARO',
        'hero_title': 'MOUNT KILIMANJARO',
        'hero_desc': 'Conquer Africa\'s highest peak, Mount Kilimanjaro, standing majestically at 5,895 meters above sea level. It is the world\'s highest free-standing mountain.',
        'hero_bg': 'kilimanjaro2.jpg',
        'about_img': 'kilimanjaro3.jpg', # Kili specific image
        'about_title': 'About Mount Kilimanjaro',
        'about_html': '''<p class="mb-4">Mount Kilimanjaro is Africa's highest mountain, standing at 5,895 meters (19,341 feet) above sea level. Located in northeastern Tanzania, this dormant volcano is one of the world's most accessible high summits.</p>
                        <p class="mb-4">The mountain has three volcanic cones: Kibo, Mawenzi, and Shira. The climb takes you through five distinct climate zones, from cultivated land and rainforest to moorland, alpine desert, and finally the arctic summit.</p>''',
        'highlights': [
            ('fa-flag', 'Uhuru Peak', 'Reach the highest point in Africa at 5,895 meters.'),
            ('fa-globe', 'Five Climate Zones', 'Experience diverse ecosystems from rainforest to arctic.'),
            ('fa-camera', 'Volcanic Cones', 'View Kibo, Mawenzi, and Shira cones.'),
            ('fa-map-signs', 'Scenic Routes', 'Choose from Lemosho, Machame, Marangu and more.'),
            ('fa-paw', 'Colobus Monkeys', 'Spot wildlife in the lower rainforest slopes.')
        ],
        'tours_title': 'Experience Kilimanjaro\'s Top Tours',
        'tour_images': ['kilimanjaro2.jpg', 'pro3.jpg', 'kilimanjaro3.jpg', 'photo1.jpeg'],
        'nearby_text': 'After your climb, relax by visiting these iconic destinations in Tanzania.',
        'nearby_replace_target': '', # No self-reference in Nearby (Ngo, Manyara, Tar, Zan). But we could add Serengeti if we wanted. For now, leave as is.
        'nearby_replace_html': '',   # Or maybe replace Zanzibar with something else? No, Zanzibar is perfect after Kili.
        'faq': [
            ('What is the best time to climb Kilimanjaro?', 'The best times are the warm and dry months: <strong>January to March</strong> and <strong>June to October</strong>.'),
            ('How many days does it take to climb?', 'Most routes take between <strong>5 to 9 days</strong>. We recommend longer routes (7+ days) for better acclimatization.'),
            ('Do I need technical climbing skills?', '<strong>No</strong>, Kilimanjaro is a "walk-up" mountain. You do not need technical climbing gears, but good physical fitness is essential.')
        ]
    },
    'destination-mikumi.html': {
        'title': 'Mikumi National Park - Kilimora Adventures',
        'keywords': 'Mikumi, Wildlife, Safari, National Park, Tanzania',
        'desc': 'Explore Mikumi National Park, Tanzania\'s fourth-largest national park with abundant wildlife.',
        'hero_subtitle': 'MIKUMI DESTINATIONS',
        'hero_title': 'MIKUMI',
        'hero_desc': 'Explore Mikumi National Park, Tanzania\'s fourth-largest park with abundant wildlife and stunning landscapes, often called "The Little Serengeti".',
        'hero_bg': 'mix.jpg',
        'about_img': 'pundamilia.jpeg', # Zebra
        'about_title': 'About Mikumi',
        'about_html': '''<p class="mb-4">Mikumi National Park is Tanzania's fourth-largest national park, covering an area of 3,230 square kilometers. Located between the Uluguru Mountains and the Lumango range.</p>
                        <p class="mb-4">The park is characterized by its Mkata Floodplain, which is often compared to the Serengeti plains due to its open horizons and abundant wildlife including lions, elephants, buffaloes, and zebras.</p>''',
        'highlights': [
            ('fa-globe', 'Mkata Floodplain', 'Open savanna plains teeming with diverse wildlife.'),
            ('fa-paw', 'Big Game', 'Home to lions, elephants, buffaloes and giraffes.'),
            ('fa-road', 'Accessible Safari', 'Easily accessible from Dar es Salaam (4-5 hours).'),
            ('fa-binoculars', 'Bird Life', 'Over 400 bird species recorded in the park.'),
            ('fa-water', 'Hippo Pools', 'View hippos and crocodiles close to the main gate.')
        ],
        'tours_title': 'Experience Mikumi\'s Top Tours',
        'tour_images': ['mix.jpg', 'pro3.jpg', 'pundamilia.jpeg', 'photo1.jpeg'],
        'nearby_text': 'Combine your Mikumi safari with these other Tanzanian destinations.',
        'nearby_replace_target': '', # No self-reference (Ngo, Manyara, Tar, Zan).
        'nearby_replace_html': '',
        'faq': [
            ('How do I get to Mikumi National Park?', 'Mikumi is very accessible. It is about a <strong>4-5 hour drive</strong> from Dar es Salaam on a good tarmac road.'),
            ('When is the best time to visit Mikumi?', 'The dry season from <strong>June to October</strong> is best for wildlife viewing as vegetation is thinner.'),
            ('What animals can I expect to see?', 'You can see the Mkata Floodplain ecosystem which supports elands, buffaloes, zebras, giraffes, elephants, lions, and leopards.')
        ]
    }
}

def restore_file(filename, data):
    new_content = template
    
    # 1. Metadata
    new_content = re.sub(r'<title>.*?</title>', f'<title>{data["title"]}</title>', new_content)
    new_content = re.sub(r'name="keywords".*?>', f'name="keywords" content="{data["keywords"]}">', new_content)
    new_content = re.sub(r'name="description".*?>', f'name="description" content="{data["desc"]}">', new_content)
    
    # 2. Hero
    new_content = new_content.replace('SERENEGETI DESTINATIONS', data['hero_subtitle'])
    new_content = re.sub(r'<h1 class="text-white mb-3 animated slideInDown" style="font-size: 3rem;">SERENGETI</h1>', f'<h1 class="text-white mb-3 animated slideInDown" style="font-size: 3rem;">{data["hero_title"]}</h1>', new_content)
    new_content = re.sub(r'<p class="fs-6 text-white mb-4 animated slideInDown">.*?</p>', f'<p class="fs-6 text-white mb-4 animated slideInDown">{data["hero_desc"]}</p>', new_content, flags=re.DOTALL)
    new_content = new_content.replace('url(img/nyumbu-migrate.jpeg)', f'url(img/{data["hero_bg"]})')
    
    # 3. About
    new_content = new_content.replace('<img class="img-fluid" src="img/twiga.jpg"', f'<img class="img-fluid" src="img/{data["about_img"]}"')
    new_content = new_content.replace('About Serengeti', data['about_title'])
    # Fix: Use specific title in regex to avoid replacing "Highlights" section structure
    # The About text is inside a div after the header div. 
    # But wait, looking at template structure:
    # <div class="h-100">
    #    <div class="d-flex ..."><h2 ...>About ...</h2></div>
    #    <p>...</p> </div>
    # The regex r'(<h2 ...>...</h2>\s*</div>\s*).*?</div>' matches up to the closing div of the h-100 container?
    # No, it matches until the first </div>. Structure is:
    # <div> <h2>...</h2> </div> (Header Div)
    # <p>...</p> (Content)
    # </div> (Container Div)
    # So .*?</div> matches the Header Div closing div? BOOM.
    # Actually: (<h2...>...</h2>\s*</div>\s*) consumes the Header Div and its closing tag.
    # Then .*?</div> consumes content up to the NEXT </div>, which is the Container Div closing tag.
    # So yes, it works for About. 
    # But for Highlights:
    # <div> <h2>Highlights</h2> </div> (Header Div)
    # <div class="row g-4"> (Row Div)
    # ... </div> (Row Div close)
    # So it replaces the Row Div start and content!
    
    # We MUST use the specific title to only target the About section.
    new_content = re.sub(
        r'(<h2 class="mb-0">' + re.escape(data['about_title']) + r'</h2>\s*</div>\s*).*?</div>', 
        f'\\1{data["about_html"]}</div>', 
        new_content, 
        flags=re.DOTALL
    )
    
    # 4. Highlights
    # Replace the entire Highlights Section block
    hl_html = generate_highlights_html(data['highlights'])
    new_content = re.sub(
        r'<!-- Highlights Section -->.*?<!-- Top Tours Carousel -->',
        f'{hl_html}\n\n    <!-- Top Tours Carousel -->',
        new_content,
        flags=re.DOTALL
    )
    
    # 5. Tours
    new_content = new_content.replace('Experience Serengeti\'s Top Tours', data['tours_title'])
    t_imgs = data['tour_images']
    # Updated regex to match new 'img-fluid tour-img' class
    new_content = re.sub(r'(<!-- Tour Item 1 -->.*?<img class="img-fluid tour-img" src=")img/[^"]+(")', f'\\1img/{t_imgs[0]}\\2', new_content, flags=re.DOTALL)
    new_content = re.sub(r'(<!-- Tour Item 2 -->.*?<img class="img-fluid tour-img" src=")img/[^"]+(")', f'\\1img/{t_imgs[1]}\\2', new_content, flags=re.DOTALL)
    new_content = re.sub(r'(<!-- Tour Item 3 -->.*?<img class="img-fluid tour-img" src=")img/[^"]+(")', f'\\1img/{t_imgs[2]}\\2', new_content, flags=re.DOTALL)
    new_content = re.sub(r'(<!-- Tour Item 4 -->.*?<img class="img-fluid tour-img" src=")img/[^"]+(")', f'\\1img/{t_imgs[3]}\\2', new_content, flags=re.DOTALL)

    # 6. Nearby Destinations
    # Replace the descriptive text
    if 'nearby_text' in data:
        new_content = re.sub(r'Extend your safari adventure by visiting these iconic destinations near Serengeti\.', data['nearby_text'], new_content)
    
    # Replace self-reference if needed
    target = data.get('nearby_replace_target')
    replace_html = data.get('nearby_replace_html')
    if target and replace_html:
        pattern = re.compile(r'(<div class="row [^"]+">\s*<div class="col-lg-6 position-relative">.*?<h3 class="dest-country">' + re.escape(target) + r'</h3>.*?</div>\s*</div>)', re.DOTALL)
        new_content = pattern.sub(replace_html, new_content)

    # 7. FAQ Replacement
    faq_html = generate_faq_html(data['faq'])
    new_content = re.sub(
        r'<!-- FAQ Section -->.*?<!-- Footer Start -->', 
        f'{faq_html}\n\n    <!-- Footer Start -->', 
        new_content, 
        flags=re.DOTALL
    )

    # Write
    with open(f"d:\\website template\\kilimora\\{filename}", 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"[OK] RE-Restored {filename}")

print("Starting Universal Restoration...")
for fname, fdata in content_map.items():
    restore_file(fname, fdata)
print("Complete.")
