from django.http import Http404
from django.shortcuts import render

PRODUCTS = [
    {
        'slug': 'apex-r-elite',
        'name': 'Apex-R Elite',
        'category': 'Racing Suits',
        'label': 'Pro Edition',
        'image': '/static/images/racingsuit1-front.jpeg',
        'short_desc': 'One-piece leather racing suit with CE protection and premium finishing.',
        'description': 'Built for professional riders who want race-ready protection, a tailored fit, and premium leather craftsmanship.',
        'highlights': [
            'CE-level impact protection',
            'Premium cowhide and kangaroo panels',
            'Custom fit and branding options',
        ],
        'specs': ['Full-grain leather', 'Airbag compatible', 'OEM-ready finishing'],
        'gallery_images': ['/static/images/racingsuit1-front.jpeg', '/static/images/racingsuit1-back.jpeg'],
    },
    {
        'slug': 'pro-racer-x',
        'name': 'Pro-Racer X',
        'category': 'Racing Suits',
        'label': 'Competition Ready',
        'image': '/static/images/racingsuit2-front.jpeg',
        'short_desc': 'Advanced racing suit engineered for maximum performance and protection.',
        'description': 'Professional-grade racing suit with premium leather and advanced safety features.',
        'highlights': ['Advanced armor integration', 'Lightweight construction', 'Race-ready finish'],
        'specs': ['Premium leather', 'Reinforced panels', 'Pro finishing'],
        'gallery_images': ['/static/images/racingsuit2-front.jpeg', '/static/images/racingsuit2-back.jpeg'],
    },
    {
        'slug': 'elite-guard',
        'name': 'Elite Guard',
        'category': 'Racing Gloves',
        'label': 'Track Ready',
        'image': '/static/images/gloves.jpeg',
        'short_desc': 'Precision racing gloves designed for ultimate grip and protection on the track.',
        'description': 'High-performance gloves with reinforced knuckles and premium leather construction.',
        'highlights': ['Enhanced grip technology', 'Carbon knuckle protection', 'Track-tested design'],
        'specs': ['Kangaroo leather', 'Palm sliders', 'Custom branding'],
        'gallery_images': ['/static/images/gloves.jpeg'],
    },
    {
        'slug': 'apex-b-elite',
        'name': 'Apex-B Elite',
        'category': 'Bags',
        'label': 'Premium Storage',
        'image': '/static/images/bags.jpeg',
        'short_desc': 'Premium leather bag built for durability and style.',
        'description': 'A versatile bag perfect for riders and travelers seeking quality and functionality.',
        'highlights': ['Waxed leather', 'Durable hardware', 'Spacious compartments'],
        'specs': ['Premium construction', 'Weather resistant', 'Professional finish'],
        'gallery_images': ['/static/images/bags.jpeg'],
    },
    {
        'slug': 'sialkot-classic-rider-jacket',
        'name': 'Sialkot Classic Rider Jacket',
        'category': 'Garments',
        'label': 'Signature Series',
        'image': '/static/images/1.jpeg',
        'short_desc': 'A bold motorcycle garment designed for comfort, durability, and style.',
        'description': 'A versatile leather garment for everyday riders and premium club collections.',
        'highlights': ['Durable YKK zippers', 'Soft inner lining', 'Available in custom colors'],
        'specs': ['Cowhide leather', 'Weather-ready finish', 'Branded hardware'],
        'gallery_images': ['/static/images/hero-final.jpeg', '/static/images/leather.jpeg', '/static/images/garments-final.jpeg'],
    },
    {
        'slug': 'apex-g',
        'name': 'Apex-G',
        'category': 'Garments',
        'label': 'New Release',
        'image': '/static/images/garments-final.jpeg',
        'short_desc': 'Premium garment collection designed for riders who demand excellence.',
        'description': 'Crafted with premium leather and modern design principles for ultimate comfort and style.',
        'highlights': ['Premium materials', 'Modern design', 'Perfect fit'],
        'specs': ['High-quality leather', 'Expert craftsmanship', 'Rider-tested'],
        'gallery_images': ['/static/images/garments-final.jpeg'],
    },
    {
        'slug': 'custom-oem',
        'name': 'Brand-Ready Custom Program',
        'category': 'OEM Custom',
        'label': 'OEM Service',
        'image': '/static/images/labelsttitching.png',
        'short_desc': 'Turn your brand concept into a production-ready collection with our OEM team.',
        'description': 'From prototypes to bulk manufacturing, we support private label and custom gear projects for international brands.',
        'highlights': ['Logo placement and embroidery', 'Packaging and labeling', 'Bulk production support'],
        'specs': ['Private label ready', 'Sampling support', 'Export packaging'],
        'gallery_images': ['/static/images/readytobuildproductline.jpg', '/static/images/prototyping.jpg', '/static/images/manufacturing2.jpg'],
    },
]


def products_list(request):
    """Render the full products catalog."""
    return render(request, 'products/products.html', {'products': PRODUCTS})


def product_detail(request, slug):
    product = next((item for item in PRODUCTS if item['slug'] == slug), None)
    if product is None:
        raise Http404('Product not found.')
    return render(request, 'products/product_detail.html', {'product': product})


def motorcycle_racing_suit(request):
    return product_detail(request, 'motorcycle-racing-suit')
