from rest_framework.viewsets import ModelViewSet
from ..models.comment import Comment
from ..serializers.comment_serializer import CommentSerializer

class CommentModelViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    http_method_names = ['get','post','put','patch','delete']