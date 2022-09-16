from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views
from django.conf.urls.static import static
from django.conf import settings

from users.views import CreateUserView, UserView, activate_user
from notifications.views import NotificationsListCreateView, NotificationsDeleteUpdateView
from bug_report.views import BugReportCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user_data/', UserView.as_view()),
    path('api/bug_report/', BugReportCreateView.as_view()),
    path('api/register/', CreateUserView.as_view()),
    path('api/activate/<int:uid>/<str:token>/', activate_user),
    path('api/api-token-auth/', views.obtain_auth_token),
    path('api/notifications/', NotificationsListCreateView.as_view()),
    path('api/notifications/<int:pk>', NotificationsDeleteUpdateView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
