from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from news_app.views import RegisterView, UserView, PeopleView, UserPostsView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('me/', UserView.as_view(), name='get_me'),
    path('users/', PeopleView.as_view(), name='get_user'),
    path('users/<int:user_id>/posts/', UserPostsView.as_view(), name='get_user_posts'),
    path('signup/', RegisterView.as_view(), name='signup'),
    path('token/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('news_app.urls'))
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
