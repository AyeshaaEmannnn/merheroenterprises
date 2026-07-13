from django.test import TestCase
from django.urls import reverse


class ProductsPageTests(TestCase):
    def test_products_list_page_renders(self):
        response = self.client.get(reverse('products_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'All Products')

    def test_product_detail_page_renders(self):
        response = self.client.get(reverse('product_detail', args=['motorcycle-racing-suit']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Apex-R Elite')
