from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly #Todos tienen acceso al GET, pero solo usuarios autenticados tienen acceso a POST, PUT y DELETE.
from ..models.post import Post
from ..models.category import Category
from ..serializers.post_serializer import PostSerializer

class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ['get','post','put','patch','delete']

    def perform_create(self, serializer):
        # Asignar automaticamente el usuario logueado como author
        post = serializer.save(author=self.request.user)
        default_category = Category.objects.get(title="General")
        post.category.add(default_category)
        