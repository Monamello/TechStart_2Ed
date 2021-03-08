from django.test import TestCase
from .models import Product, Category
from rest_framework.test import APITestCase

class CategoryTests(APITestCase):

    def test_create_category(self):
        response = self.client.post('/categories/', {'name':'Category name', 'description':'Description to category'})
        self.assertEqual(response.status_code, 201)

    def test_update_category(self):
        self.client.post('/categories/', {'name':'Category name', 'description':'Description to category'})
        response = self.client.put('/categories/1/', {'name':'New category name', 'description':'Description to category'})
        self.assertEqual(response.status_code, 200)

    def test_list_all_categories(self):
        self.client.post('/categories/', {'name':'Category name', 'description':'Description to category'})
        response = self.client.get('/categories/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)


class ProductTests(APITestCase):

    def test_create_product(self):
        self.client.post('/categories/', {'name':'Category name', 'description':'Description to category'})
        response = self.client.post('/products/', {
            "name": "Product name",
            "description": "Description to product",
            "price": 120.00,
            "categories": [1]
            })
        self.assertEqual(response.status_code, 201)


    def test_update_product(self):
        self.client.post('/categories/', {'name':'Category name', 'description':'Description to category'})
        self.client.post('/products/', {
            "name": "Product name",
            "description": "Description to product",
            "price": 120.00,
            "categories": [1]
            })
        response = self.client.put('/products/1/', {
            "name": "New product name",
            "description": "Description to product",
            "price": 120.00,
            "categories": [1]
            })
        self.assertEqual(response.status_code, 200)

    def test_list_all_product(self):
        self.client.post('/categories/', {'name':'Category name', 'description':'Description to category'})
        self.client.post('/products/', {
            "name": "Product name",
            "description": "Description to product",
            "price": 120.00,
            "categories": [1]
            })
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)


    def test_list_by_name_product(self):
        self.client.post('/categories/', {'name':'Category name', 'description':'Description to category'})
        self.client.post('/products/', {
            "name": "Product name",
            "description": "Description to product",
            "price": 120.00,
            "categories": [1]
            })
        response = self.client.get('/products/?name=Product name/')
        self.assertEqual(response.status_code, 200)


    def test_list_by_all_params_product(self):
        self.client.post('/categories/', {'name':'Category name', 'description':'Description to category'})
        self.client.post('/products/', {
            "name": "Product name",
            "description": "Description to product",
            "price": 120.00,
            "categories": [1]
            })
        response = self.client.get('/products/?name=Product name&description=Description to product&price=120.00&categories=1')
        self.assertEqual(response.status_code, 200)

    def test_delete_product(self):
        self.client.post('/categories/', {'name':'Category name', 'description':'Description to category'})
        self.client.post('/products/',
        {
            "name": "Product name",
            "description": "Description to product",
            "price": 120.00,
            "categories": [1]
        })
        response = self.client.delete('/products/1/')
        self.assertEqual(response.status_code, 204)

