from rest_framework import serializers
from .models import Post, Like


class PostCreate(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ['pk', 'author', 'title', 'likes', 'date']


class LikeSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Like
        fields = ['author', 'post', 'liked_date']


class LikeAnalyticsSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField()
    likes = serializers.IntegerField()

    class Meta:
        model = Like
        fields = ['date', 'likes']