from django.urls import path, include
from rest_framework import routers
from .views import ActivateUserView, RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

router = routers.DefaultRouter()
router.register('register', RegisterView, basename='register')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('auth/user-activate/<str:token>/', ActivateUserView.as_view(), name='activate'),
    path('', include(router.urls))
]
