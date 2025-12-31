from rest_framework import serializers
from apiv1.models import Comment, Post


class PostNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title']


class CommentSerializer(serializers.ModelSerializer):
    post = PostNestedSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'post', 'nickname', 'comment', 'comment_date', 'ip_address', 'status']  