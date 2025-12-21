from rest_framework.routers import DefaultRouter
from .views.post_views import PostModelViewSet
from .views.category_views import CategoryModelViewSet
from .views.comment_views import CommentModelViewSet

router = DefaultRouter()
router.register(prefix='posts', basename='posts', viewset=PostModelViewSet)
router.register(prefix='categories', basename='categories', viewset=CategoryModelViewSet)
router.register(prefix='comments', basename='comments', viewset=CommentModelViewSet)
