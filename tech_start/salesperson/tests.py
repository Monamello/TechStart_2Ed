from django.test import TestCase
from .models import SalesPerson, Address
from rest_framework.test import APITestCase

class SalesPersonTests(APITestCase):

    def test_create_salesperson(self):
        response = self.client.post('/salesperson/',
            {
                "name": "SalesPerson name",
                "company_name": "Company name",
                "cnpj": 90180605000102,
                "email": "salesperson@gmail.com",
                "telephone": 4832659785,
                "address": {
                    "street": "SalesPerson street",
                    "number": 33,
                    "neighborhood": "SalesPerson Neighborhood",
                    "complement_address": "SalesPerson complement"
                }
            }, format="json")
        self.assertEqual(response.status_code, 201)


    def test_update_salesperson(self):
        self.client.post('/salesperson/',
            {
                "name": "SalesPerson name",
                "company_name": "Company name",
                "cnpj": 90180605000102,
                "email": "salesperson@gmail.com",
                "telephone": 4832659785,
                "address": {
                    "street": "SalesPerson street",
                    "number": 33,
                    "neighborhood": "SalesPerson Neighborhood",
                    "complement_address": "SalesPerson complement"
                }
            }, format="json")
        response = self.client.put('/salesperson/1/',
            {
                "name": "SalesPerson name",
                "company_name": "Company name",
                "cnpj": 90180605000102,
                "email": "salesperson@gmail.com",
                "telephone": 4832659785,
                "address": {
                    "street": "SalesPerson street",
                    "number": 33,
                    "neighborhood": "SalesPerson Neighborhood",
                    "complement_address": "SalesPerson complement"
                }
            }, format="json")
        self.assertEqual(response.status_code, 200)

    def test_list_all_salesperson(self):
        self.client.post('/salesperson/',
            {
                "name": "SalesPerson name",
                "company_name": "Company name",
                "cnpj": 90180605000102,
                "email": "salesperson@gmail.com",
                "telephone": 4832659785,
                "address": {
                    "street": "SalesPerson street",
                    "number": 33,
                    "neighborhood": "SalesPerson Neighborhood",
                    "complement_address": "SalesPerson complement"
                }
            }, format="json")
        response = self.client.get('/salesperson/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_delete_salesperson(self):
        self.client.post('/salesperson/',
            {
                "name": "SalesPerson name",
                "company_name": "Company name",
                "cnpj": 90180605000102,
                "email": "salesperson@gmail.com",
                "telephone": 4832659785,
                "address": {
                    "street": "SalesPerson street",
                    "number": 33,
                    "neighborhood": "SalesPerson Neighborhood",
                    "complement_address": "SalesPerson complement"
                }
            }, format="json")
        response = self.client.delete('/salesperson/1/')
        self.assertEqual(response.status_code, 204)
