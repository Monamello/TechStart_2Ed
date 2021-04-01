from django.test import TestCase
from rest_framework.test import APITestCase

class MarketplaceTests(APITestCase):

    def test_create_marketplace(self):
        response = self.client.post('/marketplaces/',
        {
            "name": "Marketplace name",
            "description": "Marketplace description",
            "site": "marketplace.com",
            "telephone": 4899587122,
            "email": "marketplace@gmail.com",
            "support_contact": "marketplace_contac@gmail.com"
        })
        self.assertEqual(response.status_code, 201)

    def test_update_marketplace(self):
        self.client.post('/marketplaces/',
        {
            "name": "Marketplace name",
            "description": "Marketplace description",
            "site": "marketplace.com",
            "telephone": 4899587122,
            "email": "marketplace@gmail.com",
            "support_contact": "marketplace_contac@gmail.com"
        })
        response = self.client.put('/marketplaces/1/',
        {
            "name": "New marketplace name",
            "description": "Marketplace description",
            "site": "marketplace.com",
            "telephone": 4899587122,
            "email": "marketplace@gmail.com",
            "support_contact": "marketplace_contac@gmail.com"
        })
        self.assertEqual(response.status_code, 200)

    def test_list_all_marketplaces(self):
        self.client.post('/marketplaces/',
         {
            "name": "Marketplace name",
            "description": "Marketplace description",
            "site": "marketplace.com",
            "telephone": 4899587122,
            "email": "marketplace@gmail.com",
            "support_contact": "marketplace_contac@gmail.com"
        })
        response = self.client.get('/marketplaces/')
        self.assertEqual(response.status_code, 200)

    def test_delete_marketplace(self):
        self.client.post('/marketplaces/',
        {
            "name": "Marketplace name",
            "description": "Marketplace description",
            "site": "marketplace.com",
            "telephone": 4899587122,
            "email": "marketplace@gmail.com",
            "support_contact": "marketplace_contac@gmail.com"
        })
        response = self.client.delete('/marketplaces/1/')
        self.assertEqual(response.status_code, 204)