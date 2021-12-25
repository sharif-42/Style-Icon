from django.urls import path
from user.rest_api import views

app_name = 'user'

urlpatterns = [
    path('', views.UserListCreateAPIView.as_view(), name='user-list-create'),
]
