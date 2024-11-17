from django.urls import path, re_path
from . import views

# urlpatterns = [
#     path('products/', views.ProductListView.as_view(), name='products-list'),
# ]


# Allow an optional id parameter, re_path is for greater flexibility

urlpatterns = [
    re_path(r'^products/(?P<id>\d+)?/?$', views.ProductsView.as_view(), name='products'),
]

