from rest_framework import routers
from news_app.views import NewsViewSet


router = routers.DefaultRouter()
router.register(r'news', NewsViewSet, basename='news')

urlpatterns = router.urls