import re

# 1. Read the Template (Serengeti) - Re-reading to be safe
with open('d:\\website template\\kilimora\\destination-serengeti.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Define FAQ HTML Generator function
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

# Reuse the content map from previous step
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
        # Highlights: (icon, title, desc)
        'highlights': [
            ('fa-paw', 'Big 5 Safari', 'One of the best places to see the Big 5 in a single day.'),
            ('fa-camera', 'Black Rhino', 'A sanctuary for the endangered Black Rhino.'),
            ('fa-globe', 'Volcanic Caldera', 'The world\'s largest inactive, intact and unfilled volcanic caldera.'),
            ('fa-cloud', 'Maasai Culture', 'Witness the coexistence of Maasai herdsmen and wildlife.'),
            ('fa-binoculars', 'Bird Watching', 'Flamingos in Lake Magadi and diverse avian life.')
        ],
        'tours_title': 'Experience Ngorongoro\'s Top Tours',
        'tour_images': ['ngo.jpg', 'pro3.jpg', 'tembo10.jpeg', 'photo1.jpeg'],
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
                        wildebeest, zebras, and predators in this world-renowned ecosystem that offers unrivaled
                        wildlife viewing year-round.
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
        'about_html': '''<p class="mb-4">Tarangire National Park is the sixth largest national park in Tanzania, it is located in Manyara Region. The name of the park originates from the Tarangire River that crosses the park.</p>
                        <p class="mb-4">The river is the primary source of fresh water for wild animals in the Tarangire Ecosystem during the annual dry season. The park is famous for its high density of elephants and baobab trees.</p>''',
        'highlights': [
            ('fa-paw', 'Elephant Herds', 'Largest concentration of elephants in the world.'),
            ('fa-camera', 'Baobab Trees', 'Iconic ancient trees dotting the landscape.'),
            ('fa-globe', 'Tarangire River', 'Lifeline of the park attracting wildlife.'),
            ('fa-cloud', 'Dry Season Safari', 'Incredible game viewing from June to October.'),
            ('fa-binoculars', 'Bird Life', 'A paradise for birders with over 550 species.')
        ],
        'tours_title': 'Experience Tarangire\'s Top Tours',
        'tour_images': ['tembo.jpg', 'pro3.jpg', 'tarangire.jpg', 'photo1.jpeg'],
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
    }
}

