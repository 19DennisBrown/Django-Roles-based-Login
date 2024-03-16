from django.urls import path
from . import views


urlpatterns = [
  path('', views.admin_view, name='admin'),
  path('user/', views.user_view, name='user'),
]