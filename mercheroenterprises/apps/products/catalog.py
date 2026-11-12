"""
Catalog data for the Products section.

Structure
---------
CATEGORIES is a list of "main categories" (Leather Apparel, Motorcycle Track
Racing Gear, ...). A main category never has its own page — it only exists
to organise the navbar dropdown and the /products/ overview.

- If a category HAS subcategories, only the subcategories get real pages
  (hero + description + product grid). Visiting the category itself
  redirects to its first subcategory.
- If a category has NO subcategories (e.g. Leather Gloves, Custom Leather
  Manufacturing), the category itself acts as the page — same hero +
  description + product grid treatment.

Every subcategory (and every subcategory-less category) carries its own
`products` list. Product entries are placeholders (clearly named "Sample"),
ready to be swapped for real names/photos/SKUs — the page layout and data
flow already work end-to-end.
"""

# Number of placeholder products generated for each subcategory / leaf category.
_PRODUCTS_PER_GROUP = 4

CATEGORIES = [
    {
        'slug': 'leather-apparel',
        'name': 'Leather Apparel',
        'tagline': 'Premium leather garments crafted for style, durability, and comfort.',
        'image': '/static/images/garments-final.jpeg',
        'subcategories': [
            {'slug': 'leather-jackets', 'name': 'Leather Jackets'},
            {'slug': 'leather-coats', 'name': 'Leather Coats'},
            {'slug': 'leather-vests', 'name': 'Leather Vests'},
            {'slug': 'leather-blazers', 'name': 'Leather Blazers'},
            {'slug': 'leather-track-suits', 'name': 'Leather Track Suits'},
            {'slug': 'leather-uniforms', 'name': 'Leather Uniforms'},
            {'slug': 'leather-shirts', 'name': 'Leather Shirts'},
            {'slug': 'leather-pants', 'name': 'Leather Pants'},
            {'slug': 'leather-shorts', 'name': 'Leather Shorts'},
            {'slug': 'leather-chaps', 'name': 'Leather Chaps'},
            {'slug': 'leather-skirts', 'name': 'Leather Skirts'},
        ],
    },
    {
        'slug': 'motorcycle-track-racing-gear',
        'name': 'Motorcycle Track Racing Gear',
        'tagline': 'High-performance racing gear engineered for speed, safety, and aerodynamics.',
        'image': '/static/images/racing-suit.jpeg',
        'subcategories': [
            {
                'slug': 'motorcycle-track-racing-suits',
                'name': 'Motorcycle Track Racing Suits',
                'description': 'Premium one-piece and two-piece motorbike racing suits engineered for professional circuit performance, track days, and high-speed touring. Each suit blends advanced abrasion resistance, CE-approved armor, and precision ergonomics for serious riders.',
                'page_specs': [
                    ['Item', 'Professional One-Piece / Two-Piece Racing Suits'],
                    ['Material', 'Genuine Cowhide Leather, Optional Kangaroo Leather, High-Abrasion Resistant Buffalo Leather'],
                    ['Lining', 'Breathable Polyester Mesh, Satin Interior, Optional Removable Thermal Lining'],
                    ['Size Range', 'S, M, L, XL, XXL, XXXL (Custom Sizing & Made-to-Measure Available)'],
                    ['Design Fit', 'Pre-Curved Ergonomic Fit, Aerodynamic Speed Hump, Flexible Stretch Panels'],
                    ['Protection', 'CE-Approved Armor (Shoulders, Elbows, Knees, Hips, Back), Reinforced Impact Zones'],
                    ['Ventilation', 'Perforated Leather Panels, Strategic Air Vents, Breathable Stretch Zones'],
                    ['Closures', 'Heavy-Duty YKK Zippers, Waist Connection Zipper for Two-Piece Configurations'],
                    ['Branding', 'Embossed Logos, Rubber/Silicone Patches, Woven Labels, Private Label Support'],
                    ['Usage', 'Professional Circuit Racing, Track Days, Touring, Performance Riding'],
                ],
                'page_overview': 'Ride with absolute confidence in high-quality motorbike leather suits designed by MERCHERO Enterprises for maximum protection, durability, and comfort. Perfect for professional racers, touring riders, and motorsport enthusiasts, these suits provide advanced abrasion resistance, robust impact protection, and an ergonomic fit to ensure safety and peak performance on every ride.',
                'page_features': [
                    'Premium leather construction with cowhide, kangaroo, or high-abrasion buffalo leather.',
                    'CE-approved armor inserts at shoulders, elbows, knees, hips, and back.',
                    'Ergonomic pre-curved fit with aerodynamic speed hump and flexible stretch panels.',
                    'Perforated leather panels and stretch zones for optimized ventilation and rider comfort.',
                    'Heavy-duty YKK zippers, reinforced safety seams, and durable performance hardware.',
                ],
                'page_why_choose': [
                    'Professionally designed for racing, touring, and recreational riding.',
                    'Premium leather and protective materials ensuring long-lasting safety.',
                    'Comfortable, ergonomic, and breathable architecture for all-day use.',
                    'Full private label customization including custom logos, colorways, and packaging.',
                    'Professional OEM & ODM manufacturing services.',
                    'Competitive factory-direct pricing with worldwide shipping support.',
                ],
                'page_faqs': [
                    {
                        'question': 'Can I customize the colors and add my own team or brand logo?',
                        'answer': 'Yes, MERCHERO Enterprises provides full private label customization, allowing you to select your preferred color palette, integrate your brand logo via embossing or patches, and customize packaging.',
                    },
                    {
                        'question': 'Are these suits certified for professional track racing?',
                        'answer': 'Our suits feature CE-approved armor and triple-stitched high-stress safety seams built to meet rigorous protection standards required for track days and racing.',
                    },
                    {
                        'question': 'Do you offer custom sizing if standard sizes do not fit?',
                        'answer': 'Yes, alongside standard sizes from S to XXXL, we offer complete made-to-measure custom sizing options.',
                    },
                ],
            },
            {'slug': 'motorcycle-track-racing-jackets', 'name': 'Motorcycle Track Racing Jackets'},
            {'slug': 'motorcycle-track-racing-gloves', 'name': 'Motorcycle Track Racing Gloves'},
            {'slug': 'motorcycle-track-racing-boots', 'name': 'Motorcycle Track Racing Boots'},
        ],
    },
    {
        'slug': 'motorcycle-road-riding-gear',
        'name': 'Motorcycle Road Riding Gear',
        'tagline': 'Versatile road riding gear built for comfort, protection, and long journeys.',
        'image': '/static/images/hero1.jpeg',
        'subcategories': [
            {'slug': 'cordura-motorcycle-riding-suits', 'name': 'Cordura Motorcycle Riding Suits'},
            {'slug': 'motorcycle-riding-jackets', 'name': 'Motorcycle Riding Jackets'},
            {'slug': 'motorcycle-riding-shirts', 'name': 'Motorcycle Riding Shirts'},
            {'slug': 'motorcycle-riding-pants', 'name': 'Motorcycle Riding Pants'},
            {'slug': 'motorcycle-riding-gloves', 'name': 'Motorcycle Riding Gloves'},
            {'slug': 'motorcycle-riding-boots', 'name': 'Motorcycle Riding Boots'},
        ],
    },
    {
        'slug': 'motorbike-motocross-gear',
        'name': 'Motorbike Motocross Gear',
        'tagline': 'Rugged motocross gear designed for off-road durability and maximum mobility.',
        'image': '/static/images/hero-final.jpeg',
        'subcategories': [
            {'slug': 'motocross-riding-suits', 'name': 'Motocross Riding Suits'},
            {'slug': 'motocross-riding-gloves', 'name': 'Motocross Riding Gloves'},
            {'slug': 'motocross-riding-boots', 'name': 'Motocross Riding Boots'},
        ],
    },
    {
        'slug': 'leather-gloves',
        'name': 'Leather Gloves',
        'tagline': 'Fine leather gloves for fashion, riding, work, and outdoor pursuits.',
        'image': '/static/images/gloves.jpeg',
        'subcategories': [
            {'slug': 'motorcycle-riding-leather-gloves', 'name': 'Motorcycle Riding Gloves'},
            {'slug': 'driving-leather-gloves', 'name': 'Driving Leather Gloves'},
            {'slug': 'winter-leather-gloves', 'name': 'Winter Leather Gloves'},
            {'slug': 'casual-fashion-leather-gloves', 'name': 'Casual & Fashion Leather Gloves'},
            {'slug': 'work-safety-leather-gloves', 'name': 'Work & Safety Leather Gloves'},
            {'slug': 'tactical-leather-gloves', 'name': 'Tactical Leather Gloves'},
            {'slug': 'fingerless-leather-gloves', 'name': 'Fingerless Leather Gloves'},
        ],
    },
    {
        'slug': 'leather-bags',
        'name': 'Leather Bags',
        'tagline': 'Handcrafted leather bags blending timeless elegance with everyday functionality.',
        'image': '/static/images/bags.jpeg',
        'subcategories': [
            {'slug': 'leather-backpacks', 'name': 'Leather Backpacks'},
            {'slug': 'leather-duffel-bags', 'name': 'Leather Duffel Bags'},
            {'slug': 'leather-travel-bags', 'name': 'Leather Travel Bags'},
            {'slug': 'leather-messenger-bags', 'name': 'Leather Messenger Bags'},
            {'slug': 'leather-shoulder-bags', 'name': 'Leather Shoulder Bags'},
            {'slug': 'leather-tote-bags', 'name': 'Leather Tote Bags'},
            {'slug': 'leather-handbags', 'name': 'Leather Handbags'},
            {'slug': 'leather-purses', 'name': 'Leather Purses'},
            {'slug': 'leather-laptop-bags', 'name': 'Leather Laptop Bags'},
            {'slug': 'leather-briefcases', 'name': 'Leather Briefcases'},
            {'slug': 'motorcycle-saddle-bags', 'name': 'Motorcycle Saddle Bags'},
            {'slug': 'leather-tool-bags', 'name': 'Leather Tool Bags'},
            {'slug': 'leather-utility-bags', 'name': 'Leather Utility Bags'},
            {'slug': 'leather-luggage-bags', 'name': 'Leather Luggage Bags'},
        ],
    },
    {
        'slug': 'leather-hats-and-caps',
        'name': 'Leather Hats & Caps',
        'tagline': 'Distinctive leather headwear crafted for timeless style and character.',
        'image': '/static/images/hero-final.jpeg',
        'subcategories': [
            {'slug': 'leather-biker-hats', 'name': 'Leather Biker Hats'},
            {'slug': 'leather-cowboy-hats', 'name': 'Leather Cowboy Hats'},
            {'slug': 'leather-baseball-caps', 'name': 'Leather Baseball Caps'},
            {'slug': 'leather-flat-caps', 'name': 'Leather Flat Caps'},
            {'slug': 'leather-newsboy-caps', 'name': 'Leather Newsboy Caps'},
            {'slug': 'leather-aviator-hats', 'name': 'Leather Aviator Hats'},
            {'slug': 'leather-trapper-hats', 'name': 'Leather Trapper Hats'},
            {'slug': 'leather-bucket-hats', 'name': 'Leather Bucket Hats'},
        ],
    },
    {
        'slug': 'equestrian-gear',
        'name': 'Equestrian Gear',
        'tagline': 'Professional equestrian equipment for riders who demand quality and performance.',
        'image': '/static/images/hero-final.jpeg',
        'subcategories': [
            {'slug': 'horse-riding-boots', 'name': 'Horse Riding Boots'},
            {'slug': 'horse-riding-chaps', 'name': 'Horse Riding Chaps'},
            {'slug': 'horse-riding-gloves', 'name': 'Horse Riding Gloves'},
            {'slug': 'horse-saddles', 'name': 'Horse Saddles'},
            {'slug': 'horse-bridles', 'name': 'Horse Bridles'},
            {'slug': 'horse-halters', 'name': 'Horse Halters'},
            {'slug': 'horse-reins', 'name': 'Horse Reins'},
            {'slug': 'horse-girths', 'name': 'Horse Girths'},
            {'slug': 'horse-saddle-bags', 'name': 'Horse Saddle Bags'},
        ],
    },
    {
        'slug': 'custom-leather-manufacturing',
        'name': 'Custom Leather Manufacturing',
        'tagline': 'End-to-end OEM/ODM leather manufacturing solutions tailored to your brand.',
        'image': '/static/images/manufacturing2.jpg',
        'subcategories': [],
    },
]


