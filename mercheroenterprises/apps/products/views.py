from urllib.parse import quote

from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse

from . import catalog

# Real inquiry channels used on the product detail page.
# Update these two values whenever the company's contact details change.
WHATSAPP_NUMBER = '447858811371'  # from templates/contact/inquiryform.html
INQUIRY_EMAIL = 'info@mercheroenterprises.com'


def _inquiry_links(product):
    """Build ready-to-click WhatsApp and email inquiry links for a product."""
    message = f"Hi, I'm interested in {product['name']} ({product['sku']}). Could you share more details?"
    whatsapp_link = f'https://wa.me/{WHATSAPP_NUMBER}?text={quote(message)}'
    email_link = f"mailto:{INQUIRY_EMAIL}?subject={quote('Inquiry: ' + product['name'])}&body={quote(message)}"
    return whatsapp_link, email_link


def products_list(request):
    """Overview page: shows all main categories (no dedicated page per category)."""
    return render(request, 'products/products.html', {
        'categories': catalog.CATEGORIES,
    })


def category_detail(request, category_slug):
    """A main category never has its own page.

    - If it has subcategories, forward straight to the first one.
    - If it doesn't (a "leaf" category), render it exactly like a
      subcategory page — hero, description, product grid.
    """
    category = catalog.get_category(category_slug)
    if category is None:
        raise Http404('Category not found.')

    if category['subcategories']:
        first_sub = category['subcategories'][0]
        return redirect(reverse('subcategory_detail', args=[category['slug'], first_sub['slug']]))

    return render(request, 'products/subcategory_page.html', {
        'category': category,
        'subcategory': None,
        'page_name': category['name'],
        'page_image': category['image'],
        'page_description': category['description'],
        'products': category['products'],
    })


def subcategory_detail(request, category_slug, subcategory_slug):
    category, subcategory = catalog.get_subcategory(category_slug, subcategory_slug)
    if category is None or subcategory is None:
        raise Http404('Subcategory not found.')

    return render(request, 'products/subcategory_page.html', {
        'category': category,
        'subcategory': subcategory,
        'page_name': subcategory['name'],
        'page_image': subcategory['image'],
        'page_description': subcategory['description'],
        'products': subcategory['products'],
    })


def product_detail(request, product_slug):
    product = catalog.get_product(product_slug)
    if product is None:
        raise Http404('Product not found.')

    category = catalog.get_category(product['category_slug'])
    subcategory = None
    if product.get('subcategory_slug'):
        _, subcategory = catalog.get_subcategory(product['category_slug'], product['subcategory_slug'])

    related_products = catalog.get_related_products(product)
    whatsapp_link, email_link = _inquiry_links(product)

    return render(request, 'products/product_detail.html', {
        'product': product,
        'category': category,
        'subcategory': subcategory,
        'related_products': related_products,
        'whatsapp_link': whatsapp_link,
        'email_link': email_link,
    })
