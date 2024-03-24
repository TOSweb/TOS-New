from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
    carousel = HomeCarousel.objects.all()
    seo = get_object_or_404(SEO, id=1)
    about = get_object_or_404(AboutPage, id=1)
    services = Service.objects.all()
    creatives = Creatives.objects.all()[:5]

    context = {
        'carousel': carousel,
        'seo': seo,
        'about': about,
        'services': services,
        'creatives': creatives,
    }
    return render(request, 'index.html', context)

def about(request):

    return render(request, 'about.html')