# ---------------------------------------------------------------------------
# Size-chart templates, picked per subcategory by keyword so every product
# gets a sensible chart without hand-writing one for all ~70 subcategories.
# ---------------------------------------------------------------------------

_CLOTHING_CHART = {
    'columns': ['Size', 'Chest (in)', 'Waist (in)', 'Length (in)'],
    'rows': [
        ['S', '38', '32', '27'],
        ['M', '40', '34', '28'],
        ['L', '42', '36', '29'],
        ['XL', '44', '38', '30'],
        ['XXL', '46', '40', '31'],
    ],
    'note': 'Standard size run shown below — every garment is also available in fully custom, made-to-measure sizing.',
}

_GLOVE_CHART = {
    'columns': ['Size', 'Palm Width (in)', 'Hand Length (in)'],
    'rows': [
        ['S', '3.3', '6.7'],
        ['M', '3.5', '7.0'],
        ['L', '3.7', '7.5'],
        ['XL', '4.0', '8.0'],
    ],
    'note': 'Measure around the palm (excluding thumb) and from wrist crease to middle fingertip for the best fit.',
}

_BOOT_CHART = {
    'columns': ['EU', 'UK', 'US', 'Foot Length (cm)'],
    'rows': [
        ['40', '6.5', '7.5', '25.4'],
        ['42', '8', '9', '26.7'],
        ['44', '9.5', '10.5', '28.0'],
        ['46', '11', '12', '29.4'],
    ],
    'note': 'Half sizes and wide-fit lasts are available on request for bulk orders.',
}

