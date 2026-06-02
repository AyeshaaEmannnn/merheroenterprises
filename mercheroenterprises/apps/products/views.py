from django.shortcuts import render


def products_list(request):
    """Category page: Motorcycle Racing Suits."""
    products = [
        {
            'slug': 'motorcycle-racing-suit',
            'name': 'Apex-R Elite',
            'label': 'Pro Edition',
            'image': '/static/images/racing-suit.jpeg',
        },
        {
            'slug': 'motorcycle-racing-suit',
            'name': 'Apex-R Pro',
            'label': 'Track Suit',
            'image': '/static/images/racing-suit1.jpeg',
        },
        {
            'slug': 'motorcycle-racing-suit',
            'name': 'Storm GT-R',
            'label': 'Race Spec',
            'image': '/static/images/suit.png',
        },
        {
            'slug': 'motorcycle-racing-suit',
            'name': 'Venom X1',
            'label': 'Airbag Ready',
            'image': '/static/images/racing-suit.jpeg',
        },
        {
            'slug': 'motorcycle-racing-suit',
            'name': 'Thunder RR',
            'label': 'Club Edition',
            'image': '/static/images/racing-suit1.jpeg',
        },
        {
            'slug': 'motorcycle-racing-suit',
            'name': 'Cobra K1',
            'label': 'Kangaroo Leather',
            'image': '/static/images/suit.png',
        },
        {
            'slug': 'motorcycle-racing-suit',
            'name': 'Phantom RS',
            'label': 'OEM Custom',
            'image': '/static/images/racing-suit.jpeg',
        },
        {
            'slug': 'motorcycle-racing-suit',
            'name': 'Blade MK-II',
            'label': 'Entry Pro',
            'image': '/static/images/racing-suit1.jpeg',
        },
    ]
    return render(request, 'products/products_list.html', {'products': products})


def motorcycle_racing_suit(request):
    return render(request, 'products/motorcycle_racing_suit.html')
