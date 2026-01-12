import os
import re

# Define the new footer HTML (from index.html)
NEW_FOOTER = '''    <!-- Footer Start -->
    <!-- Awards Section (Auto Scrolling) -->
    <section class="py-5" style="background:#fff;">
        <div class="container text-center mb-4">
            <h2 class="fw-bold" style="font-size:40px;">
                <span style="border-left:5px solid #d4a017; padding-left:15px;">Awards</span>
            </h2>
        </div>

        <div class="awards-slider">
            <div class="awards-track">
                <!-- Original Set -->
                <img src="img/logo1.png" alt="Awards" class="award-img">
                <img src="img/logo1.png" alt="Awards" class="award-img">
                <img src="img/logo1.png" alt="Awards" class="award-img">
                <img src="img/logo1.png" alt="Awards" class="award-img">
                <img src="img/logo1.png" alt="Awards" class="award-img">
                <img src="img/logo1.png" alt="Awards" class="award-img">
                <img src="img/logo1.png" alt="Awards" class="award-img">
                <img src="img/logo1.png" alt="Awards" class="award-img">

                <!-- Duplicate Set for Seamless Loop -->
                <img src="img/logo1.png" alt="Awards" class="award-img">
                <img src="img/logo1.png" alt="Awards" class="award-img">
                <img src="img/logo1.png" alt="Awards" class="award-img">
                <img src="img/logo1.png" alt="Awards" class="award-img">
                <img src="img/logo1.png" alt="Awards" class="award-img">
                <img src="img/logo1.png" alt="Awards" class="award-img">
                <img src="img/logo1.png" alt="Awards" class="award-img">
                <img src="img/logo1.png" alt="Awards" class="award-img">
            </div>
        </div>
    </section>

    <style>
        .awards-slider {
            overflow: hidden;
            white-space: nowrap;
            position: relative;
            width: 100%;
            /* Optional: Add background color or padding if needed */
        }

        /* Fade effects on edges */
        .awards-slider::before,
        .awards-slider::after {
            content: "";
            position: absolute;
            top: 0;
            width: 150px;
            /* Width of the fade */
            height: 100%;
            z-index: 2;
        }

        .awards-slider::before {
            left: 0;
            background: linear-gradient(to right, white, transparent);
        }

        .awards-slider::after {
            right: 0;
            background: linear-gradient(to left, white, transparent);
        }

        .awards-track {
            display: inline-flex;
            gap: 80px;
            /* Space between logos */
            animation: scrollAwards 40s linear infinite;
            /* Increased time for smoother slow scroll */
        }

        /* Pause animation on hover */
        .awards-slider:hover .awards-track {
            animation-play-state: paused;
        }

        .award-img {
            height: 110px;
            object-fit: contain;
            flex-shrink: 0;
            /* Prevent shrinking */
        }

        @keyframes scrollAwards {
            0% {
                transform: translateX(0);
            }

            100% {
                /* Move by half the width of the track (since we duplicated the content) */
                transform: translateX(-50%);
            }
        }
    </style>

    <!-- Divider Line -->
    <hr style="border-top:1px solid #ccc; margin:40px auto; width:90%;">


    <!-- FOOTER START -->
    <footer class="pt-5" style="background:#fff; color:#000;">

        <div class="container">

            <!-- TOP ROW LINKS -->
            <div class="row gy-4">

                <!-- About -->
                <div class="col-lg-2 col-md-6">
                    <h5 class="fw-bold mb-3">About Kilimora</h5>
                    <ul class="list-unstyled footer-list">
                        <li><a href="#">Why Book with Kilimora</a></li>
                        <li><a href="#">Our Guides</a></li>
                        <li><a href="#">Our Vehicles</a></li>
                        <li><a href="#">See All Tours</a></li>
                        <li><a href="#">Kilimora Foundation</a></li>
                        <li><a href="#">Kilimora DMC Tanzania</a></li>
                    </ul>
                    <!-- <img src="img/logo.png" style="width:160px; margin-top:10px;"> -->
                </div>

                <!-- Destinations -->
                <div class="col-lg-2 col-md-6">
                    <h5 class="fw-bold mb-3">Top Destinations</h5>

                    <ul class="list-unstyled footer-list">
                        <li><a href="#">Serengeti</a></li>
                        <li><a href="#">Ngorongoro</a></li>
                        <li><a href="#">Mount Kilimanjaro</a></li>
                        <li><a href="#">Tarangire</a></li>
                        <li><a href="#">Lake Manyara</a></li>
                        <li><a href="#">Mikumi National Park</a></li>

                    </ul>
                </div>

                <!-- Experiences -->
                <div class="col-lg-2 col-md-6">
                    <h5 class="fw-bold mb-3">Top Experiences</h5>
                    <ul class="list-unstyled footer-list">
                        <li><a href="#">Tanzania Safari</a></li>
                        <li><a href="#">Great Migration</a></li>
                        <li><a href="#">Zanzibar</a></li>
                        <li><a href="#">Mt. Kilimanjaro</a></li>
                    </ul>
                </div>

                <!-- Booking Resource -->
                <div class="col-lg-2 col-md-6">
                    <h5 class="fw-bold mb-3">Booking Resource</h5>
                    <ul class="list-unstyled footer-list">
                        <li><a href="#">Contact Us</a></li>
                        <li><a href="#">Payment and Terms</a></li>
                        <li><a href="#">Blog</a></li>
                    </ul>
                </div>

                <!-- Useful Information -->
                <div class="col-lg-2 col-md-6">
                    <h5 class="fw-bold mb-3">Useful Information</h5>
                    <ul class="list-unstyled footer-list">
                        <li><a href="#">Health Entry Details TZ</a></li>
                        <li><a href="#">Safari Packing List</a></li>
                        <li><a href="#">Pack for Kilimanjaro</a></li>
                        <li><a href="#">Visa to Tanzania</a></li>
                    </ul>
                </div>

                <!-- Newsletter -->
                <div class="col-lg-2 col-md-6">
                    <h5 class="fw-bold mb-3">Sign up for the Newsletter</h5>
                    <form class="newsletter-form">
                        <input type="email" class="form-control mb-2" placeholder="Email">
                        <button class="btn w-100"
                            style="background:#d4a017; color:#fff; font-weight:bold;">SUBSCRIBE</button>
                    </form>
                </div>

            </div>

            <!-- CONTACT ROW -->
            <div class="row mt-5 gy-4">

                <!-- Contact -->
                <div class="col-lg-4">
                    <h5 class="fw-bold mb-3">Contact</h5>
                    <p><i class="fa fa-map-marker-alt me-2"></i>Location: Usariver, Arusha,Tanzania</p>
                    <p><i class="fa fa-road me-2"></i>Street/Road: Mandela Road</p>
                    <p><i class="fa fa-landmark me-2"></i>Landmark: Near Kennedy House</p>
                </div>

                <!-- Traveler Assistance -->
                <div class="col-lg-4">
                    <h5 class="fw-bold mb-3">Traveler Assistance</h5>
                    <p style="font-size: 0.9em; color: #555; margin-bottom: 0.5rem;">All numbers operate in EAT – UTC +3
                    </p>
                    <p><i class="fa fa-phone me-2"></i>+255 796 440 555</p>
                    <p><i class="fa fa-phone me-2"></i>+255 762 008 009</p>
                    <p><i class="fa fa-phone me-2"></i>+255 717 647 994</p>
                </div>

                <!-- Social Icons -->
                <div class="col-lg-4">
                    <h5 class="fw-bold mb-3">Follow Us</h5>
                    <div class="d-flex gap-3 fs-4">
                        <a href="https://www.facebook.com/share/1GWydnMmsK/?mibextid=wwXIfr"><i
                                class="fab fa-facebook"></i></a>
                        <a href="https://www.instagram.com/kilimora.adventure?igsh=cjVjaTV4dTZzZXk2"><i
                                class="fab fa-instagram"></i></a>
                        <a href="#"><i class="fab fa-pinterest"></i></a>
                        <a href="#"><i class="fab fa-youtube"></i></a>
                        <a href="https://www.tiktok.com/@kilimora_adventure?_r=1&_t=ZS-92vfi2bYN0b"><i
                                class="fab fa-tiktok"></i></a>
                        <a href="#"><i class="fab fa-linkedin"></i></a>
                        <a href="#"><i class="fab fa-x-twitter"></i></a>
                    </div>
                </div>

            </div>

            <div class="text-center mt-4 py-3" style="color:#777;">
                © 2025 Kilimora Adventures — All Rights Reserved
            </div>

        </div>
    </footer>

    <style>
        .footer-list li {
            margin-bottom: 8px;
        }

        .footer-list a {
            color: #000;
            text-decoration: none;
        }

        .footer-list a:hover {
            text-decoration: underline;
        }
    </style>

    <!-- Footer End -->'''

# Directory containing HTML files
directory = r"d:\website template\kilimora"

# Get all HTML files except index.html
html_files = [f for f in os.listdir(directory) if f.endswith('.html') and f != 'index.html']

print(f"Found {len(html_files)} HTML files to update (excluding index.html)")

# Process each file
for filename in html_files:
    filepath = os.path.join(directory, filename)
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace footer section
        # Pattern to match from <!-- Footer Start --> to <!-- Footer End -->
        pattern = r'<!-- Footer Start -->.*?<!-- Footer End -->'
        
        if re.search(pattern, content, re.DOTALL):
            # Replace the footer
            new_content = re.sub(pattern, NEW_FOOTER, content, flags=re.DOTALL)
            
            # Write back to file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"[OK] Updated: {filename}")
        else:
            print(f"[SKIP] Footer markers not found in: {filename}")
    
    except Exception as e:
        print(f"[ERROR] Error processing {filename}: {str(e)}")

print("\nFooter update complete!")