_HAT_CHART = {
    'columns': ['Size', 'Head Circumference (in)'],
    'rows': [
        ['S', '21.5 - 22'],
        ['M', '22.1 - 22.5'],
        ['L', '22.6 - 23.2'],
        ['XL', '23.3 - 23.8'],
    ],
    'note': 'Measure around the head just above the ears for an accurate fit.',
}

_BAG_CHART = {
    'columns': ['Size', 'Dimensions (L x W x H, in)', 'Approx. Weight'],
    'rows': [
        ['Small', '11 x 4 x 8', '0.9 kg'],
        ['Medium', '15 x 6 x 11', '1.3 kg'],
        ['Large', '19 x 8 x 13', '1.8 kg'],
    ],
    'note': 'Custom dimensions, compartments, and hardware finishes are available for OEM/bulk orders.',
}

_TACK_CHART = {
    'columns': ['Fit', 'Notes'],
    'rows': [
        ['Universal', 'Adjustable straps/buckles fit most horse sizes'],
        ['Custom', 'Made-to-measure fit available on request'],
    ],
    'note': 'This item ships in a universal adjustable fit; contact us for horse-specific custom sizing.',
}


def _size_chart_for(subcategory_slug):
    """Pick a sensible size-chart template based on the subcategory slug."""
    slug = subcategory_slug
    if 'glove' in slug:
        return _GLOVE_CHART
    if 'boot' in slug:
        return _BOOT_CHART
    if 'hat' in slug or 'cap' in slug:
        return _HAT_CHART
    if any(key in slug for key in ('bag', 'backpack', 'luggage', 'briefcase', 'tote', 'handbag', 'purse', 'duffel', 'messenger')):
        return _BAG_CHART
    if any(key in slug for key in ('saddle', 'bridle', 'halter', 'rein', 'girth')):
        return _TACK_CHART
    return _CLOTHING_CHART


