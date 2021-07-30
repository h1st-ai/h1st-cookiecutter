from django.urls import path
from h1st_api import views

urlpatterns = [
    path('foo', views.default),
    path('translate', views.translate),
]