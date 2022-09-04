from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from django.conf.urls.static import static
from django.conf import settings

from users.views import CreateUserView, UserView, CustomAuthentication
from notifications.views import NotificationsListCreateView, NotificationsDeleteUpdateView

# router = DefaultRouter()


def trigger_error(request):  # ToDo удалить на релизе
    """test sentry"""
    division_by_zero = 1 / 0


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(router.urls)),
    path('auth/', include('rest_framework_social_oauth2.urls')),
    path('api/user_data/', UserView.as_view()),
    # path('api-custom-auth/', CustomAuthentication.as_view()),
    path('api/register/', CreateUserView.as_view()),
    path('api/api-token-auth/', views.obtain_auth_token),
    path('api/notifications/', NotificationsListCreateView.as_view()),
    path('api/notifications/<int:pk>', NotificationsDeleteUpdateView.as_view()),
    path('sentry-debug/', trigger_error),  # ToDo удалить на релизе
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
