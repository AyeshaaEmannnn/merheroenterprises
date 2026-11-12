from django.test import TestCase
from django.urls import reverse

from . import catalog


class ProductsPageTests(TestCase):
    def test_products_list_page_renders(self):
        response = self.client.get(reverse('products_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Leather Apparel')

    def test_category_with_subcategories_redirects_to_first_subcategory(self):
        response = self.client.get(reverse('category_detail', args=['leather-apparel']))
        self.assertEqual(response.status_code, 302)
        self.assertIn('leather-jackets', response.url)

    def test_category_with_subcategories_redirects_to_first_subcategory(self):
        response = self.client.get(reverse('category_detail', args=['leather-gloves']))
        self.assertEqual(response.status_code, 302)
        self.assertIn('motorcycle-riding-leather-gloves', response.url)

    def test_leaf_category_renders_products_directly(self):
        response = self.client.get(reverse('category_detail', args=['custom-leather-manufacturing']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Custom Leather Manufacturing')

    def test_subcategory_page_renders(self):
        response = self.client.get(reverse('subcategory_detail', args=['leather-apparel', 'leather-jackets']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Leather Jackets')

    def test_leather_gloves_subcategory_page_renders(self):
        response = self.client.get(reverse('subcategory_detail', args=['leather-gloves', 'motorcycle-riding-leather-gloves']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Motorcycle Riding Gloves')

    def test_product_detail_page_renders(self):
        _, _, product = next(catalog.iter_all_products())
        response = self.client.get(reverse('product_detail', args=[product['slug']]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, product['name'])

    def test_invalid_category_404s(self):
        response = self.client.get(reverse('category_detail', args=['not-a-real-category']))
        self.assertEqual(response.status_code, 404)

    def test_motorcycle_track_racing_suits_products(self):
        cat, sub = catalog.get_subcategory('motorcycle-track-racing-gear', 'motorcycle-track-racing-suits')
        self.assertIsNotNone(sub)
        self.assertEqual(len(sub['products']), 6)
        for prod in sub['products']:
            response = self.client.get(reverse('product_detail', args=[prod['slug']]))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, prod['name'])
            self.assertEqual(len(prod['images']), 2)

