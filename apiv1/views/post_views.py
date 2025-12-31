from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apiv1.models import Post
from apiv1.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly] #Cualquier usuario puede hacer GET, pero solo los autenticados pueden hacer POST, PUT, PATCH, DELETE
    queryset = Post.objects.all()
    serializer_class = PostSerializer