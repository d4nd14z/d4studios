from rest_framework.serializers import ModelSerializer
from ..models.comment import Comment

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'username', 'content', 'ip_address', 'created_at']