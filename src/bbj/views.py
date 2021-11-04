from django.shortcuts import render
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = 'bbj/index.html'
class HomeEng(TemplateView):
    template_name = 'bbj/index-eng.html'
