from django.db import models
from services.mixins import DateMixin
from services.uploader import Uploader
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify



class BlogCategory(DateMixin):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Blog Category'
        verbose_name_plural = 'Blog Category'


class Tag(DateMixin):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Blog(DateMixin):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to=Uploader.blog_image)
    slug = models.SlugField(null=True, blank=True)
    short_descriptions = RichTextField()
    long_descriptions = RichTextField()
    blog_category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='blog_category')
    tag = models.ManyToManyField(Tag, related_name='blog_tag')
    date = models.DateField(null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'
