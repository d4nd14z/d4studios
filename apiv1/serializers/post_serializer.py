from rest_framework import serializers
from django.contrib.auth import get_user_model
from apiv1.models import Post

User = get_user_model()

class PostSerializer(serializers.ModelSerializer):

    class AuthorSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ['id', 'username', 'email']

    author = AuthorSerializer(read_only=True)
    categories = serializers.StringRelatedField(many=True)
    comments = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'categories', 'creation_date', 'is_published', 'comments']

    