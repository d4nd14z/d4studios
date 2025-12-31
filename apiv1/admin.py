from django.contrib import admin
from apiv1.models import Post, Category, Comment


# Tabular Inline
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    #readonly_fields = ("nickname", "comment", "comment_date", "status")
    can_delete = True
    readonly_fields = ("nickname", "comment", "comment_date", "status")



# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'display_categories', 'creation_date', 'is_published']
    list_display_links = ['id', 'title']
    filter_horizontal = ("categories",)
    inlines = [CommentInline]

    def display_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all()])
    
    display_categories.short_description = "Categorías"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'description', 'creation_date', 'status']
    list_display_links = ['id', 'name']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'nickname', 'comment', 'comment_date', 'ip_address', 'status']
    list_display_links = ['id', 'nickname']