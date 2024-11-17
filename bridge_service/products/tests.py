from django.test import TestCase
from rest_framework.test import APIClient  
from unittest.mock import patch   # pip install requests-mock
import requests
from rest_framework.test import APITestCase
from rest_framework import status

class ProductsViewTests(APITestCase):

    @patch('requests.get')
    def test_fetch_all_products(self, mock_get):
        # Mock the response from the external API
        mock_get.return_value.json.return_value = [
            {"id": 1, "name": "Product 1", "price": 20.0},
            {"id": 2, "name": "Product 2", "price": 30.0}
        ]

        # Add the authorization token in the headers
        headers = {
            "Authorization": "Bearer it-is-secure-token"
        }

        # Make the GET request to the endpoint
        response = self.client.get('/api/products/', headers=headers)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Optionally, check the data returned in the response
        self.assertEqual(len(response.json()), 2)  # Assuming there are two products in the mock data
