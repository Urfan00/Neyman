from rest_framework import serializers
from .models import Blog, BlogCategory, Tag



class BlogCREATESerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'photo', 'slug', 'short_descriptions', 'long_descriptions', 'blog_category', 'tag', 'created_at', 'updated_at']


class BlogCategoryREADSerializer(serializers.ModelSerializer):
    blog = BlogCREATESerializer(many=True, read_only=True, source='blog_category')

    class Meta:
        model = BlogCategory
        fields = ['id', 'name', 'created_at', 'updated_at', 'blog']


class BlogCategoryCREATESerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['id', 'name', 'created_at', 'updated_at']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'created_at', 'updated_at']


class BlogREADSerializer(serializers.ModelSerializer):
    blog_category = BlogCategoryCREATESerializer()
    tag = TagSerializer(many=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'photo', 'slug', 'short_descriptions', 'long_descriptions', 'blog_category', 'tag', 'created_at', 'updated_at']
