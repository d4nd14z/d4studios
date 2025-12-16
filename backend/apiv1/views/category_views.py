from rest_framework.viewsets import ModelViewSet
from ..models.category import Category
from ..serializers.category_serializer import CategorySerializer

class CategoryModelViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    http_method_names = ['get','post','put','patch','delete']