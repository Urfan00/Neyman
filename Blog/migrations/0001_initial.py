# Generated by Django 4.2.3 on 2023-10-28 08:46

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import services.uploader


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Blog Category',
                'verbose_name_plural': 'Blog Category',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to=services.uploader.Uploader.blog_image)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('short_descriptions', ckeditor.fields.RichTextField()),
                ('long_descriptions', ckeditor.fields.RichTextField()),
                ('date', models.DateField(null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('blog_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_category', to='Blog.blogcategory')),
                ('tag', models.ManyToManyField(related_name='blog_tag', to='Blog.tag')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blog',
            },
        ),
    ]