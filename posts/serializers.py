from rest_framework import serializers
from .models import School, Comment


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'town', 'description', 'image']


# class CommentSerializer(serializers.ModelSerializer):
#     rating = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Comment
#         fields = ['id', 'up_votes', 'down_votes', 'rating']
#
#     def get_rating(self, obj):
#         return obj.rating