from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from news_app.views import RegisterView, UserView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('me/', UserView.as_view(), name='get_user'),
    path('signup/', RegisterView.as_view(), name='signup'),
    path('token/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('news_app.urls'))
]
