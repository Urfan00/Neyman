from rest_framework import serializers
from .models import (LastWorks,
                     Package,
                     PackageProperty,
                     ServiceCategory,
                     ServiceProperty,
                     Services,
                     ServicesPropertyDetails)



class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['id', 'title', 'slug', 'logo', 'photo', 'content', 'created_at', 'updated_at']


class ServicePropertyREADSerializer(serializers.ModelSerializer):
    services = ServiceSerializer()

    class Meta:
        model = ServiceProperty
        fields = ['id', 'title','description', 'photo', 'services', 'created_at', 'updated_at']


class ServicePropertyCREATESerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProperty
        fields = ['id', 'title','description', 'photo', 'services', 'created_at', 'updated_at']


class ServicesPropertyDetailsREADSeriazlier(serializers.ModelSerializer):
    services_property = ServicePropertyCREATESerializer()

    class Meta:
        model = ServicesPropertyDetails
        fields = ['id', 'title', 'content', 'services_property', 'created_at', 'updated_at']


class ServicesPropertyDetailsCREATESeriazlier(serializers.ModelSerializer):
    class Meta:
        model = ServicesPropertyDetails
        fields = ['id', 'title', 'content', 'services_property', 'created_at', 'updated_at']


class ServiceCategoryREADSerializer(serializers.ModelSerializer):
    services = ServiceSerializer()

    class Meta:
        model = ServiceCategory
        fields = ['id', 'name', 'icon', 'services', 'created_at', 'updated_at']


class ServiceCategoryCREATESerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ['id', 'name', 'icon', 'services', 'created_at', 'updated_at']


class LastWorksREADSerializer(serializers.ModelSerializer):
    services_category = ServiceCategoryCREATESerializer()

    class Meta:
        model = LastWorks
        fields = ['id', 'company_name', 'photo', 'services_category', 'created_at', 'updated_at']


class LastWorksCREATESerializer(serializers.ModelSerializer):
    class Meta:
        model = LastWorks
        fields = ['id', 'company_name', 'photo', 'services_category', 'created_at', 'updated_at']


class PackageREADSerializer(serializers.ModelSerializer):
    services_category = ServiceCategoryCREATESerializer()

    class Meta:
        model = Package
        fields = ['id', 'package_name', 'price_period', 'price', 'symbol', 'color', 'services_category', 'created_at', 'updated_at']


class PackageCREATESerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['id', 'package_name', 'price_period', 'price', 'symbol', 'color', 'services_category', 'created_at', 'updated_at']


class PackagePropertyREADSeriazlier(serializers.ModelSerializer):
    package = PackageCREATESerializer()

    class Meta:
        model = PackageProperty
        fields = ['id', 'property_name', 'icon', 'package', 'created_at', 'updated_at']


class PackagePropertyCREATESeriazlier(serializers.ModelSerializer):
    class Meta:
        model = PackageProperty
        fields = ['id', 'property_name', 'icon', 'package', 'created_at', 'updated_at']
