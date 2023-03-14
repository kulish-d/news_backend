from rest_framework import routers
from news_app.views import PostViewSet


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = router.urls
