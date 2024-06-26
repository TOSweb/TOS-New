# Generated by Django 5.0.3 on 2024-03-19 14:51

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Aboutpage_heading', models.CharField(max_length=300)),
                ('Aboutshort', models.TextField()),
                ('Who_are_we', models.TextField()),
                ('Mission_Vision', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text')),
            ],
        ),
        migrations.CreateModel(
            name='HomeCarousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Heading', models.CharField(max_length=300)),
                ('Paragraph', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HomePageSEO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title_of_page', models.CharField(blank=True, max_length=300, null=True)),
                ('Meta_description', models.TextField(blank=True, null=True)),
                ('Meta_keyword', models.TextField(blank=True, null=True)),
                ('Schema', models.JSONField(blank=True, null=True)),
            ],
        ),
    ]
