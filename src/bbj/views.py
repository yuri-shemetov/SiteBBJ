from django.shortcuts import render
from django.views.generic import TemplateView

class HomeEng(TemplateView):
    template_name = 'bbj/index-eng.html'
class HomeRus(TemplateView):
    template_name = 'bbj/index-rus.html'
