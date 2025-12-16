from django.db import models
import bleach # Evitar XSS  Scripting
from apiv1.models.post import Post

class Comment (models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    username = models.CharField(max_length=50)
    content = models.TextField(max_length=512)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

    def save(self, *args, **kwargs):
        # Limpiar contenido para evitar XSS
        self.content = bleach.clean(self.content)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} on {self.post.title}"