def restore_file(filename, data):
    new_content = template
    
    # 1. Metadata
    new_content = re.sub(r'<title>.*?</title>', f'<title>{data["title"]}</title>', new_content)
    new_content = re.sub(r'name="keywords".*?>', f'name="keywords" content="{data["keywords"]}">', new_content)
    new_content = re.sub(r'name="description".*?>', f'name="description" content="{data["desc"]}">', new_content)
    
    # 2. Hero
    new_content = re.sub(r'SERENEGETI DESTINATIONS', data['hero_subtitle'], new_content)
    new_content = re.sub(r'<h1 class="text-white mb-3 animated slideInDown" style="font-size: 3rem;">SERENGETI</h1>', f'<h1 class="text-white mb-3 animated slideInDown" style="font-size: 3rem;">{data["hero_title"]}</h1>', new_content)
    new_content = re.sub(r'<p class="fs-6 text-white mb-4 animated slideInDown">.*?</p>', f'<p class="fs-6 text-white mb-4 animated slideInDown">{data["hero_desc"]}</p>', new_content, flags=re.DOTALL)
    new_content = re.sub(r'url\(img/nyumbu-migrate.jpeg\)', f'url(img/{data["hero_bg"]})', new_content)
    
    # 3. About
    new_content = re.sub(r'<img class="img-fluid" src="img/twiga.jpg"', f'<img class="img-fluid" src="img/{data["about_img"]}"', new_content)
    new_content = re.sub(r'About Serengeti', data['about_title'], new_content)
    new_content = re.sub(r'(<h2 class="mb-0">.*?</h2>\s*</div>\s*).*?</div>', f'\\1{data["about_html"]}</div>', new_content, flags=re.DOTALL)
    
    # 4. Highlights
    # Replace icons and text for all 5 highlights
    hl = data['highlights']
    # Helper for Highlights replacement - doing it sequentially
    # Item 1
    new_content = re.sub(r'(<h5>)The Great Migration(</h5>\s*<p class="mb-0">).*?(</p>)', f'\\1{hl[0][1]}\\2{hl[0][2]}\\3', new_content, count=1, flags=re.DOTALL)
    new_content = re.sub(r'<i class="fa fa-paw"></i>', f'<i class="fa {hl[0][0]}"></i>', new_content, count=1)
    
    # Item 2
    new_content = re.sub(r'(<h5>)Big 5 Safari(</h5>\s*<p class="mb-0">).*?(</p>)', f'\\1{hl[1][1]}\\2{hl[1][2]}\\3', new_content, count=1, flags=re.DOTALL)
    new_content = re.sub(r'<i class="fa fa-camera"></i>', f'<i class="fa {hl[1][0]}"></i>', new_content, count=1)
    
    # Item 3
    new_content = re.sub(r'(<h5>)Endless Plains(</h5>\s*<p class="mb-0">).*?(</p>)', f'\\1{hl[2][1]}\\2{hl[2][2]}\\3', new_content, count=1, flags=re.DOTALL)
    new_content = re.sub(r'<i class="fa fa-globe"></i>', f'<i class="fa {hl[2][0]}"></i>', new_content, count=1)
    
    # Item 4
    new_content = re.sub(r'(<h5>)Balloon Safaris(</h5>\s*<p class="mb-0">).*?(</p>)', f'\\1{hl[3][1]}\\2{hl[3][2]}\\3', new_content, count=1, flags=re.DOTALL)
    new_content = re.sub(r'<i class="fa fa-cloud"></i>', f'<i class="fa {hl[3][0]}"></i>', new_content, count=1)
    
    # Item 5
    new_content = re.sub(r'(<h5>)Bird Watching(</h5>\s*<p class="mb-0">).*?(</p>)', f'\\1{hl[4][1]}\\2{hl[4][2]}\\3', new_content, count=1, flags=re.DOTALL)
    new_content = re.sub(r'<i class="fa fa-binoculars"></i>', f'<i class="fa {hl[4][0]}"></i>', new_content, count=1)
    
    # 5. Tours
    new_content = re.sub(r'Experience Serengeti\'s Top Tours', data['tours_title'], new_content)
    t_imgs = data['tour_images']
    new_content = re.sub(r'(<!-- Tour Item 1 -->.*?<img class="img-fluid" src=")img/[^"]+(")', f'\\1img/{t_imgs[0]}\\2', new_content, flags=re.DOTALL)
    new_content = re.sub(r'(<!-- Tour Item 2 -->.*?<img class="img-fluid" src=")img/[^"]+(")', f'\\1img/{t_imgs[1]}\\2', new_content, flags=re.DOTALL)
    new_content = re.sub(r'(<!-- Tour Item 3 -->.*?<img class="img-fluid" src=")img/[^"]+(")', f'\\1img/{t_imgs[2]}\\2', new_content, flags=re.DOTALL)
    new_content = re.sub(r'(<!-- Tour Item 4 -->.*?<img class="img-fluid" src=")img/[^"]+(")', f'\\1img/{t_imgs[3]}\\2', new_content, flags=re.DOTALL)

    # 6. Nearby Destinations
    # Replace the block containing the target name
    target = data['nearby_replace_target']
    replace_html = data['nearby_replace_html']
    pattern = re.compile(r'(<div class="row [^"]+">\s*<div class="col-lg-6 position-relative">.*?<h3 class="dest-country">' + re.escape(target) + r'</h3>.*?</div>\s*</div>)', re.DOTALL)
    new_content = pattern.sub(replace_html, new_content)

    # 7. FAQ Replacement (Robust)
    faq_html = generate_faq_html(data['faq'])
    # Replace the entire FAQ Section block using comments
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

print("Starting FINAL Restoration...")
for fname, fdata in content_map.items():
    restore_file(fname, fdata)
print("Complete.")