def _build_products(group_slug, group_name, category, count=_PRODUCTS_PER_GROUP):
    """Generate placeholder product entries for a subcategory/leaf category.

    These are clearly labelled samples so the pages are never empty — swap
    the name/image/sku fields here (or move this data to the database) once
    real product photography and copy are ready.
    """
    size_chart = _size_chart_for(group_slug)

    if group_slug == 'motorcycle-track-racing-suits':
        return [
            {
                'slug': 'merchero-professional-one-piece-motorbike-racing-suit',
                'name': 'MERCHERO Professional One-Piece Motorbike Racing Suit',
                'image': '/static/images/racingsuit1-front.jpeg',
                'images': [
                    '/static/images/racingsuit1-front.jpeg',
                    '/static/images/racingsuit1-back.jpeg',
                ],
                'sku': 'MTRS-001',
                'short_desc': 'Professional motorbike racing suit engineered for track performance, comfort, and customizable OEM branding.',
                'description': (
                    'Ride with absolute confidence in high-quality motorbike leather suits designed by MERCHERO Enterprises for maximum protection, durability, and comfort. '
                    'Perfect for professional racers, touring riders, and motorsport enthusiasts, these suits provide advanced abrasion resistance, robust impact protection, and an ergonomic fit to ensure safety and peak performance on every ride. '
                    'MERCHERO Enterprises manufactures custom motorbike leather suits for global brands, racing teams, and private-label retailers worldwide. Our OEM and ODM services allow full customization of materials, colorways, sizing specifications, and brand iconography.'
                ),
                'features': [
                    'Premium leather construction with cowhide, kangaroo, or high-abrasion buffalo leather.',
                    'CE-approved armor at shoulders, elbows, knees, hips, and back.',
                    'Ergonomic pre-curved fit with aerodynamic speed hump and flexible stretch panels.',
                    'Perforated leather panels and breathable stretch zones for optimized ventilation.',
                    'Heavy-duty YKK zippers, reinforced safety seams, and durable performance hardware.',
                ],
                'size_chart': size_chart,
                'category_slug': category['slug'],
                'subcategory_slug': group_slug,
            },
            {
                'slug': 'merchero-cyanide-velocity-motorbike-leather-suit',
                'name': 'MERCHERO Cyanide Velocity Motorbike Leather Suit',
                'image': '/static/images/racingsuit2-front.jpeg',
                'images': [
                    '/static/images/racingsuit2-front.jpeg',
                    '/static/images/racingsuit2-back.jpeg',
                ],
                'sku': 'MTRS-002',
                'short_desc': 'High-velocity motorbike leather suit featuring striking Cyanide accents and race ergonomics.',
                'description': (
                    'The MERCHERO Cyanide Velocity Motorbike Leather Suit provides dynamic flexibility, '
                    'abrasion-resistant full-grain leather, and optimal ventilation for peak track performance.'
                ),
                'features': [
                    'Full-grain cowhide leather with high-abrasion resistance',
                    'CE-approved internal armors on shoulders, elbows, and knees',
                    'Aerodynamic speed hump and ventilation perforations',
                ],
                'size_chart': size_chart,
                'category_slug': category['slug'],
                'subcategory_slug': group_slug,
            },
            {
                'slug': 'merchero-ignite-gp-leather-racing-suit',
                'name': 'MERCHERO Ignite GP Leather Racing Suit',
                'image': '/static/images/racingsuit3-front.png',
                'images': [
                    '/static/images/racingsuit3-front.png',
                    '/static/images/racingsuit3-back.png',
                ],
                'sku': 'MTRS-003',
                'short_desc': 'Grand Prix inspired leather suit built for aggressive leaning and maximum track speed.',
                'description': (
                    'The MERCHERO Ignite GP Leather Racing Suit delivers top-tier competition performance with heat '
                    'dissipation panels, pre-curved sleeves, and multi-stitched main seams for ultimate durability on the circuit.'
                ),
                'features': [
                    'Pre-curved arms and legs for natural racing position',
                    'Replaceable TPU knee sliders and shoulder TPU sliders',
                    'Breathable mesh inner lining and stretch Kevlar accordion panels',
                ],
                'size_chart': size_chart,
                'category_slug': category['slug'],
                'subcategory_slug': group_slug,
            },
            {
                'slug': 'merchero-monaco-gold-custom-leather-racing-suit',
                'name': 'MERCHERO Monaco Gold Custom Leather Racing Suit',
                'image': '/static/images/racingsuit4-front.jpeg',
                'images': [
                    '/static/images/racingsuit4-front.jpeg',
                    '/static/images/racingsuit4-back.jpeg',
                ],
                'sku': 'MTRS-004',
                'short_desc': 'Bespoke Monaco Gold edition track suit combining luxury aesthetic with professional race tech.',
                'description': (
                    'Crafted for riders who demand luxury style alongside serious protection, the MERCHERO Monaco Gold Custom '
                    'Leather Racing Suit features custom gold highlights, titanium sliders, and premium leather contouring.'
                ),
                'features': [
                    'Exclusive Monaco Gold design and custom tailorable badging',
                    'Titanium external shoulder and elbow protection armor',
                    'High-density foam padding in hip and tailbone areas',
                ],
                'size_chart': size_chart,
                'category_slug': category['slug'],
                'subcategory_slug': group_slug,
            },
            {
                'slug': 'merchero-vortex-gold-motorbike-leather-suit',
                'name': 'MERCHERO Vortex Gold Motorbike Leather Suit',
                'image': '/static/images/racingsuit5-front.png',
                'images': [
                    '/static/images/racingsuit5-front.png',
                    '/static/images/racingsuit5-back.png',
                ],
                'sku': 'MTRS-005',
                'short_desc': 'Aerodynamic Vortex Gold track suit designed for stability and high-speed cornering.',
                'description': (
                    'Designed for high-speed aerodynamics and intense track sessions, the MERCHERO Vortex Gold Motorbike '
                    'Leather Suit utilizes ergonomic body mapping and heavy-duty stitching for maximum rider confidence.'
                ),
                'features': [
                    'Ergonomic stretch panels on groin, chest, and knees',
                    'Aerodynamic back hump for airflow stability',
                    'Heavy-duty YKK zippers and reinforced double-layer leather seating',
                ],
                'size_chart': size_chart,
                'category_slug': category['slug'],
                'subcategory_slug': group_slug,
            },
            {
                'slug': 'merchero-stealth-forest-leather-track-suit',
                'name': 'MERCHERO Stealth Forest Leather Track Suit',
                'image': '/static/images/racingsuit6-front.png',
                'images': [
                    '/static/images/racingsuit6-front.png',
                    '/static/images/racingsuit6-back.png',
                ],
                'sku': 'MTRS-006',
                'short_desc': 'Tactical Stealth Forest track suit offering refined dark aesthetic and race protection.',
                'description': (
                    'The MERCHERO Stealth Forest Leather Track Suit blends subtle dark green stealth styling with '
                    'uncompromising track safety specifications, offering superior flexibility and impact absorption.'
                ),
                'features': [
                    'Stealth forest matte finish with abrasion protection',
                    'Removable CE Level 2 back and joint protectors',
                    'Perforated chest panels for optimal airflow control',
                ],
                'size_chart': size_chart,
                'category_slug': category['slug'],
                'subcategory_slug': group_slug,
            },
        ]

    products = []
    for i in range(1, count + 1):
        slug = f'{group_slug}-{i:02d}'
        name = f'{group_name} \u2014 Sample {i}'
        products.append({
            'slug': slug,
            'name': name,
            'image': category['image'],
            'sku': f'MCH-{group_slug[:3].upper()}-{i:03d}',
            'short_desc': f'{group_name} sample entry from our {category["name"]} line.',
            'description': (
                f'Placeholder description for {name}. Replace with the real material breakdown, '
                f'construction details, and customization options once the product photos are ready.'
            ),
            'features': [
                'Genuine leather / performance-grade material construction',
                'Reinforced stitching for daily and heavy-duty use',
                'Available in custom colors, logos, and sizing for OEM orders',
            ],
            'size_chart': size_chart,
            'category_slug': category['slug'],
            'subcategory_slug': group_slug if group_slug != category['slug'] else None,
        })
    return products


