from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.HomeEng.as_view(), name='index'),
    path('rus', views.HomeRus.as_view(), name='rus')]