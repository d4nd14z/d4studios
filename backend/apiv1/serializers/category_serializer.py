from rest_framework.serializers import ModelSerializer
from ..models.category import Category

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'created_at']