# Attach `description` + `products` to every subcategory and to every
# subcategory-less ("leaf") category, then build lookup indexes.
_CATEGORY_MAP = {}
_SUBCATEGORY_MAP = {}
_PRODUCT_MAP = {}

for cat in CATEGORIES:
    _CATEGORY_MAP[cat['slug']] = cat
    if cat['subcategories']:
        for sub in cat['subcategories']:
            sub.setdefault(
                'description',
                'Explore our {name} collection \u2014 part of the {cat_name} range, {tagline}'.format(
                    name=sub['name'],
                    cat_name=cat['name'],
                    tagline=cat['tagline'][0].lower() + cat['tagline'][1:],
                )
            )
            sub.setdefault('image', cat['image'])
            sub['products'] = _build_products(sub['slug'], sub['name'], cat)
            _SUBCATEGORY_MAP[(cat['slug'], sub['slug'])] = sub
            for prod in sub['products']:
                _PRODUCT_MAP[prod['slug']] = prod
    else:
        # Leaf category: it plays the role of its own "subcategory" page.
        cat.setdefault('description', cat['tagline'])
        cat['products'] = _build_products(cat['slug'], cat['name'], cat)
        for prod in cat['products']:
            _PRODUCT_MAP[prod['slug']] = prod


def get_category(category_slug):
    """Get a main category by slug."""
    return _CATEGORY_MAP.get(category_slug)


def get_subcategory(category_slug, subcategory_slug):
    """Get a (category, subcategory) pair by slugs."""
    category = get_category(category_slug)
    if category is None:
        return None, None
    subcategory = _SUBCATEGORY_MAP.get((category_slug, subcategory_slug))
    return category, subcategory


def get_product(product_slug):
    """Get a single product by its slug."""
    return _PRODUCT_MAP.get(product_slug)


def get_related_products(product, limit=4):
    """Other products from the same subcategory/leaf category."""
    category = get_category(product['category_slug'])
    if category is None:
        return []
    if product.get('subcategory_slug'):
        _, group = get_subcategory(product['category_slug'], product['subcategory_slug'])
    else:
        group = category
    if group is None:
        return []
    return [p for p in group['products'] if p['slug'] != product['slug']][:limit]


def iter_all_products():
    """Iterate over every product in the catalog."""
    for cat in CATEGORIES:
        if cat['subcategories']:
            for sub in cat['subcategories']:
                for prod in sub['products']:
                    yield cat, sub, prod
        else:
            for prod in cat['products']:
                yield cat, None, prod
