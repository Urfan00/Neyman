from django.contrib import admin
from .models import LastWorks, Package, PackageProperty, ServiceCategory, ServiceProperty, Services, ServicesPropertyDetails



class ServicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'logo', 'photo', 'content', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'slug']


class ServicePropertyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'photo', 'services', 'created_at', 'updated_at']
    list_display_links = ['id','title']
    search_fields = ['title', 'services__title', 'services__slug']


class ServicesPropertyDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'services_property', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'services_property__up_title', 'services_property__down_title']


class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'icon', 'services', 'created_at', 'updated_at']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'services__title']


class LastWorksAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'photo', 'services_category', 'created_at', 'updated_at']
    list_display_links = ['id', 'company_name']
    search_fields = ['company_name', 'services_category__name']


class PackageAdmin(admin.ModelAdmin):
    list_display = ['id', 'package_name', 'price_period', 'price', 'services_category', 'created_at', 'updated_at']
    list_display_links = ['id', 'package_name']
    search_fields = ['package_name', 'services_category__name']


class PackagePropertyAdmin(admin.ModelAdmin):
    list_display = ['id', 'property_name', 'icon', 'package', 'created_at', 'updated_at']
    list_display_links = ['id', 'property_name']
    search_fields = ['property_name', 'package__package_name']



admin.site.register(Services, ServicesAdmin)
admin.site.register(ServiceProperty, ServicePropertyAdmin)
admin.site.register(ServicesPropertyDetails, ServicesPropertyDetailsAdmin)
admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(LastWorks, LastWorksAdmin)
admin.site.register(Package, PackageAdmin)
admin.site.register(PackageProperty, PackagePropertyAdmin)
