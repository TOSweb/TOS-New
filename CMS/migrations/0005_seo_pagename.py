# Generated by Django 5.0.3 on 2024-03-21 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0004_rename_homepageseo_seo_homecarousel_alttext_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='seo',
            name='PageName',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]