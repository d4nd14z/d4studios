from rest_framework.viewsets import ModelViewSet
from ..models.post import Post
from ..serializers.post_serializer import PostSerializer

class PostModelViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    http_method_names = ['get','post','put','patch','delete']