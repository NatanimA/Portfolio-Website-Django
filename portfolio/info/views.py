from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,DetailView)
from .models import *
from django.shortcuts import get_object_or_404
from django.shortcuts import render
# Create your views here.
def about(request):
    about=About.objects.all()
    context= {'about' :about}
    template='portfolio/index.html'
    return render(request,template,context)


class QuoteList(ListView):
    model =Quote

class WorkList(ListView):
    model = Work

class TestimonyList(ListView):
    model = Testimonies

class TechnologyList(ListView):
    model = Technologies
