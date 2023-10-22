from django.db import models
from services.mixins import DateMixin
from services.uploader import Uploader
from django.template.defaultfilters import slugify


class Services(DateMixin):
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)
    logo = models.CharField(max_length=255)
    photo = models.ImageField(upload_to=Uploader.services_photo)
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class ServiceProperty(DateMixin):
    # up_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to=Uploader.services_property_photo)
    services = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='services_property')

    def __str__(self):
        return f"{self.services.title}'s property"

    class Meta:
        verbose_name = 'Service Property'
        verbose_name_plural = 'Service Property'


class ServicesPropertyDetails(DateMixin):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    services_property = models.ForeignKey(ServiceProperty, on_delete=models.CASCADE, related_name='services_property_details')

    def __str__(self):
        return f"{self.services_property.services.title}' property details {self.title}"

    class Meta:
        verbose_name = 'Services Property Details'
        verbose_name_plural = 'Services Property Details'


class ServiceCategory(DateMixin):
    name = models.CharField(max_length=255)
    # icon = models.ImageField(upload_to=Uploader.services_category_icon)
    icon = models.CharField(max_length=255)
    services = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='services_category')

    def __str__(self):
        return f"{self.services.title}'s {self.name} category"

    class Meta:
        verbose_name = 'Services Category'
        verbose_name_plural = 'Services Category'


class LastWorks(DateMixin):
    company_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to=Uploader.services_category_last_works)
    services_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='services_category_last_works')

    def __str__(self):
        return f"{self.services_category.services.title}'s {self.services_category.name} category {self.company_name}'s last work"

    class Meta:
        verbose_name = 'Last Work'
        verbose_name_plural = 'Last Work'


class Package(DateMixin):
    package_name = models.CharField(max_length=255)
    price_period = models.CharField(max_length=50)
    price = models.FloatField()
    services_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='services_category_packages')

    def __str__(self):
        return f"{self.services_category.services.title}'s {self.services_category.name} category {self.package_name}'s package name"


    class Meta:
        verbose_name = 'Package'
        verbose_name_plural = 'Package'


class PackageProperty(DateMixin):
    property_name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to=Uploader.services_package_icon)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='package_property')

    def __str__(self):
        return f"{self.package.package_name}'s {self.property_name} property"

    class Meta:
        verbose_name = 'Package Property'
        verbose_name_plural = 'Package Property'
