from django.views.generic import TemplateView
from info.models import *
from django.shortcuts import render





def home(request):
    about = About.objects.all()
    quote = Quote.objects.all()
    context = {'about': about ,'quote':quote}
    template = 'portfolio/index.html'
    return render(request, template, context)
