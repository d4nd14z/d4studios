from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from ..models.post import Post
from ..models.category import Category
from ..models.comment import Comment

# Serializadores anidados para el PostSerializer
class AuthorSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'first_name', 'last_name', 'email']

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'created_at']

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'username', 'content', 'ip_address', 'created_at']


# Serializador propio de el modelo POST
class PostSerializer(ModelSerializer):
    author = AuthorSerializer(read_only=True) #Aquí se incluye el serializador anidado
    category = CategorySerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'category', 'published', 'created_at', 'comments']
        