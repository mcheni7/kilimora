import os
import re

# Define the directory
directory = r"d:\website template\kilimora"

# Files to update
files_to_update = [
    "exp-big5.html",
    "exp-ngorongoro.html", 
    "exp-serengeti.html",
    "exp-tarangire.html",
    "exp-zanzibar.html"
]

# Old and new topbar content
old_topbar = '''<small class="me-3 text-light"><i class="fa fa-map-marker-alt me-2"></i>123 Arusha, Kilimanjaro,
                        Tanzania</small>
                    <small class="me-3 text-light"><i class="fa fa-phone-alt me-2"></i>+255 784 554 555</small>'''

new_topbar = '''<small class="me-3 text-light"><i class="fa fa-map-marker-alt me-2"></i>Usariver, Arusha - Mandela Road</small>
                    <small class="me-3 text-light"><i class="fa fa-phone-alt me-2"></i>+255 762 008 009</small>'''

# Old and new footer content (for dark footer style)
old_footer_dark = '''<p class="mb-2"><i class="fa fa-map-marker-alt me-3"></i>123 Arusha, Kilimanjaro, Tanzania</p>
                    <p class="mb-2"><i class="fa fa-phone-alt me-3"></i>+255 784  554 555</p>'''

new_footer_dark = '''<p class="mb-2"><i class="fa fa-map-marker-alt me-3"></i>Usariver, Arusha - Mandela Road (Near Kennedy House)</p>
                    <p class="mb-2"><i class="fa fa-phone-alt me-3"></i>+255 762 008 009</p>
                    <p class="mb-2"><i class="fa fa-phone-alt me-3"></i>+255 755 252 956</p>
                    <p class="mb-2"><i class="fa fa-phone-alt me-3"></i>+255 717 647 994</p>'''

# Process each file
for filename in files_to_update:
    filepath = os.path.join(directory, filename)
    
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace topbar
            content = content.replace(old_topbar, new_topbar)
            
            # Replace footer (try to handle variations)
            # Pattern for footer contact section
            footer_pattern = r'(<p class="mb-2"><i class="fa fa-map-marker-alt me-3"></i>)123 Arusha, Kilimanjaro, Tanzania(</p>\s*<p class="mb-2"><i class="fa fa-phone-alt me-3"></i>)\+255 784 554 555(</p>)'
            footer_replacement = r'\1Usariver, Arusha - Mandela Road (Near Kennedy House)\2+255 762 008 009</p>\n                    <p class="mb-2"><i class="fa fa-phone-alt me-3"></i>+255 755 252 956</p>\n                    <p class="mb-2"><i class="fa fa-phone-alt me-3"></i>+255 717 647 994\3'
            
            content = re.sub(footer_pattern, footer_replacement, content)
            
            # Write back
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✓ Updated {filename}")
        except Exception as e:
            print(f"✗ Error updating {filename}: {e}")
    else:
        print(f"✗ File not found: {filename}")

print("\nUpdate complete!")
