from django.urls import path
from . import views

urlpatterns = [
    path('', views.images),
    path('get_texts/', views.get_texts)
]