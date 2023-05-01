from rest_framework import routers
from news_app.views import PostViewSet, CommentViewSet


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = router.urls
