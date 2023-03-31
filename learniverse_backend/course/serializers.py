from django.contrib.auth.models import User
from rest_framework import serializers


from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

        fields = [
            'id',
            'title',
            'slug',
            'short_description'
        ]


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course

        fields = [
            'id',
            'title',
            'slug',
            'short_description',
            'get_image'
        ]


class CourseSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(many=False)
    categories = serializers.StringRelatedField(many=True)

    class Meta:
        model = Course

        fields = [
            'id',
            'title',
            'slug',
            'long_description',
            'categories',
            'created_by'
        ]



class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons

        fields = (
            'id',
            'title',
            'slug',
            'lesson_type',
            'short_description',
            'long_description',
            'youtube_id',
        )

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'name',
            'content',
            'created_at',
            
        ]


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz

        fields = ('id', 'lesson_id', 'question', 'answer','opt1', 'opt2','opt3',)
   


