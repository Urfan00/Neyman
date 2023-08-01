import django_filters.rest_framework
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import BlogCREATESerializer, BlogCategoryCREATESerializer, BlogCategoryREADSerializer, BlogREADSerializer, TagSerializer
from .models import Blog, BlogCategory, Tag



class GenericAPIViewSerializerMixin:
    def get_serializer_class(self):
        return self.serializer_classes[self.request.method]


# Blog Category GET & POST
class BlogCategoryListCreateAPIView(GenericAPIViewSerializerMixin, ListCreateAPIView):
    queryset = BlogCategory.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    serializer_classes = {
        'GET' : BlogCategoryREADSerializer,
        'POST' : BlogCategoryCREATESerializer
    }

# Blog Category GET & PUT & PATCH & DELETE
class BlogCategoryRetrieveUpdateDestroyAPIView(GenericAPIViewSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = BlogCategory.objects.all()
    serializer_classes = {
        'GET' : BlogCategoryREADSerializer,
        'PUT' : BlogCategoryCREATESerializer,
        'PATCH' : BlogCategoryCREATESerializer
    }

# Tag GET & POST
class TagListCreateAPIView(ListCreateAPIView):
    queryset = Tag.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    serializer_class = TagSerializer

# Tag GET & PUT & PATCH & DELETE
class TagRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# Blog GET & POST
class BlogListCreateAPIView(GenericAPIViewSerializerMixin, ListCreateAPIView):
    queryset = Blog.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['blog_category', 'tag']
    search_fields = ['title']
    serializer_classes = {
        'GET' : BlogREADSerializer,
        'POST' : BlogCREATESerializer
    }

# Blog GET & PUT & PATCH & DELETE
class BlogRetrieveUpdateDestroyAPIView(GenericAPIViewSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_classes = {
        'GET' : BlogREADSerializer,
        'PUT' : BlogCREATESerializer,
        'PATCH' : BlogCREATESerializer
    }