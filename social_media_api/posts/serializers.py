from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'author_username', 'title', 'content', 'created_at', 'updated_at', 'comments_count']
        read_only_fields = ['author', 'created_at', 'updated_at', 'comments_count']

class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'author_username', 'content', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']