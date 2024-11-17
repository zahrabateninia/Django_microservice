from django.shortcuts import render
import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# class ProductListView(APIView):
#     """
#     A bridge between clients and the Fake Store API.
#     Requires a valid token to fetch product data.
#     """
#     def get(self, request):
#         # Extract token from the Authorization header
#         token = request.headers.get('Authorization')

#         if token != f"Bearer {settings.HARD_CODED_TOKEN}":
#             return Response(
#                 {"error": "Forbidden: Invalid token."},
#                 status=status.HTTP_403_FORBIDDEN
#             )

#         # Fetch data from the Fake Store API
#         url = "https://fakestoreapi.com/products"
#         try:
#             response = requests.get(url)
#             response.raise_for_status()  # Raise error for non-200 responses
#             return Response(response.json(), status=status.HTTP_200_OK)
#         except requests.exceptions.RequestException as e:
#             return Response(
#                 {"error": "Failed to fetch products", "details": str(e)},
#                 status=status.HTTP_500_INTERNAL_SERVER_ERROR
#             )


from rest_framework.exceptions import PermissionDenied


class ProductsView(APIView):
    def get(self, request, id=None):
        # Custom token validation
        valid_token = "it-is-secure-token"
        auth_token = request.headers.get('Authorization', '').replace('Bearer ', '')

        if auth_token != valid_token:
            raise PermissionDenied({"error": "Forbidden: Invalid token."})

        if id is None:
            # Fetch all products
            response = requests.get("https://fakestoreapi.com/products")
            return Response(response.json())
        else:
            # Fetch product by ID
            response = requests.get(f"https://fakestoreapi.com/products/{id}")
            if response.status_code == 404:
                return Response({"error": "Product not found."}, status=404)
            return Response(response.json())
