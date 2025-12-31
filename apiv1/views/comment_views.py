from rest_framework import viewsets
from apiv1.models import Comment
from apiv1.serializers import CommentSerializer
from apiv1.permissions import CommentPermission

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CommentPermission]