from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.Home.as_view(), name='index'),
    path('eng', views.HomeEng.as_view(), name='eng')]