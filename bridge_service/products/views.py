from django.shortcuts import render

# Create your views here.

import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class ProductListView(APIView):
    """
    A bridge between clients and the Fake Store API.
    Requires a valid token to fetch product data.
    """
    def get(self, request):
        # Extract token from the Authorization header
        token = request.headers.get('Authorization')

        if token != f"Bearer {settings.HARD_CODED_TOKEN}":
            return Response(
                {"error": "Forbidden: Invalid token."},
                status=status.HTTP_403_FORBIDDEN
            )

        # Fetch data from the Fake Store API
        url = "https://fakestoreapi.com/products"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise error for non-200 responses
            return Response(response.json(), status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            return Response(
                {"error": "Failed to fetch products", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


