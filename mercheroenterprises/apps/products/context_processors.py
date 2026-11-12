# Context processors for products app
from . import catalog


def product_navigation(request):
    """Provide product navigation data to all templates."""
    return {
        'product_navigation_categories': catalog.CATEGORIES,
    }

