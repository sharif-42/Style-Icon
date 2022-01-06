from django.urls import path

from search.rest_api import views

urlpatterns = [
     path('products/', views.ProductSearchAPIView.as_view(), name='product-search'),
]