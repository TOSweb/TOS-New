from django.db import models
from django_ckeditor_5.widgets import CKEditor5Widget
from django_ckeditor_5.fields import CKEditor5Field
from PIL import Image
from stdimage import StdImageField
# Create your models here.

class HomeCarousel(models.Model):
    Heading = models.CharField(max_length=300)
    Paragraph = CKEditor5Field('Text', config_name='extends')
    image1x = models.ImageField(upload_to='images1x/')
    image2x = models.ImageField(upload_to='images2x/')
    image3x = models.ImageField(upload_to='images3x/')
    alttext = models.CharField(max_length=300)

    def __str__(self):
        return self.Heading


class SEO(models.Model):
    PageName = models.CharField(max_length=300)
    Title_of_page = models.CharField(max_length=300, null=True, blank=True)
    Meta_description = models.TextField(null=True, blank=True)
    Meta_keyword = models.TextField(null=True, blank=True)
    Schema = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.PageName

class AboutPage(models.Model):
    Aboutpage_heading = models.CharField(max_length=300)
    Aboutshort = models.TextField()
    Who_are_we = CKEditor5Field('Who_are_we', config_name='extends')
    Mission = CKEditor5Field('Mission', config_name='extends')
    Vision = CKEditor5Field('Vision', config_name='extends')
    slug = models.SlugField(unique=True, default="slug")
    
    def __str__(self):
        return self.Aboutpage_heading
    
    
class Service(models.Model):
    Title_of_page = models.CharField(max_length=300, null=True, blank=True)
    Meta_description = models.TextField(null=True, blank=True)
    Meta_keyword = models.TextField(null=True, blank=True)
    Schema = models.JSONField(null=True, blank=True)
    Service = models.CharField(max_length=300)
    image1x = models.ImageField(upload_to='images1x/')
    image2x = models.ImageField(upload_to='images2x/')
    image3x = models.ImageField(upload_to='images3x/')
    service_short = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.Title_of_page

class Subservice(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    Title_of_page = models.CharField(max_length=300, null=True, blank=True)
    Meta_description = models.TextField(null=True, blank=True)
    Meta_keyword = models.TextField(null=True, blank=True)
    Schema = models.JSONField(null=True, blank=True)
    Service = models.CharField(max_length=300)
    service_short = models.TextField()
    image1x = models.ImageField(upload_to='images1x/')
    image2x = models.ImageField(upload_to='images2x/')
    image3x = models.ImageField(upload_to='images3x/')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.Title_of_page

class SubSubService(models.Model):
    subservice = models.ForeignKey(Subservice, on_delete=models.CASCADE)
    Title_of_page = models.CharField(max_length=300, null=True, blank=True)
    Meta_description = models.TextField(null=True, blank=True)
    Meta_keyword = models.TextField(null=True, blank=True)
    Schema = models.JSONField(null=True, blank=True)
    Service = models.CharField(max_length=300)
    service_short = models.TextField()
    image1x = models.ImageField(upload_to='images1x/')
    image2x = models.ImageField(upload_to='images2x/')
    image3x = models.ImageField(upload_to='images3x/')
    alt_text = models.CharField(max_length=500)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.Title_of_page
    
class Projects(models.Model):
    Title_of_page = models.CharField(max_length=300, null=True, blank=True)
    Meta_description = models.TextField(null=True, blank=True)
    Meta_keyword = models.TextField(null=True, blank=True)
    Schema = models.JSONField(null=True, blank=True)
    Project = models.CharField(max_length=300)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    image1x = models.ImageField(upload_to='images1x/')
    image2x = models.ImageField(upload_to='images2x/')
    image3x = models.ImageField(upload_to='images3x/')
    alt_text = models.CharField(max_length=500)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.Project
    
class CreativeCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Creatives(models.Model):
    category = models.ForeignKey(CreativeCategory, on_delete=models.CASCADE)
    creatives1x = models.ImageField(upload_to='images1x/')
    creatives2x = models.ImageField(upload_to='images2x/', null=True, blank=True)
    creatives3x = models.ImageField(upload_to='images3x/', null=True, blank=True)
    alt_text = models.CharField(max_length=500)

    def __str__(self):
        return self.alt_text
    