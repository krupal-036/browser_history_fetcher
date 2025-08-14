from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('api/history/', views.api_history, name='api_history'),
]
