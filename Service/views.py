import django_filters.rest_framework
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import (LastWorks,
                     Package,
                     PackageProperty,
                     ServiceCategory,
                     ServiceProperty, Services,
                     ServicesPropertyDetails)
from .serializers import (LastWorksSerializer,
                          PackageCREATESerializer,
                          PackagePropertySeriazlier,
                          PackageREADSerializer,
                          ServiceCREATESerializer,
                          ServiceCategoryCREATESerializer,
                          ServiceCategoryREADSerializer,
                          ServicePropertyCREATESerializer,
                          ServicePropertyREADSerializer,
                          ServiceREADSerializer,
                          ServicesPropertyDetailsSeriazlier)



class GenericAPIViewSerializerMixin:
    def get_serializer_class(self):
        return self.serializer_classes[self.request.method]


# Package Property GET & POST
class PackagePropertyListCreateAPIView(ListCreateAPIView):
    queryset = PackageProperty.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['property_name']
    serializer_class = PackagePropertySeriazlier

# Package Property GET & PUT & PAtch & DELETE
class PackagePropertyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = PackageProperty.objects.all()
    serializer_class = PackagePropertySeriazlier


# Package GET & POST
class PackageListCreateAPIView(GenericAPIViewSerializerMixin, ListCreateAPIView):
    queryset = Package.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['price_period', 'price']
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


# Last Works GET & POST
class LastWorksListCreateAPIView(ListCreateAPIView):
    queryset = LastWorks.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['services_category']
    search_fields = ['company_name']
    serializer_class = LastWorksSerializer

# Last Works GET & PUT & PAtch & DELETE
class LastWorksRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = LastWorks.objects.all()
    serializer_class = LastWorksSerializer


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


# Services Property Details GET & POST
class ServicesPropertyDetailsListCreateAPIView(ListCreateAPIView):
    queryset = ServicesPropertyDetails.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    serializer_class = ServicesPropertyDetailsSeriazlier

# Services Property Details GET & PUT & PAtch & DELETE
class ServicesPropertyDetailsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ServicesPropertyDetails.objects.all()
    serializer_class = ServicesPropertyDetailsSeriazlier


# Service Property GET & POST
class ServicePropertyListCreateAPIView(GenericAPIViewSerializerMixin, ListCreateAPIView):
    queryset = ServiceProperty.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['services']
    search_fields = ['up_title', 'down_title']
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


# Service GET & POST
class ServicesListCreateAPIView(GenericAPIViewSerializerMixin, ListCreateAPIView):
    queryset = Services.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'slug']
    serializer_classes = {
        'GET' : ServiceREADSerializer,
        'POST' : ServiceCREATESerializer
    }

# Service GET & PUT & PAtch & DELETE
class ServicesRetrieveUpdateDestroyAPIView(GenericAPIViewSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = Services.objects.all()
    serializer_classes = {
        'GET' : ServiceREADSerializer,
        'PUT' : ServiceCREATESerializer,
        'PATCH' : ServiceCREATESerializer
    }


