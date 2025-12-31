from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apiv1.models import Category
from apiv1.serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly] #Cualquier usuario puede hacer GET, pero solo los autenticados pueden hacer POST, PUT, PATCH, DELETE
    queryset = Category.objects.all()
    serializer_class = CategorySerializer