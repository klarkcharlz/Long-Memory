from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from users.views import CreateUserView, RetrieveUserAPIView, UpdateUserAPIView
from notifications.views import NotificationsListCreate, NotificationsRetrieveUpdateDestroy

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('user/<pk>/', RetrieveUserAPIView.as_view()),
    path('update/user/<pk>/', UpdateUserAPIView.as_view()),
    path('api/', include(router.urls)),
    path('api/register/', CreateUserView.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/notifications/', NotificationsListCreate.as_view()),
    path('api/notifications/<int:pk>/', NotificationsRetrieveUpdateDestroy.as_view())
]
