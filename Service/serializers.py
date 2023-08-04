from rest_framework import serializers
from .models import (LastWorks,
                     Package,
                     PackageProperty,
                     ServiceCategory,
                     ServiceProperty,
                     Services,
                     ServicesPropertyDetails)


class PackagePropertySeriazlier(serializers.ModelSerializer):
    class Meta:
        model = PackageProperty
        fields = ['id', 'property_name', 'icon', 'package', 'created_at', 'updated_at']


class PackageREADSerializer(serializers.ModelSerializer):
    services_cat_packages = PackagePropertySeriazlier(many=True, read_only=True, source='services_category_packages')

    class Meta:
        model = Package
        fields = ['id', 'package_name', 'price_period', 'price', 'services_category', 'services_cat_packages', 'created_at', 'updated_at']


class PackageCREATESerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['id', 'package_name', 'price_period', 'price', 'services_category', 'created_at', 'updated_at']


class LastWorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = LastWorks
        fields = ['id', 'company_name', 'photo', 'services_category', 'created_at', 'updated_at']


class ServiceCategoryREADSerializer(serializers.ModelSerializer):
    l_work = LastWorksSerializer(many=True, read_only=True, source='services_category_last_works')
    packages = PackageREADSerializer(many=True, read_only=True, source='services_category_packages')

    class Meta:
        model = ServiceCategory
        fields = ['id', 'name', 'icon', 'services', 'l_work', 'packages', 'created_at', 'updated_at']


class ServiceCategoryCREATESerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ['id', 'name', 'icon', 'services', 'created_at', 'updated_at']


class ServicesPropertyDetailsSeriazlier(serializers.ModelSerializer):
    class Meta:
        model = ServicesPropertyDetails
        fields = ['id', 'title', 'content', 'services_property', 'created_at', 'updated_at']


class ServicePropertyREADSerializer(serializers.ModelSerializer):
    serv_pro_details = ServicesPropertyDetailsSeriazlier(many=True, read_only=True, source='services_property_details')

    class Meta:
        model = ServiceProperty
        fields = ['id', 'up_title', 'down_title', 'description', 'photo', 'services', 'serv_pro_details', 'created_at', 'updated_at']


class ServicePropertyCREATESerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProperty
        fields = ['id', 'up_title', 'down_title', 'description', 'photo', 'services', 'created_at', 'updated_at']


class ServiceREADSerializer(serializers.ModelSerializer):
    serv_property = ServicePropertyREADSerializer(many=True, read_only=True, source='services_property')
    serv_category = ServiceCategoryREADSerializer(many=True, read_only=True, source='services_category')

    class Meta:
        model = Services
        fields = ['id', 'title', 'slug', 'logo', 'photo', 'content', 'serv_property', 'serv_category', 'created_at', 'updated_at']


class ServiceCREATESerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['id', 'title', 'slug', 'logo', 'photo', 'content', 'created_at', 'updated_at']
