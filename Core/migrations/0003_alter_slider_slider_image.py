# Generated by Django 4.2.3 on 2023-07-31 11:51

from django.db import migrations, models
import services.uploader


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_remove_ourteam_threads'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='slider_image',
            field=models.ImageField(upload_to=services.uploader.Uploader.slider_image),
        ),
    ]
