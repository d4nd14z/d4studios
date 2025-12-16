from django.contrib import admin
from .models import Post, Category, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    readonly_fields = ['username', 'content', 'ip_address', 'created_at', ]
    can_delete = True
    def created_at_formatted(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %H:%M:%S')
    created_at_formatted.short_description = 'Fecha de creación'

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'published', 'created_at']
    list_display_links = ['title']
    filter_horizontal = ['category'] 
    inlines = [CommentInline]
    ordering = ['id']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_display_links = ['title']
    ordering = ['id']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'ip_address', 'created_at']
    list_display_links = ['username', 'ip_address']
    ordering = ['created_at']
