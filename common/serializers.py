# serializers.py
from rest_framework import serializers
from .models import Post, School

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'image', 'subject', 'grade', 'created_at']


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'town', 'description', 'image']