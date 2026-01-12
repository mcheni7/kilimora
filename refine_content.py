import re

# Define the Serengeti Block to use as a replacement for self-references
SERENGETI_BLOCK = '''            <!-- Serengeti Block -->
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
            </div>'''

# FAQ Data for each destination
faq_data = {
    'destination-ngorongoro.html': [
        ('When is the best time to visit Ngorongoro?', 'Wildlife viewing inside the crater is excellent <strong>year-round</strong>. However, the dry season (June to October) is often preferred as grass is shorter, making animals easier to spot.'),
        ('Do I need a 4x4 vehicle?', '<strong>Yes</strong>, a 4x4 safari vehicle is mandatory for descending into the Ngorongoro Crater due to the steep and rough terrain of the descent and ascent roads.'),
        ('Can I see the Big 5 here?', '<strong>Absolutely</strong>. The Ngorongoro Crater is one of the few places in Africa where you have a very high chance of seeing all of the Big 5 (Lion, Leopard, Elephant, Rhino, Buffalo) in a single day.')
    ],
    'destination-terangile.html': [
        ('When is the best time to visit Tarangire?', 'The best time is during the <strong>dry season (June to October)</strong> when thousands of elephants and other animals migrate to the Tarangire River, the only permanent water source in the area.'),
        ('What is Tarangire famous for?', 'Tarangire is most famous for its <strong>massive elephant herds</strong> and iconic <strong>baobab trees</strong>. It is often called the "Elephant Playground" of Tanzania.'),
        ('How far is Tarangire from Arusha?', 'Tarangire is approximately <strong>120 km (2 hours drive)</strong> from Arusha, making it an accessible start or end point for many Northern Circuit safaris.')
    ],
    'destination-manyara.html': [
        ('What is special about Lake Manyara?', 'Lake Manyara is famous for its <strong>tree-climbing lions</strong>, vast flocks of <strong>flamingos</strong>, and diverse landscape ranging from groundwater forests to the alkaline lake.'),
        ('When is the best time for bird watching?', 'For bird watching, the <strong>wet season (November to May)</strong> is ideal as migratory birds arrive and the lake is full. For big game, the dry season (June to October) is better.'),
        ('Can I do a day trip to Lake Manyara?', '<strong>Yes</strong>, due to its proximity to Arusha (approx. 1.5 - 2 hours), Lake Manyara is perfect for a day trip, although an overnight stay allows you to experience the park at a more relaxed pace.')
    ],
    'destination-kilimanjaro.html': [
        ('What is the best time to climb Kilimanjaro?', 'The best times are the warm and dry months: <strong>January to March</strong> and <strong>June to October</strong>. Avoid the wet seasons (April-May and November) for better trekking conditions.'),
        ('How many days does it take to climb?', 'Most routes take between <strong>5 to 9 days</strong>. We recommend longer routes (7+ days) like Lemosho or Machame for better acclimatization and a higher summit success rate.'),
        ('Do I need technical climbing skills?', '<strong>No</strong>, Kilimanjaro is a "walk-up" mountain. You do not need technical climbing gears like ropes or crampons for the standard routes, but good physical fitness and determination are essential.')
    ],
    'destination-mikumi.html': [
        ('How do I get to Mikumi National Park?', 'Mikumi is very accessible. It is about a <strong>4-5 hour drive</strong> from Dar es Salaam on a good tarmac road, making it a popular weekend getaway.'),
        ('When is the best time to visit Mikumi?', 'The dry season from <strong>June to October</strong> is best for wildlife viewing as vegetation is thinner and animals gather around waterholes.'),
        ('What animals can I expect to see?', 'You can see the <strong>Mkata Floodplain</strong> ecosystem which supports elands, buffaloes, zebras, giraffes, elephants, lions, and occasionally leopards and wild dogs.')
    ]
}

# Mapping of Self-Reference Blocks to replace with Serengeti Block
# Example: In Ngorongoro page, finding the Ngorongoro Block and replacing it with Serengeti Block
replacements = {
    'destination-ngorongoro.html': 'Ngorongoro Crater',
    'destination-terangile.html': 'Tarangire National Park',
    'destination-manyara.html': 'Lake Manyara',
    # Kilimanjaro and Mikumi likely don't list themselves if copied from Serengeti (which lists Ngo, Manyara, Tar, Zan).
    # But valid to check.
}

def update_destination_details(filename):
    filepath = f"d:\\website template\\kilimora\\{filename}"
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        print(f"Processing {filename}...")
        
        # 1. Update FAQ Section
        if filename in faq_data:
            faqs = faq_data[filename]
            
            # Construct new FAQ HTML
            new_faq_html = '<div class="accordion" id="accordionExample">\n'
            
            for i, (q, a) in enumerate(faqs):
                is_show = 'show' if i == 0 else ''
                is_collapsed = 'collapsed' if i != 0 else ''
                aria_expanded = 'true' if i == 0 else 'false'
                
                new_faq_html += f'''                        <div class="accordion-item">
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
                        </div>\n'''
            
            new_faq_html += '                    </div>'
            
            # Regex to replace the entire accordion div
            content = re.sub(
                r'<div class="accordion" id="accordionExample">.*?</div>\s*</div>\s*</div>',
                f'{new_faq_html}\n                </div>\n            </div>',
                content,
                flags=re.DOTALL
            )
            print(f"  [OK] Updated FAQs")

        # 2. Update Nearby Destinations (Remove Self-Reference)
        if filename in replacements:
            self_name = replacements[filename]
            # Regex to find the block containing the self-name header
            # Looking for <div class="row ..."> ... <h3 class="dest-country">Self Name</h3> ... </div>
            
            pattern = re.compile(
                r'(<!-- .*? Block -->\s*<div class="row [^"]+">.*?<h3 class="dest-country">' + re.escape(self_name) + r'</h3>.*?</div>\s*</div>)',
                re.DOTALL
            )
            
            if pattern.search(content):
                content = pattern.sub(SERENGETI_BLOCK, content)
                print(f"  [OK] Replaced self-reference '{self_name}' with Serengeti Block")
            else:
                print(f"  [SKIP] Self-reference '{self_name}' not found in Nearby section")
                
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
    except Exception as e:
        print(f"[ERROR] Error processing {filename}: {str(e)}")

# Run for all destination files
dest_files = [
    'destination-ngorongoro.html',
    'destination-terangile.html',
    'destination-manyara.html',
    'destination-kilimanjaro.html',
    'destination-mikumi.html', 
    'destination-serengeti.html' # Serengeti doesn't need changes but good to be generic
]

print("Starting content refinement...")
print("=" * 60)

for f in dest_files:
    update_destination_details(f)

print("=" * 60)
print("Refinement complete!")
