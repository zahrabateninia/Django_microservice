# **Django Products Microservice**

This is a simple Django-based microservice that fetches product data from an external API ([Fake Store API](https://fakestoreapi.com/docs)). The service is protected using a Bearer token-based authentication mechanism and provides endpoints to fetch all products or a specific product by ID.

---

## **Features**
- Fetch all products or specific product details by ID.
- External API integration with `requests`.
- Secure access via Bearer token authentication.
- Well-structured unit tests for endpoints.
- API documentation using `drf_yasg`.

---

## **Endpoints**

| Endpoint                      | Method | Description                               | Example                                                                 |
|-------------------------------|--------|-------------------------------------------|-------------------------------------------------------------------------|
| `/api/products/`              | `GET`  | Fetch all products                       | `curl -H "Authorization: Bearer <token>" http://127.0.0.1:8000/api/products/` |
| `/api/products/{id}/`         | `GET`  | Fetch a product by its ID                | `curl -H "Authorization: Bearer <token>" http://127.0.0.1:8000/api/products/1` |

---

## **Tech Stack**
### **Backend**
- Python
- Django
- Django Rest Framework (DRF)

### **Testing**
- `unittest` (via `django.test.TestCase`)
- `unittest.mock.patch` for mocking external API calls.

---

## **Testing the Microservice**

To run unit tests:
```bash
python manage.py test products
```


## Dependencies
- Django: Python web framework.
- djangorestframework: For building RESTful APIs.
- drf_yasg: For generating Swagger and ReDoc API documentation.
- requests: For making HTTP requests to external APIs.
