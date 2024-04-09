from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
    carousel = HomeCarousel.objects.all()
    seo = get_object_or_404(SEO, id=1)
    about = get_object_or_404(AboutPage, id=1)
    services = Service.objects.prefetch_related('subservice_set').all()  # Assuming a reverse relationship name 'subservice_set'
    
    
    context = {
        'carousel': carousel,
        'seo': seo,
        'about': about,
        'services': services,
        
    }
    return render(request, 'index.html', context)

def about(request):
    about = get_object_or_404(AboutPage, id=1)
    seo = get_object_or_404(SEO, id=1)
    context = {
        'about': about,
        'seo': seo,
    }
    return render(request, 'about.html', context)

def servicedetail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    subservices = service.subservice_set.all()
    case_studies = CaseStudies.objects.none()  # Start with an empty queryset # Empty queryset for case studies
    web_projects = WebProjects.objects.none()   # Empty queryset for web projects
    branding_projects = BrandingProjects.objects.none()
    # Check if the service is "Digital Marketing"
    case_studies = CaseStudies.objects.filter(Subservice__in=subservices).order_by('-id')[:3]
    web_projects = WebProjects.objects.filter(Subservice__in=subservices).order_by('-id')[:3]
    branding_projects = BrandingProjects.objects.filter(Subservice__in=subservices).order_by('-id')[:3]
    context = {
        'service': service,
        'subservices': subservices,
        'case_studies': case_studies,
        'web_projects': web_projects,
        'branding_projects': branding_projects,
    }
    return render(request, 'services.html', context)

def subservicedetail(request, service_slug, subservice_slug):
    subservice = get_object_or_404(Subservice, slug=subservice_slug)
    context = {
       'subservice': subservice,
    }
    return render(request,'subservice.html', context)