import django_filters.rest_framework
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import (LastWorks,
                     Package,
                     PackageProperty,
                     ServiceCategory,
                     ServiceProperty,
                     Services,
                     ServicesPropertyDetails)
from .serializers import (ServiceSerializer,
                          ServicePropertyCREATESerializer,
                          ServicePropertyREADSerializer,
                          ServicesPropertyDetailsREADSeriazlier,
                          ServicesPropertyDetailsCREATESeriazlier,
                          ServiceCategoryREADSerializer,
                          ServiceCategoryCREATESerializer,
                          LastWorksREADSerializer,
                          LastWorksCREATESerializer,
                          PackageREADSerializer,
                          PackageCREATESerializer,
                          PackagePropertyREADSeriazlier,
                          PackagePropertyCREATESeriazlier)



class GenericAPIViewSerializerMixin:
    def get_serializer_class(self):
        return self.serializer_classes[self.request.method]


# Service GET & POST
class ServicesListCreateAPIView(ListCreateAPIView):
    queryset = Services.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'slug']
    serializer_class = ServiceSerializer


# Service GET & PUT & PAtch & DELETE
class ServicesRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'slug'


# Service Property GET & POST
class ServicePropertyListCreateAPIView(GenericAPIViewSerializerMixin, ListCreateAPIView):
    queryset = ServiceProperty.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['services']
    search_fields = ['title']
    serializer_classes = {
        'GET' : ServicePropertyREADSerializer,
        'POST' : ServicePropertyCREATESerializer
    }


# Service Property GET & PUT & PAtch & DELETE
class ServicePropertyRetrieveUpdateDestroyAPIView(GenericAPIViewSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = ServiceProperty.objects.all()
    serializer_classes = {
        'GET' : ServicePropertyREADSerializer,
        'PUT' : ServicePropertyCREATESerializer,
        'PATCH' : ServicePropertyCREATESerializer
    }


# Services Property Details GET & POST
class ServicesPropertyDetailsListCreateAPIView(GenericAPIViewSerializerMixin, ListCreateAPIView):
    queryset = ServicesPropertyDetails.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['services_property']
    search_fields = ['title']
    serializer_classes = {
        'GET' : ServicesPropertyDetailsREADSeriazlier,
        'POST' : ServicesPropertyDetailsCREATESeriazlier
    }


# Services Property Details GET & PUT & PAtch & DELETE
class ServicesPropertyDetailsRetrieveUpdateDestroyAPIView(GenericAPIViewSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = ServicesPropertyDetails.objects.all()
    serializer_classes = {
        'GET' : ServicesPropertyDetailsREADSeriazlier,
        'PUT' : ServicesPropertyDetailsCREATESeriazlier,
        'PATCH' : ServicesPropertyDetailsCREATESeriazlier
    }


# Service Category GET & POST
class ServiceCategoryListCreateAPIView(GenericAPIViewSerializerMixin, ListCreateAPIView):
    queryset = ServiceCategory.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['services']
    search_fields = ['name']
    serializer_classes = {
        'GET' : ServiceCategoryREADSerializer,
        'POST' : ServiceCategoryCREATESerializer
    }


# Service Category GET & PUT & PAtch & DELETE
class ServiceCategoryRetrieveUpdateDestroyAPIView(GenericAPIViewSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = ServiceCategory.objects.all()
    serializer_classes = {
        'GET' : ServiceCategoryREADSerializer,
        'PUT' : ServiceCategoryCREATESerializer,
        'PATCH' : ServiceCategoryCREATESerializer
    }


# Last Works GET & POST
class LastWorksListCreateAPIView(GenericAPIViewSerializerMixin, ListCreateAPIView):
    queryset = LastWorks.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['services_category']
    search_fields = ['company_name']
    serializer_classes = {
        'GET' : LastWorksREADSerializer,
        'POST' : LastWorksCREATESerializer
    }


# Last Works GET & PUT & PAtch & DELETE
class LastWorksRetrieveUpdateDestroyAPIView(GenericAPIViewSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = LastWorks.objects.all()
    serializer_classes = {
        'GET' : LastWorksREADSerializer,
        'PUT' : LastWorksCREATESerializer,
        'PATCH' : LastWorksCREATESerializer
    }


# Package GET & POST
class PackageListCreateAPIView(GenericAPIViewSerializerMixin, ListCreateAPIView):
    queryset = Package.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['services_category', 'price_period']
    search_fields = ['package_name', 'price']
    serializer_classes = {
        'GET' : PackageREADSerializer,
        'POST' : PackageCREATESerializer
    }


# Package GET & PUT & PAtch & DELETE
class PackageRetrieveUpdateDestroyAPIView(GenericAPIViewSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = Package.objects.all()
    serializer_classes = {
        'GET' : PackageREADSerializer,
        'PUT' : PackageCREATESerializer,
        'PATCH' : PackageCREATESerializer
    }


# Package Property GET & POST
class PackagePropertyListCreateAPIView(GenericAPIViewSerializerMixin, ListCreateAPIView):
    queryset = PackageProperty.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['package']
    search_fields = ['property_name']
    serializer_classes = {
        'GET' : PackagePropertyREADSeriazlier,
        'POST' : PackagePropertyCREATESeriazlier
    }


# Package Property GET & PUT & PAtch & DELETE
class PackagePropertyRetrieveUpdateDestroyAPIView(GenericAPIViewSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = PackageProperty.objects.all()
    serializer_classes = {
        'GET' : PackagePropertyREADSeriazlier,
        'PUT' : PackagePropertyCREATESeriazlier,
        'PATCH' : PackagePropertyCREATESeriazlier
    }
