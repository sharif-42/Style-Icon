from django.urls import path
from product.rest_api import views


app_name = 'product'

urlpatterns = [
    path('', views.ProductListApiView.as_view(), name='products'),
    path('<uuid:uuid>/details/', views.ProductDetailsApiView.as_view(), name='product-details'),
]
