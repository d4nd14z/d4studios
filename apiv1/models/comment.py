from django.db import models
from .post import Post

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = 'comments')
    nickname = models.CharField(max_length=20)
    comment = models.TextField(max_length=128)
    comment_date = models.DateTimeField(auto_now_add=True)    
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

    def __str__(self):
        return f"({self.nickname}) - {self.comment}"
