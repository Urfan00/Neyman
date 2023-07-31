from django.db import models


class DateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SosialMedia(models.Model):
    github = models.URLField(max_length=200, null=True, blank=True)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    linkedln = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    tweeter = models.URLField(max_length=200, null=True, blank=True)
    # threads= models.URLField(max_length=200, null=True, blank=True)
    # = models.URLField(max_length=200, null=True, blank=True)
    # = models.URLField(max_length=200, null=True, blank=True)
    # = models.URLField(max_length=200, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

