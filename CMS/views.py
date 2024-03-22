from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    carousel = HomeCarousel.objects.all()
    seo = SEO.objects.get or 404([1])
    about = AboutPage.objects.get or 404([1])
    context = {
        'carousel': carousel,
        'seo': seo,
        'about': about,
    }
    return render(request, 'index.html', context)

def about(request):

    return render(request, 'about.html')