from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from users.views import CreateUserView
from notifications.views import NotificationsListCreate, NotificationsRetriveUpdateDestroy

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/register/', CreateUserView.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
    path('notifications/', NotificationsListCreate.as_view()),
    path('notifications/<int:pk>/', NotificationsRetriveUpdateDestroy.as_view())
]
